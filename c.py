n = eval(input())
str = input()
q = [i if str[i] == '*' for i in len(str)]

diff = (len(q) - 5) // 4
if len(q) < 5:
    print("no")
else:
    for i in len(str):
        