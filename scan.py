import sys
from pathlib import Path

image_files = list()
document_files = list()
music_files = list()
video_files = list()
folders = list()
archives = list()
others = list()
unknown = set()
extensions = set()

registered_extensions = {
    "JPEG": image_files,
    "JPG": image_files,
    "PNG": image_files,
    "SVG": image_files,
    "AVI": video_files,
    "MP4": video_files,
    "MOV": video_files,
    "MKV": video_files,
    "MP3": music_files,
    "OGG": music_files,
    "WAV": music_files,
    "AMR": music_files,
    "DOC": document_files,
    "DOCX": document_files,
    "TXT": document_files,
    "PDF": document_files,
    "PPTX": document_files,
    "XLSX": document_files,
    "ZIP": archives,
    "GZTAR": archives,
    "TAR": archives,
}

def get_extensions(file_name):
    return Path(file_name).suffix[1:].upper()

def scan(folder):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ("PICTURES", "VIDEO", "DOCUMENTS", "MUSIC", "OTHERS", "ARCHIVES"):
                folders.append(item)
                scan(item)
            continue

        extension = get_extensions(item.name)
        new_name = folder/item.name
        if not extension:
            others.append(new_name)
        else:
            try:
                container = registered_extensions[extension]
                extensions.add(extension)
                container.append(new_name)
            except KeyError:
                unknown.add(extension)
                others.append(new_name)
