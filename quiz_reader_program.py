import tkinter as tk
from tkinter import ttk, Button, Radiobutton, IntVar

# Color
header_clr = '#d496a7' # Dark Pink
main_clr = '#f1dede' # Light Pink
font_clr = '#542e38' # Darker Pink

# Parent window
window = tk.Tk()

window.geometry('600x500')
window.title('Quiz Reader') # Title bar

# Aesthetics
window.configure(bg=main_clr) # Background color

header = tk.Frame(window, bg=header_clr, height=100, bd=1, relief='solid')
header.pack(fill="x")

header_label = tk.Label(header, text="Quiz Reader", bg=header_clr, fg=font_clr, font=("trebuchet MS", 45, "bold"))
header_label.grid(padx=40, sticky="w")

footer = tk.Frame(window, bg=header_clr, height=60, bd=1, relief='solid')
footer.pack(fill="x", side='bottom')

# Question Text
question_text = tk.Label(window, text='Question:', font=('Trebuchet MS', 25, 'bold'),
                         fg=font_clr, bg=main_clr)
question_text.pack(padx=40, pady=10, anchor='w')

# Question Textbox
question_textbox = tk.Text(window, font=('Arial', 15), height=1, bd=1, relief='solid',
                           state='disabled')
question_textbox.pack(padx=40, anchor='w')

# Functionalities
var = tk.IntVar()

def answer_field(window, var_value, option_letter):
    frame = tk.Frame(window, bg=main_clr)
    frame.pack(padx=40, pady=10, anchor='w')

    ans_textbox = tk.Text(frame, font=('Arial', 10), height=1, width=65, bd=1, relief='solid', state='disabled')
    ans_textbox.pack(side='left')

    radio_btn = Radiobutton(frame, variable=var, value=var_value, bg=main_clr,
                           selectcolor=header_clr)
    radio_btn.pack(side='left', padx=(10, 2))

   # Label Letters
    label = tk.Label(frame, text=option_letter, font=('Arial', 12, 'bold'),
                     fg=font_clr, bg=main_clr)
    label.pack(side='left', padx=(0, 10))

    return ans_textbox

option_a = answer_field(window,1, 'A')
option_b = answer_field(window,2, 'B')
option_c = answer_field(window,3, 'C')
option_d = answer_field(window,4, 'D')

# Bottom Buttons
load_btn = Button(window, text="Load Quiz", bg=header_clr,
                  font=('Trebuchet MS', 15, 'bold'), bd=1, relief='solid', activebackground=main_clr,
                  width=15) # Add command=
load_btn.pack(side='left', padx=40)

nextq_btn = Button(window, text="Next", bg=header_clr,
                  font=('Trebuchet MS', 15, 'bold'), bd=1, relief='solid', activebackground=main_clr,
                  width=10) # Add command=
nextq_btn.pack(side='left', padx=0)

exit_btn = Button(window, text="Exit", bg=header_clr,
                  font=('Trebuchet MS', 15, 'bold'), bd=1, relief='solid', activebackground=main_clr,
                  width=10) # Add command=
exit_btn.pack(side='left', padx=40)



window.mainloop()