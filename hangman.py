import random

lst = ["ardvark", "baboon", "camel"]
life = 5
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
empty = ''
word = random.choice(lst)
length = len(word)
for m in range(1, length + 1):
    empty += "_ "
splited = list(empty.split())
print(f"the word is {length} words long!\n")
print(f"\t\t{empty}")
for i in splited:
    while "_" in splited:
        if "_" not in splited:
            print("YOU WIN!!!")
            quit()
        guess = input("Enter a letter to guess:").lower()
        Found = False
        for positon in range(length):
            if guess == word[positon]:
                Found = True
                splited[positon] = guess
        if not Found:
            print(stages[life])
            if life < 1:
                print("YOU LOSE")
                quit()
            life -= 1
        print(splited)
