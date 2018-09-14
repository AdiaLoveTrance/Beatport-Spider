from PIL import Image,ImageFilter

logo=Image.open("logo.jpg")
newlogo=logo.filter(ImageFilter.SHARPEN)
newlogo.save("newlogo.jpg")
newlogo.show()