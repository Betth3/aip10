from PIL import Image, ImageDraw, ImageFont

postcards = {
    "1 сентября": "открытка.jpg",
    "новый год": "new_year.jpg",
    "день рождения": "birthday.jpg",
    "8 марта": "march8.jpg"
}

holiday = input("Для какого праздника Вы хотите открытку (1 сентября, новый год, день рождения, 8 марта): ").strip().lower()
if holiday in postcards:
    name = input("Введите имя того, кого хотите поздравить: ").strip()
    text = f"{name}, поздравляю!"
    img = Image.open(postcards[holiday])
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("segoesc.ttf", 60)
    # Текст по центру
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x = (img.width - text_width) // 2
    y = img.height - 100

    draw.text((x, y), text, font=font, fill=(148, 0, 211))

    img.save("поздравление.png")
    img.show()
    print(f"Открытка к празднику '{holiday}' готова!")
else:
    print("Извините, открытки для такого праздника у меня нет!")
