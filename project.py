''' IMPORTING NECCESARY PACKAGES'''

from tkinter import *                        #tkinter is a GUI package for python
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image 
import webbrowser  
''' IMPORTING SUCCESSFUL'''

#Compilation of various phone models
#[a,b,c,d,e]
# a = Phone Name, b = price, c = size in inches, d = memory, e =type of keyboard, f=battery life
iPhone8 = [['iPhone 8 64GB', 729, 4.7, 64,'t', 14],['iPhone 8 128GB', 799, 4.7, 128,'t', 14]] #0,1,2,3,4,5
iPhone8Plus = [['iPhone 8 Plus 64GB', 899, 5.5, 64,'t', 21],['iPhone 8 Plus 128GB', 969, 5.5, 128,'t', 21]]
iPhone11Pro = [["iPhone 11 Pro 64GB",1649,5.8,64,'t', 16],["iPhone 11 Pro 256GB",1889,5.8,256,'t', 16],["iPhone 11 Pro 512GB",2199,5.8,512,'t', 16]]
iPhone11ProMax = [["iPhone 11 Pro Max 64GB",1799,6.5,64,'t', 21],["iPhone 11 Pro Max 256GB",2039,6.5,256,'t', 21],["iPhone 11 Pro Max 512GB",2349,6.5,512,'t', 21]]
Nokia = [["Nokia 800 Tough 4GB",172,2.4,4,'k', 12], ["Nokia 106 4MB",60.99,1.8,0.004,'k', 14], ["Nokia C1 16GB",68,5.45,16,'t',48]]
Samsung = [["Samsung Galaxy Fold 512GB Large 7.3",3088,7.3,512,'t', 24], ["Samsung Galaxy S20 Ultra 128GB", 1898,6.9,128,'t', 37]]
Xiaomi = [['Redmi Note 8 64GB', 195, 6.22,64,'t', 41],["Xiaomi Redmi Note 8 Pro 128GB",325,6.53,128,'t', 41],["Xiaomi Mi Note 10 Pro 256GB",740,6.47,256,'t', 50], ["Xiaomi Black Shark 3 Pro",911,6.67,256,'t',66]]
BlackBerry = [["BlackBerry Q10 16GB",200,3.1,16,'q', 13], ["Blackberry Key2 64GB",605,4.5,64,'q',86]]
Sony = [['Sony Xperia 1', 1299, 6.5, 512,'t', 79], ['Sony Xperia 5', 1099, 6.1, 128, 't', 96]]
Huawei = [["Huawei P40 Pro 8+ 5G",1448,6.58,256,'t',94], ["Huawei Y6s",155,6.09,64,'t',86], ["Huawei Y7p",245,6.39,64,'t',57]]
Oneplus = [["Oneplus 7T",750,6.55,128,'t',90]]
Google = [["Google Pixel 4 5.7",1119,5.7,64,'t',62], ["Google Pixel 4 5.7",1269,5.7,128,'t',62]]
vivo = [["vivo V17",358,6.44,128,'t',64], ["vivo Y12 64GB",169,6.35,64,'t',61]]
Oppo = [["Oppo A5s (AX5s)",199,6.2,64,'t',61], ["Oppo Reno 10x Zoom",1299,6.6,256,'t',107], ["Oppo F15",480,6.4,128,'t',66]]
Asus = [["Asus Zenfone 5 ZE620KL",437,5.7,64,'t',58], ["Zenfone Max Pro M1 ZB601KL/ZB602K",348,5.99,32,'t',51]]
Lenovo = [["Lenovo A7000 Plus",242,5.5,16,'t',56], ["Lenovo K10 Note",273,6.3,64,'t',61]]
HTC = [['Wildfire R70 32GB', 245, 6.53, 32, 't',  35], ['Desire 19s 32GB', 299, 6.2, 32, 't', 30], ['Exodus 1 64GB', 768, 5.7, 64, 't', 30], ['Wildfire X 32GB', 400, 6.2, 32, 't', 30], ['One X9 32GB', 520, 5.5, 32, 't', 25], ['Desire 19+ 64GB', 380, 6.2, 64, 't', 35], ['Desire 19+ 128GB', 480, 6.2, 128, 't', 35], ['Desire 12 16GB', 160, 5.5, 16, 't', 28], ['Desire 12 32GB', 220, 5.5, 32, 't', 28]]
LG = [['LG G6 32GB', 680, 5.7, 32, 't', 33], ['LG G6 64G', 938, 5.7, 64, 't', 33], ['LG G6 128GB', 1345, 5.7, 128, 't', 33], ['G8 ThinQ 128GB', 925, 6.1, 128, 't', 30], ['V50 ThinQ 128GB', 1100, 6.4, 128, 't', 40], ['V40 ThinQ 64GB', 800, 6.4, 64, 't', 28], ['V40 ThinQ 128GB', 1000, 6.4, 128, 't', 28], ['LG G7 ThinQ 64GB', 1000, 6.1, 64, 't', 34], ['LG G7 ThinQ 128GB', 1250, 6.1, 128, 't', 34], ['LG G8 ThinQ 128GB', 1300, 6.1, 128, 't', 38]]
PhoneBrands = [iPhone8,iPhone8Plus,iPhone11Pro,iPhone11ProMax,Nokia,Samsung,Xiaomi,BlackBerry,Sony,Huawei,Oneplus,Google,vivo,Oppo,Asus,Lenovo,HTC,LG]
memorysize = {1:64,2:64,3:128,4:256,5:512}
screensize = {1:5,2:6.5,3:6.5}
batterylife = {1:15,2:25,3:25}


