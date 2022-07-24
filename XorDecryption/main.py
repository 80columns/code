#!/usr/bin/python3

import itertools

def main():
    ascii_characters = []
    data = []
    plaintext = ""
    plaintext_ascii_sum = 0

    for x in range(97, 123):
        ascii_characters.append(x)

    with open("p059_cipher.txt", "r") as input_file:
        data = [int(x) for x in input_file.readline().split(",")]

    for x in itertools.permutations(ascii_characters, 3):
        plaintext = xor_decrypt(x, data)

        if " the " in plaintext:
            print(f"\n{plaintext}")
            break

    for x in plaintext:
        plaintext_ascii_sum += ord(x)

    print(f"\nplaintext ascii sum is {plaintext_ascii_sum}")

def xor_decrypt(password, data):
    print(f"checking password {password}")
    plaintext = ""
    
    password_index = 0
    data_index = 0

    while password_index < len(password) and data_index < len(data):
        plaintext += chr(password[password_index] ^ data[data_index])

        password_index = (password_index + 1) % 3
        data_index += 1

    return plaintext

if __name__ == "__main__":
    main()
