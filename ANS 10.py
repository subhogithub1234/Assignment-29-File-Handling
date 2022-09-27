""" 
10. Write a Python script to extract book data from a bookfile using pickle. Also print
extracted book data.
 """


import pickle
try:
    file= pickle.load(open(input("Enter the file name:"), "rb"))
    for i in file:
        print(i,'-->',file[i])
except FileNotFoundError:
    print("Flie not found!!!")

#================================OUTPUT================================================
""" 


Enter the file name:bookfile.p
Clean Code --> 500
 Introduction to Algorithms --> 700
A Code of Conduct for Professional Programmers --> 800
Software Construction --> 900
 """
