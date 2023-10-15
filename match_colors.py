import numpy as np
from PIL import Image, ImageDraw
from patterns import complement

def generate_color():
    return tuple(np.random.choice(range(256), size=3))

# Rozmiar obrazu
width = 400
height = 200

# Inicjalizacja obrazu
image = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(image)

# Kolor kwadratu 1
color1 = generate_color()

# Kolor kwadratu 2
color2_orig = complement(*color1)
color2 = np.array(color2_orig)/255 + np.random.exponential(1/10, size=3)
color2 *= 255
difference = np.array(color2_orig) - color2
color2 = tuple(color2.astype(int))

# Wymiary i pozycja kwadratu 1
x1 = 0
y1 = 0
size1 = 200

# Wymiary i pozycja kwadratu 2
x2 = 200
y2 = 0
size2 = 200

# Rysowanie kwadratów
draw.rectangle([x1, y1, x1 + size1, y1 + size1], fill=color1)
draw.rectangle([x2, y2, x2 + size2, y2 + size2], fill=color2_orig)
draw.rectangle([x2, y2, x2 + size2, y2 + size2], fill=color2)

# Zapis obrazu
image.save("two_squares.png")

# Wyświetlenie obrazu
image.show()
