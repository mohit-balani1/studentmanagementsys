from tkinter import *
import time
import random
from tkinter import ttk,messagebox
import pymysql

root = Tk()
root.title("Student Management System")
root.geometry('1250x700+150+50')
root.resizable(False,False)
s = ttk.Style()

s.configure('Wild.TButton', background='black', foreground='#32a88b', highlightthickness='20',
            font=('Helvetica', 18, 'bold', 'italic'),anchor='w')
s.configure('id.TButton', background='red', foreground='#32a88b', highlightthickness='10',
            font=('Times', 10, 'bold', 'italic'))
################# database operations ################
global cursor,con
con = pymysql.connect(host = "localhost",user ="root",password="mohit123",db='sms')

# prepare a cursor object using cursor() method
cursor = con.cursor()



#
# def insert():
#     con = pymysql.connect(host="localhost", user="root", password="mohit123", db='sms')
#
#     # prepare a cursor object using cursor() method
#     cursor = con.cursor()
#     query = "insert into sms values('%d','%s','%s','%s','%s','%s','%s')"
#     params =(name,'abc','def','ghi','jkl','mno','pqr')
#     cursor.execute(query % params)
#     con.commit()
#     con.close()
#
















########### submit button function ###########
def submit():
    pass

########### time function #############
def times():
    time_string = time.strftime("%H:%M:%S")
    weather.config(text=time_string)
    weather.after(200,times)

############ quote changer ##############
def qouteschanger():
    quote_list = ["It always seems impossible until it’s done",
                  "There is no substitute for hard work",
                  ". A book is like a garden that can be carried in your pocket ",
                  "Change your thoughts and you will change your world"]

    texts = random.choice(quote_list)
    quotes.config(text = texts , anchor = "center");
##################### FORM ####################
def loadform():
    check = Toplevel(master=data_frame)
    check.title("data entry")
    check.geometry("450x500+200+150")
    check.resizable(False, False)
    check.grab_set()

    rno = Label(check,text = " Enter Roll No :", font=('Times',20,'bold'),relief = GROOVE,anchor = "w")
    rno.place(x=10,y=20)
    name = Label(check, text=" Enter Name :", font=('Times', 20, 'bold'), anchor="w")
    name.place(x=10, y=80)


    mob= Label(check, text=" Enter Mobile :", font=('Times', 20, 'bold'), anchor="w")
    mob.place(x=10, y=140)
    email = Label(check, text=" Enter Email :", font=('Times', 20, 'bold'), anchor="w")
    email.place(x=10, y=200)
    address = Label(check, text=" Enter Address :", font=('Times', 20, 'bold'), anchor="w")
    address.place(x=10, y=260)
    gen= Label(check, text=" Enter Gender :", font=('Times', 20, 'bold'), anchor="w")
    gen.place(x=10, y=340)
    dob = Label(check, text=" Enter DOB :", font=('Times', 20, 'bold'), anchor="w")
    dob.place(x=10, y=400)

    ######### ENTRY WIDGET ##########
    rollvar = StringVar()



    rollEntry = Entry(check,font=('roman',15,'bold'),bd=5,textvariable=rollvar)
    rollEntry.place(x=220,y=20)
    print(rollEntry.get()+"ascacsacc")
    nameEntry = Entry(check, font=('roman', 15, 'bold'), bd=5)
    nameEntry.place(x=220, y=80)
    print(nameEntry.get())
    mobEntry = Entry(check, font=('roman', 15, 'bold'), bd=5)
    mobEntry.place(x=220, y=140)
    print(mobEntry.get())

    emailEntry = Entry(check, font=('roman', 15, 'bold'), bd=5)
    emailEntry.place(x=220, y=200)
    addressEntry = Text(check,width = 25,height = 3,borderwidth=3)
    addressEntry.place(x=220, y=260,height=60)
    combo_gender = ttk.Combobox(check,text="Gender",font=('roman', 15, 'bold'),state='readonly')
    combo_gender['values']=("male","female","other")
    combo_gender.place(x=220,y=340)
    dobsEntry = Entry(check, font=('roman', 15, 'bold'), bd=5)
    dobsEntry.place(x=220, y=400)
    ############## submit button ############
    submits = ttk.Button(check, text="Submit", style='Wild.TButton', width=15, command=submit)
    submits.place(x=110,y=450)



