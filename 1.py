poundsList = []

numStudents = int(input('How many students do you have?'))
for i in range(numStudents):
    studentWeight = int(input("What is the student's weight in lbs?"))
    poundsList.append(studentWeight)

kgList = [round((poundsList[i]/2.2), 2) for i in range(numStudents)]

print(poundsList)
print(kgList)
