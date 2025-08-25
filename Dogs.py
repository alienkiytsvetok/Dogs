# Получение по API с сайта dog.ceo в формате JSON {"ключ": "значение"}
# сайт postman.co для получения ссылки на любой сайт, картинку

from tkinter import*
from PIL import Image, ImageTk
from tkinter messagebox as mb
import requests
from io import BytesIO




def show_image():
    image_url = get_dog_image()
    if image_url:
        try:
            response = requests.get(image_url, stream=True) # получаем ссылку на картинку
            response.raise_for_status()
            img_data = BytesIO(response.content)
            img = Image.open(img_data) #обрабатываем с помощью PIL и получаем картинку
            img.thumbnail((300, 300)) # Подгоняем картинку под нужные размеры окна
            label.config(image=img)
            label.image = img # чтобы сборщик мусора не собрал картинку
        except Exception as e:
            mb.showerror("ошибка", f"Возникла ошибка {e}")

window = Tk()
window.title("Картинки с собачками")
window.geometry("360x420")

label = label()
label.pack(pady=10)

button = Button(text="Загрузить изображение", command=show_image)
button.pack(pady=10)

window.mainloop()