# ============================================================
#  Password Strength Checker
#  DecodeLabs Industrial Training Kit — Project 1
# ============================================================

import re
import hmac

COMMON_PASSWORDS = {
    "password", "123456", "qwerty", "abc123", "letmein",
    "iloveyou", "admin", "welcome", "monkey", "dragon",
    "111111", "123456789", "password1", "sunshine", "master"
}

def check_password_strength(password: str) -> dict:
    has_length = len(password) >= 8
    has_upper  = any(c.isupper() for c in password)
    has_digit  = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    is_common = any(
        hmac.compare_digest(password.lower(), p) for p in COMMON_PASSWORDS
    )

    criteria = {
        "length"   : has_length,
        "uppercase": has_upper,
        "digit"    : has_digit,
        "symbol"   : has_symbol,
    }

    # Rule: length < 8 = immediate Weak (no further checks)
    # Rule: length >= 8, check uppercase + digit + symbol (3 criteria)
    #   - 1 or 2 met = Medium
    #   - all 3 met  = Strong
    extra_score = sum([has_upper, has_digit, has_symbol])

    if is_common or not has_length:
        strength = "Weak"
    elif extra_score <= 2:
        strength = "Medium"
    else:
        strength = "Strong"

    return {
        "strength" : strength,
        "criteria" : criteria,
        "is_common": is_common,
    }


def display_result(password: str, result: dict) -> None:
    bars     = {"Weak": "###", "Medium": "######", "Strong": "#########"}
    colors   = {"Weak": "\033[91m", "Medium": "\033[93m", "Strong": "\033[92m"}
    RESET    = "\033[0m"

    color = colors[result["strength"]]
    bar   = bars[result["strength"]]

    print("\n" + "=" * 45)
    print(f"  Password : {'*' * len(password)}")
    print(f"  Strength : {color}{result['strength']}{RESET}")
    print(f"  {color}[{bar}]{RESET}")
    print("-" * 45)

    checks = {
        "length"   : "At least 8 characters",
        "uppercase": "Uppercase letter [A-Z]",
        "digit"    : "Contains a digit [0-9]",
        "symbol"   : "Contains a symbol [!@#$...]",
    }

    for key, label in checks.items():
        status = "\033[92m✔\033[0m" if result["criteria"][key] else "\033[91m✘\033[0m"
        print(f"  {status}  {label}")

    if result["is_common"]:
        print(f"\n  \033[91m⚠ Found in leaked password lists!\033[0m")

    print("=" * 45 + "\n")


def main():
    print("\n  DecodeLabs — Password Strength Checker")
    print("  Type 'quit' to exit.\n")

    while True:
        password = input("  Enter password: ")
        if password.lower() == "quit":
            print("  Exiting. Stay secure!\n")
            break
        if not password:
            print("  Please enter a password.\n")
            continue
        result = check_password_strength(password)
        display_result(password, result)


if __name__ == "__main__":
    main()