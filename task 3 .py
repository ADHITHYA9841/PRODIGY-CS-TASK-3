
print("##### PASSWORD COMPLEXITY CHECK TOOL #####")
print("##### BY ADHITHYA MANGALAMPETA #####")
def assess_password_strength(password):
    criteria = {
        "length": False,
        "uppercase": False,
        "lowercase": False,
        "number": False,
        "special": False
    }

    if len(password) >= 8:
        criteria["length"] = True
    
    for char in password:
        if char.isupper():
            criteria["uppercase"] = True
        elif char.islower():
            criteria["lowercase"] = True
        elif char.isdigit():
            criteria["number"] = True
        elif not char.isalnum():
            criteria["special"] = True

    score = sum(criteria.values())

    feedback = {
        0: "Very Weak: Password should be at least 8 characters long and contain uppercase, lowercase, numbers, and special characters.",
        1: "Weak: Password should be at least 8 characters long and contain uppercase, lowercase, numbers, and special characters.",
        2: "Moderate: Password should be at least 8 characters long and contain a mix of uppercase, lowercase, numbers, and special characters.",
        3: "Fair: Password should be at least 8 characters long and contain a mix of uppercase, lowercase, numbers, and special characters.",
        4: "Strong: Password should be at least 8 characters long and contain a mix of uppercase, lowercase, numbers, and special characters.",
        5: "Very Strong: Password is strong."
    }

    strength = feedback[score]

    return {"strength": strength, "score": score}

password = input("Enter password: ")
result = assess_password_strength(password)

print("Password Strength:", result["strength"])
print("Password Score:", result["score"])
