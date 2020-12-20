from tkinter import *
from tkinter import messagebox
from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk
import backend


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Database Management System")
        self.root.config(bg="cadet blue")
        self.root.resizable(False,False)
        self.root.geometry("1350x750+90+30")
        # self.root.resizable(False, False)

        # creating variables
        std_id = StringVar()
        std_fn = StringVar()
        std_ln = StringVar()
        std_dob = StringVar()
        std_age = StringVar()
        std_gender = StringVar()
        std_address = StringVar()
        std_phone = StringVar()

        # ===================== Functions ===========================
        def exit_btn():
            ask = messagebox.askyesno("Student Database Management System", "Confirm If You Want To Exit")
            if ask > 0:
                root.destroy()
                return

        def clear_btn():
            self.stdid_txt.delete(0, END)
            self.stdfn_txt.delete(0, END)
            self.stdln_txt.delete(0, END)
            self.stddob_txt.delete(0, END)
            self.stdage_txt.delete(0, END)
            self.stdgender_txt.delete(0, END)
            self.stdadd_txt.delete(0, END)
            self.stdphone_txt.delete(0, END)

        def add_btn():
            if (len(std_id.get()) != 0):
                backend.add_data(std_id.get(), std_fn.get(), std_ln.get(), std_dob.get(), std_age.get(),
                                 std_gender.get(), std_address.get(), std_phone.get())
                std_list.delete(0, END)
                std_list.insert(END, std_id.get(), std_fn.get(), std_ln.get(), std_dob.get(), std_age.get(),
                                std_gender.get(), std_address.get(), std_phone.get())

        def display_btn():
            std_list.delete(0, END)
            for row in backend.display_data():
                std_list.insert(END, row, str(""))

        def studentrec(event):
            try:
                global sd
                searchsd = std_list.curselection()
                sd = std_list.get(searchsd)


                self.stdid_txt.delete(0, END)
                self.stdid_txt.insert(END, sd[1])
                self.stdfn_txt.delete(0, END)
                self.stdfn_txt.insert(END, sd[2])
                self.stdln_txt.delete(0, END)
                self.stdln_txt.insert(END, sd[3])
                self.stddob_txt.delete(0, END)
                self.stddob_txt.insert(END, sd[4])
                self.stdage_txt.delete(0, END)
                self.stdage_txt.insert(END, sd[5])
                self.stdgender_txt.delete(0, END)
                self.stdgender_txt.insert(END, sd[6])
                self.stdadd_txt.delete(0, END)
                self.stdadd_txt.insert(END, sd[7])
                self.stdphone_txt.delete(0, END)
                self.stdphone_txt.insert(END, sd[8])
            except :
                messagebox.showerror("Student Database Management System","Please Select Proper Input")

        def delete_btn():
            if (len(std_id.get()) != 0):
                backend.delete_data(sd[0])

        def search_btn():
            std_list.delete(0, END)
            for row in backend.search_data(std_id.get(), std_fn.get(), std_ln.get(), std_dob.get(), std_age.get(), std_gender.get(), std_address.get(), std_phone.get()):
                std_list.insert(END, row, str(""))

        def update_btn():
            backend.delete_data(sd[0])
            backend.add_data(std_id.get(), std_fn.get(), std_ln.get(), std_dob.get(), std_age.get(),
                             std_gender.get(), std_address.get(), std_phone.get())

        # =====================lables and entry widgets===========================

        title_frame = Frame(root)
        title_frame.pack(side=TOP)
        self.title_lbl = Label(title_frame, font="arial 47 bold", text="Student Database Management System   ")
        self.title_lbl.grid(padx=100)

        bottom_frame = Frame(root, bd=2, width=1450, height=70, pady=10, bg="ghost white", relief=RIDGE)
        bottom_frame.pack(side=BOTTOM)

        data_frame = Frame(root, bd=1, width=1450, height=400, pady=20, bg="cadet blue")
        data_frame.pack(side=TOP)

        dataleft_frame = LabelFrame(data_frame, bd=1, width=1000, height=600, padx=20, pady=20, bg="ghost white",
                                    relief=RIDGE, font="arial 20 bold", text="Student Info")
        dataleft_frame.pack(side=LEFT, padx=25)
        dataright_frame = LabelFrame(data_frame, bd=1, width=350, height=600, padx=31, pady=3, bg="ghost white",
                                     relief=RIDGE, font="arial 20 bold", text="Student Details")
        dataright_frame.pack(side=RIGHT, padx=25)

        # =====================buttons and Entry===========================

        self.stdid_lbl = ttk.Label(dataleft_frame, font="arial 20 bold",
                               text=" Student ID: ")
        self.stdid_lbl.grid(row=0, column=0)
        self.stdid_txt = ttk.Entry(dataleft_frame, font="arial 20 bold",
                               textvariable=std_id)
        self.stdid_txt.grid(row=0, column=1, padx=40, pady=10)


        self.stdfn_lbl = ttk.Label(dataleft_frame, font="arial 20 bold",
                               text=" First Name: ")
        self.stdfn_lbl.grid(row=1, column=0)
        self.stdfn_txt = ttk.Entry(dataleft_frame, font="arial 20 bold",
                               textvariable=std_fn)
        self.stdfn_txt.grid(row=1, column=1, padx=40, pady=10)


        self.stdln_lbl = ttk.Label(dataleft_frame, font="arial 20 bold",
                               text=" Last Name: ")
        self.stdln_lbl.grid(row=2, column=0)
        self.stdln_txt = ttk.Entry(dataleft_frame, font="arial 20 bold",
                               textvariable=std_ln)
        self.stdln_txt.grid(row=2, column=1, padx=40, pady=10)


        self.stddob_lbl = ttk.Label(dataleft_frame, font="arial 20 bold",
                                text="Date Of Birth:")
        self.stddob_lbl.grid(row=3, column=0)
        self.stddob_txt = ttk.Entry(dataleft_frame, font="arial 20 bold",
                                textvariable=std_dob)
        self.stddob_txt.grid(row=3, column=1, padx=40, pady=10)


        self.stdage_lbl = ttk.Label(dataleft_frame, font="arial 20 bold",
                                text=" Age: ")
        self.stdage_lbl.grid(row=4, column=0)
        self.stdage_txt = ttk.Entry(dataleft_frame, font="arial 20 bold",
                                textvariable=std_age)
        self.stdage_txt.grid(row=4, column=1, padx=40, pady=10)


        self.stdgender_lbl = ttk.Label(dataleft_frame, font="arial 20 bold",
                                   text=" Gender: ")
        self.stdgender_lbl.grid(row=5, column=0)
        self.stdgender_txt = ttk.Entry(dataleft_frame, font="arial 20 bold",
                                   textvariable=std_gender)
        self.stdgender_txt.grid(row=5, column=1, padx=40, pady=10)


        self.stdadd_lbl = ttk.Label(dataleft_frame, font="arial 20 bold",
                                text=" Address: ")
        self.stdadd_lbl.grid(row=6, column=0)
        self.stdadd_txt = ttk.Entry(dataleft_frame, font="arial 20 bold",
                                textvariable=std_address)
        self.stdadd_txt.grid(row=6, column=1, padx=40, pady=10)


        self.stdphone_lbl = ttk.Label(dataleft_frame, font="arial 20 bold",
                                  text=" Phone No: ")
        self.stdphone_lbl.grid(row=7, column=0)
        self.stdphone_txt = ttk.Entry(dataleft_frame, font="arial 20 bold",
                                  textvariable=std_phone)
        self.stdphone_txt.grid(row=7, column=1, padx=40, pady=10)


        # =====================scrollbar and listbox===========================

        std_scroll = ttk.Scrollbar(dataright_frame)
        std_scroll.grid(row=0, column=1, sticky=N + S)

        std_list = Listbox(dataright_frame, width=50, height=18, font='arial 12 bold'
                           , yscrollcommand=std_scroll.set)
        std_list.grid(row=0, column=0)
        std_list.bind('<<ListboxSelect>>', studentrec)
        std_scroll.config(command=std_list.yview)

        # =====================buttons for bottom frame==================
        add_btn = Button(bottom_frame, text="Add New", font="arial 20 bold", height=1, width=10, bd=4, command=add_btn)
        add_btn.grid(row=0, column=0, padx=4)
        display_btn = Button(bottom_frame, text="Display", font="arial 20 bold", height=1, width=10, bd=4,
                             command=display_btn)
        display_btn.grid(row=0, column=1, padx=4)
        clear_btn = Button(bottom_frame, text="Clear", font="arial 20 bold", height=1, width=10, bd=4,
                           command=clear_btn)
        clear_btn.grid(row=0, column=2, padx=4)
        delete_btn = Button(bottom_frame, text="Delete", font="arial 20 bold", height=1, width=10, bd=4,
                            command=delete_btn)
        delete_btn.grid(row=0, column=3, padx=4)
        search_btn = Button(bottom_frame, text="Search", font="arial 20 bold", height=1, width=10, bd=4,
                            command=search_btn)
        search_btn.grid(row=0, column=4, padx=4)
        update_btn = Button(bottom_frame, text="Update", font="arial 20 bold", height=1, width=10, bd=4,
                            command=update_btn)
        update_btn.grid(row=0, column=5, padx=4)
        exit_btn = Button(bottom_frame, text="Exit", font="arial 20 bold", height=1, width=10, bd=4, command=exit_btn)
        exit_btn.grid(row=0, column=6, padx=4)


def main():
    root = ThemedTk(theme="smog")
    root.iconbitmap(r'icons/icon.ico')
    app = Student(root)
    root.mainloop()

main()