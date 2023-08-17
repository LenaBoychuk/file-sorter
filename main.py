import scan
import normalize
import re
import shutil
from pathlib import Path

def handle_file(path, root_folder, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder/normalize.normalize(path.name))

def handle_archive(path, root_folder, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
        
    new_name = normalize.normalize(path.name)
    new_name = re.sub(r"(.zip|.gztar|.tar)", '', new_name)
   
    archive_folder = root_folder / dist / new_name
    archive_folder.mkdir(exist_ok=True)

    try:
        shutil.unpack_archive(str(path.resolve()), root_folder / dist / new_name)
    except shutil.ReadError or FileNotFoundError:
        archive_folder.rmdir()
        return
    path.unlink()

def remove_empty_folders(path):
    for item in path.iterdir():
        if item.is_dir():
            remove_empty_folders(item)
            try:
                item.rmdir()
            except OSError:
                pass
            
def get_folder_objects(root_path):
    for folder in root_path.iterdir():
        if folder.is_dir():
            remove_empty_folders(folder)
            try:
                folder.rmdir()
            except OSError:
                pass

def main(folder_path):
    scan.scan(folder_path)
    
    for file in scan.image_files:
        handle_file(file, folder_path, "IMAGES")

    for file in scan.document_files:
        handle_file(file, folder_path, "DOCUMENTS")

    for file in scan.music_files:
        handle_file(file, folder_path, "MUSIC")

    for file in scan.video_files:
        handle_file(file, folder_path, "VIDEO")

    for file in scan.others:
        handle_file(file, folder_path, "OTHERS")

    for file in scan.archives:
        handle_archive(file, folder_path, "ARCHIVES")

    get_folder_objects(folder_path)
