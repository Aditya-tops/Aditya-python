#Write a Python program to write a list to a file. 

cake_list=['plum cake','ferrero cake','chocolate cake','cup cake ']
print(cake_list)

textfile = open('c:\Users\Adity\Desktop\Aditya-python\assignment\Module-4\cake.txt','w')

content = "\n".join(cake_list)

textfile.writelines(content)