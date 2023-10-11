#
# print(chr(65))
#
# print(ord('a'))

for i in range(500_000):
    if i % 50:
        print()
    print(chr(i), end=' ')
