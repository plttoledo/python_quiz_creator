import tkinter as tk
from tkinter import ttk, Button, Radiobutton, IntVar

# Color
header_clr = '#d496a7' # Dark Pink
main_clr = '#f1dede' # Light Pink
font_clr = '#542e38' # Darker Pink

# The parent window and its contents
window = tk.Tk()

window.geometry('600x500')
window.title('Quiz Creator') #Title bar

# Aesthetics
window.configure(bg=main_clr) # Background color

header = tk.Frame(window, bg="#c48c9f", height=100)
header.pack(fill="x")

header_label = tk.Label(header, text="Quiz Creator", bg="#c48c9f",
                        fg=font_clr, font=("Trebuchet MS", 45, "bold"))
header_label.grid(padx=20, sticky="w")

# Remember to update the question # per next question
question = tk.Label(window, text='Question:', font=('Trebuchet MS', 25, 'bold'),
                    fg=font_clr, bg=main_clr)
question.pack(padx=20, pady=(10), anchor='w')

# Textbox
textbox_q = tk.Text(window, font=('Arial', 10), height=1)
textbox_q.pack(padx=25)

textbox_a = tk.Text(window, font=('Arial', 10), height=1)
textbox_a.pack(padx=70, pady=10)

textbox_b = tk.Text(window, font=('Arial', 10), height=1)
textbox_b.pack(padx=70, pady=10)

textbox_c = tk.Text(window, font=('Arial', 10), height=1)
textbox_c.pack(padx=70, pady=10)

textbox_d = tk.Text(window, font=('Arial', 10), height=1)
textbox_d.pack(padx=70, pady=10)

# Buttons, will move these to the bottom
btn_one = Button(window, text="Next Question")
btn_one.pack()

btn_two = Button(window, text="Save")
btn_two.pack()

btn_three = Button(window, text="Exit")
btn_three.pack()

# Radio Buttons, should be beside the text boxes
r = IntVar()

radio_one = Radiobutton(window,variable=r, value=1, bg=main_clr, selectcolor=header_clr).pack()

radio_two = Radiobutton(window,variable=r, value=2, bg=main_clr, selectcolor=header_clr).pack()

radio_three = Radiobutton(window,variable=r, value=3, bg=main_clr, selectcolor=header_clr).pack()

radio_four = Radiobutton(window,variable=r, value=4, bg=main_clr, selectcolor=header_clr).pack()

window.mainloop()
