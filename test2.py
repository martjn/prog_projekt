import os
import imghdr

def files(path="."):
    return os.listdir(path)

def imgs_in_folder(arg):
    images = set()
    for el in arg:
        img = imghdr.what(el)
        if img:
            images.add(el)
    if len(images):
        return images
    return None

ls = files()
images = imgs_in_folder(ls)


print("All files in dir")
print(ls)
print("\nAll images in dir")
print(images)

if images != None:
    for i in images:
        print(i)
