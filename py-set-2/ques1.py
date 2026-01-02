wordFrequency = dict()
sentence = "I walk apple i eat apple i sleep apple"

for word in sentence.split(' ') : 
    wordFrequency[word] = wordFrequency.get(word,0)+1

for word in wordFrequency:
    if(wordFrequency[word] > 1):
        print(f"word is {word} and it has been repeated {wordFrequency[word]} times")

