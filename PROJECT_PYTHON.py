from tkinter import *
from tkinter import messagebox
from tkinter import Radiobutton
import mysql.connector
def main_gui():
    global main
    main = Tk()
    main.title("Student Records")
    main.geometry("400x200")

    lblmain = Label(main, text = "Hey User What Do You Want To Update :)").place(x = 0 ,y =10 )

    btn1 = Button(main,text = "Add Record", command = onclick_main_add).place(x= 10, y= 100)
    btn2 = Button(main,text = "Delete Record", command = onclick_main_delete).place(x= 100, y= 100)
    btn3 = Button(main,text = "Update Record", command = onclick_main_update).place(x= 200, y= 100)
    btn4 = Button(main,text = "View Record", command = onclick_main_view).place(x= 300, y= 100)
    main.mainloop()
def add_gui():
    global entrname,entrbranch,entrphone, entrroll
    global hey
    hey = Tk()
    hey.title("Add Student Record")
    hey.geometry("500x300")

    lblName = Label(hey, text="Enter Name :", font="Arial 16").place(x= 10, y = 20)

    entrname = Entry(hey, font="Arial 16")
    entrname.place(x = 250, y = 20)
    lblRoll = Label(hey, text="Enter Roll_No :", font="Arial 16").place(x= 10, y = 60)
    entrroll = Entry(hey,font = "Arial 16")
    entrroll.place(x= 250, y = 60)
    lblBranch = Label(hey, text="Enter Your Branch :", font="Arial 16").place(x= 10, y = 100)
    entrbranch = Entry(hey,font = "Arial 16")
    entrbranch.place(x=250, y = 100)
    lblPhone = Label(hey, text="Enter Phone Number :", font="Arial 16").place(x= 10, y = 140)
    entrphone = Entry(hey, font = "Arial 16")
    entrphone.place(x = 250, y = 140)

    btnSave = Button(hey, text="Save Information",font="Arial 16", command=add)
    btnSave.place(x = 40, y = 180)

    btnback = Button(hey, text="Back To Main Menu", command=onclick_insert, font="Arial 16")
    btnback.place(x = 240, y = 180)
    hey.mainloop()

def update_gui():
    global window
    window = Tk()
    window.geometry("500x500")
    window.title("Updating Information")
    global updateName, newName
    global updateRoll, newRoll
    global updateBranch, newBranch
    global updatePhone, newPhone
    global radbtn1,radbtn2,radbtn3,radbtn4,radbtn5,radbtn6,radbtn7,radbtn8
    global radiobutton,radiobutton2
    radiobutton = IntVar()
    radiobutton2 = IntVar()

    lblsay = Label(window, text = "Hey User! Which Thing You Want To Update.....").place(x= 5, y = 5)
    radbtn1 = Radiobutton(window, variable=radiobutton, value=1, text="Name", command=radio1)
    radbtn1.place(x = 30, y = 30)
    lblnewname = Label(window, text="Enter New Name:",font = "Arial 16").place(x = 0, y = 130)

    newName = Entry(window, state=DISABLED, font = "Arial 16")
    newName.place(x = 250, y = 130)

    radbtn2 = Radiobutton(window, variable=radiobutton, value=2, text="Roll_No", command=radio2)
    radbtn2.place(x = 130, y = 30)
    lblnewroll = Label(window, text="Enter New Roll",font = "Arial 16").place(x = 0, y = 170)
    newRoll = Entry(window, state=DISABLED, font = "Arial 16")
    newRoll.place(x = 250, y = 170)

    radbtn3 = Radiobutton(window, variable=radiobutton, value=3, text="Branch", command=radio3)
    radbtn3.place(x = 230, y = 30)
    lblnewbranch = Label(window, text="Enter New Branch",font = "Arial 16").place(x = 0, y = 210)
    newBranch = Entry(window, state=DISABLED, font = "Arial 16")
    newBranch.place(x = 250, y = 210)

    radbtn4 = Radiobutton(window, variable=radiobutton, value=4, text="Phone", command=radio4)
    radbtn4.place(x = 330, y = 30)
    lblnewphone = Label(window, text="Enter New Phone",font = "Arial 16").place(x =0, y =250)
    newPhone = Entry(window, state=DISABLED,font = "Arial 16")
    newPhone.place(x = 250, y =250)


    lblsay1 = Label(window, text = "By Which Option You Want To Update......").place(x = 5, y = 55)
    radbtn5 = Radiobutton(window, variable=radiobutton2, value=1, text="By Name", command=radio5, state=DISABLED)
    radbtn5.place(x = 30, y = 80)
    lblname = Label(window, text="Enter Existing Name",font = "Arial 16").place(x =0, y =290)
    updateName = Entry(window, state=DISABLED,font = "Arial 16")
    updateName.place(x =250, y =290)

    radbtn6 = Radiobutton(window, variable=radiobutton2, value=2, text="By Roll_No", command=radio6, state=DISABLED)
    radbtn6.place(x = 130, y = 80)
    lblroll = Label(window, text="Enter Existing Roll",font = "Arial 16").place(x =0, y =330)
    updateRoll = Entry(window, state=DISABLED,font = "Arial 16")
    updateRoll.place(x =250, y =330)

    radbtn7 = Radiobutton(window, variable=radiobutton2, value=3, text="By Branch", command=radio7, state=DISABLED)
    radbtn7.place(x = 230, y = 80)
    lblbranch = Label(window, text="Enter Existing Branch",font = "Arial 16").place(x =0, y =370)
    updateBranch = Entry(window, state=DISABLED,font = "Arial 16")
    updateBranch.place(x = 250, y =370)

    radbtn8 = Radiobutton(window, variable=radiobutton2, value=4, text="By Phone", command=radio8, state=DISABLED)
    radbtn8.place(x = 330, y = 80)
    lblphone = Label(window, text="Enter Existing Phone",font = "Arial 16").place(x =0, y =410)
    updatePhone = Entry(window, state=DISABLED,font = "Arial 16" )
    updatePhone.place(x =250, y =410)

    btnSave = Button(window, text="Update Information", command=update)
    btnSave.place(x = 40, y = 470)

    btnback = Button(window, text="Back To Main Menu", command=onclick_update)
    btnback.place(x=240, y=470)

    window.mainloop()

