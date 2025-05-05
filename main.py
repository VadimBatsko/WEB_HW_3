import time
from pathlib import Path
from threading import Thread
import shutil


def cop_file(copy_folder: Path, past_folder: Path):
    for path in copy_folder.iterdir():
        if path.is_dir():
            tr = Thread(target=cop_file, args=(path, past_folder,))
            tr.start()
        elif path.is_file():
            dir_path = past_folder / path.suffix[1:].upper()
            try:
                dir_path.mkdir(parents=True, exist_ok=False)
                shutil.copy(path, dir_path)
            except FileExistsError:
                shutil.copy(path, dir_path)
        else:
            print(path)


if __name__ == '__main__':

    past_fold = Path(r"D:\GoIt\HW_3\pythonProject\dist")
    copy_fold = Path(r"D:\GoIt\HW_3\pythonProject\picture")
    cop_file(copy_fold, past_fold)

