"""ex01_relational_operators_for_COMP110."""

__author__ = "730395734"

input_variable_one: str = input("Left-hand side: ")
input_variable_two: str = input("Right-hand side: ")
left_hand_number: int = int(input_variable_one)
right_hand_number: int = int(input_variable_two)
print(input_variable_one + " < " + input_variable_two + " is " + str(bool(left_hand_number < right_hand_number)))
print(input_variable_one + " >= " + input_variable_two + " is " + str(bool(left_hand_number >= right_hand_number)))
print(input_variable_one + " == " + input_variable_two + " is " + str(bool(left_hand_number == right_hand_number)))
print(input_variable_one + " != " + input_variable_two + " is " + str(bool(left_hand_number != right_hand_number)))
