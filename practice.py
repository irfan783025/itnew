from tkinter import *
root=Tk()

root.geometry("500x300" )


def getvals():
    print("Your given deatails are Accepted")

#width , hight
root.minsize(200,100)
root.maxsize(600,400)

Label(root, text = "Rajshree Ragistration Form ", font = "arial 15 bold ").grid(row=0 , column=3)

#Field name
name=Label(root , text = "Name").grid(row=1, column=2)
phone=Label(root , text = "Phone").grid(row=2 , column=2)
emialid=Label(root , text = "Email Id").grid(row=3 , column=2)
gender=Label(root , text = "Gender").grid(row=4, column=2)
paymentmood=Label(root , text = "Payment Mode").grid(row=5 , column=2)

#packing of Field



#Variable for storing data

namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentmoodvalue = StringVar
checkvalue = IntVar

#Creating entry Field

nameentry = Entry(root, textvariable = namevalue).grid(row=1,column=3)
phoneentry = Entry(root, textvariable = phonevalue).grid(row=2,column=3)
genderentry = Entry(root, textvariable = gendervalue).grid(row=3,column=3)
emergencyentry = Entry(root, textvariable = emergencyvalue).grid(row=4,column=3)
paymentmoodentry = Entry(root, textvariable = paymentmoodvalue).grid(row=5,column=3)

#packing entry Fields






#Creating Check box

checkbtn= Checkbutton(text = "remember me?" , variable = checkvalue)
checkbtn.grid(row=6, column=3)


#submit Button
Button(text= "submit", command= getvals).grid(row=7, column = 3)



#gui logic here
root.mainloop()
