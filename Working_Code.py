from tkinter import *
from random import *
import sqlite3

from tkinter.ttk import Treeview


# from contextlib import closing


############################################################################################
## ===================ABDULAZIM AHMED============================================##
############################################################################################


class HomeFrame:

    def __init__(self, page_color, goto_login_page, *args, **kwargs):
        ####### create frame
        self.app_frame = Frame(root,
                               bg=page_color)

        ##### create title label
        self.title_label = Label(self.app_frame,
                                 text="Welcome to the Quiz Generator System",
                                 font=("Calibri", 40),
                                 fg=page_color, bg="white")
        self.title_label.grid(row=0, column=1,
                              ipady=50, ipadx=50,
                              pady=50, padx=50,
                              columnspan=2)

        # create the forward button
        self.button_pic = PhotoImage(file="Forward_button.png")
        self.forward_btn = Button(self.app_frame,
                                  image=self.button_pic,
                                  bg=page_color,
                                  borderwidth=0,
                                  command=lambda: self.goto_login(goto_login_page))
        self.forward_btn.grid(row=1, column=1,
                              columnspan=2)


        ##### question bank button
        self.admin_page_btn = Button(self.app_frame,
                                     text="Admin Page",
                                     bg="white", fg=page_color,
                                     borderwidth=0,
                                     command=lambda: self.admin_page())
        self.admin_page_btn.grid(row=3, column=2,
                                 ipady=10, ipadx=10,
                                 pady=50, padx=50,
                                 sticky="w")

        ########### QUIT BTN
        self.quit_btn = Button(self.app_frame,
                               text="Quit",
                               bg="white", fg=page_color,
                               borderwidth=0,
                               command=lambda: quit())
        self.quit_btn.grid(row=11, column=1,
                           columnspan=2,
                           ipady=10, ipadx=10,
                           pady=5, padx=50,
                           )



        ##### create empty space
        self.app_frame.grid_columnconfigure(0, weight=1)
        self.app_frame.grid_columnconfigure(10, weight=1)

        self.app_frame.grid_rowconfigure(2, weight=1)

    def goto_login(self, goto_login_page):
        self.app_frame.pack_forget()
        goto_login_page.display_frame()

    def show_user_record(self):
        user_database = sqlite3.connect("user_database.db")
        cursor = user_database.cursor()

        rows = cursor.execute("SELECT * FROM users").fetchall()
        print(rows)

        user_database.close()

    def display_frame(self):
        self.app_frame.pack(fill='both', expand=1, )

    def admin_page(self):
        self.app_frame.pack_forget()
        AdminPage("#4C7F99").display_frame()


