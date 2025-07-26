import tkinter as tk
root=tk.Tk()
root.title("New GUI Application")
root.geometry("400x300")
lable = tk.Label(root, text="Welcome to the New GUI Application!")
lable.pack(pady=10)
root.mainloop()