def delete_gui():
    global say
    say = Tk()
    say.geometry("540x450")
    lblTitle = Label(say, text="Delete Student Record",font = "Arial 16")
    lblTitle.place(x=150,y=0)
    global existingName, existingRoll, existingPhone, existingBranch
    global v
    v = IntVar()
    global radbtn9,radbtn10,radbtn11,radbtn12
    radbtn9 = Radiobutton(say, variable=v, value=1, text="By Name",font = "Arial 14", command=rad1)
    radbtn10 = Radiobutton(say, variable=v, value=2, text="By Roll Number",font = "Arial 14", command=rad2)
    radbtn11 = Radiobutton(say, variable=v, value=3, text="By Branch",font = "Arial 14", command=rad3)
    radbtn12 = Radiobutton(say, variable=v, value=4, text="By Phone",font = "Arial 14", command=rad4)
    radbtn9.place(x=10,y=30)
    radbtn10.place(x=120,y=30)
    radbtn11.place(x=290,y=30)
    radbtn12.place(x=420,y=30)

    lblDname = Label(say, text="Enter Your Name",font = "Arial 14")
    lblDname.place(x=10,y=80)
    existingName = Entry(say, state=DISABLED,font = "Arial 14")
    existingName.place(x=200,y=80)

    lblDroll = Label(say, text="Enter Your Roll_No",font = "Arial 14")
    lblDroll.place(x=10,y=160)
    existingRoll = Entry(say, state=DISABLED,font = "Arial 14")
    existingRoll.place(x=200,y=160)

    lblDbranch = Label(say, text="Enter Your Branch",font = "Arial 14")
    lblDbranch.place(x=10,y=240)
    existingBranch = Entry(say, state=DISABLED,font = "Arial 14")
    existingBranch.place(x=200,y=240)

    lblDphone = Label(say, text="Enter Your Phone",font = "Arial 14")
    lblDphone.place(x=10,y=320)
    existingPhone = Entry(say, state=DISABLED,font = "Arial 14")
    existingPhone.place(x=200,y=320)

    btnSave = Button(say, text="Delete Record", command=delete,font = "Arial 16")
    btnSave.place(x=100,y=380)

    btnback = Button(say, text="Back To Main Menu", command=onclick_delete,font = "Arial 16")
    btnback.place(x=300,y=380)

    say.mainloop()

