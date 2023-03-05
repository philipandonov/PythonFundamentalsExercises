shelf_with_books = input().split("&")
command = input()

while True:

    if command == "Done":

        break
    book_is_there = False
    is_not_in_list = True
    first_book_is_in = False
    second_book_is_in = False
    current_command = command.split(' | ')
    cur_command = current_command[0]

    if cur_command == "Add Book":
        for i in shelf_with_books:
            if i == current_command[1]:
                is_not_in_list = False
        if is_not_in_list:
            shelf_with_books.insert(0, current_command[1])
    elif cur_command == "Take Book":
        for s in shelf_with_books:
            if current_command[1] == s:
                shelf_with_books.remove(current_command[1])
    elif cur_command == "Swap Books":
        for i, n in enumerate(shelf_with_books):
            if n == current_command[1]:
                index1 = i
                book1 = n
                first_book_is_in = True
        for j, k in enumerate(shelf_with_books):
            if k == current_command[2]:
                index2 = j
                book2 = k
                second_book_is_in = True
        if first_book_is_in and second_book_is_in:
            shelf_with_books[index1], shelf_with_books[index2] = shelf_with_books[index2], shelf_with_books[index1]
    elif cur_command == "Insert Book":
        for i in shelf_with_books:
            if i != current_command[1]:
                book_is_there = True
        if book_is_there:
            shelf_with_books.append(current_command[1])
    elif cur_command == "Check Book" and 0 <= int(current_command[1]) < len(shelf_with_books):
        print(shelf_with_books[int(current_command[1])])
    command = input()
print(", ".join(s for s in shelf_with_books))

