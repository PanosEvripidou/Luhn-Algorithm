import random


#Generate 10 random digits 0-9 (AccountName)

#for x in range(0, 10):
#    RandomNum = random.randint(0,9)
#    AccountName.append(RandomNum)
#print(AccountName)


def LuhnAlgorithm():
    AccountName = []
    UserCheckDigit = 0
    AccNameList = []
    AccName = input('Enter the Account Name:')
    while len(str(AccName)) != 11:
        AccName = input('Enter the Account Name:')
    for x in range(0,11):
       if x != 10 :
            AccountName.append(int(AccName[x]))
            AccNameList.append(int(AccName[x]))
       else:
            UserCheckDigit = AccName[10]
            AccNameList.append(int(AccName[x]))
    print(AccountName)
    print(UserCheckDigit)
#Multiply each digit by 1 or 2
    Payload=[]
    for x in range(0,10):
        if x%2 == 0:
            Payload.append(int(AccountName[x])*1)

        else:
            Payload.append(int(AccountName[x]*2))
    print(Payload)

#If there are 2 digit answers in Payload list we split and add the digits
    for x in range(0,10):
        if len(str(Payload[x])) == 2:
            Payload[x] = Payload[x]%10+1
    print(Payload)

#add all digits together and validating check digit
    PayloadSum = 0
    for x in range(0,10):
        PayloadSum = PayloadSum + int(Payload[x])
    print(PayloadSum)

    CheckDigit =  10-(PayloadSum%10)
    AccountName.append(CheckDigit)
    print(Payload)
    print(CheckDigit)
    print(AccNameList)
    return AccountName, AccNameList


AccountName, AccNameList = LuhnAlgorithm()
print()
while AccountName != AccNameList:
    LuhnAlgorithm()
print("Valid Information")
'''if AccountName == AccNameList:
    print("Valid Information")
else:
    LuhnAlgorithm()'''