import os
from src.initial import localize_objects, crop_and_save_object
from src.dominant_color import detect_dominant_color
from src.match_colors import check_complementary
from src.monochromatic_decision import decide_if_monochromatic
import json

def main():
    colors = {}
    folder_name = "images/inputs"
    folder_path = os.path.join(os.getcwd(), folder_name)
    file_list = [item for item in os.listdir(folder_path) if item != ".gitkeep"]
    for file in file_list:
        file_path = os.path.join(folder_path, file)
        dict_of_vertices = localize_objects(file_path)
        crop_and_save_object(file_path, dict_of_vertices)

    folder_name = "images/outputs/test_Michal_2_output"
    folder_path = os.path.join(os.getcwd(), folder_name)
    file_list = [item for item in os.listdir(folder_path) if item.endswith("jpg")]
    for file in file_list:
        file_path = os.path.join(folder_path, file)
        colors[file_path] = detect_dominant_color(file_path)

    clothes = {key.split("/")[-1].replace(".jpg",""): val for key, val in colors.items() if "Pants" in key or "Outerwear" in key}

    wear_types = {}
    wear_types['complementary'] = check_complementary(clothes["Pants"], clothes["Outerwear"], (60, 40, 40))

    wear_types['monochromatic'] = decide_if_monochromatic([clothes["Pants"], clothes["Outerwear"]])

    with open(os.path.join(folder_name, "output2.json"), 'w') as f:
        json.dump(wear_types, f)





if __name__ == "__main__":
    main()
