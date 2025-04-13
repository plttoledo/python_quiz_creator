import tkinter as tk
from tkinter import ttk, Button, Radiobutton, IntVar

# Color
header_clr = '#d496a7'
main_clr = '#f1dede'

# The parent window and its contents
window = tk.Tk()

window.geometry('600x500')
window.title('Quiz Creator') #Title bar

# Aesthetics
window.configure(bg=main_clr) # Background color

label = tk.Label(window, text='Quiz Creator', font=('Trebuchet MS', 40, 'bold'), fg=('white'), bg=main_clr) # Title
label.pack(padx=20, pady=20)

# Textbox
textbox_a = tk.Text(window, font=('Arial', 10), height=1)
textbox_a.pack(padx=20, pady=10)

textbox_b = tk.Text(window, font=('Arial', 10), height=1)
textbox_b.pack(padx=20, pady=10)

textbox_c = tk.Text(window, font=('Arial', 10), height=1)
textbox_c.pack(padx=20, pady=10)

textbox_d = tk.Text(window, font=('Arial', 10), height=1)
textbox_d.pack(padx=20, pady=10)

# Buttons, will move these to the bottom
btn_one = Button(window, text="Next Question")
btn_one.pack()

btn_two = Button(window, text="Save")
btn_two.pack()

btn_three = Button(window, text="Exit")
btn_three.pack()

# Radio Buttons, should be beside the text boxes
r = IntVar()

Radiobutton(window,variable=r, value=1).pack()
Radiobutton(window,variable=r, value=2).pack()
Radiobutton(window,variable=r, value=3).pack()
Radiobutton(window,variable=r, value=4).pack()

window.mainloop()
