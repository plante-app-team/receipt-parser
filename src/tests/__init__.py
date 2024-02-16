import os


def get_stub_file_path(rel_path: str) -> str:
    dir_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(dir_path, "stubs", rel_path)


def load_stub_file(rel_path: str) -> str:
    with open(get_stub_file_path(rel_path), "r", encoding="utf8") as file:
        file = file.read()
    return file
