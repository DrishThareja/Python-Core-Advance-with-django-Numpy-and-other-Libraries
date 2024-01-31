"""
ques 9:
a
bb
ccc
dddd
eeeee
"""

for i in range(1, 6):
    for j in range(0,i):
        print(chr(ord('a') + i - 1), end='')
    print()

