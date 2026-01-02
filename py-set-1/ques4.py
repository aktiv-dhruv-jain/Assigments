templist = ['being','Cat','ni@c','w%ijk']
vowels = ['a','e','i','o','u']
specChars = ['!','@','#','$','%','&','*','^']
numberList = ['1','2','3','4','5','6','7','8','9']
result = []
for item in templist : 
    if(item[0].islower() and item[0] not in vowels):
        allChars = list(item)
        all_spec_condition_check = all(inneritem not in specChars for inneritem in allChars)
        all_num_condition_check = all(char not in numberList for char in item)
        if(all_spec_condition_check and all_num_condition_check):
            result.append(item)

print(f"Conditionally correct strings are : {result}")

