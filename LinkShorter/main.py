import pyshorteners

url = input("Enter URL: ")
shortener = pyshorteners.Shortener()
x = shortener.tinyurl.short(url)
print(x)
