# Получение по API с сайта dog.ceo в формате JSON {"ключ": "значение"}
# сайт postman.co для получения ссылки на любой сайт, картинку

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
            img.thumbnail((300, 300)) # Подгоняем картинку под нужные размеры окна
            img = ImageTk.PhotoImage(img)
            label.config(image=img)
            label.image = img # чтобы сборщик мусора не собрал картинку
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

window.mainloop()