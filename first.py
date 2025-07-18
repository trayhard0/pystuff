import tkinter as tk
import tkinter.font as tkFont
root = tk.Tk()
root.geometry("230x380")
root.title("Calculator")
root.resizable(False, False)
calculate_area = tk.Frame(root)
top_font = tkFont.Font(size=20)
text = tk.Text(calculate_area, height=2, width=42, font=top_font)
calculate_area.pack()
text.pack()
text.insert("1.0", "")
text.config(state="disabled")  # Make the text area read-only
num_area = tk.Frame(root)
num_area.pack()
numbers_font = tkFont.Font(size=15)
clear = tk.Button(num_area, text="C", width=4, height=2,
                  font=numbers_font, command=lambda: clear_calculation())
clear.grid(row=0, column=2)
delete = tk.Button(num_area, text="DEL", width=4, height=2,
                   font=numbers_font, command=lambda: delete_last())
delete.grid(row=0, column=3)
num9 = tk.Button(num_area, text="9", width=4, height=2,
                 font=numbers_font, command=lambda: button_click("9"))
num9.grid(row=1, column=2)
num8 = tk.Button(num_area, text="8", width=4, height=2,
                 font=numbers_font, command=lambda: button_click("8"))
num8.grid(row=1, column=1)
num7 = tk.Button(num_area, text="7", width=4, height=2,
                 font=numbers_font, command=lambda: button_click("7"))
num7.grid(row=1, column=0)
num6 = tk.Button(num_area, text="6", width=4, height=2,
                 font=numbers_font, command=lambda: button_click("6"))
num6.grid(row=2, column=2)
num5 = tk.Button(num_area, text="5", width=4, height=2,
                 font=numbers_font, command=lambda: button_click("5"))
num5.grid(row=2, column=1)
num4 = tk.Button(num_area, text="4", width=4, height=2,
                 font=numbers_font, command=lambda: button_click("4"))
num4.grid(row=2, column=0)
num3 = tk.Button(num_area, text="3", width=4, height=2,
                 font=numbers_font, command=lambda: button_click("3"))
num3.grid(row=3, column=2)
num2 = tk.Button(num_area, text="2", width=4, height=2,
                 font=numbers_font, command=lambda: button_click("2"))
num2.grid(row=3, column=1)
num1 = tk.Button(num_area, text="1", width=4, height=2,
                 font=numbers_font, command=lambda: button_click("1"))
num1.grid(row=3, column=0)
num0 = tk.Button(num_area, text="0", width=4, height=2,
                 font=numbers_font, command=lambda: button_click("0"))
num0.grid(row=4, column=0)
multiply = tk.Button(num_area, text="x", width=4, height=2,
                     font=numbers_font, command=lambda: button_click("*"))
multiply.grid(row=2, column=3)
divide = tk.Button(num_area, text="/", width=4, height=2,
                   font=numbers_font, command=lambda: button_click("/"))
divide.grid(row=1, column=3)
subtract = tk.Button(num_area, text="-", width=4, height=2,
                     font=numbers_font, command=lambda: button_click("-"))
subtract.grid(row=3, column=3)
add = tk.Button(num_area, text="+", width=4, height=2,
                font=numbers_font, command=lambda: button_click("+"))
add.grid(row=4, column=3)
equals = tk.Button(num_area, text="=", width=4, height=2,
                   font=numbers_font, command=lambda: calculate())
equals.grid(row=4, column=2)
decimal = tk.Button(num_area, text=".", width=4, height=2,
                    font=numbers_font, command=lambda: button_click("."))

decimal.grid(row=4, column=1)
leftparenthesis = tk.Button(num_area, text="(", width=4, height=2,
                            font=numbers_font, command=lambda: button_click("("))
leftparenthesis.grid(row=0, column=0)
rightparenthesis = tk.Button(num_area, text=")", width=4, height=2,
                             font=numbers_font, command=lambda: button_click(")"))
rightparenthesis.grid(row=0, column=1)

calculation = ""


def button_click(operation):
    print("hello")
    global calculation
    if len(calculation) > 0 and operation == "(" and calculation[-1] in "0123456789":
        button_click("*")
    calculation = calculation + operation
    text.config(state="normal")
    text.delete("1.0", tk.END)
    text.insert("1.0", calculation)
    text.config(state="disabled")


def calculate():
    try:
        global calculation
        result = eval(calculation)
        calculation = str(result)
        text.config(state="normal")
        text.delete("1.0", tk.END)
        text.insert("1.0", result)
        text.config(state="disabled")
    except Exception as e:
        calculation = ""
        text.config(state="normal")
        text.delete("1.0", tk.END)
        text.insert("1.0", "ERROR")
        text.config(state="disabled")


def clear_calculation():
    global calculation
    calculation = ""
    text.config(state="normal")
    text.delete("1.0", tk.END)
    text.config(state="disabled")


def delete_last():
    global calculation
    calculation = calculation[:-1]
    text.config(state="normal")
    text.delete("1.0", tk.END)
    text.insert("1.0", calculation)
    text.config(state="disabled")


root.mainloop()
