""" 
1. Write a Python script to print the following status of a file:
a. Whether a file is read only
b. Whether a file is closed or not
c. Which file opening mode is used
d. Name of the file

 """
with open(input("Enter the file name:"),'r') as f:
    f.read()
    if f.mode==True:
        print("File is open.")
    else:
        print("File is closed.")
    print('The opening mode of the file is ',f.mode)
    print("The name of the file is ",f.name)         

#=======================OUTPUT=============================================
    """ 
Enter the file name:ans1.txt
File is closed.
The opening mode of the file is  r
The name of the file is  ans1.txt
     """