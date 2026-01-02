tempList = ['this','is','The','test','St2ing']
vowels = ['a','e','i','o','u']
numberList = ['0','1','2','3','4','5','6','7','8','9']
validWords = []
for word in tempList : 
    firstChar = word[0]
    if(firstChar.isupper() and (firstChar not in vowels) and all([char not in numberList for char in word])):
        validWords.append(word)
        
print("valid words are",validWords)