####################### data Entry functions ############

def add():
    loadform()

def delete():
    print("delete")
def update():
    up = Toplevel(master=data_frame)
    up.title("update entry")
    up.geometry("450x500+200+150")
    up.resizable(False, False)
    up.grab_set()
    loadform(up)
    up.mainloop()
def export():
    print("export")
def exit():
    res = messagebox.askyesnocancel('Notification','Do you Want to exit ?')
    if(res == True):
        root.destroy()

def search():
    print("search")
def show():
    print("show")

################ DATA FRAME ############
data_frame = Frame(root,bg= 'cyan',relief = GROOVE,borderwidth=4)
data_frame.place(x=10,y=180,width = 400,height = 500)


####################### buttons for data entry ########
add = ttk.Button(data_frame, text="1. Add Student", style='Wild.TButton',width=20,command = add)
add.pack(side=TOP,expand = True)

delete = ttk.Button(data_frame , text="2. Delete Student", style='Wild.TButton',width=20,command = delete)
delete.pack(side=TOP,expand = True)

update = ttk.Button(data_frame, text="3. Update Student", style='Wild.TButton',width=20,command = update)
update.pack(side=TOP,expand = True)

show = ttk.Button(data_frame, text="4. Show All", style='Wild.TButton',width=20,command = show)
show.pack(side=TOP,expand = True)

export = ttk.Button(data_frame, text="5. Graph", style='Wild.TButton',width=20, command = export)
export.pack(side=TOP,expand = True)

exit = ttk.Button(data_frame, text="6.  Exit", style='Wild.TButton',width=20,command = exit)
exit.pack(side=TOP,expand = True)





################ content FRAME ############
content_frame = Frame(root,bg= 'cyan',relief = GROOVE,borderwidth=4)
content_frame.place(x=415,y=180,width = 825,height = 500)
###########serach opt ###################
search_label = Label(root,text="Search By",bg='cyan',font=("times" ,15,'italic'))
search_label.place(x=450,y=190)

search_combo = ttk.Combobox(root,state = 'readonly')
search_combo['values'] = ("Roll No","Names","Contact")
search_combo.place(x=550,y=193)

searchEntry = Entry(root, font=('', 10, 'italic'), bd=2)
searchEntry.place(x=700, y=193)

search_btn= ttk.Button(root, text="Search",command = search)
search_btn.place(x=850,y=190)


########## table frame ###############
table_frame = Frame(root,bg= 'blue',relief = GROOVE,borderwidth=4)
table_frame.place(x=425,y=250,width = 805,height = 425)

scroll_x = Scrollbar(table_frame,orient=HORIZONTAL)
scroll_y = Scrollbar(table_frame,orient=VERTICAL)
student_table = ttk.Treeview(table_frame,columns=("roll","Name","Email","Gender","Contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_x.config(command=student_table.xview)
scroll_y.config(command=student_table.yview)
student_table.heading("roll",text="Roll No")
student_table.heading("Name",text="Name")
student_table.heading("Email",text="Email")
student_table.heading("Gender",text="Gender")
student_table.heading("Contact",text="Contact")
student_table.heading("DOB",text="DOB")
student_table.heading("Address",text="Address")
student_table['show']='headings'
student_table.pack(fill=BOTH,expand=1)



################ title ###################
t = " Student Management System "
Title = Label(root,text = t ,borderwidth=6,bg='cyan',font =('chiller',25))
Title.place(x=400,y=110)

############# quotes ###############

quotes = Label(root,text = "hi" ,borderwidth=6,bg='cyan',font =('chiller',25))
quotes.place(x=300,y=10)
qouteschanger()

############### weather ############

weather = Label(root,text = "hi" ,borderwidth=6,bg='cyan',font =('chiller',25),width=10)
weather.place(x=25,y=25)
times()

################### database ########





















root.mainloop()