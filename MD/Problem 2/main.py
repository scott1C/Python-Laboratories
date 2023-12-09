import random
import math

alphabet_mapping = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    " ": 27,
    "!": 28,
    ",": 29,
    ".": 30,
    "?": 31,
    "1": 32,
    "2": 33,
    "4": 34,
    "5": 35,
    "6": 36,
    "7": 37,
    "8": 38,
    "9": 39,
    "0": 40,
    "3": 41,
}


def alphabet_encode(message):
    return [alphabet_mapping[char.lower()] for char in message]


def find_letter(value):
    mapping = {v: k for k, v in alphabet_mapping.items()}
    if value in mapping:
        return mapping[value]
    else:
        return None


def gcd(a, b):
    if a % b:
        return gcd(b, a % b)
    return b


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x


def is_prime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    else:
        return True


def generate_N():
    P = random.randint(1, 200)
    Q = random.randint(1, 300)
    if is_prime(P) and is_prime(Q) and P != Q:
        return P, Q
    return generate_N()


def generate_fi(P, Q):
    return (P - 1) * (Q - 1)


def generate_e(fi):
    e = random.randint(2, fi)
    if gcd(e, fi) == 1:
        return e
    return generate_e(fi)


P, Q = generate_N()
N = P * Q
fi_N = generate_fi(P, Q)
e = generate_e(fi_N)
_, d, _ = extended_gcd(e, fi_N)
if d < 0:
    d += fi_N

string = input("Enter the string you want to encrypt: ")
message = alphabet_encode(string)
encrypted_message = [element**e % N for element in message]
initial_message = "".join(str(char) for char in encrypted_message)
decrypted_message = [element**d % N for element in encrypted_message]
final_message = "".join(find_letter(char) for char in decrypted_message)

print(f"Encrypted message of the string: {string} is: {initial_message}")
print(f"Decrypted message of the number: {initial_message} is: {final_message}")
