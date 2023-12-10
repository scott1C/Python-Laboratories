def password_strength(password):
    strength = 0
    lower = upper = numeric = special = repeat = consecutive = 0

    for i in range(len(password)):
        if (
            i >= 1
            and "0" <= password[i] <= "9"
            and "0" <= password[i - 1] <= "9"
            and (int(password[i]) - int(password[i - 1])) == 1
        ):
            consecutive += 1
        if i >= 2 and password[i] == password[i - 1] == password[i - 2]:
            repeat += 1
        if "0" <= password[i] <= "9":
            numeric += 1
        elif "a" <= password[i] <= "z":
            lower += 1
        elif "A" <= password[i] <= "Z":
            upper += 1
        elif password[i] in '~`!@#$%^&*()-_+={}[]|\;:"<>,./?':
            special += 1

    missing_types = 4 - bool(lower) - bool(upper) - bool(numeric) - bool(special)
    strength = missing_types + repeat + consecutive

    if len(password) < 8:
        return 8 - len(password)
    elif len(password) > 20:
        return len(password) - 20

    if strength == 0:
        return "good"
    else:
        return strength


password = input("Enter your password: ")
print(password_strength(password))
