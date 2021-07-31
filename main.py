# Создать приложение, которое будет считать, бьет ли заданная фигура другую.
# Координаты фигур должны вводиться с помощью визуального интерфейса, наподобие того, который представлен ниже.
# Функция по вычислению бьет ли фигура другую выполняется по нажатию на кнопку.
# Результат также должен быть показан в этом окне.
# Задание на 2 плюса:
# Вместо того, чтобы у вас была фиксированная фигура,
# вам надо сделать dropdown menu, где можно будет выбрать одну из
# фигур, которые вам выдавались для 1 лабораторной работы.
# После нажатия на кнопку вычислить, будет высчитываться именно для выбранной фигуры.

from tkinter import *
from tkinter.ttk import Combobox
from Classes.Pieces import Pawn, King, Queen, Bishop, Knight, Rook

piece_names = {'White Pawn': Pawn(True), 'Black Pawn': Pawn(False), 'King': King(), 'Queen': Queen(),
               'Bishop': Bishop(), 'Knight': Knight(), 'Rook': Rook()}

window = Tk()
window.title('Check?')
window.geometry('400x300')

king_label = Label(window, text='King')
king_x = Entry(window, width=5)
king_y = Entry(window, width=5)

king_label.grid(column=0, row=0)
king_x.grid(column=1, row=0)
king_y.grid(column=2, row=0)

# Drop down piece menu
piece_menu = Combobox(window)
pieces = list(piece_names.keys())
pieces.insert(0, 'Choose a Piece')
piece_menu['values'] = tuple(pieces)
piece_menu.current(0)
piece_x = Entry(window, width=5)
piece_y = Entry(window, width=5)
answer_label = Label(window, text='')

piece_menu.grid(column=0, row=1)
piece_x.grid(column=1, row=1)
piece_y.grid(column=2, row=1)
answer_label.grid(column=0, row=2)


# for checking if entry windows contain numbers
def is_int(x):
    try:
        for num in x:
            int(num)
        return True
    except ValueError:
        return False


def calculate_check():
    piece = piece_menu.get()
    answer_label.configure(text='', fg='black')
    if piece in piece_names:
        coordinates = [piece_x.get(), piece_y.get(), king_x.get(), king_y.get()]
        if is_int(coordinates):
            response = piece_names[piece].beats_victim_piece(int(coordinates[0]),
                                                             int(coordinates[1]),
                                                             int(coordinates[2]),
                                                             int(coordinates[3]))
        else:
            response = 'Please, enter valid coordinates'
        if response == 'True':
            answer_label.configure(text=f'{piece} beats King', fg='black')
        elif response != 'False':
            answer_label.configure(text=response, fg='red')
        else:
            answer_label.configure(text=f'{piece} does not beat King', fg='black')
    else:
        answer_label.configure(text='Please, choose a valid piece', fg='red')


calc_button = Button(window, text='Calculate', command=calculate_check)
calc_button.grid(column=3, row=2)

window.mainloop()
