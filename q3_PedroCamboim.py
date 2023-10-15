from PIL import Image, ImageEnhance

enhanceImage = lambda img = Image.open('black-hole.png'), factor = float(input("Digite o fator de brilho: ")) : ImageEnhance.Brightness(img).enhance(factor)

enhanceImage().show()
