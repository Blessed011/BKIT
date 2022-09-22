from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import cowsay


def main():
    r = Rectangle("синего", 16, 16)
    c = Circle("зеленого", 16)
    s = Square("красного", 16)
    print(r)
    print(c)
    print(s)
    cowsay.cow('done!')

if __name__ == "__main__":
    main()