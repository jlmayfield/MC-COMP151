# Top-Down Design w/ Stub Definitions


# stub definition 
def to8bit(pic,sx,sy,ex,ey):
  pass

# stub with return
def pixelate(pic,sx,sy,ex,ey):
  return pic

setMediaPath('/home/jlmayfield/Pictures/c151-pro1/')
def main():
  kids = makePicture('bothkids.jpg')
  cat = makePicture('flossie.jpg')
  mcfriends = makePicture('mc-friends.png')
  pandas = makePicture('Minecraft-panda.jpg')
  kids = pixelate(kids,100,234,400,327)
  to8bit(kids,100,234,400,327)
  to8bit(kids,400,550,500,600)
  to8bit(cat,100,100,300,275)
  explore(kids)
  #show(cat)
  #show(mcfriends)
  