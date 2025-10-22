with open("text.txt", "r") as f:
    content = f.read()
    print(content)

s = "This is the beggining to learn Data Science"

F = open("text2.txt", "w")
F.write(s)
F.close()
F = open("text2.txt", "r")
print(F.read())
F.close()