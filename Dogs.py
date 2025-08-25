# Получение по API с сайта dog.ceo в формате JSON {"ключ": "значение"}
# сайт postman.co для получения ссылки на любой сайт, картинку

from tkinter import*
from PIL import Image, ImageTk
import requests
from io import BytesIO


window = Tk()
window.title("Картинки с собачками")
window.geometry("360x420")

label = label()
label.pack(pady=10)

button = Button(text="Загрузить изображение", command=show_image)
button.pack(pady=10)

window.mainloop()