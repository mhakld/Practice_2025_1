import sys
from tkinter import *
import tkinter.filedialog

root = Tk()
root.title("Текстовый редактор")
root.geometry("600x400")  # фиксированный стартовый размер

# Глобальные переменные для шрифта и размера
current_font = StringVar(value="Helvetica")
current_size = IntVar(value=12)

# Верхняя панель
toolbar = Frame(root)
toolbar.grid(row=0, column=0, sticky="w")

# Текстовое поле
text = Text(root, wrap="word", font=(current_font.get(), current_size.get()))
text.grid(row=1, column=0, sticky="nsew")

# Настройка сетки
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Сохранить файл
def saveas():
    t = text.get("1.0", "end-1c")
    savelocation = tkinter.filedialog.asksaveasfilename(defaultextension=".txt",
                                                        filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if savelocation:
        with open(savelocation, "w", encoding="utf-8") as file:
            file.write(t)

# Открыть файл
def openfile():
    filepath = tkinter.filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filepath:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
            text.delete("1.0", END)
            text.insert("1.0", content)

# Обновить шрифт с новым размером и/или типом
def update_font(*args):
    text.config(font=(current_font.get(), current_size.get()))

# Кнопки
Button(toolbar, text="Открыть", command=openfile).grid(row=0, column=0, padx=2, pady=2)
Button(toolbar, text="Сохранить", command=saveas).grid(row=0, column=1, padx=2, pady=2)

# Меню шрифтов
font_menu = Menubutton(toolbar, text="Шрифт", relief=RAISED)
font_menu.grid(row=0, column=2, padx=2, pady=2)
font_menu.menu = Menu(font_menu, tearoff=0)
font_menu["menu"] = font_menu.menu

fonts = ["Helvetica", "Courier", "Arial", "Times New Roman", "Verdana", "Comic Sans MS"]
for f in fonts:
    font_menu.menu.add_radiobutton(label=f, variable=current_font, value=f, command=update_font)

# Меню размеров
size_menu = Menubutton(toolbar, text="Размер", relief=RAISED)
size_menu.grid(row=0, column=3, padx=2, pady=2)
size_menu.menu = Menu(size_menu, tearoff=0)
size_menu["menu"] = size_menu.menu

sizes = [8, 10, 12, 14, 16, 18, 20, 24, 28, 32]
for s in sizes:
    size_menu.menu.add_radiobutton(label=str(s), variable=current_size, value=s, command=update_font)

root.mainloop()