def rad1():
    existingName.config(state=NORMAL)
    existingRoll.config(state=DISABLED)
    existingBranch.config(state=DISABLED)
    existingPhone.config(state=DISABLED)
def rad2():
    existingName.config(state=DISABLED)
    existingRoll.config(state=NORMAL)
    existingBranch.config(state=DISABLED)
    existingPhone.config(state=DISABLED)
def rad3():
    existingName.config(state=DISABLED)
    existingRoll.config(state=DISABLED)
    existingBranch.config(state=NORMAL)
    existingPhone.config(state=DISABLED)

def rad4():
    existingName.config(state=DISABLED)
    existingRoll.config(state=DISABLED)
    existingBranch.config(state=DISABLED)
    existingPhone.config(state=NORMAL)

def radio1():
    radbtn5.config(state = DISABLED)
    radbtn6.config(state = NORMAL)
    radbtn7.config(state=NORMAL)
    radbtn8.config(state=NORMAL)
    newName.config(state = NORMAL)
    newRoll.config(state = DISABLED)
    newBranch.config(state=DISABLED)
    newPhone.config(state=DISABLED)

def radio2():

    radbtn5.config(state=NORMAL)
    radbtn6.config(state=DISABLED)
    radbtn7.config(state=NORMAL)
    radbtn8.config(state=NORMAL)
    newRoll.config(state=NORMAL)
    newName.config(state=DISABLED)
    newBranch.config(state=DISABLED)
    newPhone.config(state=DISABLED)

def radio3():
    radbtn5.config(state=NORMAL)
    radbtn6.config(state=NORMAL)
    radbtn7.config(state=DISABLED)
    radbtn8.config(state=NORMAL)
    newBranch.config(state=NORMAL)
    newName.config(state=DISABLED)
    newRoll.config(state=DISABLED)
    newPhone.config(state=DISABLED)

def radio4():
    radbtn5.config(state=NORMAL)
    radbtn6.config(state=NORMAL)
    radbtn7.config(state=NORMAL)
    radbtn8.config(state=DISABLED)
    newPhone.config(state=NORMAL)
    newName.config(state=DISABLED)
    newRoll.config(state=DISABLED)
    newBranch.config(state=DISABLED)

def radio5():
    updateName.config(state=NORMAL)
    updateRoll.config(state=DISABLED)
    updateBranch.config(state=DISABLED)
    updatePhone.config(state=DISABLED)

def radio6():
    updateName.config(state=DISABLED)
    updateRoll.config(state=NORMAL)
    updateBranch.config(state=DISABLED)
    updatePhone.config(state=DISABLED)

def radio7():
    updateName.config(state=DISABLED)
    updateRoll.config(state=DISABLED)
    updateBranch.config(state=NORMAL)
    updatePhone.config(state=DISABLED)

def radio8():
    updateName.config(state=DISABLED)
    updateRoll.config(state=DISABLED)
    updateBranch.config(state=DISABLED)
    updatePhone.config(state=NORMAL)

