
import os
from google.cloud import vision




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
            print(f"fraction: {color.pixel_fraction}")
            print(f"\tr: {color.color.red}")
            print(f"\tg: {color.color.green}")
            print(f"\tb: {color.color.blue}")



        if response.error.message:
            raise Exception(
                "{}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors".format(response.error.message)
            )


def main():
    file_name = "test.png"
    folder_name = "images/inputs"
    folder_path = os.path.join(os.getcwd(), folder_name)
    file_list = os.listdir(folder_path)
    for file in file_list:
        file_path = os.path.join(folder_path, file)
        detect_dominant_color(file_path)
        # dict_of_vertices = localize_objects(file_path)
        # crop_and_save_object(file_path, dict_of_vertices)


if __name__ == main():
    main()
