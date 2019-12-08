import numpy as nm

A = nm.loadtxt(open("adult.csv", "rb"), delimiter=",", dtype=object, skiprows=1, usecols=range(15))
print(len(A))
i = 0
while i < len(A):
    for j in range(15):
        if (A[i][j] == '"?"' or (j == 13 and A[i][j] != '"United-States"')):
            A = nm.delete(A, i, 0)
            i -= 1
            break
    i += 1

for i in range(len(A)):
    if(A[i][9] == '"Female"'):
        A[i][9] = 1
    else:
        A[i][9] = 0
for i in range(len(A)):
    if(A[i][14] == '">50K"'):
        A[i][14] = 1
    else:
        A[i][14] = 0
for i in range(len(A)):
    if(A[i][8] == '"White"'):
        A[i][8] = 0
    elif(A[i][8] == '"Asian-Pac-Islander"'):
        A[i][8] = 1
    elif (A[i][8] == '"Amer-Indian-Eskimo"'):
        A[i][8] = 2
    elif (A[i][8] == '"Other"'):
        A[i][8] = 3
    else:
        A[i][8] = 4
for i in range(len(A)):
    if(A[i][7] == '"Wife"'):
        A[i][7] = 0
    elif(A[i][7] == '"Own-child"'):
        A[i][7] = 1
    elif (A[i][7] == '"Husband"'):
        A[i][7] = 2
    elif (A[i][7] == '"Not-in-family"'):
        A[i][7] = 3
    elif (A[i][7] == '"Other-relative"'):
        A[i][7] = 4
    else:
        A[i][7] = 5

for i in range(len(A)):
    if(A[i][5] == '"Married-civ-spouse"'):
        A[i][5] = 0
    elif(A[i][5] == '"Divorced"'):
        A[i][5] = 1
    elif (A[i][5] == '"Never-married"'):
        A[i][5] = 2
    elif (A[i][5] == '"Separated"'):
        A[i][5] = 3
    elif (A[i][5] == '"Widowed"'):
        A[i][5] = 4
    elif (A[i][5] == '"Married-spouse-absent"'):
        A[i][5] = 5
    else:
        A[i][5] = 6

for i in range(len(A)):
    if(A[i][1] == '"Private"'):
        A[i][1] = 0
    elif(A[i][1] == '"Self-emp-not-inc"'):
        A[i][1] = 1
    elif (A[i][1] == '"Self-emp-inc"'):
        A[i][1] = 2
    elif (A[i][1] == '"Federal-gov"'):
        A[i][1] = 3
    elif (A[i][1] == '"Local-gov"'):
        A[i][1] = 4
    elif (A[i][1] == '"State-gov"'):
        A[i][1] = 5
    elif (A[i][1] == '"Without-pay"'):
        A[i][1] = 6
    else:
        A[i][1] = 7

for i in range(len(A)):
    if(A[i][6] == '"Tech-support"'):
        A[i][6] = 0
    elif(A[i][6] == '"Craft-repair"'):
        A[i][6] = 1
    elif (A[i][6] == '"Other-service"'):
        A[i][6] = 2
    elif (A[i][6] == '"Sales"'):
        A[i][6] = 3
    elif (A[i][6] == '"Exec-managerial"'):
        A[i][6] = 4
    elif (A[i][6] == '"Prof-specialty"'):
        A[i][6] = 5
    elif (A[i][6] == '"Handlers-cleaners"'):
        A[i][6] = 6
    elif (A[i][6] == '"Machine-op-inspct"'):
        A[i][6] = 7
    elif (A[i][6] == '"Adm-clerical"'):
        A[i][6] = 8
    elif (A[i][6] == '"Farming-fishing"'):
        A[i][6] = 9
    elif (A[i][6] == '"Transport-moving"'):
        A[i][6] = 10
    elif (A[i][6] == '"Priv-house-serv"'):
        A[i][6] = 11
    elif (A[i][6] == '"Protective-serv"'):
        A[i][6] = 12
    else:
        A[i][6] = 13
A = nm.delete(A, 13, 1)
A = nm.delete(A, 3, 1)
A = nm.delete(A, 2, 1)

nm.savetxt("adultProcessed.csv", A, delimiter=",", fmt='%s')