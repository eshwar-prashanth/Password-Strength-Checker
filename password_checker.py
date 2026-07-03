import re

def check_password_strength(password):
    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Password should be at least 8 characters long.")

    # Check uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Check lowercase letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Check digit
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # Check special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    # Determine strength
    if score == 5:
        strength = "🟢 Strong"
    elif score >= 3:
        strength = "🟡 Medium"
    else:
        strength = "🔴 Weak"

    return strength, suggestions


def main():
    print("=" * 45)
    print("      PASSWORD STRENGTH CHECKER")
    print("=" * 45)

    password = input("\nEnter your password: ")

    strength, suggestions = check_password_strength(password)

    print("\nPassword Strength:", strength)

    if suggestions:
        print("\nSuggestions to improve your password:")
        for suggestion in suggestions:
            print("•", suggestion)
    else:
        print("\nExcellent! Your password meets all security requirements.")

    print("\nThank you for using Password Strength Checker!")


if __name__ == "__main__":
    main()
