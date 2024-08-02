import aiofiles
from pathlib import Path

async def get_file(filename: str):
    try:
        dir = Path.cwd()
        async with aiofiles.open(f'{dir}/{filename}', 'r', encoding='latin-1') as file:
            content = await file.read()
            return content
    except Exception as e:
        print('error', e)
        return None