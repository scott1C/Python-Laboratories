# OOGNVMTNTCLUOGZSZSHTXAZGMOMEPKWDDQM
# EE
# 0-E


def generate_key(string, key):
    key = list(key)
    if len(string) < len(key):
        return 1
    elif len(string) == len(key):
        return key
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])

    return "".join(key)


def uncrypted_text(encrypted_string, key):
    if key == 1:
        return 1
    letter_mapping = {i: chr(i + 97) for i in range(26)}
    print(letter_mapping)
    text = []
    encrypted_string = encrypted_string.lower()

    for i in range(len(encrypted_string)):
        text.append(letter_mapping[(ord(encrypted_string[i]) - ord(key[i])) % 26])

    return "".join(text)


combinations = ["faf", "job"]
encrypted_message = "OOGNVMTNTCLUOGZSZSHTXAZGMOMEPKWDDQM"
for i in combinations:
    key = generate_key(encrypted_message, i)
    print(uncrypted_text(encrypted_message, key))
