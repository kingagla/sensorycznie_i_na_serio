
import os
from google.cloud import vision

import numpy as np


def detect_dominant_color(path):
    """Detects image properties in the file."""

    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.image_properties(image=image)
    props = response.image_properties_annotation
    print("Properties:")
    
    for color in props.dominant_colors.colors:
        print("------ Ddetect dominant values -----------")
        print(f"fraction: {color.pixel_fraction}")
        print(f"\tr: {color.color.red}")
        print(f"\tg: {color.color.green}")
        print(f"\tb: {color.color.blue}")
        break

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
    return np.array([color.color.red, color.color.green, color.color.blue])


def main():
    file_name = "/Users/mstopins/Desktop/sensorycznie_i_na_serio/Jeans.jpg"
    folder_name = "" #"images/inputs"
    folder_path = os.path.join(os.getcwd(), folder_name)
    file_list = os.listdir(folder_path)
    x = detect_dominant_color(file_name)

if __name__ == main():
    main()
