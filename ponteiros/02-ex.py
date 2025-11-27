import sys

texto = ["678"]
a = (sys.getrefcount(texto))
outro = texto
print(sys.getrefcount(texto))
print(id(a))