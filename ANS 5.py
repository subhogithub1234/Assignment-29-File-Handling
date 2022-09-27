with open(input("Enter the file name:"),"w+") as f:
     s1=[]
     x=int(input("How many cities name you want to insert:"))
     print("Enter the cities name:")
     for i in range(x):
         w=input()
         s1.append(w)

     for i in s1:
        f.write("%s\n"%i)
     else:
         print("File is saved...")

#===================================OUTPUT========================================
""" 
Enter the file name:cities.txt
How many cities name you want to insert:4
Enter the cities name:
Asansol
Kolkata
Mumbai
Chenni
File is saved...
 """