first_filter = []
second_filter = []
third_filter = []
fourth_filter = []
fifth_filter = []
phone = []

# Combine all the Phones into 1 list
for x in range(0,len(PhoneBrands)):
    for y in range(0,len(PhoneBrands[x])):
        phone.append(PhoneBrands[x][y])

''' APP LAYOUT'''
root = Tk()                                                 #opening a GUI window
root.geometry('800x750+150+20')                             #shows where window lies in the screen and swindow size 
root.configure(bg='grey')                                   #background color for the window
root.title("HandPhone Recommendation System")               #title for the window
root.resizable(width=False, height=False)                   #'window cannot be resized
top_frame = Frame(root,height=60,width=895,bg='orange')     #frame for the welcome text
path = "allphones.jpg"                                      #background image path
img = ImageTk.PhotoImage(Image.open(path))                  #opening image
label = Label(top_frame,image = img ,height=70,width=1080)             #background image for the welcome frame
label.image=img
label.place(x=0,y=0)                                        #positioning the image in the window
top_frame.place(x=0,y=5)                                  #placing the frame 
tf_label = Label(top_frame,text='Welcome To The System',font=('arial', 33, 'bold'),fg='dark blue',bg='gray89',height=50)
tf_label.pack(anchor='center')
top_frame.pack_propagate(False)
#root.iconbitmap("icon.ico")      #photo yet to upload (this is for icon of the window)

#app frame
frame = LabelFrame(root,height=80,width=1080)               #lower frame  ( content frame )
frame.place(x=10, y=70)
frame.pack_propagate(False)
path = "background.jpg"
img = ImageTk.PhotoImage(Image.open(path))
label = Label(frame,image = img ,height=400,width=1280)         #background imgae for app frame
label.image=img
label.place(x=0,y=0)



"""All functions"""  
#to clear in budget field and refresh the window after searching for one time
def refresh():
    budget.delete(0, 'end')                             #clears the entry  widget data
    disable()                                           #disables lower frames of the window
    
#for clearing filter data for next data input
def clear():
    first_filter.clear()
    second_filter.clear()
    third_filter.clear()
    fourth_filter.clear()
    fifth_filter.clear()

#opens borwser to search for the phone
def callback(url):
    #print(url_path)
    webbrowser.open_new(url)
