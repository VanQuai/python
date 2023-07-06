import os
os.system('cls')
def binary_to_text(binary_string):
    binary_list = binary_string.split()
    text = ""
    for binary in binary_list:
        decimal_value = int(binary, 2)
        char = chr(decimal_value)
        text += char
    return text

# Ví dụ sử dụng
input_binary = "01001000 01100101 01101100 01101100 01101111 00101100 00100000 01110111 01101111 01110010 01101100 01100100 00100001"
text = binary_to_text(input_binary)
print(text)
