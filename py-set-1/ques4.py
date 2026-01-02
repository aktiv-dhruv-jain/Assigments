templist = ['being','Cat','n1ic','w%ijk']
vowels = ['a','e','i','o','u']
specChars = ['!','@','#','$','%','&','*','^']
result = []
for item in templist : 
    if(item[0].islower() and item[0] not in vowels):
        allChars = list(item)
        isOkay = False
        all_condition_check = all(inneritem not in specChars for inneritem in allChars)
        #for inneritem in allChars : 
         #   if(isinstance(inneritem,int) and inneritem not in specChars):
          #      print('yes')
        #print(allChars)
        print(all_condition_check)