#produces the end results of filtering process
def recommend(filter_data, filter_count):
    if len(filter_data) == 0:
        messagebox.showinfo("Error", "There are no phones within your requirements")
        refresh()
        clear()
        #print("There are no phones within your requirements")
    elif filter_count == 5:
        top = Toplevel()
        top.title("Phone models")
        Label(top,text="These phones are most suitable for you",font=("Helvetica 19 bold"),fg='orange').grid(row=0,column=0)
        for i in range(0,len(filter_data)):
            Label(top,text=filter_data[i][0], font=("Helvetica 19 bold")).grid(row=i+1,column=0)
            link1 = Label(top, text="Click to search for this phone", fg="blue", cursor="hand2")
            link1.grid(row=i+1, column= 1)

            url_path= "https://www.amazon.com/s?k=" + filter_data[i][0] 
            #b1=ttk.Button(top, text='Click to buy this phone',command=callback ).grid(row=i+1, column=1)

            #link1.bind(url_path,"<Button-1>", lambda event , callback(event,url_path))
            link1.bind("<Button-1>", lambda e: callback)
            #print(filter_data[i][0])  #prints phone models in the terminal
            #print(url_path)
        clear()                                #clears all filter data for next input

#enabling frame children when pressing next button
def enable(childList):
    for child in childList:
        child.configure(state='active')

#Conduct a run of filtering to narrow down available phones based on user inputs(first filter append) and enable next frame
def pri():
    #print(type(str(budget_value.get())),type(budget_value.get()))
    try:
        if str(budget_value.get())  :   #check if there value is entered in entry widget
            enable(keyboard_frame.winfo_children())     #enables next frame
            for i in range(0,len(phone)):
                if phone[i][1] < budget_value.get():
                    first_filter.append(phone[i])
                else:
                    continue
    except:
        messagebox.showerror("Error", "Please enter value!")        #show warning for no data entered

#Conduct a run of filtering to narrow down available phones based on user inputs (second filter append) and enable next frame
def key_next():
    if not keyboard.get() :   #if no radiobutton is selected show warning
        messagebox.showwarning("Error", "Please select a keyboard interface!")
    else:
        enable(memory_frame.winfo_children())    #enables next  frame
        for i in range(0,len(first_filter)):
            if first_filter[i][4] == keyboard.get():
                second_filter.append(first_filter[i])
        #Check for recommendation if to continue or not
        recommend(second_filter,2) 


#Conduct a run of filtering to narrow down available phones based on user inputs (third filter append) and enable next frame   
def mem_next():
    if not memory.get() :                   # check :if no memory is selected, pop up a warning 
        messagebox.showwarning("Error", "Please select a memory requirement!")
    else:
        enable(size_frame.winfo_children())
        #Prompt user for new requirement(memory space) to further filter out phones for user
        try:
            if 0<int(memory.get())<6:
                for value in memorysize:
                    if int(memory.get()) == value:
                        memory_m = memorysize[value]          
        except:
            pass

        if int(memory.get()) == 1:
            for i in range(0,len(second_filter)):
                if second_filter[i][3] < memory_m:
                    third_filter.append(second_filter[i])
                else:
                    continue
        else:
            for i in range(0,len(second_filter)):
                if second_filter[i][3] >= memory_m: #includes bigger memory phones
                    third_filter.append(second_filter[i])
                else:
                    continue
        recommend(third_filter,3)
        
