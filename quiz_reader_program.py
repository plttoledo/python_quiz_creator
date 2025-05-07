import tkinter as tk
from tkinter import ttk, Button

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
question_tx = tk.Label(window, text='Question:', font=('Trebuchet MS', 25, 'bold'),
                    fg=font_clr, bg=main_clr)
question_tx.pack(padx=40, pady=10, anchor='w')

# Question Textbox
textbox_qstn = tk.Text(window, font=('Arial', 15), height=1, bd=1, relief='solid', state='disabled')
textbox_qstn.pack(padx=40, anchor='w')

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