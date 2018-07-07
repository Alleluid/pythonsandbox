import os

cols, lines = os.get_terminal_size()

print("#"*(cols-1))
for i in range(lines-3):
    if i == (lines - 3) // 2:
        print('|'+"hey".center(cols-3, ' ')+'|')
    print("|"+(" "*(cols-3))+"|")
print("#"*(cols-1), end="")
input()