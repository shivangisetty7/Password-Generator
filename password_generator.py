import string
import secrets

def generate_password(length=12, use_lower=True, use_upper=True,
                      use_digits=True, use_symbols=True):
    """Generate a random password based on user preferences."""
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    pools = []
    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append("!@#$%^&*()-_=+[]{};:,.<>?/")

    if not pools:
        raise ValueError("At least one character type must be selected.")

    # Make sure password has at least one character from each selected pool
    password_chars = [secrets.choice(pool) for pool in pools]

    # Fill the rest of the password length with random choices from all pools combined
    all_chars = "".join(pools)
    while len(password_chars) < length:
        password_chars.append(secrets.choice(all_chars))

    # Shuffle characters for randomness
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def check_strength(password: str) -> str:
    """Return a simple strength rating for a given password."""
    length = len(password)

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in "!@#$%^&*()-_=+[]{};:,.<>?/" for c in password)

    score = 0

    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if sum([has_lower, has_upper, has_digit, has_symbol]) >= 3:
        score += 1
    if sum([has_lower, has_upper, has_digit, has_symbol]) == 4:
        score += 1

    if score <= 1:
        return "Weak"
    elif score == 2:
        return "Moderate"
    elif score == 3:
        return "Strong"
    else:
        return "Very Strong"


def main():
    print("=== Password Generator & Strength Checker ===")
    try:
        length = int(input("Enter desired password length (e.g., 12): "))
    except ValueError:
        print("Invalid input. Using default length 12.")
        length = 12

    use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == "y"
    use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == "y"
    use_digits = input("Include digits? (y/n): ").strip().lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == "y"

    try:
        password = generate_password(
            length=length,
            use_lower=use_lower,
            use_upper=use_upper,
            use_digits=use_digits,
            use_symbols=use_symbols,
        )
    except ValueError as e:
        print(f"Error: {e}")
        return

    strength = check_strength(password)

    print("\nGenerated Password:", password)
    print("Password Strength :", strength)
    print("\nTip: Use a mix of letters, numbers, and symbols with at least 12 characters.")


if __name__ == "__main__":
    main()
