# WAP to test whether a passed letter(sentence) is a vowel or not 

x=input("Enter the sentence:- ")
count=0
for i in x :
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        print(i)
        count=count+1
if count==0:
    print("No vowel found")
else:
    print("Number of vowels :-  ",count)