###############################################################################################################
class AdminPage:
    def __init__(self, page_color, *args, **kwargs):
        self.tree_frame = Frame(root,
                                bg=page_color)
        self.top_button_frame = Frame(root,
                                      bg=page_color,
                                      )

        self.bottom_entry_frame = Frame(root, bg=page_color)

        self.bottom_button_frame = Frame(root,
                                         bg=page_color,
                                         )
        #################################
        ####################### TOP BUTTONS
        self.maths_btn = Button(self.top_button_frame,
                                text="Maths",
                                bg="white", fg=page_color,
                                borderwidth=0, height=3, width=20
                                , command=lambda: self.view_maths())
        self.maths_btn.pack(side=LEFT,
                            padx=10, pady=10)

        self.history_btn = Button(self.top_button_frame,
                                  text="History",
                                  bg="white", fg=page_color,
                                  borderwidth=0, height=3, width=20
                                  , command=lambda: self.view_history())
        self.history_btn.pack(side=LEFT,
                              padx=10, pady=10)

        self.science_btn = Button(self.top_button_frame,
                                  text="Science",
                                  bg="white", fg=page_color,
                                  borderwidth=0, height=3, width=20
                                  , command=lambda: self.view_science())
        self.science_btn.pack(side=LEFT,
                              padx=10, pady=10)

        ##############################
        ######################### BOTTOM LABELS ENTRY
        self.module_label = Label(self.bottom_entry_frame,
                                  text="Module",
                                  font=("Calibri", 12, "bold"),
                                  bg=page_color, fg="white"
                                  )
        self.module_label.grid(column=0, row=0,
                               ipady=5, ipadx=5,
                               pady=5, padx=5, )

        self.question_label = Label(self.bottom_entry_frame,
                                    text="Question",
                                    font=("Calibri", 12, "bold"),
                                    bg=page_color, fg="white"
                                    )
        self.question_label.grid(column=1, row=0,
                                 ipady=5, ipadx=5,
                                 pady=5, padx=5, )

        self.questionid_label = Label(self.bottom_entry_frame,
                                      text="QuestionID",
                                      font=("Calibri", 12, "bold"),
                                      bg=page_color, fg="white"
                                      )
        self.questionid_label.grid(column=2, row=0,
                                   ipady=5, ipadx=5,
                                   pady=5, padx=5, )

        self.type_label = Label(self.bottom_entry_frame,
                                text="Type",
                                font=("Calibri", 12, "bold"),
                                bg=page_color, fg="white"
                                )
        self.type_label.grid(column=3, row=0,
                             ipady=5, ipadx=5,
                             pady=5, padx=5, )

        self.wa1_label = Label(self.bottom_entry_frame,
                               text="Wrong 1",
                               font=("Calibri", 12, "bold"),
                               bg=page_color, fg="white"
                               )
        self.wa1_label.grid(column=4, row=0,
                            ipady=5, ipadx=5,
                            pady=5, padx=5, )

        self.wa2_label = Label(self.bottom_entry_frame,
                               text="Wrong 2",
                               font=("Calibri", 12, "bold"),
                               bg=page_color, fg="white"
                               )
        self.wa2_label.grid(column=5, row=0,
                            ipady=5, ipadx=5,
                            pady=5, padx=5, )

        self.wa3_label = Label(self.bottom_entry_frame,
                               text="Wrong 3",
                               font=("Calibri", 12, "bold"),
                               bg=page_color, fg="white"
                               )
        self.wa3_label.grid(column=6, row=0,
                            ipady=5, ipadx=5,
                            pady=5, padx=5, )

        self.ca_label = Label(self.bottom_entry_frame,
                              text="Correct",
                              font=("Calibri", 12, "bold"),
                              bg=page_color, fg="white"
                              )
        self.ca_label.grid(column=7, row=0,
                           ipady=5, ipadx=5,
                           pady=5, padx=5, )

        self.review_label = Label(self.bottom_entry_frame,
                                  text="Review",
                                  font=("Calibri", 12, "bold"),
                                  bg=page_color, fg="white"
                                  )
        self.review_label.grid(column=8, row=0,
                               ipady=5, ipadx=5,
                               pady=5, padx=5, )

        ###############################
        ######################## BOTTOM ENTRIES

        self.module_entry = Entry(self.bottom_entry_frame,
                                  font=("Calibri", 12, "bold"),
                                  fg=page_color, width=17
                                  )
        self.module_entry.grid(column=0, row=1,
                               ipady=5, ipadx=5,
                               pady=5, padx=5,
                               )

        self.question_entry = Entry(self.bottom_entry_frame,
                                    font=("Calibri", 12, "bold"),
                                    fg=page_color, width=17
                                    )
        self.question_entry.grid(column=1, row=1,
                                 ipady=5, ipadx=5,
                                 pady=5, padx=5,
                                 )

        self.questionid_entry = Entry(self.bottom_entry_frame,
                                      font=("Calibri", 12, "bold"),
                                      fg=page_color, width=17
                                      )
        self.questionid_entry.grid(column=2, row=1,
                                   ipady=5, ipadx=5,
                                   pady=5, padx=5,
                                   )

        self.type_entry = Entry(self.bottom_entry_frame,
                                font=("Calibri", 12, "bold"),
                                fg=page_color, width=17
                                )
        self.type_entry.grid(column=3, row=1,
                             ipady=5, ipadx=5,
                             pady=5, padx=5,
                             )

        self.wa1_entry = Entry(self.bottom_entry_frame,
                               font=("Calibri", 12, "bold"),
                               fg=page_color, width=17
                               )
        self.wa1_entry.grid(column=4, row=1,
                            ipady=5, ipadx=5,
                            pady=5, padx=5,
                            )

        self.wa2_entry = Entry(self.bottom_entry_frame,
                               font=("Calibri", 12, "bold"),
                               fg=page_color, width=17
                               )
        self.wa2_entry.grid(column=5, row=1,
                            ipady=5, ipadx=5,
                            pady=5, padx=5,
                            )

        self.wa3_entry = Entry(self.bottom_entry_frame,
                               font=("Calibri", 12, "bold"),
                               fg=page_color, width=17
                               )
        self.wa3_entry.grid(column=6, row=1,
                            ipady=5, ipadx=5,
                            pady=5, padx=5,
                            )

        self.ca_entry = Entry(self.bottom_entry_frame,
                              font=("Calibri", 12, "bold"),
                              fg=page_color, width=17
                              )
        self.ca_entry.grid(column=7, row=1,
                           ipady=5, ipadx=5,
                           pady=5, padx=5,
                           )

        self.review_entry = Entry(self.bottom_entry_frame,
                                  font=("Calibri", 12, "bold"),
                                  fg=page_color, width=17
                                  )
        self.review_entry.grid(column=8, row=1,
                               ipady=5, ipadx=5,
                               pady=5, padx=5,
                               )

        ###############################
        ################## BOTTOM BUTTONS

        self.add_question_btn = Button(self.bottom_button_frame,
                                       text="Add Question",
                                       bg="white", fg=page_color,
                                       borderwidth=0, height=3, width=20
                                       , command=lambda: self.add_question())

        self.delete_question_btn = Button(self.bottom_button_frame,
                                       text="Delete Question",
                                       bg="white", fg=page_color,
                                       borderwidth=0, height=3, width=20
                                       , command=lambda: self.delete_question())

        self.delete_module_process_btn = Button(self.bottom_button_frame,
                                                text="Delete Module",
                                                bg="white", fg=page_color,
                                                borderwidth=0, height=3, width=20,
                                                command=lambda: self.delete_topic()
                                                )

        self.add_module_process_btn = Button(self.bottom_button_frame,
                                             text="Add Module",
                                             bg="white", fg=page_color,
                                             borderwidth=0, height=3, width=20,
                                             command=lambda: self.add_topic())

        self.add_module_process_btn.pack(side=LEFT,
                                         padx=10, pady=10)
        self.delete_module_process_btn.pack(side=LEFT,
                                            padx=10, pady=10)

        self.add_question_btn.pack(side=LEFT,
                                   padx=10, pady=10)
        self.delete_question_btn.pack(side=LEFT,
                                   padx=10, pady=10)

        ################### TREE TABLE
        self.scrollbary = Scrollbar(self.tree_frame, orient=VERTICAL)
        self.scrollbarx = Scrollbar(self.tree_frame, orient=HORIZONTAL)

        self.module_tree = Treeview(self.tree_frame, columns=("Module",
                                                              "Question",
                                                              "QuestionID",
                                                              "Type",
                                                              "wa1",
                                                              "wa2",
                                                              "wa3",
                                                              "ca",
                                                              "Review"),
                                    selectmode="extended",
                                    height=300,
                                    yscrollcommand=self.scrollbary.set,
                                    xscrollcommand=self.scrollbarx.set)

        self.scrollbary.config(command=self.module_tree.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)
        self.scrollbarx.config(command=self.module_tree.xview)
        self.scrollbarx.pack(side=BOTTOM, fill=X)

        self.module_tree.heading('Module', text="Module", anchor=W)
        self.module_tree.heading('Question', text="Question", anchor=W)
        self.module_tree.heading('QuestionID', text="QuestionID", anchor=W)
        self.module_tree.heading('Type', text="Type", anchor=W)
        self.module_tree.heading('wa1', text="Wrong 1", anchor=W)
        self.module_tree.heading('wa2', text="Wrong 2", anchor=W)
        self.module_tree.heading('wa3', text="Wrong 3", anchor=W)
        self.module_tree.heading('ca', text="Correct", anchor=W)
        self.module_tree.heading('Review', text="Review", anchor=W)

        self.module_tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.module_tree.column('#1', stretch=NO, minwidth=0, width=200)
        self.module_tree.column('#2', stretch=NO, minwidth=0, width=200)
        self.module_tree.column('#3', stretch=NO, minwidth=0, width=200)
        self.module_tree.column('#4', stretch=NO, minwidth=0, width=200)
        self.module_tree.column('#5', stretch=NO, minwidth=0, width=200)
        self.module_tree.column('#6', stretch=NO, minwidth=0, width=200)
        self.module_tree.column('#7', stretch=NO, minwidth=0, width=200)
        self.module_tree.column('#8', stretch=NO, minwidth=0, width=200)
        self.module_tree.column('#9', stretch=NO, minwidth=0, width=200)

        self.module_tree.pack()

    def display_frame(self):
        self.top_button_frame.pack(side=TOP)
        self.bottom_button_frame.pack(side=BOTTOM)
        self.bottom_entry_frame.pack(side=BOTTOM)
        self.tree_frame.pack(side=BOTTOM)

    def delete_question(self):
        connection = sqlite3.connect("question_bank.db")
        x = connection.cursor()

        module_name = self.module_entry.get()
        module_name_str = ''.join(module_name)

        questionID_name = self.questionid_entry.get()
        questionID_name_str = ''.join(questionID_name)

        x.execute("DELETE FROM '{}' WHERE QuestionID = '{}'".format(module_name_str, questionID_name_str))

        connection.commit()
        connection.close()

    def add_question(self):
        connection = sqlite3.connect("question_bank.db")
        x = connection.cursor()

        module_name = self.module_entry.get()
        module_name_str = ''.join(module_name)

        question_name = self.question_entry.get()
        question_name_str = ''.join(question_name)

        questionID_name = self.questionid_entry.get()
        questionID_name_str = ''.join(questionID_name)

        type_name = self.type_entry.get()
        type_name_str = ''.join(type_name)

        wa1_name = self.wa1_entry.get()
        wa1_name_str = ''.join(wa1_name)

        wa2_name = self.wa2_entry.get()
        wa2_name_str = ''.join(wa2_name)

        wa3_name = self.wa3_entry.get()
        wa3_name_str = ''.join(wa3_name)

        ca_name = self.ca_entry.get()
        ca_name_str = ''.join(ca_name)

        review_name = self.review_entry.get()
        review_name_str = ''.join(review_name)

        x.execute(
            "INSERT INTO '{}' VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(module_name_str,
                                                                                                   module_name_str,
                                                                                                   question_name_str,
                                                                                                   questionID_name_str,
                                                                                                   type_name_str,
                                                                                                   wa1_name_str,
                                                                                                   wa2_name_str,
                                                                                                   wa3_name_str,
                                                                                                   ca_name_str,
                                                                                                   review_name_str))

        connection.commit()
        connection.close()

    def add_topic(self):
        connection = sqlite3.connect("question_bank.db")
        x = connection.cursor()

        module_name = self.module_entry.get()
        module_name_str = ''.join(module_name)
        x.execute("CREATE TABLE IF NOT EXISTS {} (Module,  Question, QuestionID, Type, WA1, WA2, WA3, CA)".format(
            module_name_str))

        connection.commit()
        connection.close()

    def delete_topic(self):
        connection = sqlite3.connect("question_bank.db")
        x = connection.cursor()

        module_name = self.module_entry.get()
        module_name_str = ''.join(module_name)
        x.execute("DROP TABLE {};".format(module_name_str))

    def view_maths(self):
        connect = sqlite3.connect("question_bank.db")
        x = connect.cursor()

        self.module_tree.delete(*self.module_tree.get_children())
        x.execute("SELECT * FROM Maths ORDER BY 'QuestionID'")
        questions = x.fetchall()
        for q in questions:
            self.module_tree.insert('', 'end', values=(q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8]))

        connect.close()

    def view_history(self):
        connect = sqlite3.connect("question_bank.db")
        x = connect.cursor()

        self.module_tree.delete(*self.module_tree.get_children())
        x.execute("SELECT * FROM History ORDER BY 'QuestionID'")
        questions = x.fetchall()
        for q in questions:
            self.module_tree.insert('', 'end', values=(q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8]))

        connect.close()

    def view_science(self):
        connect = sqlite3.connect("question_bank.db")
        x = connect.cursor()

        self.module_tree.delete(*self.module_tree.get_children())
        x.execute("SELECT * FROM Science ORDER BY 'QuestionID'")
        questions = x.fetchall()
        for q in questions:
            self.module_tree.insert('', 'end', values=(q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8]))

        connect.close()


