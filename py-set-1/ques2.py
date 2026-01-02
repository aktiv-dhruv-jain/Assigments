#armstrong number

digit = 123 

def checkArmstrong():
    raiseTo = 0
    sum = 0
    temp = digit
    while(temp>0):
        target = temp%10
        temp = temp//10
        raiseTo+=1
    temp = digit
    while(temp>0):
        target = temp%10
        print(target)
        temp = temp//10
        sum+=target**raiseTo
    if(sum == digit):
        return True
    else : 
        return False

    
print(checkArmstrong())
