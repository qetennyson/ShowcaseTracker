import csv
import sys
import re
import time
import pizza_roll_panic as pizza_roll

# TODO: Refactor main functions into a module.
# TODO: Frame transition to game as "Your student needs to take a quick test to complete the process"

name_pattern = re.compile(r'[A-Za-z]+')
phone_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
email_pattern = re.compile(r'[^@]+@[^@]+\.[^@]+')

# TODO: PK should just be the final appended number.
# Theoretically, you could set the PK to dummy data here, and then
# the PK is always based on the final appended values, but that
# seems janky.
student_pk = 0
parent_pk = 0


def print_student_header():
    print("Hello!  Welcome to the Fern Creek CS Academy Showcase Tracker (we built this!). \n")
    print("Please complete our interactive form to provide us with your information. \n")


def print_parent_header(s_first, s_last):
    print(f"Please have the parent of {s_first} {s_last} "
          f"continue this form.\n".upper())


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


# TODO: Refactor CSV code below to here.
def save_info():
    pass


# TODO: Are these going to be different?
def write_to_file():
    pass


def show_info(first_name, last_name, email='', phone=''):
    """

    :param first_name: Parent/Student FN
    :param last_name: Parent/Student LN
    :param email: Parent Only
    :param phone: Parent Only
    :return: Boolean to indicate information is correct/incorrect.
    """
    print("Here's the info you submitted: \n")
    print(f"{first_name} {last_name} \n{email} \n{phone}\n")

    is_correct = input("Is this correct? (Y/N): ")
    if is_correct[0].lower().strip() == 'y':
        print("\nThanks for verifying your information!\n")
        return True
    else:
        return False


def get_student_info():
    """

    :return: student dictionary containing verified student FN, LN.
    """
    while True:
        student_first = get_first_name()
        student_last = get_last_name()
        if show_info(student_first, student_last):
            student = {
                'id': student_pk,
                'first_name': student_first,
                'last_name': student_last,
            }
            return student
        else:
            continue


def get_parent_info():
    """

    :return: parent dictionary containing verified FN, LN, email, phone.
    """
    while True:
        parent_first = get_first_name()
        parent_last = get_last_name()
        parent_email = get_parent_email()
        parent_phone = get_parent_phone()
        if show_info(parent_first, parent_last, parent_email, parent_phone):
            parent = {
                'id': parent_pk,
                'first_name': parent_first,
                'last_name': parent_last,
                'parent_email': parent_email,
                'parent_phone': parent_phone,
            }
            return parent
        else:
            continue


def check_admin_pass(password):
    return password == 'cheesecake'


def admin_menu():
    admin_cmd = input("[C]lose and save the roster, or restart [P]izza Panic: ")
    if admin_cmd.lower().strip()[0] == 'c':
        """ Shuts the program down and saves the CSV  !! RESETS PKs (maybe fix this)!!"""
        while True:
            confirm = input("Are you sure you want to finalize the roster and close the program? ("
                            "Y/N): \n")
            if confirm[0].lower().strip() == 'y':
                sys.exit()
            elif confirm[0].lower().strip() == 'n':
                break
            else:
                print("Enter a valid command.\n")
    elif admin_cmd.lower().strip()[0] == 'p':
        while True:
            confirm = input("Are you sure you want to start a game of Pizza Roll Panic (Y/N): \n")
            if confirm.lower().strip()[0] == 'y':
                pizza_roll.pizza_main()
            else:
                break


def main():
    # Maintains primary key count for student/parent dictionaries.
    global student_pk
    global parent_pk

    while True:
        new_student = {}
        new_parent = {}

        cmd = input("Type [n]ew to add contact information, or "
                    "[a] to enter admin mode: \n")
        if cmd[0].lower().strip() == 'n':

            # Displays a student-oriented greeting.
            print_student_header()

            new_student = get_student_info()

            # increment the student PK (globally)
            student_pk += 1

            # Grab these just for use in print_parent_header.
            student_first = new_student['first_name']
            student_last = new_student['last_name']

            # Displays a parent-oriented greeting.
            print_parent_header(student_first, student_last)

            new_parent = get_parent_info()

            # increment the parent PK (globally)
            parent_pk += 1

            print("\n *** STUDENT MUST FINISH FORM! *** \n")
            time.sleep(6)
            print("\n...\n")
            time.sleep(6)

            verify_student = input(f"Are you back {student_first} {student_last}?  Enter Y to continue: ")
            try:
                if verify_student.lower().strip()[0] == 'y':
                    print(f"\nWelcome back, {student_first} {student_last}.  We have a short test for you.\n")
                    time.sleep(4)
                    print(f"\nDon't worry, everyone passes, we just want to see how you do.\n")
                    pizza_roll.pizza_main()
            except IndexError:
                continue

            # appends the student and parent dictionaries
            with open('roster.csv', 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(new_student.values())
                writer.writerow(new_parent.values())

        elif cmd[0].lower().strip() == 'a':
            wrong_count = 0
            while True:
                password = input("Enter the admin password or e[x]it (hint: an offtrack conversation is?): ")
                if check_admin_pass(password):
                    admin_menu()
                elif password == 'x':
                    break
                else:
                    print("Incorrect password.")
                    wrong_count += 1

                if wrong_count >= 3:
                    print("Too many incorrect passwords.")
                    time.sleep(2)
                    break


        else:
            print("Enter a valid command or ask for help.")


if __name__ == '__main__':
    main()
