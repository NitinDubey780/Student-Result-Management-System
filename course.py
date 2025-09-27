from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
class Course:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()




        title = Label(self.root, text="Manage Course Details", font=("Comic Sans MS", 20, "bold"), bg="#033054", fg="pink")
        title.place(x=10, y=15, width=1180, height=35)


        #===========================Variables================================#


        self.var_courses = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()





        #=========================Widgets==================================#

        lbl_courseName = Label(self.root, text="Course Name", font=("Comic Sans MS", 15, 'bold' ), bg='white' ).place(x=10, y=60)
        lbl_duration = Label(self.root, text="Duration", font=("Comic Sans MS", 15, 'bold' ), bg='white' ).place(x=10, y=100)
        lbl_charges = Label(self.root, text="Charges", font=("Comic Sans MS", 15, 'bold' ), bg='white' ).place(x=10, y=140)
        lbl_description = Label(self.root, text="Description", font=("Comic Sans MS", 15, 'bold' ), bg='white' ).place(x=10, y=180)




        #==============================Entry ===================#

        self.txt_courseName = Entry(self.root, textvariable=self.var_courses, font=("Comic Sans MS", 15, 'bold' ), bg='lightgray' )
        self.txt_courseName.place(x=150, y=60, width=200)
        txt_duration = Entry(self.root, textvariable=self.var_duration,font=("Comic Sans MS", 15, 'bold' ), bg='lightgray' ).place(x=150, y=100, width=200)
        txt_charges = Entry(self.root, textvariable=self.var_charges , font=("Comic Sans MS", 15, 'bold' ), bg='lightgray' ).place(x=150, y=140, width=200)
        self.txt_description = Text(self.root,font=("Comic Sans MS", 15, 'bold' ), bg='lightgray' )
        self.txt_description.place(x=150, y=180, width=500, height=130)








        # =============================== Buttons================================#

        self.btn_add = Button(self.root, text = 'Save', font=("Comic Sans MS", 15, 'bold'), bg="#068162", fg="white", cursor="hand2", command=self.add)
        self.btn_add.place(x=150, y=400, width=110, height=40)

        self.btn_update = Button(self.root, text = 'Update', font=("Comic Sans MS", 15, 'bold'), bg="#04709b", fg="black", cursor="hand2", command=self.update)
        self.btn_update.place(x=270, y=400, width=110, height=40)

        self.btn_delete = Button(self.root, text = 'Delete', font=("Comic Sans MS", 15, 'bold'), bg="#9C08E0", fg="white", cursor="hand2", command=self.delete)
        self.btn_delete.place(x=390, y=400, width=110, height=40)

        self.btn_clear = Button(self.root, text = 'Clear', font=("Comic Sans MS", 15, 'bold'), bg="#9E97A1", fg="white", cursor="hand2", command=self.clear)
        self.btn_clear.place(x=510, y=400, width=110, height=40)





        #==============================Search Panel =======================#

        self.var_search = StringVar()

        lbl_search_courseName = Label(self.root, text="Course Name ", font=("Comic Sans MS", 15, 'bold' ), bg='white' ).place(x=720, y=60)


        txt_search_courseName = Entry(self.root, textvariable=self.var_search, font=("Comic Sans MS", 15, 'bold' ), bg='lightgray' ).place(x=870, y=60, width=180)

        btn_search = Button(self.root, text = 'Search', font=("Comic Sans MS", 15, 'bold'), bg="#03a9f4", fg="white", cursor="hand2", command=self.search).place(x=1070, y=60, width=120, height=28)









        #=====================================Contents=========================#


        self.C_Frame = Frame(self.root, bd= 2, relief=RIDGE)
        self.C_Frame.place(x = 720, y = 100, width = 470, height=340)


        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)


        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("cid","Name", "Duration", "Charges", "Description" ), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)


        self.CourseTable.heading("cid", text="Course ID")
        self.CourseTable.heading("Name", text="Name")
        self.CourseTable.heading("Duration", text="Duration")
        self.CourseTable.heading("Charges", text="Charges")
        self.CourseTable.heading("Description", text="Description")
        self.CourseTable["show"] = 'headings'
        self.CourseTable.column("cid", width=100)
        self.CourseTable.column("Name", width=100)
        self.CourseTable.column("Duration", width = 100)
        self.CourseTable.column("Charges", width=100)
        self.CourseTable.column("Description", width=150)
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()







    def get_data(self,ev):
        self.txt_courseName.config(state='readonly')
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]
        self.var_courses.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])

        self.txt_description.delete('1.0', END)
        self.txt_description.insert(END, row[4])





    #================================ADD Data in DataBase ===============================+++++++++++


    def add(self):
        con = sqlite3.connect(database="Result_Manage.db")
        cur = con.cursor()
        try:
            if self.var_courses.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM course WHERE name = ?", (self.var_courses.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Course Name is Already Present", parent=self.root)
                else:
                    cur.execute("insert into course (Name, Duration, Charges, Description) values(?,?,?,?)",(
                        self.var_courses.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0", END)

                    ))

                    con.commit()
                    messagebox.showinfo("Success", "Course Added Successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)


    #==============================Show Data On Table DataBase========================================


    def show(self):
        con = sqlite3.connect(database="Result_Manage.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM course")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)




    #======================================Update Course===============================================

    def update(self):
        con = sqlite3.connect(database="Result_Manage.db")
        cur = con.cursor()
        try:
            if self.var_courses.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM course WHERE name = ?", (self.var_courses.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Select Course from List ", parent=self.root)
                else:
                    cur.execute("update course set Duration=?, Charges=?, Description=? where Name = ?",(
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0", END),
                        self.var_courses.get()

                    ))

                    con.commit()
                    messagebox.showinfo("Success", "Course Update Successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)





    #======================================Clear Button Functionality==============================
    def clear(self):
        self.show()
        self.var_courses.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete('1.0', END)
        self.txt_courseName.config(state=NORMAL)


    #==============================Delete Function==========================================

    def delete(self):
        con = sqlite3.connect(database="Result_Manage.db")
        cur = con.cursor()
        try:
            if self.var_courses.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM course WHERE name = ?", (self.var_courses.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Please Select course from the list", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete ? ", parent=self.root)
                    if op==True:
                        cur.execute("delete from course where Name = ?", (self.var_courses.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Delete Successfully", parent= self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)




    #======================================Search Funtion =======================================


    def search(self):
        con = sqlite3.connect(database="Result_Manage.db")
        cur = con.cursor()
        try:
            cur.execute(f"SELECT * FROM course where name like '%{self.var_search.get()}%'")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)






















if __name__ == "__main__":
    root = Tk()
    obj = Course(root)
    root.mainloop()