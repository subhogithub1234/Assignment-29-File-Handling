""" 
9. Write a Python script to store book data in a file. Book data is in the form of a
dictionary in which book name is the key and price is its value. Use pickle to store
data into a file (say bookfile)
 """

import pickle
try:
    d=dict()
    for i in range(int(input("How namy book you want to be insert:"))):
        key=input("Enter the book name:")
        value=int(input("Enter the books price:"))
        d[key]=value
        pickle.dump(d, open("bookfile.p", "wb"))
except Exception:
    print("Something is wrong please try again!!!!")         


#=================================output===================================
""" 
How many books you want to insert:4
Enter the book name:Clean Code
Enter the book price:500
Enter the book name: Introduction to Algorithms
Enter the book price:700
Enter the book name:A Code of Conduct for Professional Programmers
Enter the book price:800
Enter the book name:Software Construction
Enter the book price:900

 """