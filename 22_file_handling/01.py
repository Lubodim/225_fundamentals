# 2 задача
with open("data.txt", "a") as d:
    while True:
        new_text = input("Enter a txt: ")
        if new_text == "end":
            break
        d.write(f"{new_text}\n")




# 1 задача
# with open("output.txt", "w") as ou:
#     ou.write("some text\n")
#
# with open("output.txt", "r") as gosho:
#     print(gosho.read())