# Toy (small/simple) Picture examples for tracing

# this is a rediculus picture but it's small and simple
def buildToy():
  toypic = makeEmptyPicture(3,4)
  for c in range(0,3):
    p = getPixelAt(toypic,c,0)
    setColor(p,makeColor((c+1)*75,0,0))
  for c in range(0,3):
    p = getPixelAt(toypic,c,1)
    setColor(p,makeColor((c+1)*75,(c+1)*75,0))
  for c in range(0,3):
    p = getPixelAt(toypic,c,2)
    setColor(p,makeColor(0,(c+1)*75,0))
  for c in range(0,3):
    p = getPixelAt(toypic,c,3)
    setColor(p,makeColor(0,0,(c+1)*75))
  return toypic

# Loops = Repetition. What are they repeating and how? 

def pixelloop(picture):
  print 'coords','pixel'
  for px in getPixels(picture):
    print "(", getX(px), ",", getY(px), ")", px
    

def rangeloop(picture):
  print 'index','coords','pixel'
  pixarray = getPixels(picture)
  for index in range(len(pixarray)/2,len(pixarray)):  
    px = pixarray[index]
    print index,"(", getX(px), ",", getY(px), ")", px


def rangeloop_halfs(picture):
  print 'index','offset index','coords@index','coords@offset','pixel@index','pixel@offset'
  pixarray = getPixels(picture)
  for index in range(0,len(pixarray)/2):  
    px = pixarray[index]
    px2 = pixarray[index+len(pixarray)/2]
    print index,index+len(pixarray)/2,\
    "(", getX(px), ",", getY(px), ")",\
    "(", getX(px2), ",", getY(px2), ")",\
    px,px2


def rangeloop_mirror(picture):
  print 'index','target','coords@index','coords@target','pixel@index','pixel@target'
  pixarray = getPixels(picture)
  target = len(pixarray)/2
  for index in range(0,len(pixarray)/2):  
    px = pixarray[index]
    px2 = pixarray[target]
    print index,target,\
    "(", getX(px), ",", getY(px), ")",\
    "(", getX(px2), ",", getY(px2), ")",\
    px,px2
    target = target+1

    