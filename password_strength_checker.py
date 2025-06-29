import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Check length
    if len(password) >= 8:
        strength += 1

    # Check for lowercase and uppercase
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        strength += 1

    # Check for digits
    if re.search("[0-9]", password):
        strength += 1

    # Check for special characters
    if re.search("[@_!#$%^&*()<>?/\\|}{~:]", password):
        strength += 1

    # Evaluate strength
    if strength == 4:
        remarks = "Very Strong 💪"
    elif strength == 3:
        remarks = "Strong 👍"
    elif strength == 2:
        remarks = "Moderate ⚠️"
    else:
        remarks = "Weak ❌"

    return remarks

def main():
    print("🔐 Password Strength Checker")
    pwd = input("Enter your password: ")
    result = check_password_strength(pwd)
    print("Password Strength:", result)

if __name__ == "__main__":
    main()
