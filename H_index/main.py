citations = [3,0,6,1,5]

H_Index = 0
NumberOfPaper = len(citations)

while (H_Index < NumberOfPaper):

    NumberOfPaper = len(citations)
    H_Index += 1

    for i in range (len(citations)):
        if H_Index > citations[i]:
            NumberOfPaper -= 1
    

if H_Index == NumberOfPaper:
    print(H_Index)
else:
    print(H_Index-1)