def update():
    i = radiobutton.get()
    j = radiobutton2.get()
    if i == 1:
        if j == 2:
            try:
                name = newName.get()
                roll = updateRoll.get()
                update1 = "update student set name = '{}' where roll = '{}'".format(name, roll)
                con = mysql.connector.connect(username="root", password="", host="localhost", database="python")
                cursor = con.cursor()
                cursor.execute(update1)
                con.commit()
                messagebox.showinfo("Updated","Record Has Been Updated")
            except:
                messagebox.showerror("ERROR", "YOU HAVE NOT FILLED ANY FIELD")

        elif j == 3:
            try:
                name = newName.get()
                branch = updateBranch.get()
                update2 = "update student set name = '{}' where branch = '{}'".format(name, branch)
                con = mysql.connector.connect(username="root", password="", host="localhost", database="python")
                cursor = con.cursor()
                cursor.execute(update2)
                con.commit()
                messagebox.showinfo("Updated","Record Has Been Updated")
            except:
                messagebox.showerror("ERROR", "YOU HAVE NOT FILLED ANY FIELD")
        elif j == 4:
            try:
                name = newName.get()
                phone = updatePhone.get()
                update3 = "update student set name = '{}' where phone = '{}'".format(name, phone)
                con = mysql.connector.connect(username="root", password="", host="localhost", database="python")
                cursor = con.cursor()
                cursor.execute(update3)
                con.commit()
                messagebox.showinfo("Updated","Record Has Been Updated")
            except:
                messagebox.showerror("ERROR", "YOU HAVE NOT FILLED ANY FIELD")
    elif i == 2:
        if j == 1:
            try:
                roll = newRoll.get()
                name = updateName.get()
                update4 = "update student set roll = '{}' where name = '{}'".format(roll, name)
                con = mysql.connector.connect(username="root", password="", host="localhost", database="python")
                cursor = con.cursor()
                cursor.execute(update4)
                con.commit()
                messagebox.showinfo("Updated","Record Has Been Updated")
            except:
                messagebox.showerror("ERROR", "YOU HAVE NOT FILLED ANY FIELD")
        elif j == 3:
            try:
                roll = newRoll.get()
                branch = updateBranch.get()
                update5 = "update student set roll = '{}' where branch = '{}'".format(roll, branch)
                con = mysql.connector.connect(username="root", password="", host="localhost", database="python")
                cursor = con.cursor()
                cursor.execute(update5)
                con.commit()
                messagebox.showinfo("Updated","Record Has Been Updated")
            except:
                messagebox.showerror("ERROR", "YOU HAVE NOT FILLED ANY FIELD")
        elif j == 4:
            try:
                roll = newRoll.get()
                phone = updatePhone.get()
                update6 = "update student set roll = '{}' where phone = '{}'".format(roll, phone)
                con = mysql.connector.connect(username="root", password="", host="localhost", database="python")
                cursor = con.cursor()
                cursor.execute(update6)
                con.commit()
                messagebox.showinfo("Updated","Record Has Been Updated")
            except:
                messagebox.showerror("ERROR", "YOU HAVE NOT FILLED ANY FIELD")
    elif i == 3:
        if j == 1:
            try:
                branch = newBranch.get()
                name = updateName.get()
                update7 = "update student set branch = '{}' where name = '{}'".format(branch, name)
                con = mysql.connector.connect(username="root", password="", host="localhost", database="python")
                cursor = con.cursor()
                cursor.execute(update7)
                con.commit()
                messagebox.showinfo("Updated","Record Has Been Updated")
            except:
                messagebox.showerror("ERROR", "YOU HAVE NOT FILLED ANY FIELD")
        elif j == 2:
            try:
                branch = newBranch.get()
                roll = updateRoll.get()
                update8 = "update student set branch = '{}' where roll = '{}'".format(branch, roll)
                con = mysql.connector.connect(username="root", password="", host="localhost", database="python")
                cursor = con.cursor()
                cursor.execute(update8)
                con.commit()
                messagebox.showinfo("Updated","Record Has Been Updated")
            except:
                messagebox.showerror("ERROR", "YOU HAVE NOT FILLED ANY FIELD")
        elif j == 4:
            try:
                branch = newBranch.get()
                phpne = updatePhonel.get()
                update9 = "update student set branch = '{}' where phone = '{}'".format(branch, phone)
                con = mysql.connector.connect(username="root", password="", host="localhost", database="python")
                cursor = con.cursor()
                cursor.execute(update9)
                con.commit()
                messagebox.showinfo("Updated","Record Has Been Updated")
            except:
                messagebox.showerror("ERROR", "YOU HAVE NOT FILLED ANY FIELD")
    elif i==4 :
        if j == 1:
            try:
                phone = newPhone.get()
                name = updatePhone.get()
                update10 = "update student set phone = '{}' where name = '{}'".format(phone, name)
                con = mysql.connector.connect(username="root", password="", host="localhost", database="python")
                cursor = con.cursor()
                cursor.execute(update10)
                con.commit()
                messagebox.showinfo("Updated","Record Has Been Updated")
            except:
                messagebox.showerror("ERROR", "YOU HAVE NOT FILLED ANY FIELD")
        elif j == 2:
            try:
                phone = newPhone.get()
                roll = updateRoll.get()
                update11 = "update student set phone = '{}' where roll = '{}'".format(phone, roll)
                con = mysql.connector.connect(username="root", password="", host="localhost", database="python")
                cursor = con.cursor()
                cursor.execute(update11)
                con.commit()
                messagebox.showinfo("Updated","Record Has Been Updated")
            except:
                messagebox.showerror("ERROR", "YOU HAVE NOT FILLED ANY FIELD")
        elif j == 3 :
            try:
                phone = newPhone.get()
                branch = updateBranch.get()
                update12 = "update student set phone = '{}' where branch = '{}'".format(phone, branch)
                con = mysql.connector.connect(username="root", password="", host="localhost", database="python")
                cursor = con.cursor()
                cursor.execute(update12)
                con.commit()
                messagebox.showinfo("Updated","Record Has Been Updated")
            except:
                messagebox.showerror("ERROR", "YOU HAVE NOT FILLED ANY FIELD")
    else:
        messagebox.showerror("Error", "Please Select Any Option For Deletion")
