from os import popen
from glob import glob

# folders-name
input_path = "./img-input"
output_path = "./img-output"

# quality of produced .webp images [0-100]
quality = input("Quality (default 80): ") or "80"

if int(quality) < 0 or int(quality) > 100:
    print("image quality out of range[0-100]")
    exit(0)

img_list = []
for img_name in glob(input_path+'/*'):
    # can use more image types(bmp,tiff,gif)
    if img_name.endswith(".jpg") or img_name.endswith(".png") or img_name.endswith(".jpeg"):
        # extract images' name(image_name.[jpg|png]) from the full path
        img_list.append(img_name.split('\\')[-1])
# print(img_list)   # debug

for img_name in img_list:
    cmd ='"bin/cwebp" \"'+input_path+'/'+img_name+'\" -q '+quality+' -o \"'+output_path+'/'+(img_name.split('.')[0])+'.webp\"'
    popen(cmd)
    # print(cmd)    # debug
