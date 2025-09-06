import math
sTotal = int(input("Digite uma quantidade de segundos que resulte no máximo em 1 dia: "))
if sTotal > 24* 60 * 60:
    print("A quantidade de segundos digitada excede 1 dia.")
else:
    h = math.floor(sTotal / 3600)
    m = math.floor(sTotal % 3600 / 60)
    s = sTotal % 60
    print (f"{h}:{m}:{s}")