##################################################################################################
## ===================================SORAN AZIZ======================================== ##
##################################################################################################
class LoginFrame:

    def __init__(self, page_color, logged_in_page, register_page, *args, **kwargs):
        # Create page frame
        self.app_frame = Frame(root,
                               bg=page_color)
        # title label "login"
        self.title_label = Label(self.app_frame,
                                 text="Login",
                                 font=("Calibri", 40),
                                 fg=page_color, bg="white")  # fg = dark turquoise

        self.title_label.grid(column=1, row=0,
                              columnspan=2,
                              ipady=15, ipadx=150,
                              pady=15, padx=15)

        ################### username row
        self.username_text = Label(self.app_frame,
                                   text="Username",
                                   font=("Calibri", 24, "bold"),
                                   bg=page_color, fg="white")
        self.username_entry = Entry(self.app_frame,
                                    font=("Calibri", 24, "bold"),
                                    fg=page_color)

        self.username_entry.grid(column=2, row=2,
                                 pady=5, padx=5)
        self.username_text.grid(column=1, row=2,
                                pady=5,
                                ipadx=10)

        ################# password row
        self.password_text = Label(self.app_frame,
                                   text="Password",
                                   font=("Calibri", 24, "bold"),
                                   bg=page_color, fg="white")
        self.password_entry = Entry(self.app_frame,
                                    show="*",
                                    font=("Calibri", 24, "bold"),
                                    fg=page_color)

        self.password_entry.grid(column=2, row=3,
                                 pady=5, padx=5)
        self.password_text.grid(column=1, row=3,
                                pady=5,
                                ipadx=10)

        ###### show/hide password button
        self.show_pass_btn = Button(self.app_frame,
                                    text="show",
                                    font=("Calibri", 16, "bold"),
                                    bg="white", fg=page_color,
                                    borderwidth=0,
                                    command=lambda: self.show_password())
        self.show_pass_btn.grid(column=2, row=4)

        self.hide_pass_btn = Button(self.app_frame,
                                    text="hide",
                                    font=("Calibri", 16, "bold"),
                                    bg="white", fg=page_color,
                                    borderwidth=0,
                                    command=lambda: self.hide_password())

        ########## login button
        self.login_btn = Button(self.app_frame,
                                text="Log in",
                                font=("Calibri", 24, "bold"),
                                bg="white", fg=page_color,
                                borderwidth=0,
                                command=lambda: self.check_entry_then_login(logged_in_page))
        self.login_btn.grid(column=1, row=5,
                            columnspan=2,
                            pady=40)

        ########## register button
        self.register_btn = Button(self.app_frame,
                                   text="Register for an account ->",
                                   font=("Calibri", 16, "bold"),
                                   bg=page_color, fg="white",
                                   borderwidth=0,
                                   command=lambda: self.goto_register_page(register_page))
        self.register_btn.grid(column=1, row=7,
                               columnspan=2,
                               sticky="w")

        ######## wrong try again
        self.wrong_label = Label(self.app_frame,
                                 text="Username or Password is wrong",
                                 font=("Calibri", 16, "bold"),
                                 bg=page_color, fg="red")

        self.quit_btn = Button(self.app_frame,
                               text="Quit",
                               bg="white", fg=page_color,
                               borderwidth=0,
                               command=lambda: quit())
        self.quit_btn.grid(row=100, column=1,
                           columnspan=2,
                           ipady=10, ipadx=10,
                           pady=5, padx=50,
                           )

        ########## empty columns
        self.app_frame.grid_columnconfigure(0, weight=1)
        self.app_frame.grid_columnconfigure(10, weight=1)

        self.app_frame.grid_rowconfigure(1, weight=1)
        self.app_frame.grid_rowconfigure(10, weight=2)

    def display_frame(self):
        self.app_frame.pack(fill='both', expand=1)

    def show_password(self):
        self.password_entry.config(show="")
        self.show_pass_btn.grid_forget()
        self.hide_pass_btn.grid(column=2, row=4)

    def hide_password(self):
        self.password_entry.config(show="*")
        self.hide_pass_btn.grid_forget()
        self.show_pass_btn.grid(column=2, row=4)

    def check_entry_then_login(self, logged_in_page):
        global result_username_str, result_password_str

        user_database = sqlite3.connect("user_database.db")
        cursor = user_database.cursor()

        username = self.username_entry.get()
        cursor.execute("SELECT username FROM users WHERE username = ?", [username])
        result_username = cursor.fetchone()
        if result_username is None:
            self.wrong_label.grid(column=1, row=6,
                                  columnspan=2)
        else:
            result_username_str = ''.join(result_username)

        password = self.password_entry.get()
        cursor.execute("SELECT password FROM users WHERE password = ?", [password])
        result_password = cursor.fetchone()
        if result_password is None:
            self.wrong_label.grid(column=1, row=6,
                                  columnspan=2)
        else:
            result_password_str = ''.join(result_password)

        user_database.close()

        if username == result_username_str:
            if password == result_password_str:
                self.app_frame.pack_forget()
                logged_in_page.display_frame()

    def goto_register_page(self, register_page):
        self.app_frame.pack_forget()
        register_page.display_frame()


