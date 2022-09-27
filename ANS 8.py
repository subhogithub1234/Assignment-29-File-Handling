""" 
8. Write a Python script to create a copy of a file.
 """
try: 
    with open(input("Enter the file name which you want to copy:"),'r') as f:
       x=f.read()
    with open(input("Enter the copy file name:"),'w') as f:
      f.write(x)   
except FileNotFoundError:
    print("File not found!!!")
except Exception:
    print("Please check something is wrong...")    
else:
    print("copied succesfully....")            

#=============================================OUTPUT======================================================
""" 
Enter the file name which you want to copy:myfile.txt
Enter the copy file name:myfile_copy.txt
copied succesfully....
 """