#Conduct a run of filtering to narrow down available phones based on user inputs (fourth filter append) and enable next frame
def size_next():
    if not size.get():      #is any size selected? check for it
        messagebox.showwarning("Error", "Please select required phone size!")
    else:  
        enable(battery_frame.winfo_children())
        try:
            if 0<int(size.get())<4:
                for value in screensize:
                    if int(size.get()) == value:
                        screen = screensize[value]          
        except:
            pass
    
        if int(size.get()) == 1:
            for i in range(0,len(third_filter)):
                if third_filter[i][2] <= screen:
                    fourth_filter.append(third_filter[i])
                else:
                    continue      
        elif int(size.get()) == 2:
            for i in range(0,len(third_filter)):
                if third_filter[i][2] < screen and third_filter[i][2] > 5:
                    fourth_filter.append(third_filter[i])
                else:
                    continue
        else:
            for i in range(0,len(third_filter)):
                if third_filter[i][2] >= screen:
                    fourth_filter.append(third_filter[i])
                else:
                    continue
        recommend(fourth_filter,4)

#for disabling the lower frames
def disable():
    for child in keyboard_frame.winfo_children():
        child.configure(state='disable')
    for child in memory_frame.winfo_children():
        child.configure(state='disable')
    for child in size_frame.winfo_children():
        child.configure(state='disable')
    for child in battery_frame.winfo_children():
        child.configure(state='disable')

#Conduct a run of filtering to narrow down available phones based on user inputs (fifth filter append) and search for the result models
def batt_next():
    if not battery.get():       # check if battery field is selected
        messagebox.showwarning("Error", "Please select all fields!")
    else:
        try:
            if 0<int(battery.get())<4:
                for value in batterylife:
                    if int(battery.get()) == value:
                        battery_m = batterylife[value]          
        except:
            pass

        if int(battery.get()) == 1:
            for i in range(0,len(fourth_filter)):
                if fourth_filter[i][5] <= battery_m:
                    fifth_filter.append(fourth_filter[i])
                else:
                    continue      
        elif int(battery.get()) == 2:
            for i in range(0,len(fourth_filter)):
                if fourth_filter[i][5] < battery_m and fourth_filter[i][5] > 5:
                    fifth_filter.append(fourth_filter[i])
                else:
                    continue
        else:
            for i in range(0,len(fourth_filter)):
                if fourth_filter[i][5] >= battery_m:
                    print("4")
                    fifth_filter.append(fourth_filter[i])
                else:
                    continue
        #print(fifth_filter)
        refresh()
        recommend(fifth_filter,5)


#budget frame and getting data to budget_value
budget_value= IntVar()
budget_frame = LabelFrame(frame)
budget_frame.grid(row=1, column = 0, sticky=W)
Label(budget_frame, text='Enter your max budget for the phone:    $', font=("Helvetica", 13), fg = 'black' ).grid(row=1, column=0, padx= 10, sticky=W)
budget = Entry(budget_frame,width = 25,fg='blue',textvariable=budget_value, font=("Helvetica", 15))
budget.delete(0, 'end') 
budget.insert(0,'Enter currency in Dollar')
budget.bind("<FocusIn>", lambda args: budget.delete('0', 'end'))
budget.grid(row=1, column=1, padx= 10,pady=10, ipady = 5,sticky =E)
ttk.Button(budget_frame, text='NEXT',command=pri).grid(row=1, column=2)

#keyboard interface frame and getting keyboard interface value to keyboard variable
keyboard_frame = LabelFrame(frame)
keyboard_frame.grid(row=2, column=0, padx=10, pady= 10, sticky=W)
Label(keyboard_frame, text="Please input the type of interface for phone  :",font=("Helvetica", 13), fg = 'black').grid(row=2, column=0, sticky=W)
keyboard= StringVar()
Radiobutton(keyboard_frame, text="QWERTY Keyboard", variable=keyboard, value='q',font=("Helvetica", 13), fg = 'red',indicatoron=5).grid(row= 2, column=1,sticky=W)
Radiobutton(keyboard_frame, text="Keypad Keyboard", variable=keyboard, value='k',font=("Helvetica", 13), fg = 'blue').grid(row= 3, column=1,sticky=W)
Radiobutton(keyboard_frame, text="Touchscreen", variable=keyboard, value='t',font=("Helvetica", 13), fg = 'orange').grid(row= 4, column=1,sticky=W)
ttk.Button(keyboard_frame, text='NEXT',command=key_next).grid(row=2, column=4)



