templist = [3452,123,6654,1352,5736]
result = []
def checkOdd(n):
    if(n%2==0):
        return False
    return True
    
def divBy3or7(n):
    if(n%3==0 or n%7==0):
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

    if(item >= 1000 and item <=9999):
        firstPos = item//(10**(raiseTo-1))
        if(checkOdd(firstPos) and (not checkOdd(item%10)) and divBy3or7(item)):
            result.append(item)
print(f"The conditionally correct digits are : {result}")

