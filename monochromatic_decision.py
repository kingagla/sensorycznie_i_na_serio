import numpy as np
from random import randint
from converting import hex2rgb

def decide_if_monochromatic(avarage_values: list[np.array]) -> bool:
    """
    Function expects list of np.array object which has values 
    of avarage pixel in given clothing.

    It will take under consideration only 2 first objects supplied.
    """
    tolereance_r: int = 30
    tolereance_g: int = 30
    tolereance_b: int = 30

    obj1: np.array = avarage_values[0]
    obj2: np.array = avarage_values[1]

    if abs(obj1[0]-obj2[0]) >= tolereance_r:
        return False
    if abs(obj1[1]-obj2[1]) >= tolereance_g:
        return False
    if abs(obj1[2]-obj2[2]) >= tolereance_b:
        return False    
    return True


def validate(number: int) -> int:
    if number < 0:
        return 0
    if number > 255:
        return 255
    return number

for i in range(5):
    test_r = randint(-30, 30)
    test_g = randint(-30, 30)
    test_b = randint(-30, 30)
    x = np.array([randint(1, 255),randint(1, 255), randint(1, 255)])


    input = [x, np.array([validate(x[0]+test_r), validate(x[1]+test_g), validate(x[2]+test_b)])]

    output = decide_if_monochromatic(input)

    print(output, "--", x, input[1])

    import numpy as np
    from PIL import Image, ImageDraw
    from patterns import complement

    def generate_color():
        return tuple(x)

    # Rozmiar obrazu
    width = 400
    height = 200

    # Inicjalizacja obrazu
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

    # Kolor kwadratu 1
    color1 = tuple(x)
    color2 = tuple(input[1].astype(int))

    # Kolor kwadratu 2



    # Wymiary i pozycja kwadratu 1
    x1 = 0
    y1 = 0
    size1 = 200

    # Wymiary i pozycja kwadratu 2
    x2 = 200
    y2 = 0
    size2 = 200

    # Rysowanie kwadratów
    #draw.text(xy=(0,0))
    draw.rectangle([x1, y1, x1 + size1, y1 + size1], fill=color1)
    draw.rectangle([x2, y2, x2 + size2, y2 + size2], fill=color2)

    #draw.rectangle([x2, y2, x2 + size2, y2 + size2], fill=color2)

    # Zapis obrazu
    
    # Wyświetlenie obrazu
    # image.show()
    image.close()
