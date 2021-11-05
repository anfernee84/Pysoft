from pathlib import Path
from aiopath import AsyncPath, AsyncPurePath
import shutil
import asyncio 

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



async def parse_folder(path: AsyncPath):
    for folder_item in await path.iterdir():
        if folder_item.is_dir():
            if folder_item.name not in ['IMAGES', 'VIDEOS', 'DOC', 'OTHER', 'MUSIC', 'ARCH']:
                parse_folder(folder_item)
                continue
        else:
            ext = folder_item.suffix[1:]
            if ext.upper() in REGISTERED_EXT.keys():
                REGISTERED_EXT[ext.upper()].append(folder_item)
    return REGISTERED_EXT


async def handle_file(root_path, file_path: AsyncPath):
    ext = await file_path.suffix[1:].upper()
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



# async def sort_folder_command(file_path):
#     reg_ext = parse_folder(file_path)
#     for item in reg_ext.values():
#         for file in item:
#             try: 
#                 handle_file(AsyncPath(file_path), file)
#             except FileNotFoundError:
#                 continue

async def sort_folder_command(file_path):
    reg_ext = await parse_folder(file_path)
    for item in reg_ext.values():
        for file in item:
            try: 
                await handle_file(AsyncPath(file_path), file)
            except FileNotFoundError:
                continue

async def delfolder(path: AsyncPath):
    for folder in path.iterdir():
        if folder.name not in ['IMAGES', 'DOC', 'ARCH', 'OTHER', 'VIDEOS', 'MUSIC'] and folder.is_dir():
            shutil.rmtree(folder)

if __name__ == '__main__':
    path = AsyncPath()
    print (path)
    sort_folder_command(path)