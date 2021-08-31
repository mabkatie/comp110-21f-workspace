"""ex01_relational_operators_for_COMP110."""

__author__ = "730395734"

first_input_function: str = input("Left-hand side: ")
second_input_function: str = input("Right-hand side: ")
left_hand_number: int = 17
right_hand_number: int = 8
print(str(first_input_function) + " < " + str(second_input_function) + " is " + str(bool(left_hand_number < right_hand_number)))
print("17 >= 8 is " + str(bool(left_hand_number >= right_hand_number)))
print("17 == 8 is " + str(bool(left_hand_number == right_hand_number)))
print("17 != 8 is " + str(bool(left_hand_number != right_hand_number)))
