import os
from termcolor import colored


def ensure_folder_exists(folder_name: str) -> None:
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    folder_path = os.path.join(desktop_path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(colored(f"Folder created at: {folder_path}", "light_green"))
    else:
        print(colored(f"Folder already exists at: {
              folder_path}", "light_green"))
