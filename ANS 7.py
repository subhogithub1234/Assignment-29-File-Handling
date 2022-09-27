
import keyword
c=0
with open('key.txt','r+') as f:

     for i in keyword.kwlist:
         c+=1
         f.write(i)
     print(c," of Python keywords occurring in a python source file.")

#========================================OUTPUT======================================
""" 
35 of Python keywords occurring in a python source file.
 """