from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
from PIL import Image,ImageTk
#import CenterScreen

w=Tk()
width=430
height=250
sw=w.winfo_screenwidth()
sh=w.winfo_screenheight()
x=(sw/2)-(width/2)
y=(sh/2)-(height/2)
w.geometry("%dx%d+%d+%d"%(width,height,x,y))
w.config(background="lightblue")

lb1=Label(w,text="ATTENDANCE MANAGER",fg='white',font=('Arial',20),bg='lightblue')
lb1.pack(pady=70)

s=ttk.Style()
s.theme_use('clam')
s.configure("red.horizontal.TpProgressbar",fg='red',bg='lightblue',border=0)
progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate')
progress.pack(side='bottom')

w.overrideredirect(1)

def log():
	u=e.get()
	p=e1.get()

	if (u=='admin') and (p=='12345'):
		new()
	
	
	
def toggle():
	lf=LabelFrame(win,width="6cm",bg="lightblue")
	lf.pack(side=LEFT,fill=Y)

	def exp():
		lf.destroy()
	b=Button(lf,text="close",command=exp,bg='light blue').pack(side=TOP)
	b2=Button(lf,text='DashBoard',bg="lightblue",bd=0).pack(fill=X)
	b3=Button(lf,text='Attendance',bg="lightblue",bd=0).pack(fill=X)
			

def new():
	m_s.destroy()
	global win
	win=Tk()
	win.title("Attendance Dashboard")
	w1=500
	h1=500
	sw2 = win.winfo_screenwidth()
	sh2 = win.winfo_screenheight()
	x1 = (sw2	 / 2) - (w1 / 2)
	y1 = (sh2 / 2) - (h1 / 2)
	win.geometry("%dx%d+%d+%d"%(w1,h1,x1,y1))
	l=Button(win,text="open",command=toggle).place(x=0,y=0)
	
	win.mainloop()

def main_screen():
	global m_s
	m_s=Tk()
	m_s.title("Main Screen")
	width1=1280
	height1=418
	sw1=m_s.winfo_screenwidth()
	sh1=m_s.winfo_screenheight()
	x1=(sw1/2)-(width1/2)
	y1=(sh1/2)-(height1/2)
	m_s.geometry("%dx%d+%d+%d"%(width1,height1,x1,y1))
	bg=ImageTk.PhotoImage(file="R1.png")
	#m_s.overrideredirect(1)
	lb=Label(m_s,image=bg)
	lb.place(x=0,y=0,relwidth=1,relheight=1)
	hello(m_s)
	
	
def hello(m_s):
	f=LabelFrame(m_s,width="10cm",height="12cm",pady=20,bg="#1a435f",bd=0)
	f.place(x=850,y=50)	
	pic=ImageTk.PhotoImage(file="1.png")
	l3=Label(f,image=pic,bg="#1a435f")
	l3.grid(row=0,column=2)
	
	###...Label Creation...

	l=Label(f,text="Username",font=('Arial',16),bg="#1a435f")
	l.grid(row=1,column=1)
	#l.place(x=20,y=50)
	l1=Label(f,text="Password",font=('Arial',16),bg="#1a435f")
	l1.grid(row=3,column=1) 
	
	###...Empty Labels...
		
	le1=Label(f,text=" ",width=2,bg="#1a435f")
	le1.grid(row=1,column=0)

	le2=Label(f,text=" ",width=2,bg="#1a435f")
	le2.grid(row=2,column=1)

	le3=Label(f,text=" ",width=2,bg="#1a435f")
	le3.grid(row=4,column=1)
	
	le4=Label(f,text=" ",width=2,bg="#1a435f")
	le4.grid(row=0,column=0)

	le5=Label(f,text=" ",width=2,bg="#1a435f")
	le5.grid(row=2,column=5)

	###...Entry Text Box...
	global e, e1
	e=IntVar()
	e1=IntVar()
	e=Entry(f)
	e.grid(row=1,column=3)
	
	e1=Entry(f)
	e1.grid(row=3,column=3)
	
	###...Button...

	b=Button(f,text="Login",width=10,height=1,border=0,fg='#249794',bg="#c8e2f1",command=log,activebackground="lightblue")
	b.grid(row=5,column=2)
	#b.place(x=750,y=200)
	
	m_s.mainloop()

def bar():
	l2=Label(w,text='Loading.....',fg='white',bg='lightblue',font=('calibri (Body)',18))
	l2.place(x=155,y=150)

	import time
	r=0
	for i in range(100):
		progress['value']=r
		w.update_idletasks()
		time.sleep(0.01)
		r=r+1
	w.destroy()
	main_screen()


b1=Button(w,width=18,height=1,text='Get Started',command=bar,border=0,fg='#249794')
b1.place(x=155,y=200)


w.mainloop()


