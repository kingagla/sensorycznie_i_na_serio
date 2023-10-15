import os
from initial import localize_objects, crop_and_save_object

def main():
    file_name = "test.png"
    folder_name = "images/inputs"
    folder_path = os.path.join(os.getcwd(), folder_name)
    file_list = os.listdir(folder_path)
    for file in file_list:
        file_path = os.path.join(folder_path, file)
        dict_of_vertices = localize_objects(file_path)
        crop_and_save_object(file_path, dict_of_vertices)




if __name__ == main():
    main()
