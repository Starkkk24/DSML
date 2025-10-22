# doubles = [x * 2 for x in range(1,11)]
# triples = [y*3 for y in range(1,11)]
# squares = [z ** 2 for z in range(1,11)]

# fruit = ["apple", "banana", "grapes"]
# fruits = [f[0].upper() for f in fruit]
# print(doubles)
# print(triples)
# print(squares)
# print(fruits)


# # conditions

# no = [1,2,3,-4,5,-3,9,0,-2,8,-7,6]
# p_no = [p for p in no if p>=0]
# n_no = [n for n in no if n <0]
# e = [e for e in no if e%2==0]
# o = [o for o in no if o%2!=0]

# print(p_no)
# print(n_no)
# print(e)
# print(o)


def stark_birthday_wish(name="Stark"):
    diwali_vibes = ["✨", "🎇", "🪔"]
    for i in range(3):
        print(f"{diwali_vibes[i]} Happy Birthday, {name}! Level up like a Diwali rocket! {diwali_vibes[i]}")
    print("From your bro Grok: Keep shining, binary style! 🚀")

stark_birthday_wish("Stark")