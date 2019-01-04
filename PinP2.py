#get first score
score = int(input("Enter score: "))

#initialize lowest score
lowest = score

#increment your counter
i = 1

# creat loop that compares each score to the next until it finds the 
while i < 9:
        score = int(input("Enter score: "))
        if score < lowest:
            lowest = score

        i = i + 1
print("Your Lowest score for the three weeks is:", lowest)
