# Logan Mayfield
#  9/4/2020

# Tell JES where you keep your Media
setMediaPath('/home/jlmayfield/repos/CourseRepos/MC-COMP151/bookmedia/')

# bird2.jpg, statue-tower.jpg, turtle-dragon.jpg

bird = makePicture('bird2.jpg')
tower = makePicture('statue-tower.jpg')
tdrag = makePicture('turtle-dragon.jpg')

#def doCoolStuff(picture):
#  for px in getPixels(picture):
#    redc = getRed(px)
#    greenc = getGreen(px)
#    bluec = getBlue(px)
#    x = getX(px)
#    y = getY(px)
#    newColor = makeColor(... , ... , ...)
#    setColor(px, newColor)

#def doCoolStuff(picture):
#  pxArray = getPixels(picture)
#  for index in range(0,len(pxArray)):
#    px = pxArray[index]
#    redc = getRed(px)
#    greenc = getGreen(px)
#    bluec = getBlue(px)
#    x = getX(px)
#    y = getY(px)
#    newColor = makeColor(... , ... , ...)
#    setColor(px, newColor)

def lightenPicture(picture):
  for px in getPixels(picture):
    oldColor = getColor(px)
    newColor = makeLighter(oldColor)
    setColor(px, newColor)

def togray(picture):
  for px in getPixels(picture):
    redc = getRed(px)*0.299
    greenc = getGreen(px)*0.587
    bluec = getBlue(px)*0.114
    lum = (redc+greenc+bluec)
    mygray = makeColor(lum, lum ,lum)
    setColor(px, mygray)

def negate(picture):
  for px in getPixels(picture):
    redc = getRed(px)
    greenc = getGreen(px)
    bluec = getBlue(px)
    redn = 255-redc
    greenn = 255 - greenc
    bluen  = 255 - bluec
    newColor = makeColor(redn,greenn,bluen)
    setColor(px, newColor)

def reduceBlue(picture):
  for px in getPixels(picture):
    bluec = getBlue(px)
    setBlue(px,bluec*0.7)

def reduceGreen(picture):
  for px in getPixels(picture):
    greenc = getGreen(px)
    setGreen(px,greenc*0.7)
    
def sunset(picture):
  reduceBlue(picture)
  reduceGreen(picture)

def sunset2(picture):
  for px in getPixels(picture):
    greenc = getGreen(px)
    bluec = getBlue(px)
    setGreen(px,greenc*0.7)
    setBlue(px,bluec*0.7)
    

def togray2(picture):
  pxarray = getPixels(picture)
  size = len(pxarray)
  for idx in range(0,size):
    px = pxarray[idx]
    redc = getRed(px)*0.0299
    greenc = getGreen(px)*0.587
    bluec = getBlue(px)*0.114
    lum = (redc+greenc+bluec)
    mygray = makeColor(lum, lum ,lum)
    setColor(px, mygray)    
    



