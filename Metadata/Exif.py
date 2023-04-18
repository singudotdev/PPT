from PIL import Image
from PIL.ExifTags import TAGS


def exif(imgFileName):
    try:
        exifData = {}
        imgFile = Image.open(imgFileName)
        info = imgFile.getexif()
        print(info)

        if info:
            for (tag, value) in info.items():
                decoded = TAGS.get(tag, tag)
                exifData[decoded] = value
            exifGPS = exifData["GPSInfo"]
            if exifGPS:
                print("[*]", imgFileName, "GPS DATA:", exifGPS)

    except:
        pass


exif(input("Insert file path: "))
