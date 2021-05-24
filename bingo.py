import random
remain = []
picked = []
for i in range(1, 100):
    remain.append(i)
for k in range(1, 1001):
    user = input("Type ' >> ' to get a random number and Type ' << ' to check if a number is already picked(type exit to quit): ").lower()
    if user == ">>":
        b = random.choice(remain)
        print(b)
        remain.remove(b)
        picked.append(b)
        print(f"Number is {b}")
        continue
    elif user == "<<":
        check = int(input("Enter the number to check if it is already picked: "))
        if check in picked:
            print(f"The number {check} has already been picked!!!")
        elif check not in picked:
            print("No the following number is not yet picked!!!")
        else:
            print("Wrong input entered.")
            break
    elif user == 'exit':
        print('program has ended.')
        quit()
    else:
        print('sorry wrong input entered.')
