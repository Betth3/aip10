from PIL import Image

img = Image.open("открытка.jpg")
print(f"Размер оригинала: {img.size}")
cropped = img.crop((0, 330, img.width, img.height))
cropped.save("обрезанная_открытка.jpg")
print("Открытка успешно обрезана!")
print(f"Размер обрезанной открытки: {cropped.size}")
