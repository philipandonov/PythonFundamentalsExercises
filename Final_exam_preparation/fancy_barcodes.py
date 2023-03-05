import re


numbers_of_barcodes = int(input())
pattern = r"(\@\#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(\@\#+)"
for i in range(numbers_of_barcodes):
    string = input()
    digits = ''
    matches = re.search(pattern, string)
    if matches:

        for j in matches.group(2):
            if j.isdigit():
                digits += j
        if digits == '':
            print(f"Product group: 00")
        elif digits == '0':
            print(f"Product group: 0")
        else:
            print(f"Product group: {digits}")
    else:
        print("Invalid barcode")
