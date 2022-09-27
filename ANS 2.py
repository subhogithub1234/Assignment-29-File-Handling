""" 
2. Write a Python script to create a new file ‘myfile.txt’ and store user entered text
 """
def write(x,m):
    with open(x,m) as f:
        f.write(input("Enter your data:"))
write(x=input("Enter the file name like: example.txt:"),m='w') 
print("The file is created...")   

#===================================ANS=========================================
""" 
Enter the file name like: example.txt:myfile.txt
Enter your data:Hello world...
The file is created...
 """