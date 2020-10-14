# Logan Mayfield
# intro to if

# Modify the pixel if:
#  1) it's color is/isn't similar to some target color
#    'it the pixel's color is similar to purple, then ...'
#  2) it is/isn't located within a specific region of the photo
#    'if the pixel's  y coordinate is between rows 10 and 50 and
#      the x coordinate is between columns 100 and 275, then ...'

# if ( test for condtion ):
#    do when test passes

# I want to save my pictures to this location. 
setMediaPath('/home/jlmayfield/repos/CourseRepos/MC-COMP151/creations/')




def iftinker(picture):
  for px in getPixels(picture):
    # pixel coordinates
    x = getX(px)
    y = getY(px)
    # the whole color
    clr = getColor(px)
    # individual color channels
    pxRed = getRed(px)
    pxBlue = getBlue(px)
    pxGreen = getGreen(px)


# == same
# != different

#1: x:(238,252) y: (134,178)
#2: x:(252,271) y: (106,178)
def bwbox(picture,startx,endx,starty,endy):
  for px in getPixels(picture):
    # pixel coordinates
    x = getX(px)
    y = getY(px)
    if ((x >= startx and x <= endx) and (y >=starty and y <= endy)):
      pxRed = getRed(px)
      pxBlue = getBlue(px)
      pxGreen = getGreen(px)
      lum  = (pxRed + pxBlue + pxGreen)/3      
      setColor(px,makeColor(lum,lum,lum))



# r180,g30,b35
def colorTheFlower(picture,newColor):
  flr_clr = makeColor(180,30,35)
  for px in getPixels(picture):
    px_clr = getColor(px)
    if (distance(px_clr,flr_clr)) < 75:
      setColor(px,newColor)


# use full path because image is not at media path 
fish = makePicture('/home/jlmayfield/repos/CourseRepos/MC-COMP151/bookmedia/fish.jpg')

#show(fish)
#colorTheFlower(fish,pink)
#repaint(fish)
# saves to MediaPath
#writePictureTo(fish,'modified-fish.jpg')    



    