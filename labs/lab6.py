# Your Name Here


def luminance(pixel):
  r = getRed(pixel)
  b = getBlue(pixel)
  g = getGreen(pixel)
  l = (r+b+g)/3
  return l

def edgeAccent(source):
  for px in getPixels(source):
    x = getX(px)
    y = getY(px)
    if y < getHeight(source)-1 and x <getWidth(source)-1:
      botrt = getPixel(source,x+1,y+1)
      thislum = luminance(px)
      brlum = luminance(botrt)
      if abs(brlum-thislum) > 10:
        setColor(px,black)
      else:
        setColor(px,white)
 