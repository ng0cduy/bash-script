from lib import *
import subprocess
cur_dir = os.getcwd()
temp_url="https://ukmt.org.uk/competition-papers/jsf/jet-engine:free-past-papers/tax/challenge-type:75/"
temp_url="https://ukmt.org.uk/competition-papers/jsf/jet-engine:free-past-papers/tax/challenge-type:"
file_input = "test.txt"
with open(file_input,"r") as f:
    lines = f.readlines()
folder_and_link_list=[]
for line in lines:
    line = line.strip().split(",")
    url =f"{temp_url}{line[0]}/"
    link_folder = f"{cur_dir}/{line[1].replace(' ','-')}"
    folder_and_link_list.append([url,link_folder])

for item in folder_and_link_list:
    url = item[0]
    folder = item[1]
    create_folder(folder_path=folder)
    curl_cmd = split_cmd(f"curl -o {folder}/temp.html {url}")
    subprocess.run(curl_cmd)
    pdf_links = find_pdf_links_in_file(f"{folder}/temp.html")
    for pdf_link in pdf_links:
        file_name = pdf_link.split("/")[-1]
        curl_file_cmd= split_cmd(f"curl -o {folder}/{file_name} {pdf_link}")
        subprocess.run(curl_file_cmd)
    subprocess.run(split_cmd(f"rm -rf {folder}/temp.html"))