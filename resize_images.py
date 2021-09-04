from PIL import Image 
import os

fit_size = input("Enter Size : ")
try:
    fit_size = int(fit_size)
except:
    print("Invalid Input")
    quit()
output_folder = input("Enter Output Folder Name : ")

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

for filename in os.listdir("."):
    if not filename.endswith((".png", ".jpg", ".jpeg", ".jfif")):
        continue

    # open image
    image = Image.open(filename)

    # image size
    width, height = image.size

    if width > fit_size and height > fit_size:
        if width > height :
            height = int((fit_size/width)*height)
            width = fit_size

        else:
            width = int((fit_size/height)*width)
            height = fit_size

        image = image.resize((width, height))
        print("resizing " + filename + " ...")

    image = image.save(os.path.join(output_folder, filename))

    print("---------------")

print("Done All Images")
