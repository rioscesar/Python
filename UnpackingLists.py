def drop_first_last(grades):
    grades = sorted(grades)
    first, *mid, last = grades
    avg = sum(mid) / len(mid)
    print(avg)

g = [12, 3, 2, 123, 43]
#drop_first_last(g)

first = ['a', 'b', 'c']
last = ['z', 'x', 'y']

n = zip(first, last)
'''for a, b in n:
    print(a, b)'''

ans = lambda x:(
    x+3
)

print(ans(2))