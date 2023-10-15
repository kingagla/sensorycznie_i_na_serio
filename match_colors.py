import numpy as np
from PIL import Image, ImageDraw, ImageFont
from patterns import complement, monochrome
from converting import rgb2hex, hex2rgb
from pathlib import Path
def generate_color():
    return tuple(np.random.choice(range(256), size=3))

def is_significant(color1, color2, tolerance=15):
    r1, g1, b1 = color1
    color2_orig = complement(r1, g1, b1)
    r2, g2, b2 = color2
    r1, g1, b1 = color2_orig

    over_tolerance = [np.abs(x[0] - x[1]) > tolerance for x in [(r1, r2), (g1, g2), (b1, b2)]]
    return any(over_tolerance)



def plot_difference(color, pattern_func, difference, path):
    # Rozmiar obrazu
    width = 400
    height = 500

    # Inicjalizacja obrazu
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

    # Kolor kwadratu 2
    color2_orig = pattern_func(*color)
    color2 = np.array(color2_orig) + difference # np.random.exponential(1/10, size=3)
    # color2 *= 255
    color2 = np.clip(color2, 0, 255)
    difference = np.array(color2_orig) - color2
    color2 = tuple(color2.astype(int))

    # Wymiary i pozycja kwadratu 1 (górny lewy)
    x1 = 0
    y1 = 300
    size1 = 200

    # Wymiary i pozycja kwadratu 2 (górny prawy)
    x2 = 200
    y2 = 300
    size2 = 200

    # Rysowanie kwadratów (górna część)
    draw.rectangle([x1, y1, x1 + size1, y1 + size1], fill=color)
    draw.rectangle([x2, y2, x2 + size2, y2 + size2], fill=color2_orig)

    # Wymiary i pozycja kwadratu 3 (dolny lewy)
    x3 = 0
    y3 = 0
    size3 = 200

    # Wymiary i pozycja kwadratu 4 (dolny prawy)
    x4 = 200
    y4 = 0
    size4 = 200

    # Rysowanie kwadratów (dolna część)
    draw.rectangle([x3, y3, x3 + size3, y3 + size3], fill=color)
    draw.rectangle([x4, y4, x4 + size4, y4 + size4], fill=color2)

    # Dodawanie napisu o różnicy kolorów
    text = f"Difference (R, G, B): {difference}. Over tolerance: {is_significant(color2_orig, color2)}"
    draw.text((10, 250), text, fill="white", font=ImageFont.truetype(font='./arial.ttf', size=16))

    # # Zapis obrazu
    image.save(path)

    # # Wyświetlenie obrazu
    # image.show()

def main():
    n_rounds = 10
    r = 20
    color1 = generate_color()
    hex = rgb2hex(*color1)
    directory = Path(f"./pic/{hex.replace('#', '')}")
    directory.mkdir(parents=True, exist_ok=True)

    random = True
    if random:
        diffs = [np.random.randint(-r, r, 3) for _ in range(n_rounds)]
    else:
        diffs = np.linspace(0, 50, 10)

    for i, diff in enumerate(diffs):

        path = directory / f"{i}.png"
        plot_difference(color1, complement, diff, path)


if __name__ == '__main__':
    color1 = hex2rgb("#a96842")
    color2 = hex2rgb("#253754")
    print(is_significant(color1, color2, 80))
    # main()