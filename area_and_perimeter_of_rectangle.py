#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on August 2020
# This program calculates the area and perimeter of a rectangle
#   with user input


def main():
    # This function calculates area and perimeter

    # Input
    length = int(input("Enter length of rectangle (mm): "))
    width = int(input("Enter width of rectangle (mm): "))

    # Process
    area = length*width
    perimeter = 2*(length+width)

    # Output
    print("")
    print("Area is {}mm^2".format(area))
    print("Perimeter is {}mm".format(perimeter))


if __name__ == "__main__":
    main()
