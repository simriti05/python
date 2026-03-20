 

# CALCULATOR 1

# import tkinter as tk

# def click_button(value):
#     current = display.get()
#     display.delete(0, tk.END)
#     display.insert(0, current + value)

# def clear_display():
#     display.delete(0, tk.END)

# def calculate():
#     try:
#         result = eval(display.get())
#         display.delete(0, tk.END)
#         display.insert(0, str(result))
#     except Exception:
#         display.delete(0, tk.END)
#         display.insert(0, "Error")

# root = tk.Tk()
# root.title("Calculator")

# display = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='ridge', justify='right')
# display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# buttons = [
#     ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
#     ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
#     ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
#     ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
# ]

# for (text, row, col) in buttons:
#     action = lambda x=text: click_button(x) if x!='=' else calculate()
#     tk.Button(root, text=text, width=4, height=2, font=('Arial',18),
#               command=action).grid(row=row, column=col, padx=5, pady=5)

# tk.Button(root, text='C', width=4, height=2, font=('Arial',18),
#           command=clear_display).grid(row=5, column=0, columnspan=4, pady=5)

# root.mainloop()








# CALCULATOR 2

# import customtkinter as ctk
# from tkinter import messagebox

# # -----------------------------
# # Step 1: Setup main window
# # -----------------------------
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("blue")

# app = ctk.CTk()
# app.title("Mini Calculator (Star Layout)")
# app.geometry("400x500")
# app.minsize(400, 500)  # prevent collapsing too small
# app.rowconfigure(1, weight=1)  # main content expands
# app.columnconfigure(0, weight=1)

# # -----------------------------
# # Step 2: Display at top
# # -----------------------------
# display = ctk.CTkEntry(
#     app,
#     font=("Arial", 28, "bold"),
#     justify="right",
#     corner_radius=12
# )
# display.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

# # -----------------------------
# # Step 3: Functions
# # -----------------------------
# def click(symbol):
#     display.insert("end", symbol)

# def calculate():
#     try:
#         expression = display.get()
#         result = eval(expression)
#         display.delete(0, "end")
#         display.insert("end", str(result))
#     except Exception:
#         messagebox.showerror("Error", "Invalid Input")

# def clear_display():
#     display.delete(0, "end")

# # -----------------------------
# # Step 4: Frame for Buttons
# # -----------------------------
# frame = ctk.CTkFrame(app)
# frame.grid(row=1, column=0, sticky="nsew", padx=15, pady=10)

# # Configure rows and columns to expand evenly (★ STAR DIMENSIONS)
# for i in range(5):  # 5 rows (numbers & =)
#     frame.rowconfigure(i, weight=1)
# for j in range(4):  # 4 columns (1, 2, +)
#     frame.columnconfigure(j, weight=1)

# # -----------------------------
# # Step 5: Create Buttons
# # -----------------------------
# btn_style = dict(font=("Arial", 22, "bold"), corner_radius=10)

# # Row 1 → 7, 8, 9, /
# ctk.CTkButton(frame, text="7", **btn_style, command=lambda: click("7")) \
#     .grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

# ctk.CTkButton(frame, text="8", **btn_style, command=lambda: click("8")) \
#     .grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

# ctk.CTkButton(frame, text="9", **btn_style, command=lambda: click("9")) \
#     .grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

# ctk.CTkButton(frame, text="÷", fg_color="#ff9500", **btn_style, command=lambda: click("/")) \
#     .grid(row=0, column=3, sticky="nsew", padx=5, pady=5)

# # Row 2 → 4, 5, 6, ×
# ctk.CTkButton(frame, text="4", **btn_style, command=lambda: click("4")) \
#     .grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

# ctk.CTkButton(frame, text="5", **btn_style, command=lambda: click("5")) \
#     .grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

# ctk.CTkButton(frame, text="6", **btn_style, command=lambda: click("6")) \
#     .grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

# ctk.CTkButton(frame, text="×", fg_color="#ff9500", **btn_style, command=lambda: click("*")) \
#     .grid(row=1, column=3, sticky="nsew", padx=5, pady=5)

# # Row 3 → 1, 2, 3, -
# ctk.CTkButton(frame, text="1", **btn_style, command=lambda: click("1")) \
#     .grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

# ctk.CTkButton(frame, text="2", **btn_style, command=lambda: click("2")) \
#     .grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

# ctk.CTkButton(frame, text="3", **btn_style, command=lambda: click("3")) \
#     .grid(row=2, column=2, sticky="nsew", padx=5, pady=5)

# ctk.CTkButton(frame, text="-", fg_color="#ff9500", **btn_style, command=lambda: click("-")) \
#     .grid(row=2, column=3, sticky="nsew", padx=5, pady=5)

# # Row 4 → 0, ., =, +
# ctk.CTkButton(frame, text="0", **btn_style, command=lambda: click("0")) \
#     .grid(row=3, column=0, sticky="nsew", padx=5, pady=5)

# ctk.CTkButton(frame, text=".", **btn_style, command=lambda: click(".")) \
#     .grid(row=3, column=1, sticky="nsew", padx=5, pady=5)

# ctk.CTkButton(frame, text="=", fg_color="#34c759", **btn_style, command=calculate) \
#     .grid(row=3, column=2, sticky="nsew", padx=5, pady=5)

# ctk.CTkButton(frame, text="+", fg_color="#ff9500", **btn_style, command=lambda: click("+")) \
#     .grid(row=3, column=3, sticky="nsew", padx=5, pady=5)

# # Row 5 → C (clear)
# ctk.CTkButton(frame, text="C", fg_color="#ff3b30", **btn_style, command=clear_display) \
#     .grid(row=4, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# # -----------------------------
# # Step 6: Run App
# # -----------------------------
# app.mainloop()



