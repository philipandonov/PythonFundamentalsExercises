dict_of_jane = {}
command = input()
while command != "Log out":
    current_command = command.split(": ")
    if current_command[0] == "New follower":
        username = current_command[1]
        if username not in dict_of_jane:
            dict_of_jane[username] = {"Likes": 0, "Comments": 0}
    elif current_command[0] == "Like":
        username = current_command[1]
        count = int(current_command[2])
        if username not in dict_of_jane:
            dict_of_jane[username] = {"Likes": count, "Comments": 0}
        else:
            dict_of_jane[username]["Likes"] += count
    elif current_command[0] == "Comment":
        username = current_command[1]
        if username not in dict_of_jane:
            dict_of_jane[username] = {"Likes": 0, "Comments": 1}
        else:
            dict_of_jane[username]["Comments"] += 1
    elif current_command[0] == "Blocked":
        username = current_command[1]
        if username in dict_of_jane:
            del dict_of_jane[username]
        else:
            print(f"{username} doesn't exist.")

    command = input()
print(f"{len(dict_of_jane)} followers")
for key in dict_of_jane:
    likes_comments = (dict_of_jane[key]["Likes"]+dict_of_jane[key]["Comments"])
    print(f"{key}: {likes_comments}")
