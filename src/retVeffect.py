
## Functions that Return vs Functions that have an Effect
## Designing Sub-Functions and Program Organization


# go from 0 to 255 (256 values) to 4 values 
# take these four evenly spaced ranges 
# 0 to 63, 64 to 127, 128 to 191,192 to 255

def twobitcolor(co):
  if co < 64:
    return 50    
  elif co < 128:
    return 175    
  elif co < 192:
    return 190    
  else:
    return 224 

def sixbitcolor(pic,sx,sy,ex,ey):
  for x in range(sx,ex):
    for y in range(sy,ey):
      px = getPixel(pic,x,y)
      # do stuff to px
      setRed(px,twobitcolor(getRed(px)))
      setGreen(px,twobitcolor(getGreen(px)))
      setBlue(px,twobitcolor(getBlue(px)))

def toGray(pic,sx,sy,ex,ey):
  for x in range(sx,ex):
    for y in range(sy,ey):
      px = getPixel(pic,x,y)
      # do stuff to px
      setColor(px,gray)

def copydark(pic):
  w = getWidth(pic)
  h = getHeight(pic)
  tar = makeEmptyPicture(w,h)
  for x in range(0,w):
    for y in range(0,h):
      px = getPixel(pic,x,y)
      tx = getPixel(tar,x,y)
      # do stuff
      dark_clr = makeDarker(getColor(px))
      setColor(tx,dark_clr)  
  return tar

setMediaPath( '/home/jlmayfield/Pictures/c151-pro1/' )
def main():
  kids = makePicture('bothkids.jpg')
  cat = makePicture('flossie.jpg')
  toGray(kids,50,50,100,200)
  sixbitcolor(kids,200,300,400,500)
  dark_floss = copydark(cat)
  #show(kids)
  show(dark_floss)
  #show(cat)
  