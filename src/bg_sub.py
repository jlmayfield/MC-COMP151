

setMediaPath('/home/jlmayfield/repos/CourseRepos/MC-COMP151/bookmedia/')
alice = makePicture('Alice.jpg')
beach = makePicture('beach.jpg')

## chromakey substitution (replace pixels of a specifc color ('the key')
##  with pixels from another image at the same location

# program 57
def chroma(src,bg):
  for px in getPixels(src):
    x = getX(px) 
    y = getY(px)
    if distance(getColor(px),makeColor(0,255,1)) < 20:
      bgpx = getPixelAt(bg,x,y)
      bgcolor = getColor(bgpx)
      setColor(px,bgcolor)

      
      
# luminance based edge-detection program 55
      
def luminance(pixel):
  r = getRed(pixel)
  b = getBlue(pixel)
  g = getGreen(pixel)
  return (r+b+g)/3

def edge(src):
  for px in getPixels(src):
    x = getX(px)
    y = getY(px)
    if y < getHeight(src)-1 and x < getWidth(src)-1:
      br = getPixelAt(src,x+1,y+1)
      px_lum = luminance(px)
      br_lum = luminance(br)
      if abs(br_lum - px_lum) > 10:
        setColor(px,black)