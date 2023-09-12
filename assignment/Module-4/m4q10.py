# Write a Python program to count the frequency of words in a file

fd = open("example.txt","r")
data=fd.read()
fd.close()

special_char=",.?!"
for schar in special_char:
    if schar in data:
        data=data.replace(schar,"")

wordlist=data.split()
wordcount={}
for word in wordlist:
    if word in wordcount:
        wordcount[word] += 1
    else:
        wordcount[word]=1

for key,value in wordcount.items():
    print(f"{key} occurs : {value}")