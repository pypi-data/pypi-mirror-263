from gzip import open as open_gzip
from io import BytesIO
from os import remove
from os.path import basename
from tarfile import open as open_tar


def compress(source_path: str, target_path: str) -> bool:
    try:
        with open_tar(target_path, "w:gz") as tar:
            tar.add(source_path, arcname=basename(source_path))
    except Exception:
        return False

    return True


def extract(source_path: str, target_path: str, is_remove_source: bool = False) -> bool:
    try:
        with open_gzip(source_path, "rb") as gzip_file:
            with open_tar(fileobj=BytesIO(gzip_file.read()), mode="r") as tar_file:
                tar_file.extractall(path=target_path)

        if is_remove_source:
            remove(source_path)
    except Exception:
        return False

    return True