#memory frame and getting memory size to memory variable
memory_frame = LabelFrame(frame)
memory_frame.grid(row=5, column=0, padx=10, pady= 10, sticky=W)
Label(memory_frame, text="Please input the minimum desired memory space(GB) of phone  :",font=("Helvetica", 13), fg = 'black').grid(row=5, column=0, sticky=W)
memory= IntVar()
Radiobutton(memory_frame, text=" <64 GB ", variable=memory, value=1,font=("Helvetica", 13), fg = 'green').grid(row= 5, column=1,sticky=W)
Radiobutton(memory_frame, text=" 64 GB ", variable=memory, value=2,font=("Helvetica", 13), fg = 'green').grid(row= 6, column=1,sticky=W)
Radiobutton(memory_frame, text=" 128 GB ", variable=memory, value=3,font=("Helvetica", 13), fg = 'green').grid(row= 7, column=1,sticky=W)
Radiobutton(memory_frame, text=" 256 GB ", variable=memory, value=4,font=("Helvetica", 13), fg = 'green').grid(row= 8, column=1,sticky=W)
Radiobutton(memory_frame, text=" 512 GB ", variable=memory, value=5,font=("Helvetica", 13), fg = 'green').grid(row= 9, column=1,sticky=W)
ttk.Button(memory_frame, text='NEXT',command=mem_next).grid(row=5, column=2)

#phone size frame and getting phone size to size variable
size_frame = LabelFrame(frame)
size_frame.grid(row=10, column=0, padx=10, pady= 10, sticky=W)
Label(size_frame, text="Please input the desired phone screen size :",font=("Helvetica", 13)).grid(row=10, column=0, sticky=W)
size= IntVar()
Radiobutton(size_frame, text="Small <5 inches", variable=size, value=1,font=("Helvetica", 13), fg = 'orange').grid(row= 10, column=1,sticky=W)
Radiobutton(size_frame, text="Medium <6.5 inches", variable=size, value=2,font=("Helvetica", 13), fg = 'orange').grid(row=11, column=1,sticky=W)
Radiobutton(size_frame, text="Large than or equals to 6.5 inches", variable=size, value=3,font=("Helvetica", 13), fg = 'orange').grid(row= 12, column=1,sticky=W)
ttk.Button(size_frame, text='NEXT',command=size_next).grid(row=10, column=2)

#battery life frame and getting battery life value to battery variable
battery_frame = LabelFrame(frame)
battery_frame.grid(row=13, column=0, padx=10, pady= 10, sticky=W)
Label(battery_frame, text="Please input the desired battery life (talktime) of phone :",font=("Helvetica", 13)).grid(row=13, column=0, sticky=W)
battery= IntVar()
Radiobutton(battery_frame, text="Short <5 hours", variable=battery, value=1,font=("Helvetica", 13), fg = 'blue').grid(row= 13, column=1,sticky=W)
Radiobutton(battery_frame, text="Medium <25 hours", variable=battery, value=2,font=("Helvetica", 13), fg = 'blue').grid(row= 14, column=1,sticky=W)
Radiobutton(battery_frame, text="Longer or equals to 25 hours", variable=battery, value=3,font=("Helvetica", 13), fg = 'blue').grid(row= 15, column=1,sticky=W)

#search buttons and styles
style = ttk.Style()
style.theme_use('alt')
style.configure('TButton', background = '#ADD8E6', foreground = 'black', width = 20, borderwidth=1, focusthickness=3, focuscolor='black')
style.map('TButton', background=[('active','#ADD8E6')]) 
Button(frame, text='SEARCH',command=batt_next,fg='black',bg='#ADD8E6',width = 20,font=("Helvetica", 13, 'bold')).grid(row=14, column=0,ipady = 4) 

disable()   # calling this function disables all frames except budget while loading the GUI for the first time
root.mainloop() #end GUI window