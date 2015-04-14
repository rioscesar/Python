
N, M = (int(e) for e in input().split(" "))
l = [int(input(), 2) for _ in range(N)]

max_topic = list()

for i in range(N):
    for j in range(i+1, N):
        max_topic.append(str(bin(l[i]|l[j]))[2:])

length = -1
dic = {}
c = 0
for topic in max_topic:
    cmp = 0
    for letter in topic:
        if letter == "1":
            cmp += 1
    if length < cmp:
        length = cmp
    dic[str(c)] = cmp
    c+=1

counter = 0
for key in dic:
    if length == dic[key]:
        counter += 1


print(length)
print(counter)





