""" 
3. Write a Python script to read the above created file ‘myfile.txt’ and display content on
the console.
 """
def read(x):
    try:
        with open(x,'r') as f:
             print(f.read())
             print("Search completed....")
    except FileNotFoundError:
        print("file not found........")         
read(x=input('Ehter your file name which you want to search:'))

#===================================ANS=====================================
""" 
OUTPUT 1:

Ehter your file name which you want to search:myfile.txt
Hello world...
Search completed....

OUTPUT 2:

Ehter your file name which you want to search:ANS.txt
file not found........
 """