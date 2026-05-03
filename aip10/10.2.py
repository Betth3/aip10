from PIL import Image

postcards = {
    "1 сентября": "открытка.jpg",
    "новый год": "new_year.jpg",
    "день рождения": "birthday.jpg",
    "8 марта": "march8.jpg"
}

holiday = input("Для какого праздника Вы хотите открытку (1 сентября, новый год, день рождения, 8 марта): ").strip().lower()
if holiday in postcards:
    Image.open(postcards[holiday]).show()
    print(f"Открытка к празднику '{holiday}' открыта!")
else:
    print("Извините, открытки для такого праздника у меня нет!")
