
def populate_list(string):
    letter_count = {}
    for l in string:
        if l in letter_count:
            letter_count[l] += 1
        else:
            letter_count[l] = 1
    return letter_count

string = input()
letter_count = populate_list(string)

count = 0
for key in letter_count:
    if letter_count[key] % 2 != 0:
        count += 1

if count > 1:
    print("NO")
else:
    print("YES")

