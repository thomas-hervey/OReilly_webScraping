from PIL import Image, ImageFilter

import subprocess # for teseract

def pillowExample():
    kitten = Image.open('kitten.jpg')
    blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
    blurryKitten.save("kitten_blured.jpg")
    blurryKitten.show()


# teseract example
def cleanFile(filePath, newFilePath):

    # set a threshold value for the image, and save
    image = image.point(lambda x: 0 if x<143 else 255)
    image.save(newFilePath)

    # call tesseract to do OCR on the newly created image
    subprocess.call(["tesseract", newFilePath, "output"])

    # open and read the resulting data file
    outputFile = open("output.txt", "r")
    print(outputFile.read())
    outputFile.close()

cleanFile("text_2.png", "text_2_clean.png")
