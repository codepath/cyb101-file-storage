import hashlib, time
from simple_term_menu import TerminalMenu

SCRIPT_HASH = "d464563066dead6703d4f9e98327205848913cf4e338a05930c5330adfd85976"

def dramatic_print(strings):
    for string in strings:
        print(string, end="", flush=True)
        time.sleep(.8)

# Validates that main.py has not been altered
def validate():
    with open("main.py", 'rb') as file:
        script_content = file.read()
        script_hash = hashlib.sha256(script_content).hexdigest()
        if script_hash == SCRIPT_HASH:
            return True
        else:
            print("ERROR: Your main.py file has been altered.")
            print("To proceed, please reset main.py to its original state.")
            print("(Keep in mind, even an extra space counts as 'altered'!)")
            return False

def check_challenge(challenge_file, solution_hash):
    with open(challenge_file, 'rb') as file:
        file_content = file.read()
        file_hash = hashlib.sha256(file_content).hexdigest()
        file_case_hash = hashlib.sha256(file_content.upper()).hexdigest()
        dramatic_print([f"Checking {challenge_file}.", ".", ". "])
        if file_hash == solution_hash:
            print(f"✅ Correct!  The password is {file_content.decode('utf-8')}.")
            return True
        elif file_case_hash == solution_hash:
            print("⚠️ Please check your capitalization and try again.")
            return False
        else:
            print("⛔ Sorry, that's not the right answer.")
            return False

dramatic_print([f"Validating scripts.", ".", ". "])
if validate():
    print("Validated.")
else:
    exit()

with open('applicant.txt', 'r') as file:
    user = file.read().lower().strip()
    user_hash = hashlib.sha256((user+"+Sp25").encode('utf-8')).hexdigest()[-6:]
    print()

    print(f"Welcome to CYB101 Prework")
    print()
    print(f"Your email is: '{user}'")
    email_menu = TerminalMenu(["[y]", "[n]"], title="Is the above email correct?")
    if email_menu.show() == 1:
        print(f"Please correct your email in 'applicant.txt' before proceeding.")
        exit()
    
    while True:
        options = [
            "[0] Check All Challenges", 
            "[1] Check Challenge 1 only",
            "[2] Check Challenge 2 only",
            "[3] Check Challenge 3 only", 
            "[4] Exit"]
        main_menu = TerminalMenu(options, title="Please select an option:")
        response = main_menu.show()

        if response == 4:
            print("Goodbye.")
            exit()

        print()
        c1, c2, c3 = False, False, False
        if response == 0 or response == 1:
            c1 = check_challenge("challenge_1.txt", "aca4fee155368758392aca3a58e5704c8650173981160328f27181fcf67b68e4")
        if response == 0 or response == 2:
            c2 = check_challenge("challenge_2.txt", "fd65204fde7b3236df176170aaffb6116533b241c30ce28b910f9872b3f9747b")
        if response == 0 or response == 3:
            c3 = check_challenge("challenge_3.txt", "6f93481fe2c111b1c44176bfa27e6461bf26668e0c6c31fab4a32fa8a4f663e5")

        if c1 and c2 and c3:
            with open('applicant.txt', 'rb') as file:
                user_hash = hashlib.sha256(file.read()+"+Sp25".encode('utf-8')).hexdigest()[-6:]
            print()
            print("🎉 CYB101 Prework complete! 🎉")
            dramatic_print([f"Generating code for {user}.", ".", ". "])
            dramatic_print([f"Your ✨ magic code is: ", f"{user_hash}\n"])
            print()
            print("To receive credit, submit your challenge answers")
            print("and ✨ magic code by following the instructions at:")
            print("\thttps://courses.codepath.org/snippets/cyb102/prework")
            print()
            exit()