def delete():
    r = v.get()
    if r == 1:
        try:
            name = existingName.get()
            del1 = "delete from student where name = '{}'".format(name)
            con = mysql.connector.connect(username="root", password="", host="localhost", database="python")
            cursor = con.cursor()
            cursor.execute(del1)
            con.commit()
            messagebox.showinfo("Deleted","Record Has Been Deleted")
        except:
            messagebox.showerror("ERROR", "YOU HAVE NOT FILLED ANY FIELD")

    elif r == 2:
        try:
            roll = existingRoll.get()
            del2 = "delete from student where roll='{}'".format(roll)
            con = mysql.connector.connect(username="root", password="", host="localhost", database="python")
            cursor = con.cursor()
            cursor.execute(del2)
            con.commit()
            messagebox.showinfo("Deleted","Record Has Been Deleted")
        except:
            messagebox.showerror("ERROR", "YOU HAVE NOT FILLED ANY FIELD")
    elif r == 3:
        try:
            branch = existingBranch.get()
            del3 = "delete from student where branch='{}'".format(branch)
            con = mysql.connector.connect(username="root", password="", host="localhost", database="python")
            cursor = con.cursor()
            cursor.execute(del3)
            con.commit()
            messagebox.showinfo("Deleted","Record Has Been Deleted")
        except:
            messagebox.showerror("ERROR", "YOU HAVE NOT FILLED ANY FIELD")

    elif r==4 :
        try:
            phone = existingPhone.get()
            del4 = "delete from student where phone='{}'".format(phone)
            con = mysql.connector.connect(username="root", password="", host="localhost", database="python")
            cursor = con.cursor()
            cursor.execute(del4)
            con.commit()
            messagebox.showinfo("Deleted","Record Has Been Deleted")
        except:
            messagebox.showerror("ERROR", "YOU HAVE NOT FILLED ANY FIELD")
    else:
        messagebox.showerror("Error", "Please Select Any Option For Deletion")
def add():
    name = entrname.get()
    phone = entrphone.get()
    branch = entrbranch.get()
    roll = entrroll.get()
    sql = "insert into student values ('{}','{}','{}','{}')".format(name, roll, branch, phone)

    con = mysql.connector.connect(username="root", password="", host="localhost", database="python")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    messagebox.showinfo("Added","Record Has Been Added...")

def view():
    try:
        view = "select * from student"
        con = mysql.connector.connect(username="root", password="", host="localhost", database="python")
        cursor = con.cursor()
        cursor.execute(view)
        result = cursor.fetchall()

        f = open('details.txt','w')
        for data in result:
            f.write(str(data)+'\n')
        f.close()
        con.close
        import subprocess as sp
        pName = 'notepad.exe'
        fName = 'details.txt'
        sp.Popen({pName,fName})
    except :
        messagebox.showinfo("No data","No such data available")


def onclick_main_add():
    main.destroy()
    add_gui()

def onclick_main_update():
    main.destroy()
    update_gui()

def onclick_main_delete():
    main.destroy()
    delete_gui()

def onclick_main_view():
    main.destroy()
    view()
def onclick_insert():
    hey.destroy()
    main_gui()

def onclick_update():
    window.destroy()
    main_gui()

def onclick_delete():
    say.destroy()
    main_gui()

def onclick_view():
    view1.destroy()
    main_gui()

main_gui()