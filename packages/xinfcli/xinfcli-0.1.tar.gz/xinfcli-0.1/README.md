# 推理客户端

## 语言版本

- python\@3.8

## 依赖项

- aiohttp
- numpy

## 目录结构

``` txt
xinfcli
├─ api
│   ├─ inference_request.py # 推理请求输入类
│   ├─ inference_response.py # 推理请求输出类
│   └─ interface.py # 推理接口
├─ model_utils
│   ├─ data_type.py # 数据的类型
│   └─ model_config.py # 模型配置
├─ utils
│   └─ archive.py # 解压文件
└─ main.py # 运行入口
```

## 异步执行

```py
import asyncio

async def async_fn1():
    pass

async def async_fn2():
    pass

async def main():
    await asyncio.gather(async_fn1(), async_fn2()) 

if __name__ == "__main__":
    asyncio.run(main())
```

## 发送推理请求

```py
from asyncio import run as async_run, gather

from xinfcli.api import InferenceRequestInputItem, InferenceRequestOutputItem, post_inference_request
from xinfcli.model_utils import TensorDataType

async def test_inference():
    image_data = preprocess_image("./img/cat.jpg")
    inference_input = InferenceRequestInputItem(
        "input__0", image_data.shape, TensorDataType.TYPE_FP32
    )
    inference_input.set_data(image_data, True)
    inference_output = InferenceRequestOutputItem(
        "output__0", is_binary_data=True, class_count=1000
    )

    result = await post_inference_request(
        "localhost", 10111, "image", [inference_input], [inference_output]
    )

    if result is not None:
        print(result.get_output(inference_output.name)[:5])

async def main():
    await gather(
        test_inference(),
    )

if __name__ == "__main__":
    async_run(main())

```

### `post_inference_request`参数

| 参数名 | 参数类型 | 说明 |
| --- | --- | --- |
| host | str | IP地址 |
| port | int | 端口号 |
| transaction_type | str | 业务类型，例如：`image`，`text`， `audio` |
| inputs | List[InferenceRequestInputItem] | 推理的输入格式以及输入数据 |
| outputs | List[InferenceRequestOutputItem] | 推理的输出格式 |

#### input

```py
inference_input = InferenceRequestInputItem(
"input__0", image_data.shape, TensorDataType.TYPE_FP32
)
inference_input.set_data(image_data, True)
```

初始化`input`需要名称，张量形状，以及张量数据类型。

通过调用`set_data`为`input`设置输入数据，函数的第二个参数用来指定输入数据是否为二进制形式。

输入数据的类型应该是`numpy.ndarray`，且输入数据的形状应该与input所设置的形状相同。图像数据预处理示例：

```py
from numpy import array as np_array, ndarray
from PIL import Image
from torchvision import transforms

def preprocess_image(image_path: str) -> ndarray:
    image_data = Image.open(image_path)
    preprocess = transforms.Compose(
        [
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )

    return preprocess(image_data).numpy()
```

#### output

```py
inference_output = InferenceRequestOutputItem(
"output__0", is_binary_data=True, class_count=1000
)
```

初始化`output`需要名称，输出是否为二进制数据，以及分类的数量。

如果模型不支持分类，则可以不填写参数`class_count`。

### `post_inference_request`返回值

```py
result = await post_inference_request(
"localhost", 10111, "image", [inference_input], [inference_output]
)

if result is not None:
    print(result.get_output(inference_output.name)[:5])
```

请求成功后，函数返回`InferenceResponse`；请求失败后，函数返回`None`。

通过调用`get_output`函数来获取输出张量，调用函数需要传入输出的名称，输出张量的类型是`numpy.ndarray`。

## 上传模型

