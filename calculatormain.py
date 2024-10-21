from tkinter import *
from tkinter import font
root = Tk()
root.title('Calculator')
root.configure(bg='black')

def addtext(a):
    if a == '.':
        if '.' in e1.get():
            pass
        else:
            e1.insert('end',a)
    else:
        e1.insert('end',a)

def cleartext():
    current_text=e1.get()
    e1.delete(len(current_text) - 1,'end')

def clearall():
    e1.delete(0,'end')

def setoperation(op):
    global first_num,operation
    first_num = float(e1.get())
    operation = op
    e1.delete(0,'end')
    if op == '^2':
        result=first_num**2
        e1.insert(0,str(result))
        result=0

def findtotal():
    result=0
    second_num = float(e1.get())
    e1.delete(0,'end')
    if operation == '+':
        result = first_num+second_num
    elif operation == '-':
        result = first_num-second_num
    elif operation == '*':
        result = first_num*second_num
    elif operation == '/':
        result = first_num/second_num
    elif operation == '%':
        result = first_num%second_num
    elif operation == '^':
        result = first_num**second_num
    e1.insert(0,str(result))

e1 = Entry(width=22,font=font.Font(size=20),fg='white',bg='grey',justify='right')
e1.grid(row=0,column=0,columnspan=4,padx=5,pady=5)

b1=Button(text='7',command=lambda:addtext(7),width=6,height=3,padx=5,pady=5,font=font.Font(size=12),fg='white',bg='grey')
b1.grid(row=1,column=0,padx=5,pady=5)
b2=Button(text='8',command=lambda:addtext(8),width=6,height=3,padx=5,pady=5,font=font.Font(size=12),fg='white',bg='grey')
b2.grid(row=1,column=1,padx=5,pady=5)
b3=Button(text='9',command=lambda:addtext(9),width=6,height=3,padx=5,pady=5,font=font.Font(size=12),fg='white',bg='grey')
b3.grid(row=1,column=2,padx=5,pady=5)
b4=Button(text='C',command=cleartext,width=6,height=3,padx=5,pady=5,font=font.Font(size=12),fg='white',bg='grey')
b4.grid(row=1,column=3,padx=5,pady=5)

b5=Button(text='4',command=lambda:addtext(4),width=6,height=3,padx=5,pady=5,font=font.Font(size=12),fg='white',bg='grey')
b5.grid(row=2,column=0,padx=5,pady=5)
b6=Button(text='5',command=lambda:addtext(5),width=6,height=3,padx=5,pady=5,font=font.Font(size=12),fg='white',bg='grey')
b6.grid(row=2,column=1,padx=5,pady=5)
b7=Button(text='6',command=lambda:addtext(6),width=6,height=3,padx=5,pady=5,font=font.Font(size=12),fg='white',bg='grey')
b7.grid(row=2,column=2,padx=5,pady=5)
b8=Button(text='/',command=lambda:setoperation('/'),width=6,height=3,padx=5,pady=5,font=font.Font(size=12),fg='white',bg='grey')
b8.grid(row=2,column=3,padx=5,pady=5)

b9=Button(text='1',command=lambda:addtext(1),width=6,height=3,padx=5,pady=5,font=font.Font(size=12),fg='white',bg='grey')
b9.grid(row=3,column=0,padx=5,pady=5)
b10=Button(text='2',command=lambda:addtext(2),width=6,height=3,padx=5,pady=5,font=font.Font(size=12),fg='white',bg='grey')
b10.grid(row=3,column=1,padx=5,pady=5)
b11=Button(text='3',command=lambda:addtext(3),width=6,height=3,padx=5,pady=5,font=font.Font(size=12),fg='white',bg='grey')
b11.grid(row=3,column=2,padx=5,pady=5)
b12=Button(text='X',command=lambda:setoperation('*'),width=6,height=3,padx=5,pady=5,font=font.Font(size=12),fg='white',bg='grey')
b12.grid(row=3,column=3,padx=5,pady=5)

b18=Button(text='%',command=lambda:setoperation('%'),width=6,height=3,padx=5,pady=5,font=font.Font(size=12),fg='white',bg='grey')
b18.grid(row=4,column=0,padx=5,pady=5)
b17=Button(text='0',command=lambda:addtext(0),width=6,height=3,padx=5,pady=5,font=font.Font(size=12),fg='white',bg='grey')
b17.grid(row=4,column=1,padx=5,pady=5)
b19=Button(text='+',command=lambda:setoperation('+'),width=6,height=3,padx=5,pady=5,font=font.Font(size=12),fg='white',bg='grey')
b19.grid(row=4,column=2,padx=5,pady=5)
b20=Button(text='=',command=findtotal,width=6,height=3,padx=5,pady=5,font=font.Font(size=12),fg='white',bg='grey')
b20.grid(row=4,column=3,padx=5,pady=5)

b21=Button(text='.',command=lambda:addtext('.'),width=6,height=3,padx=5,pady=5,font=font.Font(size=12),fg='white',bg='grey')
b21.grid(row=5,column=0,padx=5,pady=5)
b22=Button(text='CE',command=lambda:clearall(),width=6,height=3,padx=5,pady=5,font=font.Font(size=12),fg='white',bg='grey')
b22.grid(row=5,column=1,padx=5,pady=5)
b23=Button(text='^2',command=lambda:setoperation('^2'),width=6,height=3,padx=5,pady=5,font=font.Font(size=12),fg='white',bg='grey')
b23.grid(row=5,column=2,padx=5,pady=5)
b24=Button(text='POW',command=lambda:setoperation('^'),width=6,height=3,padx=5,pady=5,font=font.Font(size=12),fg='white',bg='grey')
b24.grid(row=5,column=3,padx=5,pady=5)


root.mainloop()

