import tkinter as tk
from tkinter import ttk

# Color
header_clr = '#d496a7' # Dark Pink
main_clr = '#f1dede' # Light Pink
font_clr = '#542e38' # Darker Pink

# Parent window
window = tk.Tk()

window.geometry('600x500')
window.title('Quiz Reader') #Title bar

# Aesthetics
window.configure(bg=main_clr) # Background color

header = tk.Frame(window, bg=header_clr, height=100, bd=1, relief='solid')
header.pack(fill="x")

header_label = tk.Label(header, text="Quiz Reader", bg=header_clr,
                        fg=font_clr, font=("Trebuchet MS", 45, "bold"))
header_label.grid(padx=40, sticky="w")

footer = tk.Frame(window, bg=header_clr, height=60, bd=1, relief='solid')
footer.pack(fill="x", side='bottom')

window.mainloop()