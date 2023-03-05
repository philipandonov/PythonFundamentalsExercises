numbers = input().split(", ")

for i in numbers:
    is_palindrome = False
    backward = i[::-1]
    forward = i[:len(i)]
    if int(backward) == int(forward):
        is_palindrome = True
    print(is_palindrome)