##################################################################################
class RegisterFrame:

    def __init__(self, page_color, *args, **kwargs):
        self.app_frame = Frame(root,
                               bg=page_color)

        # title label "quiz generator"
        self.title_label = Label(self.app_frame,
                                 text="Register",
                                 font=("Calibri", 40),
                                 fg=page_color, bg="white")  # fg = dark turquoise

        self.title_label.grid(column=1, row=0,
                              columnspan=2,
                              ipady=15, ipadx=150,
                              pady=15, padx=15)

        ########### Full name row
        self.fullname = Label(self.app_frame,
                              text="Full Name",
                              font=("Calibri", 24, "bold"),
                              bg=page_color, fg="white")
        self.fullname_entry = Entry(self.app_frame,
                                    font=("Calibri", 24, "bold"),
                                    fg=page_color)

        self.fullname.grid(column=1, row=2,
                           pady=10, padx=5)
        self.fullname_entry.grid(column=2, row=2,
                                 pady=10, ipadx=10)

        ########### Username row
        self.username = Label(self.app_frame,
                              text="Username",
                              font=("Calibri", 24, "bold"),
                              bg=page_color, fg="white")
        self.username_entry = Entry(self.app_frame,
                                    font=("Calibri", 24, "bold"),
                                    fg=page_color)

        self.username.grid(column=1, row=3,
                           pady=10, padx=5)
        self.username_entry.grid(column=2, row=3,
                                 pady=10, ipadx=10)

        ############ password row
        self.password = Label(self.app_frame,
                              text="Password",
                              font=("Calibri", 24, "bold"),
                              bg=page_color, fg="white")
        self.password_entry = Entry(self.app_frame,
                                    font=("Calibri", 24, "bold"),
                                    bg="white", fg=page_color,
                                    text="Enter Your Password", )

        self.password.grid(column=1, row=4,
                           pady=10, padx=5)
        self.password_entry.grid(column=2, row=4,
                                 pady=10, ipadx=10)

        ########### username is taken row
        self.user_taken_label = Label(self.app_frame,
                                      text="Username has been taken",
                                      font=("Calibri", 16, "bold"),
                                      bg=page_color, fg="red")

        ########### user too short
        self.user_short_label = Label(self.app_frame,
                                      text="Please enter a username or password with more than 6 characters",
                                      font=("Calibri", 16, "bold"),
                                      bg=page_color, fg="red")

        ################ register and go back row
        self.register_btn = Button(self.app_frame,
                                   text="Register",
                                   font=("Calibri", 24, "bold"),
                                   bg="white", fg=page_color,
                                   borderwidth=0,
                                   command=lambda: self.register_account())
        self.register_btn.grid(column=1, row=9,
                               columnspan=2,
                               pady=40, )

        self.register_page_back_btn = Button(self.app_frame,
                                             text="Go Back",
                                             font=("Calibri", 24, "bold"),
                                             bg="white", fg=page_color,
                                             borderwidth=0,
                                             command=lambda: self.backto_login_frame())
        self.register_page_back_btn.grid(column=0, row=9,
                                         columnspan=2,
                                         pady=30, )

        ######### well done!
        self.well_done = Label(self.app_frame,
                               text="User created, you can go back",
                               font=("Calibri", 16, "bold"),
                               bg=page_color, fg="green")

        self.quit_btn = Button(self.app_frame,
                               text="Quit",
                               bg="white", fg=page_color,
                               borderwidth=0,
                               command=lambda: quit())
        self.quit_btn.grid(row=100, column=1,
                           columnspan=2,
                           ipady=10, ipadx=10,
                           pady=5, padx=50,
                           )

        ########## empty columns
        self.app_frame.grid_columnconfigure(0, weight=1)
        self.app_frame.grid_columnconfigure(10, weight=1)

        self.app_frame.grid_rowconfigure(1, weight=1)
        self.app_frame.grid_rowconfigure(10, weight=2)

    def display_frame(self):
        self.app_frame.pack(fill='both', expand=1)

    def backto_login_frame(self):
        self.app_frame.pack_forget()
        login_frame.display_frame()

    def register_account(self):
        global new_username_str, new_password_str
        user_database = sqlite3.connect("user_database.db")
        cursor = user_database.cursor()

        fullname = self.fullname_entry.get()
        fullname_str = ''.join(fullname)

        username = self.username_entry.get()
        cursor.execute("SELECT username FROM users WHERE username = ?", [username])
        result_username = cursor.fetchone()

        if len(username) < 6:
            self.user_short_label.grid(column=1, row=6,
                                       columnspan=2)

        elif result_username is None:
            new_username_str = ''.join(username)

        else:
            self.user_taken_label.grid(column=1, row=5,
                                       columnspan=2)
        #####################
        password = self.password_entry.get()

        if len(password) < 6:
            self.user_short_label.grid(column=1, row=6,
                                       columnspan=2)
        else:
            new_password_str = ''.join(password)

        cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (fullname_str, new_username_str, new_password_str))

        self.user_taken_label.destroy()
        self.user_short_label.destroy()

        self.well_done.grid(column=1, row=6,
                            columnspan=2)

        user_database.commit()
        user_database.close()


