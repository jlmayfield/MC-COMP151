# YOUR NAME HERE
# Lab 5 


# CHANGE THIS TO YOUR MEDIA DIRECTORY
setMediaPath('/home/jlmayfield/repos/CourseRepos/MC-COMP151/bookmedia/')

# 5.3

def makeBorder(pic,color,width):
  # replace return with code
  # do one border, test it, repeat ... 
  return
  

def testMakeBorder():
  img = makePicture('arch.jpg')
  px = getPixelAt(img,349,1)
  print(px,getX(px),getY(px))
  makeBorder(img,makeColor(255,0,0),25)
  px = getPixelAt(img,349,1)
  print(px,getX(px),getY(px))
  show(img)  
  

# 5.4

def makeDiagonal(pic,color):
  return

def testMakeDiagonal():
  img = makePicture('arch.jpg')
  px = getPixelAt(img,200,200)
  print(px,getX(px),getY(px))
  makeDiagonal(img,blue)
  px = getPixelAt(img,200,200)
  print(px,getX(px),getY(px))
  explore(img)
  return


# 5.5

# 5.6

# 5.7
