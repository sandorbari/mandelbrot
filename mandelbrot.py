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
    
    return None

def render(pixels: npt.DTypeLike, bounds: Tuple[int], upper_left: complex, lower_right: complex):
    pass

def save_image(filename: str, pixels: npt.DTypeLike):
    pass

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
    columns, rows = bounds[0], bounds[1]
    upper_left: complex = parse_complex(sys.argv[3].split(","))
    lower_right: complex = parse_complex(sys.argv[4].split(","))

    pixels: npt.DTypeLike = np.zeros((columns, rows))
    
    render(pixels, bounds, upper_left, lower_right)
    save_image(filename, pixels)


if __name__ == "__main__":
    main()