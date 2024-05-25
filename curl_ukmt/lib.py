import platform
import re
import os
from bs4 import BeautifulSoup

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

import re

def remove_special_characters(text):
    pattern = r'[^a-zA-Z0-9_\-\s]'
    clean_text = re.sub(pattern, '', text)
    return clean_text

def create_folder(folder_path):
    try:
        # Create the folder
        os.makedirs(folder_path, exist_ok=True)
        print(f"Folder created: {folder_path}")
    except Exception as e:
        print(f"Error creating folder: {e}")

def find_pdf_links_in_file(file_path):
    """
    Find all PDF links in an HTML file.

    :param file_path: The path to the HTML file.
    :return: A list of URLs pointing to PDF files.
    """
    pdf_links = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            for link in soup.find_all('a', href=True):
                href = link['href']
                if href.lower().endswith('.pdf'):
                    pdf_links.append(href)
    except Exception as e:
        print(f"An error occurred: {e}")

    return pdf_links