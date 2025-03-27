
from tkinter import *
from PatientClass import *
import subprocess



window=Tk()

#The following variables are declared to hold values from Entry widgets.

pname=StringVar(window)
plast=StringVar(window)
page=StringVar(window)
psick=StringVar(window)


#The following function is declared to handle the click event of List all btn .

def listAll ():
      
      subprocess.run(['python','secondwindow.py'])
      
      
 #The following function is declared in order to handle the click event of Submit btn.
      
def submit():
  
  
    file= open(r'patient.txt','a') 
    
    n=pname.get()
    l=plast.get()
    a=page.get()
    s=psick.get()
    rad=r.get()
    properties=[]
    
    
    # The following if statement says that if the Present radio btn is clicked:
    
    if rad==2:
      
       obj= Present(n,l,a,s,"present")
       nm=obj.name
       ln=obj.last
       ag=obj.age
       sk=obj.sickness
       pr=obj.present
      
       properties=[nm,ln,ag,sk,pr]
       
      
       for element in properties:
           file.write(element+",")
       file.write("\n")
          
               
         
      
    #Else Discharged btn is clicked:
       
    else :
        
       obj= Discharged(n,l,a,s,"discharged")
       nm=obj.name
       ln=obj.last
       ag=obj.age
       sk=obj.sickness
       di=obj.discharged
       properties=[nm,ln,ag,sk,di]
       
      
      
      
       for element in properties:
            file.write(element+",")
       file.write("\n") 
      
    file.close()
  
    #The Entry widget text boxes should be empty in order to register another patient:
    pname.set("")
    plast.set("")
    page.set("")
    psick.set("")
      
              


window.geometry("800x600")
window.title("Horia Hospital")
window.resizable(0,0)
icon=PhotoImage(file='hospital-icons-design-in-blue-circle-png.png')
window.iconphoto(True , icon)
window.config(background="blue")

registration=Label(window, text="Register the patient!" ,font=('Arial' ,40, 'bold'), padx=20, pady=20 ,fg='yellow' , bg='blue')
registration.pack()

nameL=Label(window ,text="Patient Name: " , font=('Arial' , 20 , 'bold ') ,fg='yellow' , bg='blue' ).place(x=40 , y=200)
lastL=Label(window ,text="Patient last Name: " , font=('Arial' , 20 , 'bold ') ,fg='yellow' , bg='blue' ).place(x=40 , y=240) 
ageL=Label(window ,text="Patient age: " , font=('Arial' , 20 , 'bold ') ,fg='yellow' , bg='blue' ).place(x=40 , y=280 ) 
sicknessL=Label(window ,text="Sickness: " , font=('Arial' , 20 , 'bold ') ,fg='yellow' , bg='blue' ).place(x=40 , y=320)

#This is a shared variable between the two radio btns:
r=IntVar()


                                  
radio1=Radiobutton(window , text="Discharged" , font=('Arial' , 20 , 'bold '), foreground='yellow' , background='blue', variable=r, value=1 ).place(x=40 , y=400) 
radio2=Radiobutton(window , text="Present" , font=('Arial' , 20 , 'bold '), foreground='yellow' , background='blue', variable=r, value=2  ).place(x=260 , y=400 )

nameInput= Entry(window , textvariable=pname, fg='yellow' , bg='blue', width=20, font=('Arial' , 20 ,' bold')  ).place(x=450 , y=200)
lastInput=Entry(window , textvariable=plast, fg='yellow' , bg='blue', width=20, font=('Arial' , 20 ,' bold')  ).place(x=450 , y=240)
ageInput=Entry(window ,textvariable=page, fg='yellow' , bg='blue', width=20, font=('Arial' , 20 ,' bold')  ).place(x=450 , y=280)
sicknessInput=Entry(window , textvariable=psick, fg='yellow' , bg='blue', width=20, font=('Arial' , 20 ,' bold')  ).place(x=450 , y=320)

   
submitbtn=Button(window, text="Submit",command= submit ,fg='yellow', bg='blue', font=('Arial' , 20 , 'bold'), width=10).place(x=40 , y=480)
listbtn=Button(window, text="List all", command=listAll, fg='yellow', bg='blue', font=('Arial' , 20 , 'bold'), width=10).place(x=560 , y=480)

       
        
    
  
                                      
window.mainloop()