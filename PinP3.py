bugs = 0
average = 0
numdays = 7
#initialize counter
i = 1

while i < 8:
    #ask user for the amount of bugs for 7 days
    day = int(input("how many bugs did you collect on day "+ str(i)+"?"))

#calculate the amount of bugs collected in the week
    bugs = bugs + day

    #increment the counter
    i = i + 1

#compute the average
average = bugs/numdays

#print the average amount
print("The average number of bugs collected this week is " + str(round(average,2)) + " bugs")
