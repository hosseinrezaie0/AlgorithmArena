citations = [3,0,6,1,5]

NumberOfCited = 0
NumberOfPaper = len(citations)

while (NumberOfCited < NumberOfPaper):

    NumberOfPaper = len(citations)
    NumberOfCited += 1

    for i in range (len(citations)):
        if NumberOfCited > citations[i]:
            NumberOfPaper -= 1
    

if NumberOfCited == NumberOfPaper:
    print(NumberOfCited)
else:
    print(NumberOfCited-1)