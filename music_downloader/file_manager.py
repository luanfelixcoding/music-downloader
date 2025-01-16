import os


def create_directory(directory: str) -> None:
    if not os.path.exists(directory):
        os.makedirs(directory)


def rename_file(old_name: str, new_name: str) -> None:
    os.rename(old_name, new_name)
