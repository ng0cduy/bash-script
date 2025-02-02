import platform
import re
import os
import subprocess
def check_architecture():
    arch = platform.machine()
    if 'arm' in arch.lower():
        return "ARM"
    elif 'amd' in arch.lower() or "x86_64" in arch.lower():
        return "AMD"
    else:
        return "Unknown"

def check_system():
    system = platform.system()
    if system == 'Windows':
        return "Windows"
    elif system == 'Linux':
        return "Linux"
    else:
        return "Unknown"

def remove_non_numeric(input_string):
    return re.sub(r'[^0-9]', '', input_string)

def split_cmd(cmd):
    return cmd.split(" ")

def remove_special_characters(text):
    pattern = r'[^a-zA-Z0-9_\-\s]'
    clean_text = re.sub(pattern, '', text)
    return clean_text

def create_folder(folder_path):
    try:
        os.makedirs(folder_path, exist_ok=True)
        print(f"Folder created: {folder_path}")
    except Exception as e:
        print(f"Error creating folder: {e}")
