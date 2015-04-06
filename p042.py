def sumWord(word):
    return sum([ord(letter)-ord('A')+1 for letter in word])

triangleNumbers =  [(x*x+x)/2 for x in range(1,50)  ]
words = open('p042_words.txt').readline().rstrip()[1:-1].split('","')
print sum([1 for i in range(len(words)) if sumWord(words[i]) in triangleNumbers])
