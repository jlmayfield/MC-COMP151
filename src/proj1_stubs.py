# Top-Down Design w/ Stub Definitions


# ****** VERSION 0 Functions ******
# reduce 256 colors to 4. Used on Blue for 8 bit color.
def twoBitColor(cval):
  if cval < 64:
    return 32
  elif cval < 128:
    return 92
  elif cval < 192:
    return 146
  else:
    return 232

# reduce 256 color to 8. Used on Red and Green for 8 bit color
def threeBitColor(cval):
  return 50

# reduce 24bit RGB to 8 bit RGB
def to8bit(pic,sx,sy,ex,ey):
  ## LOOP: Every pixel in the given region
  for x in range(sx,ex):
    for y in range(sy,ey):
      px = getPixel(pic,x,y)
      # Convert Each Color Channel
      setRed(px, threeBitColor(getRed(px))
      setGreen(px, threeBitColor(getGreen(px))
      setBlue(px, twoBitColor(getBlue(px))
  


# ****** VERSION 0.5 Function *******

# average color of the 6x6 block with upper left corner at
# x,y
def avgColor(pic,x,y):
  for i in range(x, x+6):
    for j in range(y, y+6 ):
      px = getPixel(pic,i,j)
      ## compute average color
  return makeColor(0,0,0)
  
def setBlockColor(pic,x,y,clr):
  for i in range(x, x+6):
    for j in range(y, y+6 ):
      px = getPixel(pic,i,j)
      # make px have the color clr
    

def pixelate(pic,sx,sy,ex,ey):
  # Loops !! Go through every anchor!! 
  for x in range(....):
    for y in range( .... ):
      acolor = avgColor(pic,x,y)
      setBlockColor(pic,x,y,acolor)


# ****** VERSION 0.75 ********
def crop(pic,sx,sy,ex,ey):
  t_w = ..
  t_h = ..
  target = makeEmptyPicture(.., ..)
  
  
  return target

  
# ****** VERSION 1.0 ********

def scaleDown(pic):
  target = makeEmptyPicture(... , ...)
  for x in range():
    for y in range():
      px = ...
  return target


# Program 78, General Copy Function
def copy(src,tar,tarx,tary):
  targetX = tarx
  for sx in range(0,getWidth(src)):
    targetY = tary
    for sy in range(0,getHeight(src)):
      px = getPixel(src,sx,sy)
      tx = getPixel(tar,targetX,targetY)
      setColor(tx,getColor(px))
      targetY = targetY+1
    targetX = targetX + 1

setMediaPath('/home/jlmayfield/repos/MonmCourses/MC-COMP151/projects/')
# James: 88,62 to 261,284
# Norah: 346,238 to 560,510
# Floss: 397,141 to 603,300
def main():
  kids = makePicture('bothkids.jpg')
  cat = makePicture('flossie.jpg')
  chars = makePicture('mc-friends.png')
  # make the faces blocky by assigning avg color
  pixelate(kids,88,62,261,284) #boy
  pixelate(kids,346,238,560,510) #girl
  pixelate(cat,397,141,603,300) #cat
  # 'posterize' 
  to8bit(kids,88,62,261,284) #boy
  to8bit(kids,346,238,560,510) #girl
  to8bit(cat,397,141,603,300) #cat
  # crop out faces
  boyface = crop(kids,88,62,261,284)
  # repeat for girl and cat
  boyface = scaleDown(boyface)
  # repeat for girl and cat
  copy(boyface,chars,197,24)
  # repeat for girl and cat
  show(chars)
  writePictureTo(chars,'minekids.jpg')
  