##################################################################################
class LoggedInFrame:

    def __init__(self, page_color, *args, **kwargs):
        self.app_frame = Frame(root,
                               bg=page_color)

        # title label "quiz generator"
        self.title_label = Label(self.app_frame,
                                 text="Welcome",
                                 font=("Calibri", 40),
                                 fg=page_color, bg="white")  # fg = dark turquoise

        self.title_label.grid(column=1, row=0,
                              columnspan=2,
                              ipady=15, ipadx=150,
                              pady=15, padx=15)

        ####### which module?
        self.which_topic = Label(self.app_frame,
                                 text="Type the topic of the quiz to START QUIZ or CHECK SCORE. e.g. 'Maths', 'History', 'Science'",
                                 font=("Calibri", 16, "bold"),
                                 bg=page_color, fg="white",
                                 wraplength=1000)
        self.which_topic.grid(column=1, row=2,
                              columnspan=2,
                              pady=20)

        ####### topic entry
        self.topic_entry = Entry(self.app_frame,
                                 font=("Calibri", 16, "bold"),
                                 bg="white", fg=page_color, )
        self.topic_entry.grid(column=1, row=3,
                              columnspan=2,
                              ipady=5, ipadx=10,
                              pady=10)

        ####### start button
        self.start_quiz_btn = Button(self.app_frame,
                                     text="Start Quiz",
                                     font=("Calibri", 16, "bold"),
                                     bg="white", fg=page_color,
                                     borderwidth=0,
                                     command=lambda: self.start_quiz())

        self.start_quiz_btn.grid(column=1, row=4,
                                 columnspan=2)

        self.show_scores_btn = Button(self.app_frame,
                                      text="Check Scores",
                                      font=("Calibri", 16, "bold"),
                                      bg="white", fg=page_color,
                                      borderwidth=0,
                                      command=lambda: self.show_scores())

        self.show_scores_btn.grid(column=1, row=5,
                                  columnspan=2,
                                  pady=10)

        self.quit_btn = Button(self.app_frame,
                               text="Quit",
                               bg="white", fg=page_color,
                               borderwidth=0,
                               command=lambda: quit())
        self.quit_btn.grid(row=100, column=1,
                           columnspan=2,
                           ipady=10, ipadx=10,
                           pady=5, padx=50,
                           )

        ########## empty columns
        self.app_frame.grid_rowconfigure(1, weight=1)
        self.app_frame.grid_rowconfigure(6, weight=1)

        self.app_frame.grid_rowconfigure(15, weight=4)

        self.app_frame.grid_columnconfigure(0, weight=1)
        self.app_frame.grid_columnconfigure(10, weight=1)

    def display_frame(self):
        self.app_frame.pack(fill='both', expand=1)

    def start_quiz(self):
        global which_topic
        global ca, wa1, wa2, wa3
        global randq
        global correct_counter
        global question_counter

        question_bank = sqlite3.connect("question_bank.db")
        x = question_bank.cursor()

        which_topic = self.topic_entry.get()
        randq = randint(1, 50)

        x.execute("SELECT Question from {} WHERE QuestionID={}".format(which_topic, randq))
        question = x.fetchone()

        while question is None:
            randq = randint(1, 50)

            x.execute("SELECT Question from {} WHERE QuestionID={}".format(which_topic, randq))
            question = x.fetchone()

        question = "".join(question)

        x.execute("SELECT Type from {} WHERE QuestionID={}".format(which_topic, randq))
        qtype = x.fetchone()[0]
        print(qtype)

        ################### get the answers
        if qtype == "MC":
            x.execute("SELECT Ca from {} WHERE QuestionID={}".format(which_topic, randq))
            ca = x.fetchone()[0]
            x.execute("SELECT Wa1 from {} WHERE QuestionID={}".format(which_topic, randq))
            wa1 = x.fetchone()[0]
            x.execute("SELECT Wa2 from {} WHERE QuestionID={}".format(which_topic, randq))
            wa2 = x.fetchone()[0]
            x.execute("SELECT Wa3 from {} WHERE QuestionID={}".format(which_topic, randq))
            wa3 = x.fetchone()[0]

        correct_counter = 0
        question_counter = 1

        quizFrameMC("#4C7F99", question, qtype).display_frame()
        self.app_frame.pack_forget()

        question_bank.close()

    def show_scores(self):
        global result_username_str
        global which_topic

        connection = sqlite3.connect("user_database.db")
        x = connection.cursor()

        which_topic = self.topic_entry.get()

        x.execute("SELECT Score from Test_scores WHERE User = '{}' AND Module = '{}'".format(result_username_str,
                                                                                             which_topic))
        score_list = [item[0] for item in x.fetchall()]

        x.execute("SELECT COUNT(*) FROM Test_scores WHERE User = '{}' AND Module = '{}'".format(result_username_str,
                                                                                                which_topic))
        total_attempts = x.fetchone()[0]

        ########### total attempt
        attempts_label = Label(self.app_frame,
                               text=("Total attempts: " + str(total_attempts)),
                               font=("Calibri", 16, "bold"),
                               bg="#4C7F99", fg="white")
        attempts_label.grid(column=1, row=7,
                            columnspan=2,
                            pady=2)

        ########### average score
        score_sum = 0
        for i in score_list:
            score_sum += i

        average_score = score_sum / total_attempts

        average_label = Label(self.app_frame,
                              text=("Average: " + str(round(average_score, 1))),
                              font=("Calibri", 16, "bold"),
                              bg="#4C7F99", fg="white")
        average_label.grid(column=1, row=8,
                           columnspan=2,
                           pady=2)

        ######### highest and lowest score
        highest = 0
        lowest = 5
        for i in score_list:
            if i > highest:
                highest = i

        for i in score_list:
            if i < lowest:
                lowest = i

        highest_label = Label(self.app_frame,
                              text=("Highest: " + str(highest)),
                              font=("Calibri", 16, "bold"),
                              bg="#4C7F99", fg="white")
        highest_label.grid(column=1, row=9,
                           columnspan=2,
                           pady=2)

        lowest_label = Label(self.app_frame,
                             text=("Lowest: " + str(lowest)),
                             font=("Calibri", 16, "bold"),
                             bg="#4C7F99", fg="white")
        lowest_label.grid(column=1, row=10,
                          columnspan=2,
                          pady=2)


