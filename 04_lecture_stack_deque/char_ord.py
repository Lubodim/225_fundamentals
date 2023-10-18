#
# print(chr(65))
#
# print(ord('퟿'))
#
for i in range(55295 +1):
    if i % 50 == 0:
        print()
    print(chr(i), end=', ')
