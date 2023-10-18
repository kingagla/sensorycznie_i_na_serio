import numpy as np
import cv2
import os


def localize_objects(path: str) -> dict:
    """Localize objects in the local image using Google Cloud Vision API
    :param path: the file path of the image to localize objects in.
    :return: a dictionary where keys are output file names, and values are pixel vertices
    """
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()
    dict_of_vertices = {}

    with open(path, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    objects = client.object_localization(image=image).localized_object_annotations

    print(f"Number of objects found: {len(objects)}")
    for object_ in objects:
        print(f"\n{object_.name} (confidence: {object_.score})")
        print("Normalized bounding polygon vertices: ")
        vertices = []
        for vertex in object_.bounding_poly.normalized_vertices:
            print(f" - ({vertex.x}, {vertex.y})")
            x, y = vertex.x, vertex.y
            vertices.append([x, y])
        dict_of_vertices[f"{object_.name}.jpg"] = vertices

    return dict_of_vertices


def crop_and_save_object(path: str, dict_of_vertices: dict):
    """
    Crop objects from the image based on pixel vertices and save them as separate output files.
    :param path: the file path of the image from which objects will be cropped.
    :param dict_of_vertices:
    :return:
    """
    for key, value in dict_of_vertices.items():
        input_image_name = os.path.splitext(os.path.basename(path))[0]
        output_folder = os.path.join("images/outputs", f"{input_image_name}_output")
        os.makedirs(output_folder, exist_ok=True)
        image = cv2.imread(path)
        image_height, image_width = image.shape[:2]
        pixel_vertices = np.round(np.array(value) * np.array([image_width, image_height]))
        x, y, w, h = cv2.boundingRect(pixel_vertices.astype(int))
        cropped_image = image[y:y + h, x:x + w]
        output_file = os.path.join(output_folder, key)
        cv2.imwrite(output_file, cropped_image)

