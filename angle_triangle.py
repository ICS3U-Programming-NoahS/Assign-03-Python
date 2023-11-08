#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Nov. 7th, 2023
# This program asks the user to enter two of the angles of a triangle
# then tells the user if the type of triangle it is


def main():
    # Get first angle
    angle_a_string = input("Enter angle a: ")

    # Get second angle
    angle_b_string = input("Enter angle b: ")

    # Making sure the angles are integers
    try:
        angle_a_int = int(angle_a_string)
        try:
            angle_b_int = int(angle_b_string)

            angle_c = 180 - angle_a_int - angle_b_int

            # Finding the type of triangle
            if angle_a_int == angle_b_int:
                if angle_a_int == 60:
                    print("The triangle is equilateral.")
                else:
                    print("The triangle is isosceles.")
            elif angle_c <= 0 or angle_a_int <= 0 or angle_b_int <= 0:
                print(
                    "It is not possible for the angles {} and {} to make up a triangle.".format(
                        angle_a_int, angle_b_int
                    )
                )
            elif (
                angle_a_int == angle_b_int
                or angle_a_int == angle_c
                or angle_b_int == angle_c
            ):
                print("The triangle is isosceles.")
            else:
                print("The triangle is scalene.")
        except:
            print("{} is not an integer.".format(angle_b_string))
    except:
        print("{} is not an integer.".format(angle_a_string))
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
