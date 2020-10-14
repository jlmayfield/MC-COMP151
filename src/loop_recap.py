
setMediaPath('/home/jlmayfield/repos/CourseRepos/MC-COMP151/bookmedia/')
arch = makePicture('arch.jpg')

def posterChannel(cval):
  if cval < 64:
    return 0
  elif cval < 128:
    return 64
  elif cval < 192:
    return 128
  else:
    return 192

def posterPixel(pixel):
  r = posterChannel(getRed(pixel))
  g = posterChannel(getGreen(pixel))
  b = posterChannel(getBlue(pixel))
  setColor(pixel, makeColor(r,g,b))
  

# for each pixel in the pixel array
def posterize1(src):
  for px in getPixels(src):
    rownum = getY(px)
    if rownum < getHeight(src)/2:
      posterPixel(px)


# for each index to the pixel array, get pixel... 
def posterize2(src):
  pxarray = getPixels(src)
  for index in  range(0,len(pxarray) / 2):
    px = pxarray[index]
    posterPixel(px)
  
# for every x coordinate
#   for every y coordinate 
def posterize3(src):
  stopat = getHeight(src) / 2
  for y in range(0,stopat):
    for x in range(0,getWidth(src)):
      px = getPixelAt(src,x,y)
      posterPixel(px)



def main():
  show(arch)
  posterize1(arch)
  repaint(arch)


