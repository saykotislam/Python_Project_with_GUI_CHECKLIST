from tkinter import *
#from PIL import ImageTk,Image
import random
from tkinter import messagebox

root = Tk()


def login_dis():
    root.title("CHECKLIST")
    # adjust size
    root.geometry("315x335")


    def s_in():
         root.quit()
         solve()

#    root.iconbitmap("icon.png")
    #my_img=ImageTK.PhotoImage(Image.open("icon.png"))
    #label_title = Label(root, text="CHECK LIST", bg="white")
    #label_title.grid(row=4, column=1)

    Label(root,  border=0).place(x=0, y=0)

    # Button
    # Button(root, text='CHECKLIST', bg='black', relief=GROOVE, fg="white",
    #       width=20).place(x=60, y=100)
    Button(root, text='ENTER', command=lambda: s_in(), bg='black', relief=GROOVE,fg="white",
           width=20).place(x=60, y=200)


    # running main loop
    root.mainloop()





def solve():
    def update_tasks():
        clear_listbox()
        for task in tasks:
            lb_tasks.insert("end", task)
        numtask = len(tasks)
        label_dsp_count['text'] = numtask

    def clear_listbox():
        lb_tasks.delete(0, "end")

    def add_task():
        label_dsply["text"] = ""
        Ntask = text_input.get()
        if Ntask != "":
            tasks.append(Ntask)
            update_tasks()
        else:
            label_dsply["text"] = "Enter the text"
        text_input.delete(0, 'end')

    def delete_all():
        conf = messagebox.askquestion(
            'Delete All???', 'Are you sure to delete all task?')
        print(conf)
        if conf.upper() == "YES":
            global tasks
            tasks = []
            update_tasks()
        else:
            pass

    def delete_one():
        de = lb_tasks.get("active")
        if de in tasks:
            tasks.remove(de)
        update_tasks()

    def sort_asc():
        tasks.sort()
        update_tasks()

    def sort_dsc():
        tasks.sort(reverse=True)
        update_tasks()

    def random_task():
        randtask = random.choice(tasks)
        label_dsply["text"] = randtask

    def number_task():
        numtask = len(tasks)
        label_dsply["text"] = numtask

    def save_act():
        savecon = messagebox.askquestion(
            'Save Confirmation', 'Want to save your progress?')
        if savecon.upper() == "YES":
            with open("data.txt", "w") as filehandle:
                for listitem in tasks:
                    filehandle.write('%s\n' % listitem)
        else:
            pass

    def load_info():
        messagebox.showinfo(
            "info", "This is CHECKLIST \n created by Prapti, Nabil, Saykot, Nahid, Masum", )

    def load_act():
        loadcon = messagebox.askquestion(
            'Save Confirmation', 'save your progress?')
        if loadcon.upper() == "YES":
            tasks.clear()

            with open('data.txt', 'r') as filereader:
                for line in filereader:
                    currentask = line
                    tasks.append(currentask)
                update_tasks()

        else:
            pass

    def exit_app():
        confex = messagebox.askquestion(
            'Exit Confirmation', 'Are you sue you want to EXIT?')
        if confex.upper() == "YES":
            root.destroy()
        else:
            pass

    # background
    root.configure(bg="white")
    root.title("CHECKLIST")
    root.geometry("315x335")
    # database
    tasks = []

    # main root

    #label_title = Label(root, text="Work List", bg="white")
    #label_title.grid(row=0, column=0)

    label_dsply = Label(root, text="", bg="white")
    label_dsply.grid(row=0, column=1)

    label_dsp_count = Label(root, text="", bg="white")
    label_dsp_count.grid(row=0, column=3)

    text_input = Entry(root, width=15)
    text_input.grid(row=1, column=1)

    # button
    text_add_bttn = Button(
        root, text="Add Task", bg="gray", fg="white", width=15, command=add_task)
    text_add_bttn.grid(row=1, column=0)

    delone_bttn = Button(
        root, text="Done Task", bg="gray", fg="white", width=15, command=delete_one)
    delone_bttn.grid(row=2, column=0)

    delall_bttn = Button(
        root, text="Delete", bg="gray", fg="white", width=15, command=clear_listbox)
    delall_bttn.grid(row=3, column=0)

    sort_asc = Button(root, text="Sort ASC",
                              bg="gray", fg="white", width=15, command=sort_asc)
    sort_asc.grid(row=4, column=0)

    sort_dsc = Button(root, text="Sort DSC",
                              bg="gray", fg="white", width=15, command=sort_dsc)
    sort_dsc.grid(row=5, column=0)

    random_bttn = Button(
        root, text="Random Task", bg="gray", fg="white", width=15, command=random_task)
    random_bttn.grid(row=6, column=0)

    number_task = Button(
        root, text="Number of Task", bg="gray", fg="white", width=15, command=number_task)
    number_task.grid(row=7, column=0)

    save_button = Button(root, text="Save Tasks",
                       bg="gray", fg="white", width=15, command=save_act)
    save_button.grid(row=8, column=0)

    info_bttn = Button(
        root, text="INFO", bg="gray", fg="white", width=15, command=load_info)
    info_bttn.grid(row=10, column=1)

    # save_button = Button(
    #    root, text="Save Tasks", bg="gray", fg="white", width=15, command=save_act)
    #save_button.grid(row=10, column=1)

    load_button = Button(
        root, text="Load LastTask", bg="gray", fg="white", width=15, command=load_act)
    load_button.grid(row=10, column=0)

    #info_button = Button(
     #   root, text="INFO", bg="gray", fg="white", width=15, command=load_info)
    #info_button.grid(row=11, column=0, columnspan=2)

    exit_button = Button(
        root, text="EXIT", bg="gray", fg="white", width=15, command=exit_app)
    exit_button.grid(row=11, column=0, columnspan=2)

    lb_tasks = Listbox(root)
    lb_tasks.grid(row=2, column=1, rowspan=8)

    # main loop
    root.mainloop()


if __name__ == '__main__':
    login_dis()