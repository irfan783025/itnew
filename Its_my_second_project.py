from tkinter import *
root = Tk()
root.geometry("500x300")
def getvals():
    print("your given detailes are accepted")
#width
root.minsize(200,300)
root.maxsize(1000,600)


#headlines

Label(root,text = "Python Registration Form by Irfan Khan", font = "arial 15 bold") .grid(row=0, column = 3)


#Field name
name = Label(root, text = "Name").grid(row=1,column=2)
phone = Label(root, text = "Phone").grid(row=2,column=2)
gender = Label(root, text = "Gender").grid(row=3, column=2)
emergency = Label(root, text = "Emergency").grid(row=4, column=2)
paymentmood = Label(root, text = "Payment Mood").grid(row =5, column=2)

#Variable for storing data

namevalue= StringVar
phonevalue=StringVar
gendervalue=StringVar
emergencyvalue=StringVar
paymentmoodvalue=StringVar
checkvalue=IntVar


#Creating entry Field
nameentry=Entry(root, textvariable= namevalue).grid(row=1,column=3)
phoneentry=Entry(root,textvariable=phonevalue).grid(row=2, column=3)
genderentry=Entry(root,textvariable=gendervalue).grid(row=3,column=3)
emergencyetry=Entry(root,textvariable=emergencyvalue).grid(row=4,column=3)
paymentmoodentry=Entry(root,textvariable=paymentmoodvalue).grid(row=5,column=3)

#create check buttom

checkbuttn=Checkbutton(text = "Remember me ?" ,variable = checkvalue).grid(row=6, column=3)


#create submit button
Button(text= "submit", command= getvals).grid(row=7, column = 3)


root.mainloop()