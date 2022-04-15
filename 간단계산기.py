from tkinter import *

disValue = 0
operator = {'+':1, '-':2, '*':3, '/':4, '=':5, 'c':6}
stoValue = 0
preOper = 0

def num_click(value):
    global disValue
    disValue = (disValue*10) + value
    str_value.set(disValue)

def clear():
    global disValue, operator, stoValue, preOper
    disValue = 0
    stoValue = 0
    preOper = 0
    str_value.set(str(disValue))

def ope_click(value):
    global disValue, operator, stoValue, preOper
    op = operator[value]
    if op == 6:
        clear()
    elif disValue == 0:
        preOper = 0
    elif preOper == 0:
        preOper = op
        stoValue = disValue
        disValue = 0
        str_value.set(str(disValue))
    elif op == 5:
        if preOper == 1:
            disValue = stoValue + disValue
        if preOper == 2:
            disValue = stoValue - disValue
        if preOper == 3:
            disValue = stoValue * disValue
        if preOper == 4:
            disValue = stoValue / disValue
        
        str_value.set(str(disValue))
        disValue = 0
        stoValue = 0
        preOper = 0
    else:
        clear()

def btn_click(value):
    try:
        value = int(value)
        num_click(value)
    except:
        ope_click(value)


win = Tk()
win.title('간단 계산기')
win.geometry('400x600')
win.option_add('*Font','맑은고딕 13')

str_value = StringVar()
str_value.set(str(disValue))
dis = Entry(win, textvariable = str_value, justify = 'right')
dis.grid(column = 0, row = 0, columnspan = 4, ipadx = 110, ipady = 45)

cal = [ ['1','2','3','+'],
        ['4','5','6','-'],
        ['7','8','9','*'],
        ['c','0','=','/'] ]

for i, calcol in enumerate(cal):
    for j, caltext in enumerate(calcol):
        try :
            color = int(caltext)
            color = 'black'
        except :
            color = 'white'

        btn = Button(win)
        btn.config(width = 10, height = 5) 
        btn.config(text = caltext)
        btn.config(bg = color, fg = 'green')
        btn.config(command = lambda cmd = caltext: btn_click(cmd))
        btn.grid(column = j, row = (i+1))

win.mainloop()