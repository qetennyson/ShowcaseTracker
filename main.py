import csv
import string
import re

name_pattern = re.compile(r'[A-Za-z]+')
phone_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
email_pattern = re.compile(r'[^@]+@[^@]+\.[^@]+')


def print_header():
    print("Hello!  Welcome to the Fern Creek CS Academy Showcase Tracker. \n")
    print("Please complete our interactive form to provide us with your information. \n")


def get_first_name():
    while True:
        first = input("Please enter your First Name: \n")
        if name_pattern.match(first.strip()):
            return first.strip()
        else:
            print("Please use standard characters only.")


def get_last_name():
    while True:
        last = input("Please enter your Last Name: \n")
        if name_pattern.match(last.strip()):
            return last.strip()
        else:
            print("Please use standard characters only.")


def get_parent_email():
    while True:
        email = input("Please enter the email we can contact you at: ")
        if email_pattern.match(email.strip()):
            return email.strip()
        else:
            print("Please enter a valid email or speak to one of us.")


def get_parent_phone():
    while True:
        phone = input("Please enter a contact number like so (###-###-####): ")
        if phone_pattern.match(phone.strip()):
            return phone.strip()
        else:
            print("Please enter a valid phone number as shown.")


def save_info():
    pass


def write_to_file():
    pass


def show_info(first_name, last_name, email='', phone=''):
    print("Here's the info you submitted: \n")
    print(f"{first_name} {last_name} \n{email} \n{phone}\n")

    is_correct = input("Is this correct? (Y/N): ")
    if is_correct[0].lower().strip() == 'y':
        print("\nThanks for verifying your information!\n")
        return True
    else:
        return False


def get_student_info():
    while True:
        student_first = get_first_name()
        student_last = get_last_name()
        if show_info(student_first, student_last):
            student = {
                'first_name': student_first,
                'last_name': student_last,
            }
            print(f"Great, thank you {student_first}!  Please have your parent complete "
                  "the rest of this form.\n")
            return student
        else:
            continue


def get_parent_info():
    while True:
        parent_last = get_last_name()
        parent_first = get_first_name()
        parent_email = get_parent_email()
        parent_phone = get_parent_phone()
        if show_info(parent_first, parent_last, parent_email, parent_phone):
            parent = {
                'first_name': parent_first,
                'last_name': parent_last,
                'parent_email': parent_email,
                'parent_phone': parent_phone,
            }
            return parent
        else:
            continue


def main():
    new_student = {}
    new_parent = {}

    print_header()
    new_student = get_student_info()
    student_first = new_student['first_name']
    student_last = new_student['last_name']

    while True:
        parent_confirm = input(f"Hello!  Are you the parent of {student_first} "
                               f"{student_last}? (Y/N): ")
        if parent_confirm[0].lower().strip() == 'y':
            print("\nThank you, please complete this interactive form so we have your "
                  "information on file with the CS Academy. \n")

            new_parent = get_parent_info()

            break

        else:
            print("Please enter Y to continue as the parent, or Q to quit "
                  "(this will save student information only).")


if __name__ == '__main__':
    main()
