scores = input("Enter the marks of students seperated by a space: ").split()
int_score = [int(i) for i in scores]
highest = int_score[0]
lowest = int_score[0]
for i in range(1, len(int_score)):
    if int_score[i] >= highest:
        highest = int_score[i]
    elif int_score[i] <= lowest:
        lowest = int_score[i]
print(f"highest number in the given list is {highest}")
print(f"lowest number in the given list is {lowest}")
