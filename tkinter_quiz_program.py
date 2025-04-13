import tkinter as tk

# The parent window and its contents
window = tk.Tk()

window.geometry('800x500')
window.title('Quiz Creator')

window.configure(bg='black') # Background color

label = tk.Label(window, text='Quiz Creator', font=('Arial', 18), fg=('white'), bg=('black')) # Title bar
label.pack(padx=20, pady=20)

textbox = tk.Text(window, font=('Arial', 10), height=1)
textbox.pack()

window.mainloop()