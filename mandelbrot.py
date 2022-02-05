import cmath
import sys

from numbers import Complex
from PIL import Image
from typing import List

def escape_time(c: Complex):
    pass

def save_image():
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
    upperleft: Complex = parse_complex(sys.argv[3].split(","))
    lowerright = parse_complex(sys.argv[4].split(",")) # TODO - add type hint here as well; left out for demonstration purposes

if __name__ == "__main__":
    main()