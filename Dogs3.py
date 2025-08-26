# создаем видеж ноутбук как закладки в одном окне

from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox as mb
import requests
from io import BytesIO
from tkinter import ttk


def get_dog_image():
    try:
        response = requests.get("https://dog.ceo/api/breeds/image/random") # ответом будет ссылка в формате JSON
        response.raise_for_status() # если все хорошо статус = 200
        data = response.json()
        print(data) # проверка, что возвращает в командную строку
        print(data['message']) # проверка, что возвращает в командную строку
        print(data['status']) # проверка статуса в командную строку
        return data['message'] # получает адрес картинки
    except Exception as e:
        mb.showerror("ошибка", f"Возникла ошибка при запросе к API {e}")
        return None


def show_image():
    image_url = get_dog_image()
    if image_url:
        try:
            response = requests.get(image_url, stream=True) # получаем ссылку на картинку
            response.raise_for_status()
            img_data = BytesIO(response.content)
            img = Image.open(img_data) #обрабатываем с помощью PIL и получаем картинку
            img_size = (int(width_spinbox.get()), int(height_spinbox.get()))
            img.thumbnail(img_size) # Подгоняем картинку под нужные размеры окна
            img = ImageTk.PhotoImage(img)
            # new_window = Toplevel(window) # создание нового окна для отображения картинки
            # new_window.title("случайное изображение")
            tab = ttk.Frame(notebook)
            notebook.add(tab, text=f"Фото №{notebook.index('end') +1}") # получаем номер картирки
            lb = ttk.Label(tab, image=img)
            lb.pack(padx=10, pady=10)
            lb.image = img # чтобы сборщик мусора не собрал картинку
        except Exception as e:
            mb.showerror("ошибка", f"Возникла ошибка при загрузке изображения{e}")
    progress.stop()


def prog():
    progress['value'] = 0
    progress.start(30)
    window.after(3000, show_image) # 3000 милисекунд равно 3 сек.

window = Tk()
window.title("Картинки с собачками")
window.geometry("360x420")

label = ttk.Label()
label.pack(pady=10)

button = ttk.Button(text="Загрузить изображение", command=prog)
button.pack(pady=10)

progress = ttk.Progressbar(mode="determinate", length=300)
progress.pack(pady=10)

# создаем параметры ширины спинбокса
width_label = ttk.Label(text="ширина:")
width_label.pack(side="left", padx=(10,0)) # метка будет прижата влево, padx означает отступ 10 от левого края
width_spinbox = ttk.Spinbox(from_=200, to=500, increment=50, width=5) # размеры будут изменять в диапазоне 200-500 с шагом 50
width_spinbox.pack(side="left", padx=(0,10))
width_spinbox.set(300) # устанавливаем значение ширины по умолчанию.

# создаем параметры высоты спинбокса
height_label = ttk.Label(text="высота:")
height_label.pack(side="left", padx=(10,0))
height_spinbox = ttk.Spinbox(from_=200, to=500, increment=50, width=5)
height_spinbox.pack(side="left", padx=(0,10))
height_spinbox.set(300) # устанавливаем значение высоты по умолчанию.

# Отдельное окно ноутбук с закладочкой
top_level_window = Toplevel(window)
top_level_window.title("Изображения собачек")

notebook = ttk.Notebook(top_level_window) # создаем окно
notebook.pack(expand=True, fill = 'both',padx=10, pady=10) # заполнить все пространство с отступами по 10

window.mainloop()