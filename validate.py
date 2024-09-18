import os, hashlib

EXPECTED_HASH = "ABCDEFG"

# Read the content of the script file
with open("main.py", 'rb') as file:
    script_content = file.read()
    script_hash = hashlib.sha256(script_content).hexdigest()
    if script_hash == EXPECTED_HASH:
        print("File Validated")
    else:
        print("File Invalid")

    print(f"SHA-256 hash of the script: {script_hash}")
