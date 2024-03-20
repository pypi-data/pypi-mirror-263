from base64 import b64encode
from json import dumps, loads
from pathlib import Path
from struct import pack
from typing import Any, Dict, List, Optional

from aiohttp import ClientSession

from .inference_request import InferenceRequestInputItem, InferenceRequestOutputItem
from .inference_response import InferenceResponse
from xinfcli.model_utils import ModelConfig
from xinfcli.utils import client_logger


async def post_inference_request(
    host: str,
    port: int,
    transaction_type: str,
    inputs: List[InferenceRequestInputItem],
    outputs: List[InferenceRequestOutputItem],
) -> Optional[InferenceResponse]:
    url = f"http://{host}:{port}/inferences/{transaction_type}"
    encoded_request_json: bytes = "".encode()
    request_headers: Dict[str, str] = {}
    result: Optional[InferenceResponse] = None

    async with ClientSession() as session:
        request_json: Dict[str, Any] = {
            "inputs": [input_item.serialize_to_json() for input_item in inputs],
            "outputs": [output_item.serialize_to_json() for output_item in outputs],
        }
        dumped_request_json = dumps(request_json)

        # attach bytes of tensor to the request
        total_input_binary_data: bytes = b""

        for input_item in inputs:
            if input_item.is_binary_data and input_item.binary_data is not None:
                total_input_binary_data += input_item.binary_data

        if len(total_input_binary_data) > 0:
            encoded_request_json = pack(
                "{}s{}s".format(len(dumped_request_json), len(total_input_binary_data)),
                dumped_request_json.encode(),
                total_input_binary_data,
            )
            request_headers["Inference-Header-Content-Length"] = str(
                len(dumped_request_json)
            )
        else:
            encoded_request_json = dumped_request_json.encode()

        try:
            async with session.post(
                url, data=encoded_request_json, headers=request_headers
            ) as response:
                if response.status == 200:
                    result = InferenceResponse(
                        await response.read(),
                        response.headers.get("Inference-Header-Content-Length"),
                        response.headers.get("Content-Encoding"),
                    )
                else:
                    client_logger.info(
                        f"Failed to get correct response of inference request: ({response.status}){await response.text()}"
                    )
        except Exception as e:
            client_logger.error(f"Exception occurred.\n[Exception] {e}")

    return result


async def post_model(
    host: str,
    port: int,
    model_name: str,
    version: str,
    model_path: str,
    model_config: ModelConfig,
):
    url = f"http://{host}:{port}/models/{model_name}"
    request_json = {"parameters": {"config": dumps(model_config.serialize_to_json())}}
    result: bool = False

    with open(model_path, "rb") as model_file:
        # file:{version}/{file_name}
        request_json["parameters"][f"file:{version}/{Path(model_path).name}"] = (
            b64encode(model_file.read()).decode()
        )

    async with ClientSession() as session:
        try:
            async with session.post(url, data=dumps(request_json)) as response:
                if response.status == 200:
                    result = True
                    client_logger.info(
                        f"Upload model {model_name} with version {version} successfully."
                    )
                else:
                    client_logger.info(
                        f"Failed to get correct response of uploading model: ({response.status}){await response.text()}"
                    )
        except Exception as e:
            client_logger.error(f"Exception occurred.\n[Exception] {e}")

    return result


async def get_model(
    host: str, port: int, model_name: str, *, version: str = "", store_path: str = "."
) -> bool:
    url = f"http://{host}:{port}/models/{model_name}{f'/versions/{version}' if version else ''}"
    result: bool = False

    async with ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    content = await response.read()

                    with open(f"{store_path}/{model_name}.tar.gz", "wb") as model_file:
                        model_file.write(content)
                        result = True

                    client_logger.info(f"Get model {model_name} successfully.")
                else:
                    client_logger.info(
                        f"Failed to get correct response of getting model: ({response.status}){await response.text()}"
                    )
        except Exception as e:
            client_logger.error(f"Exception occurred.\n[Exception] {e}")

    return result
