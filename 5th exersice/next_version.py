current_version = [int(s) for s in input().split(".")]
current_version[-1] += 1
for i in range(len(current_version) - 1, -1, -1):

    if current_version[i] > 9:
        current_version[i] = 0
        if i - 1 >= 0:
            current_version[i - 1] += 1
print(".".join(str(s)for s in current_version))
