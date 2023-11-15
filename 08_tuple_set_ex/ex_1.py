# print(*set(input() for _ in range(int(input()))), sep="\n")


n = int(input())
my_set = set()
for _ in range(1, n + 1):
    name = input()
    my_set.add(name)

print(*my_set, sep="\n")

# while my_set:
#     print(my_set.pop())
