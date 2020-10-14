# Logan Mayfield
# Coding Demo 8/28/2020

# 
def change1Pixel(p):
 setRed(p,255)
 setGreen(p,0)
 setBlue(p,51) 
 return
  

# r -> 255, B -> 51, G -> 0
def change4Pixels(pic, x, y):
  p = getPixel(pic,x,y)
  change1Pixel(p)
  p = getPixel(pic,x+1,y)
  change1Pixel(p)
  p = getPixel(pic,x+2,y)
  change1Pixel(p)
  p = getPixel(pic,x+3,y)
  change1Pixel(p)
  return


#  Script Here

# load some test images
ruins = makePicture('/home/jlmayfield/repos/CourseRepos/MC-COMP151/bookmedia/greekRuins.jpg')
swans = makePicture('/home/jlmayfield/repos/CourseRepos/MC-COMP151/bookmedia/swans.jpg')
# do something 'cool'
change4Pixels(ruins,300,300)
# test/inspect/view results
explore(ruins)