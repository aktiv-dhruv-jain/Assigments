templist = [3452,123,6654,1352,6744]
result = []
def checkOdd(n):
    if(n%2==0):
        return False
    return True
    
def divBy5or8(n):
    if(n%5==0 or n%8==0):
        return True
    else : 
        return False
        
for item in templist : 
    temp = item
    raiseTo = 0
    while(temp>0):
        target = temp%10
        temp = temp//10
        raiseTo+=1

    if(raiseTo == 4):
        tempdig = item//(10**(raiseTo-2))
        secondPos = tempdig%10
        if(checkOdd(secondPos) and (not checkOdd(item%10)) and divBy5or8(item)):
            result.append(item)
print(result)

