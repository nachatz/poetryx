import os
from toml import load, dump

def read_file(path: str, toml=False) -> str:
    with open(path, 'r') as file:
        if toml:
            return load(file)
        else:
            return file.read()
    
def write_file(path: str, content: str, toml=False):
    with open(path, 'w') as file:
        if toml:
            dump(content, file)
        else:
            file.write(content)

def delete_file(path: str):
    os.remove(path)