```py
from asyncio import run as async_run, gather

from xinfcli.api import post_model
from xinfcli.model_utils import ModelConfig, TensorDataType

async def test_post_model():
    model_config = ModelConfig("resnet50")
    model_config.add_input(
        "input__0",
        TensorDataType.TYPE_FP32,
        [3, 224, 224],
        reshape=[1, 3, 224, 224],
    )
    model_config.add_output(
        "output__0",
        TensorDataType.TYPE_FP32,
        [1, 1000, 1, 1],
        reshape=[1, 1000],
    )

    result = await post_model(
        "localhost", 10111, "resnet50", "2", "./models/model.pt", model_config
    )

async def main():
    await gather(
        test_post_model(),
    )

if __name__ == "__main__":
    async_run(main())
```

### `post_model`参数

| 参数名 | 参数类型 | 说明 |
| --- | --- | --- |
| host | str | IP地址 |
| port | int | 端口号 |
| model_name | str | 上传模型的名称 |
| version | str | 上传模型的新版本号 |
| model_path | str | 上传模型的文件路径，指向`.pt`文件 |
| model_config | ModelConfig | 上传模型的配置信息 |

#### 模型配置信息

```py
model_config = ModelConfig("resnet50")
model_config.add_input(
    "input__0",
    TensorDataType.TYPE_FP32,
    [3, 224, 224],
    reshape=[1, 3, 224, 224],
)
model_config.add_output(
    "output__0",
    TensorDataType.TYPE_FP32,
    [1, 1000, 1, 1],
    reshape=[1, 1000],
)
```

无论是上传未存在的新模型，还是上传已存在模型的新版本，都需要传入模型的配置信息。

初始化`model_config`需要指定模型名称，模型使用的平台，以及最大批处理数量。模型使用的平台默认为`pytorch`，若模型不支持批处理，则可以不填写最大批处理数量。

通过调用`add_input`来设置模型的输入格式。输入格式包括名称，张量数据类型，张量形状，以及可选的`reshape`。

通过调用`add_output`来设置模型的输出格式。输出格式包括名称，张量数据类型，张量形状，以及可选的`reshape`。

#### 保存模型

通过`torch.save`来将模型保存为`.pt`文件。

### `post_model`返回值

返回值的类型为`bool`，表示操作是否成功。

## 下载模型

```py
from asyncio import run as async_run, gather

from xinfcli.api import get_model

async def test_get_model():
    result = await get_model("localhost", 10111, "resnet50", store_path="./download")

async def main():
    await gather(
        test_get_model(),
    )

if __name__ == "__main__":
    async_run(main())
```

### `get_model`参数

| 参数名 | 参数类型 | 说明 |
| --- | --- | --- |
| host | str | IP地址 |
| port | int | 端口号 |
| model_name | str | 下载模型的名称 |
| version | str | 下载模型的版本号，可选，未指定则下载最新模型 |
| store_path | str | 下载模型的存储路径 |

#### 解压下载文件

```py
from utils.archive import extract

extract("./download/model_name.tar.gz", "./tmp", True)
```

下载文件的文件名为`model_name.tar.gz`，其中`model_name`与传入函数`get_model`的参数一致。

通过调用函数`extract`来解压，传入的参数包括下载文件路径，解压路径，以及解压后是否删除源文件。

解压后的目录格式：

``` txt
<model_name> # 模型名称
├─ <version> # 版本号
│   └─ model.pt # 模型的pt文件
└─ config.pbtxt # 模型配置文件
```

### `get_model`返回值

返回值的类型为`bool`，表示操作是否成功。

## 数据类型

| 模型配置 | PyTorch | NumPy|
| --- | --- | --- |
| TYPE_BOOL | kBool | bool |
| TYPE_UINT8 | kByte | uint8 |
| TYPE_INT8 | kChar | int8 |
| TYPE_INT16 | kShort | int16 |
| TYPE_INT32 | kInt | int32 |
| TYPE_INT64 | kLong | bool |
| TYPE_FP32 | kFloat | float32 |
| TYPE_FP64 | kDouble | float64 |
| TYPE_STRING | | dtype(object) |
