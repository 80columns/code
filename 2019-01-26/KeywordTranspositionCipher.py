# https://www.hackerrank.com/challenges/keyword-transposition-cipher

import sys
import string

def main():
    input_lines = sys.stdin.readlines()

    test_count = int(input_lines[0].strip())

    for i in range(0, test_count):
        keyword = input_lines[(2 * i) + 1].strip()
        cipher_text = input_lines[(2 * i) + 2].strip()

        decrypt(keyword, cipher_text)

def decrypt(keyword, cipher_text):
    columns = []
    columns_order_map = {}
    sorted_columns = []
    cipher_alphabet = []
    alphabet = list(string.ascii_uppercase)
    keyword_list = list(keyword)
    decrypted_text = ""

    for i in range(len(keyword_list) - 1, 0, -1):
        if keyword_list[i] in keyword_list[:i]:
            keyword_list.pop(i)

    keyword_list_len = len(keyword_list)

    for x in keyword_list:
        alphabet.remove(x)

    columns.append(list(keyword_list))

    i = 0

    while (keyword_list_len * i) < len(alphabet):
        alphabet_row = list(alphabet[keyword_list_len * i:(keyword_list_len * i) + keyword_list_len])

        while len(alphabet_row) < keyword_list_len:
            alphabet_row.append(None)

        columns.append(alphabet_row)

        i += 1

    keyword_list.sort()

    for i in range(0, keyword_list_len):
        columns_order_map[i] = columns[0].index(keyword_list[i])

    for i in range(0, len(columns)):
        sorted_columns.append([])

        for j in range(0, len(columns_order_map)):
            sorted_columns[i].append(columns[i][columns_order_map[j]])

    cipher_columns = [list(i) for i in list(zip(*sorted_columns))]

    for i in range(0, len(cipher_columns)):
        cipher_alphabet.extend([x for x in cipher_columns[i] if x != None])

    reverse_cipher_dictionary = dict(zip(cipher_alphabet, list(string.ascii_uppercase)))

    for x in cipher_text:
        decrypted_text += reverse_cipher_dictionary[x] if x != " " else " "

    print(decrypted_text)

if __name__ == "__main__":
    main()
