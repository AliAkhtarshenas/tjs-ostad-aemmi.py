import random
words = ["Ali", "book", "tree", "python", "bag", "umbrella", "java", "clock"]
a = random.randint(0, len(words)-1)
print(a)
word = words[a]
word = random.choice(words)
print(len(word))
for i in range(4):
    b = input()
    if b == word:
        print("great")
        break
    else:
        print("bad")