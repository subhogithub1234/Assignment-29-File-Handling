with open(input("Enter the file name:"),"r") as f:
      s=input("Enter the city name which you want to search:")
      for i in f.readlines():
           if i.strip()==s:
               print(s," is Found...")
               break
      else:
          print(s," is Not found...")

#===============================OUTPUT=================================================
""" 
Enter the file name:cities.txt
Enter the city name which you want to search:Asansol
Asansol  is Found...
 """