from unidecode import unidecode

input_string = "Tây Ninh"
output_string = unidecode(input_string.replace(' ', '').lower())
print(output_string)  # Kết quả: "tayninh"