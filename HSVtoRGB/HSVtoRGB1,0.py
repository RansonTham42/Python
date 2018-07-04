def huefunc():
    global huecom
    huecom = int(input("Enter an INTEGER between 0 and 360 "))
    if huecom > 360:
        print("Error: Integer between 0 and 360")
        huefunc()
huefunc()

def saturationfunc():
    global saturationcom
    saturationcom = int(input("Enter an INTEGER between 0 and 100 "))
    if saturationcom > 100:
        print("Error: Integer between 0 and 100")
        saturationfunc()
saturationfunc()

def valuefunc():
    global valuecom
    valuecom = int(input("Enter an INTEGER between 0 and 100 "))
    if valuecom > 100:
        print("Error: Integer between 0 and 100")
        valuefunc()
valuefunc()

if huecom == 360:
    huecom = 0

if 0 <= huecom <= 60:
    f = int(huecom) * 4.25
    red = 255
    green = int(round(f))
    blue = 0
elif 61 <= huecom <= 120:
    h = 255 - int(huecom - 60) * 4.25
    red = int(round(h))
    green = 255
    blue = 0
elif 121 <= huecom <= 180:
    i = int(huecom - 120) * 4.25
    red = 0
    green = 255
    blue = int(round(i))
elif 181 <= huecom <= 240:
    j = 255 - int(huecom - 180) * 4.25
    red = 0
    green = int(round(j))
    blue = 255
elif 241 <= huecom <= 300:
    k = int(huecom - 240) * 4.25
    red = int(round(k))
    green = 0
    blue = 255
elif 301 <= huecom <= 359:
    l = 255 - int(huecom - 300) * 4.25
    red = 255
    green = 0
    blue = int(round(l))

red1 = red
green1 = green
blue1 = blue

red = (255 - red1) * (100 - saturationcom) / 100 + red1
green = (255 - green1) * (100 - saturationcom) / 100 + green1
blue = (255 - blue1) * (100 - saturationcom) / 100 + blue1

red = red * valuecom / 100
green = green * valuecom / 100
blue = blue * valuecom / 100

print("HSV(" + str(huecom) + ", " + str(saturationcom) + ", " + str(valuecom) + ")" + " ==>> " + "RGB(" + str(red) + ", " + str(green) + ", " + str(blue) + ")")
