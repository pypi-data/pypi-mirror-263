from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.simpledialog import askstring
from time import strftime
import random
import webbrowser

class TicTacToe:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Крестики-нолики")

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = Button(self.parent, text="", font=("Arial", 20), width=5, height=2,
                                            command=lambda row=i, col=j: self.click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

        self.reset_button = Button(self.parent, text="Начать сначала", command=self.reset)
        self.reset_button.grid(row=3, column=1, columnspan=3, pady=10)

    def click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Победа!", f"Игрок {self.current_player} победил!")
                self.reset()
            elif self.check_draw():
                messagebox.showinfo("Ничья!", "Ничья!")
                self.reset()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        return True

    def reset(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")

class Calculator:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Калькулятор")

        self.equation = StringVar()
        self.entry = Entry(self.parent, textvariable=self.equation, font=("Arial", 18), bd=10, insertwidth=4, width=20)
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            button = Button(self.parent, text=text, font=("Arial", 18), width=5, height=2,
                            command=lambda t=text: self.click(t))
            button.grid(row=row, column=col)

    def click(self, text):
        if text == '=':
            try:
                result = eval(self.equation.get())
                self.equation.set(result)
            except Exception as e:
                self.equation.set("Ошибка")
        elif text == 'C':
            self.equation.set("")
        else:
            self.equation.set(self.equation.get() + text)

def update_clock(label):
    label.config(text=strftime('%H:%M:%S %p'))
    label.after(1000, lambda: update_clock(label))

def get_user_info():
    name = askstring("Введите свое имя", "Пожалуйста, введите ваше имя:")
    if name:
        messagebox.showinfo("Приветствие", f"Добро пожаловать, {name}!")
        return name
    else:
        messagebox.showwarning("Предупреждение", "Имя не было введено. Попробуйте еще раз.")
        return get_user_info()

root = Tk()
root.title("Главное окно")
root.geometry("600x400")  # Измененные размеры окна

# Создаем кнопки для открытия социальных сетей
telegram_button = Button(root, text="Telegram", bg="blue", fg="white", padx=10, pady=5, command=lambda: webbrowser.open("https://telegram.org/"))
telegram_button.grid(row=0, column=0, padx=10, pady=10)

instagram_button = Button(root, text="Instagram", bg="purple", fg="white", padx=10, pady=5, command=lambda: webbrowser.open("https://www.instagram.com/"))
instagram_button.grid(row=0, column=1, padx=10, pady=10)

vk_button = Button(root, text="ВКонтакте", bg="skyblue", fg="white", padx=10, pady=5, command=lambda: webbrowser.open("https://vk.com/"))
vk_button.grid(row=0, column=2, padx=10, pady=10)

# Функция для анимации изменения цвета фона
def change_bg_color(label):
    colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
    label.config(bg=random.choice(colors))
    label.after(1000, lambda: change_bg_color(label))

# Label для анимации изменения цвета фона
bg_label = Label(root, text="Анимация изменения цвета фона", font=('Arial', 18), pady=20)
bg_label.grid(row=1, columnspan=3)

change_bg_color(bg_label)

clock_label = Label(root, font=('Arial', 24), pady=20)
clock_label.grid(row=2, columnspan=3)

update_clock(clock_label)

calculator_button = Button(root, text="Калькулятор", command=lambda: Calculator(Toplevel(root)))
calculator_button.grid(row=3, column=0, padx=20, pady=20)

tic_tac_toe_button = Button(root, text="Крестики-нолики", command=lambda: TicTacToe(Toplevel(root)))
tic_tac_toe_button.grid(row=3, column=2, padx=20, pady=20)

user_name = get_user_info()
user_label = Label(root, text=f"Пользователь: {user_name}", font=('Arial', 12), anchor='w')
user_label.grid(row=4, columnspan=3, padx=10, pady=10, sticky='we')



root.mainloop()
