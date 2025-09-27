from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from course import Course
from student import Student
from result import Result
from report import Report
import sqlite3
class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="white")

        #===================Icon===========================#
        self.logo_dash = ImageTk.PhotoImage(file = "images/logo_dash1.png")


            #==================title========================#




        title = Label(self.root, text="Student Result Management System", padx=10, compound=LEFT, image=self.logo_dash, 
                    font=("Comic Sans MS", 20, "bold"), bg="#033054", fg="pink").place(x=0, y=0, relwidth=1, height=50)




            #==================Menu=========================#
        M_frame = LabelFrame(self.root, text= "Menu", font=("times new roman", 15), bg="white")
        M_frame.place(x=10, y=70, width=1340, height=80)

        #========================Menu Button==================================#


        button_data = [
            ("Course", self.add_course),
            ("Student", self.add_student),
            ("Result", self.add_result),
            ("View Result", self.view_report),
            ("Exit", None)
            ]
        button_width = 180
        button_height = 40
        button_spacing = 90
        start_x = 20
        y_position = 5

        for index, (text, command) in enumerate(button_data):
            x_position = start_x + index * (button_width + button_spacing)
            btn = Button(M_frame, text=text, font=("Comic Sans MS", 15, "bold"),
                        bg="#0b5377", fg="white", cursor="hand2", command=command)
            btn.place(x=x_position, y=y_position, width=button_width, height=button_height)
        


        #================================Content_Windows==========================#

        self.bg_img = Image.open("images/Designer.png")
        self.bg_img = self.bg_img.resize((920, 350), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)



        self.lbl_bg = Label(self.root, image=self.bg_img).place(x=400, y=180, width=920, height=350)




        #==========================Update Details ========================


        self.lbl_course = Label(self.root,text="Total Courses\n[ 0 ]", font=("Comic Sans MS", 20), 
                                bd=10, relief=RIDGE, bg="#e43b06", fg="white")
        self.lbl_course.place(x=400, y=530, width=300, height=100)
        

        self.lbl_student = Label(self.root,text="Total Students\n[ 0 ]", font=("Comic Sans MS", 20), 
                                bd=10, relief=RIDGE, bg="#0646f5", fg="white")
        self.lbl_student.place(x=710, y=530, width=300, height=100)
        

        self.lbl_result = Label(self.root,text="Total Results\n[ 0 ]", font=("Comic Sans MS", 20), 
                                bd=10, relief=RIDGE, bg="#005800", fg="white")
        self.lbl_result.place(x=1020, y=530, width=300, height=100)

        footer = Label(self.root, text= "Student Result Management System \nContact Us : 7307734575", 
                    font=("Comic Sans MS", 12), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)

        self.update_details()
        self.update_student()
        self.update_result()






    def update_details(self):
        con = sqlite3.connect(database="Result_Manage.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM course")
            cr = cur.fetchall()
            self.lbl_course.config(text=f"Total Course[{str(len(cr))}]")
            self.lbl_course.after(200, self.update_details)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def update_student(self):
        con = sqlite3.connect(database="Result_Manage.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM student")
            cr = cur.fetchall()
            self.lbl_student.config(text=f"Total Student[{str(len(cr))}]")
            self.lbl_student.after(200, self.update_student)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")




    def update_result(self):
        con = sqlite3.connect(database="Result_Manage.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM result")
            cr = cur.fetchall()
            self.lbl_result.config(text=f"Total Result[{str(len(cr))}]")
            self.lbl_result.after(200, self.update_result)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    
        



    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Course(self.new_win)

    
    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Student(self.new_win)
    

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Result(self.new_win)


    def view_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Report(self.new_win)






if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
