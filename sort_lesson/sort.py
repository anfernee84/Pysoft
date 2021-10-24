from pathlib import Path
import shutil


DOC_DOC = []
DOCX_DOC = []
XLSX_DOC = []
PPTX_DOC = []
PDF_DOC = []
ZIP_ARCH = []
TAR_ARCH = []
OTHER = []

REGISTERED_EXT = {

    'DOC': DOC_DOC,
    'DOCX': DOCX_DOC,
    'XLSX': XLSX_DOC,
    'PPTX': PPTX_DOC,
    'PDF': PDF_DOC,
    'ZIP': ZIP_ARCH,
    "TAR": TAR_ARCH,
    'OTHER': OTHER
}


def parse_folder(path: Path):
    for folder_item in path.iterdir():
        if folder_item.is_dir():
            if folder_item.name not in ['IMAGES', 'VIDEOS', 'DOC', 'OTHER', 'MUSIC', 'ARCH']:
                parse_folder(folder_item)
                continue
        else:
            ext = folder_item.suffix[1:]
            if ext.upper() in REGISTERED_EXT.keys():
                REGISTERED_EXT[ext.upper()].append(folder_item)
            # else:
            #     REGISTERED_EXT['OTHER'].append(folder_item)
    return REGISTERED_EXT


def handle_file(root_path, file_path: Path):
    ext = file_path.suffix[1:].upper()
    if ext in ['JPG', 'SVG', 'PNG', 'JPEG']:
        category_folder = root_path / 'IMAGES'
    elif ext in ['DOC', 'DOCX', 'PPTX', 'PDF', 'XLSX']:
        category_folder = root_path / 'DOC'
    elif ext in ['TAR', 'ZIP', 'RAR']:
        category_folder = root_path / 'ARCH'
    elif ext in ['MP3', 'OGG', 'WAV', 'AMR']:
        category_folder = root_path / 'MUSIC'
    elif ext in ['MP4', 'AVI', 'MOV', 'MKV']:
        category_folder = root_path / 'VIDEOS'
    else:
        category_folder = root_path / 'OTHER'
    category_folder.mkdir(exist_ok=True)
    type_folder = category_folder / ext
    type_folder.mkdir(exist_ok=True)
    file_path.replace(type_folder / file_path.name)


def del_empty_folders(path: Path):
    for folder in path.iterdir():
        if folder.name not in ['IMAGES', 'DOC', 'ARCH', 'OTHER', 'VIDEOS', 'MUSIC'] and folder.is_dir():
            shutil.rmtree(folder)


def sort_folder_command(file_path):
    reg_ext = parse_folder(file_path)
    for item in reg_ext.values():
        try:
            for file in item:
                try: 
                    handle_file(Path(file_path), file)
                except FileNotFoundError:
                    continue
        except FileNotFoundError:
            continue
    # del_empty_folders(file_path)


if __name__ == '__main__':
    path = Path()
    sort_folder_command(path)
