import hashlib

SCRIPT_HASH = "ABCDEFG"

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
        
def challenge_1():
    solution_hash = "aca4fee155368758392aca3a58e5704c8650173981160328f27181fcf67b68e4"
    with open("challenge_1.txt", 'rb') as file:
        file_content = file.read()
        file_hash = hashlib.sha256(file_content).hexdigest()
        file_case_hash = hashlib.sha256(file_content.upper()).hexdigest()
        if file_hash == solution_hash:
            print("Correct! The password is RAINBOW.")
        elif file_case_hash == solution_hash:
            print("Please check your capitalization and try again.")
        else:
            print("Sorry, that's not the right answer.")

if validate():##
    challenge_1()

# print(hashlib.sha256("RAINBOW".encode("utf-8")).hexdigest())