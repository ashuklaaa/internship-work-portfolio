import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Criteria 1: Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Criteria 2: Uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Criteria 3: Lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Criteria 4: Digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")

    # Criteria 5: Special characters
    if re.search(r'[^a-zA-Z0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    strength_messages = {
        0: "Very Weak",
        1: "Weak",
        2: "Moderate",
        3: "Good",
        4: "Strong",
        5: "Very Strong"
    }

    print(f"Password Strength: {strength_messages.get(score, 'Unknown')}")
    if feedback:
        print("Feedback:")
        for item in feedback:
            print(f"- {item}")

# Example usage:
password_to_check = input("Enter a password to check: ")
check_password_strength(password_to_check)