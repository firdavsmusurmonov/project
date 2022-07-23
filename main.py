# a, b, c, d, e = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# d = int(d)
# e = int(e)
# if min(a, b, c, d, e):
#     print(min)

suz = int(input())
arr = list(map(int, input().split()[:suz]))
for j in suz:
    if j.isupper():
        print(j.lower(), end="")
    else:
        print(j.upper(), end="")





