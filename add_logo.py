import os
import cv2
from PIL import Image
current_folder=os.getcwd()
destination=f"{current_folder}/phase/tmc_img"

def remove_bg(img_name,destination,img_type):
    img=Image.open(img_name)
    rgba = img.convert("RGBA")
    datas = rgba.getdata()
    newData = []
    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    rgba.putdata(newData)
    rgba.save(f"{destination}.{img_type}", "PNG")


# logo_img=f"{destination}/logo.jpg"
# destination_remove_img=f"{destination}/transparent_logo"
# remove_bg(logo_img,destination_remove_img,"png")
logo_img=cv2.imread(f"{destination}/logo.jpg")
resize_img=cv2.resize(logo_img,(100,100))
cv2.imwrite(f"{destination}/resize.jpg",resize_img)

# for image in os.listdir(destination):
#     image_name=f"{destination}/{image}"
#     im=cv2.imread(image_name)
#     print(image,im.shape)