####################################################################################
class quizFrameMC:
    def __init__(self, page_color, question, q_type, *args, **kwargs):
        self.app_frame = Frame(root,
                               bg=page_color)
        ########## show the question
        self.question_label = Label(self.app_frame,
                                    text=question,
                                    wraplength=1500,
                                    font=("Calibri", 24, "bold"),
                                    bg=page_color, fg="white")
        self.question_label.grid(column=1, row=1,
                                 columnspan=2,
                                 pady=15, padx=15)

        ########## MULTIPLE CHOICE ###########
        ### randomise the answers
        ans1_grid = 0
        ans2_grid = 0
        ans3_grid = 0
        ans4_grid = 0

        while ans1_grid == ans2_grid or ans1_grid == ans3_grid or ans1_grid == ans4_grid or ans2_grid == ans3_grid or ans2_grid == ans4_grid or ans3_grid == ans4_grid:
            ans1_grid = randint(2, 5)
            ans2_grid = randint(2, 5)
            ans3_grid = randint(2, 5)
            ans4_grid = randint(2, 5)

        ### get the answers
        # question_bank = sqlite3.connect("question_bank.db")
        # x = question_bank.cursor()
        #
        # x.execute("from")

        ##### answer labels MC QUESTIONS
        if q_type == "MC":
            self.ca_label = Label(self.app_frame,
                                  text=ca,
                                  font=("Calibri", 16, "bold"),
                                  bg=page_color, fg="white")
            self.wa1_label = Label(self.app_frame,
                                   text=wa1,
                                   font=("Calibri", 16, "bold"),
                                   bg=page_color, fg="white")
            self.wa2_label = Label(self.app_frame,
                                   text=wa2,
                                   font=("Calibri", 16, "bold"),
                                   bg=page_color, fg="white")
            self.wa3_label = Label(self.app_frame,
                                   text=wa3,
                                   font=("Calibri", 16, "bold"),
                                   bg=page_color, fg="white")

            self.ca_label.grid(column=1, row=ans1_grid,
                               columnspan=2,
                               pady=10)
            self.wa1_label.grid(column=1, row=ans2_grid,
                                columnspan=2,
                                pady=10)
            self.wa2_label.grid(column=1, row=ans3_grid,
                                columnspan=2,
                                pady=10)
            self.wa3_label.grid(column=1, row=ans4_grid,
                                columnspan=2,
                                pady=10)

        ######## answer entry
        self.answer_entry = Entry(self.app_frame,
                                  font=("Calibri", 16, "bold"),
                                  bg="white", fg=page_color)
        self.answer_entry.grid(column=1, row=6,
                               columnspan=2,
                               ipady=5, ipadx=10,
                               pady=10)

        ########## CORRECT!!!
        self.correct_label = Label(self.app_frame,
                                   text="Well done, you got it correct!",
                                   font=("Calibri", 16, "bold"),
                                   bg=page_color, fg="green")

        self.wrong_label = Label(self.app_frame,
                                 text="Sorry, your answer is wrong.",
                                 font=("Calibri", 16, "bold"),
                                 bg=page_color, fg="red")

        ####### check answer
        self.check_answer_btn = Button(self.app_frame,
                                       text="Check Answer",
                                       font=("Calibri", 16, "bold"),
                                       bg="white", fg=page_color,
                                       borderwidth=0,
                                       command=lambda: self.check_answer(page_color))
        self.check_answer_btn.grid(column=1, row=7,
                                   columnspan=2,
                                   ipadx=20, ipady=5,
                                   padx=10, pady=10)

        ######## next q button
        self.nextq_btn = Button(self.app_frame,
                                text="Next ->",
                                font=("Calibri", 16, "bold"),
                                bg="white", fg=page_color,
                                borderwidth=0,
                                command=lambda: self.next_question())

        self.nextq_btn.grid(column=1, row=16,
                            columnspan=2,
                            ipadx=20, ipady=5,
                            padx=10, pady=10)

        self.quit_btn = Button(self.app_frame,
                               text="Quit",
                               bg="white", fg=page_color,
                               borderwidth=0,
                               command=lambda: quit())
        self.quit_btn.grid(row=100, column=1,
                           columnspan=2,
                           ipady=10, ipadx=10,
                           pady=5, padx=50,
                           )

        self.app_frame.grid_columnconfigure(0, weight=1)
        self.app_frame.grid_columnconfigure(10, weight=1)

        self.app_frame.grid_rowconfigure(15, weight=2)
        self.app_frame.grid_rowconfigure(17, weight=1)

    def display_frame(self):
        self.app_frame.pack(fill='both', expand=1)

    def check_answer(self, page_color):
        global which_topic
        global randq
        global correct_counter

        question_bank = sqlite3.connect("question_bank.db")
        x = question_bank.cursor()

        x.execute("SELECT ca from {} WHERE QuestionID={}".format(which_topic, randq))
        correct_answer = x.fetchone()[0]
        correct_answer = correct_answer.capitalize()
        answer_entered = self.answer_entry.get().capitalize()

        x.execute("SELECT Review from {} WHERE QuestionID={}".format(which_topic, randq))
        feedback = x.fetchone()[0]

        if answer_entered == correct_answer:
            self.wrong_label.grid_forget()
            self.check_answer_btn.grid_forget()
            self.correct_label.grid(column=1, row=8,
                                    columnspan=2,
                                    pady=10)

            correct_counter += 1

        else:
            self.correct_label.grid_forget()
            self.check_answer_btn.grid_forget()
            self.wrong_label.grid(column=1, row=8,
                                  columnspan=2,
                                  pady=10)

            feedback_title_label = Label(self.app_frame,
                                         text="Feedback:",
                                         font=("Calibri", 16, "bold"),
                                         bg=page_color, fg="white")
            feedback_title_label.grid(column=1, row=9,
                                      columnspan=2,
                                      pady=0)

            feedback_label = Label(self.app_frame,
                                   text=feedback,
                                   font=("Calibri", 16, "bold"),
                                   bg=page_color, fg="white")
            feedback_label.grid(column=1, row=10,
                                columnspan=2,
                                pady=0)

    def next_question(self):
        global which_topic
        global ca, wa1, wa2, wa3
        global randq
        global question_counter
        global correct_counter

        question_bank = sqlite3.connect("question_bank.db")
        x = question_bank.cursor()

        if question_counter != 5:
            self.check_answer_btn.grid(column=1, row=7,
                                       columnspan=2,
                                       ipadx=20, ipady=5,
                                       padx=10, pady=10)
            randq = randint(1, 50)

            x.execute("SELECT Question from {} WHERE QuestionID={}".format(which_topic, randq))
            question = x.fetchone()

            while question is None:
                randq = randint(1, 50)

                x.execute("SELECT Question from {} WHERE QuestionID={}".format(which_topic, randq))
                question = x.fetchone()

            question = "".join(question)

            x.execute("SELECT Type from {} WHERE QuestionID={}".format(which_topic, randq))
            qtype = x.fetchone()[0]
            print(qtype)

            ################### get the answers
            if qtype == "MC":
                x.execute("SELECT Ca from {} WHERE QuestionID={}".format(which_topic, randq))
                ca = x.fetchone()[0]
                x.execute("SELECT Wa1 from {} WHERE QuestionID={}".format(which_topic, randq))
                wa1 = x.fetchone()[0]
                x.execute("SELECT Wa2 from {} WHERE QuestionID={}".format(which_topic, randq))
                wa2 = x.fetchone()[0]
                x.execute("SELECT Wa3 from {} WHERE QuestionID={}".format(which_topic, randq))
                wa3 = x.fetchone()[0]

            question_counter += 1

            quizFrameMC("#4C7F99", question, qtype).display_frame()
            self.app_frame.pack_forget()

        else:
            self.app_frame.pack_forget()

            finalScorePage = testScore("#4C7F99", correct_counter, question_counter)
            finalScorePage.display_frame()

        question_bank.close()


