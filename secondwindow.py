
from TableMaker import * # This is a class that shows data in form of table.


arr2=[]

with open("patient.txt","r") as patientfile:
  
     

     for line in patientfile:
          x=line[:-1]
          y=x.split(",")
          z=y[:-1]    #z is an array that holds each words of line as an element.
          arr2.append(z)  #arr2 is an array of z arrays.
print(arr2)                

with open("patient.txt","r") as patientfile:
        
     lines=len(patientfile.readlines())
     
cols=len(arr2[0])
table=TableMaker( lines,cols,arr2,"List of all patients") 
    
  


 
     
    
    
   
    