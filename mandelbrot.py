import numpy as np
import numpy.typing as npt
import sys

from numbers import Complex
from PIL import Image
from typing import List, Tuple
# from __future__ import annotations for Python 3.9 <

def norm_square(c: Complex) -> float:

    '''
    Calculates the normalized square of a complex number
    '''

    return c.real**2 + c.imag**2

def escape_time(c: Complex, limit: int) -> int:
    
    z = complex(0, 0)

    for i in range(0, limit):
        if norm_square(z) > 4.0:
            return i
        z = z * z + c
    
    return None


def pixel_to_point(bounds: Tuple[int], pixel: Tuple[int], upper_left: complex, lower_right: complex) -> complex:
    
    width, height = lower_right.real - upper_left.real, upper_left.imag - lower_right.imag

    real_part = upper_left.real + pixel[1] * width / bounds[1]
    im_part = upper_left.imag - pixel[0] * height / bounds[0]

    return complex(real_part, im_part)


def render(pixels: npt.DTypeLike, bounds: Tuple[int], upper_left: complex, lower_right: complex):
    
    assert(pixels.shape == bounds)

    for row in range(0, bounds[0]):
        for column in range(0, bounds[1]):
            point = pixel_to_point(bounds, (row, column), upper_left, lower_right)
            point_escape_time = escape_time(point, 255)

            if point_escape_time == None:
                pixels[row, column] = 0 # it's initialized to 0 anyway, just being explicit
            else:
                pixels[row, column] = 255 - point_escape_time


def save_image(filename: str, pixels: npt.DTypeLike):
    image = Image.fromarray(pixels)
    image = image.convert("L")
    image.save(filename)


# TODO - input validation
def parse_complex(parts: List[str]) -> Complex:
    return complex(float(parts[0]), float(parts[1]))


def main():

    if len(sys.argv) != 5:
        print("Usage: FILE PIXELS UPPERLEFT LOWERRIGHT")
        print("Example: mandel.png 1000x750 -1.20,0.35 -1,0.20")
        sys.exit()
    
    filename: str = sys.argv[1]
    bounds: List[int] = [int(x) for x in sys.argv[2].split("x")]
    rows, columns = bounds[0], bounds[1]
    upper_left: complex = parse_complex(sys.argv[3].split(","))
    lower_right: complex = parse_complex(sys.argv[4].split(","))

    pixels: npt.DTypeLike = np.zeros((rows, columns), dtype=float) # TODO - move this within the render function
    
    render(pixels, (rows, columns), upper_left, lower_right)
    save_image(filename, pixels)


if __name__ == "__main__":
    main()