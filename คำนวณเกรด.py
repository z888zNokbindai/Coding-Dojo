from tkinter import  *

def checkGrade():
    score = int(user_input.get())
    if score >= 91:
        result.configure(text = 'A')
    elif score >= 81:
        result.configure(text = 'B')
    elif score >= 71:
        result.configure(text = 'C')
    elif score >= 61:
        result.configure(text = 'D')
    else:
        result.configure(text = 'F')


main_window = Tk()
title = Label(main_window, text = 'โปรแกรมคำนวณเกรด')
title.grid(row = 0 , column = 1)
text1 = Label(main_window, text = 'กรอกคะแนน : ')
text1.grid(row = 1, column = 0)
user_input = Entry(main_window,bd = 5)
user_input.grid(row = 1, column = 1)
button1 = Button(main_window, text = 'คำนวณ', command = checkGrade)
button1.grid(row = 2, column = 1)
text2 = Label(main_window, text = 'ผลลัพธ์ : ')
text2.grid(row = 3, column = 0)
result = Label(main_window, text = '')
result.grid(row = 3 , column = 1)

main_window.mainloop()
