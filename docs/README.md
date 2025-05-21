# 2.Вариативная часть задания
# Создание простого текстового редактора на Python с использованием Tkinter

## 1. Исследование и планирование

### 1.1. Цель проекта

Создать простой, но функциональный текстовый редактор на Python, позволяющий:

- Открывать и сохранять .txt файлы.
- Изменять шрифт и размер текста.
- Обеспечить стабильную и удобную работу.

### 1.2. Изучение технологии

Изучены компоненты библиотеки Tkinter:
- Виджеты: Text, Button, Menu, Menubutton, Frame
- Файловые диалоги: askopenfilename, asksaveasfilename
- Шрифты и стили: config(font=...)
- Расположение элементов с помощью менеджера компоновки grid

---

## 2. Техническое руководство

### 2.1. Создание фиксированного графического окна и верхней панели

```python
import sys
from tkinter import *
import tkinter.filedialog
root = Tk()
root.title("Текстовый редактор")
root.geometry("600x400")

toolbar = Frame(root)
toolbar.grid(row=0, column=0, sticky="w")
```

### 2.2. Открытие и сохранение файлов

```python
def saveas():
    t = text.get("1.0", "end-1c")
    savelocation = tkinter.filedialog.asksaveasfilename(defaultextension=".txt",
                                                        filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if savelocation:
        with open(savelocation, "w", encoding="utf-8") as file:
            file.write(t)

def openfile():
    filepath = tkinter.filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filepath:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
            text.delete("1.0", END)
            text.insert("1.0", content)
```

### 2.3. Добавление шрифтов и размеров
```python
font_menu = Menubutton(toolbar, text="Шрифт", relief=RAISED)
font_menu.grid(row=0, column=2, padx=2, pady=2)
font_menu.menu = Menu(font_menu, tearoff=0)
font_menu["menu"] = font_menu.menu

fonts = ["Helvetica", "Courier", "Arial", "Times New Roman", "Verdana", "Comic Sans MS"]
for f in fonts:
    font_menu.menu.add_radiobutton(label=f, variable=current_font, value=f, command=update_font)

size_menu = Menubutton(toolbar, text="Размер", relief=RAISED)
size_menu.grid(row=0, column=3, padx=2, pady=2)
size_menu.menu = Menu(size_menu, tearoff=0)
size_menu["menu"] = size_menu.menu

sizes = [8, 10, 12, 14, 16, 18, 20, 24, 28, 32]
for s in sizes:
    size_menu.menu.add_radiobutton(label=str(s), variable=current_size, value=s, command=update_font)

```