class testScore:
    def __init__(self, page_color, correct_score, total_score, *args, **kwargs):
        self.app_frame = Frame(root,
                               bg=page_color)
        ########## show the question
        self.question_label = Label(self.app_frame,
                                    text="You have scored:",
                                    wraplength=1500,
                                    font=("Calibri", 32, "bold"),
                                    bg=page_color, fg="white")
        self.question_label.grid(column=1, row=1,
                                 columnspan=3,
                                 pady=50, padx=15)

        ########## test score row
        self.test_score_label = Label(self.app_frame,
                                      text=correct_score,
                                      wraplength=1500,
                                      font=("Calibri", 24, "bold"),
                                      bg=page_color, fg="white")
        self.test_score_label.grid(column=1, row=2,
                                   pady=15, padx=15)

        self.slash_label = Label(self.app_frame,
                                 text="/",
                                 wraplength=1500,
                                 font=("Calibri", 24, "bold"),
                                 bg=page_color, fg="white")
        self.slash_label.grid(column=2, row=2,
                              pady=15, padx=15)

        self.test_total_label = Label(self.app_frame,
                                      text=total_score,
                                      wraplength=1500,
                                      font=("Calibri", 24, "bold"),
                                      bg=page_color, fg="white")
        self.test_total_label.grid(column=3, row=2,
                                   pady=15, padx=15)

        ###### finish & save
        self.finish_btn = Button(self.app_frame,
                                 text="Finish & Save",
                                 font=("Calibri", 16, "bold"),
                                 bg="white", fg=page_color,
                                 borderwidth=0,
                                 command=lambda: self.finish_save(correct_score))
        self.finish_btn.grid(column=1, row=4, columnspan=3,
                             pady=15, padx=15,
                             ipady=5, ipadx=5)

        self.quit_btn = Button(self.app_frame,
                               text="Quit",
                               bg="white", fg=page_color,
                               borderwidth=0,
                               command=lambda: quit())
        self.quit_btn.grid(row=100, column=1,
                           columnspan=3,
                           ipady=10, ipadx=10,
                           pady=5, padx=50,
                           )

        self.app_frame.grid_columnconfigure(0, weight=1)
        self.app_frame.grid_columnconfigure(10, weight=1)

    def display_frame(self):
        self.app_frame.pack(fill='both', expand=1)

    def finish_save(self, score):
        global result_username_str
        global which_topic

        connection = sqlite3.connect("user_database.db")
        x = connection.cursor()

        x.execute("INSERT INTO Test_scores VALUES (?,?,?)", (result_username_str, which_topic, score))

        connection.commit()
        connection.close()

        self.app_frame.pack_forget()
        logged_in_frame.display_frame()


if __name__ == "__main__":
    root = Tk()
    root.title("Quiz Generator System")

    logged_in_frame = LoggedInFrame("#4C7F99")
    register_frame = RegisterFrame("#4C7F99")
    login_frame = LoginFrame("#4C7F99", logged_in_frame, register_frame)
    home_frame = HomeFrame("#4C7F99", login_frame)

    home_frame.display_frame()

    root.state("zoomed")
    root.mainloop()

    # user_database = sqlite3.connect("user_database.db")
    # cursor = user_database.cursor()

# cursor.execute("CREATE TABLE users (Full_Name TEXT, Username TEXT, Password TEXT)")

# cursor.execute("INSERT INTO users VALUES ('Soran Aziz', 'Soran03', 'password')")
# cursor.execute("INSERT INTO users VALUES ('Abdulazim Ahmed', 'Abdul03', 'password')")

# rows = cursor.execute("SELECT Full_name FROM users").fetchall()
# print(rows)


# user_database.commit()


######################### users table in user_database

#   Full_name           Username            Password

#   Soran Aziz          Soran03             password
#   Abdulazim Ahmed     Abdul03             password
#
