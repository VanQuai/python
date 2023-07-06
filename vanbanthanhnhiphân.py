import os
os.system('cls')
def text_to_binary(text):
    binary_string = ""
    for char in text:
        decimal_value = ord(char)
        binary_value = bin(decimal_value)[2:].zfill(8)
        binary_string += binary_value + " "
    return binary_string.strip()

# Ví dụ sử dụng
input_text = "yêu anh quan"
binary_text = text_to_binary(input_text)
print(binary_text)
