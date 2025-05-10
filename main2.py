from vowel_counter import count_vowels
from char_position_finder import find_positions_of_i
from star_patterns import print_right_aligned_star_array, pyramid
from sort_numbers import sort_input_numbers
from user_validation import validate_user_input
from user_authentication import authenticate_user
from advanced_email_validation import advanced_email_validation
from multiplication_tools import multiplication_tables, generate_multiplication_array

def main():
    # ------------------ String Analysis ------------------
    print("\n--- Vowel Counter ---")
    s = input("Enter a string for vowel count: ")
    print("Number of vowels in the string:", count_vowels(s))

    print("\n--- Character Position Finder ---")
    s = input("Enter a string to find positions of 'i': ")
    positions = find_positions_of_i(s) 
    print("Positions of 'i' in the string:", positions)

    # ------------------ Multiplication Tools ------------------
    print("\n--- Multiplication Table ---")
    x = int(input("Enter your number for multiplication table: "))
    multiplication_tables(x)

    print("\n--- Multiplication Table (2D Array Format) ---")
    generate_multiplication_array()

    # ------------------ Sorting and Validation ------------------
    print("\n--- Number Sorting ---")
    sort_input_numbers()

    print("\n--- User Validation ---")
    validate_user_input()

    print("\n--- User Authentication ---")
    authenticate_user()

    print("\n--- Advanced Email Validation ---")
    advanced_email_validation()

    print("\n--- Pyramid ---")
    h = int(input("Enter the height of the pyramid: "))
    for line in pyramid(h):
        print(line)

    print("\n--- Right Aligned Star Array ---")
    h = int(input("Enter the height for right-aligned stars: "))
    print_right_aligned_star_array(h)

if __name__ == "__main__":
    main() 


