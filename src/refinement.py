# Logan Mayfield
# Iterative Refinement Demo
# reduceRedEye --> p 50 --> p 64

from time import clock

setMediaPath('/home/jlmayfield/repos/CourseRepos/MC-COMP151/bookmedia/')


# ver 0:  Reduces the whole region where her eyes occur 
# ver 1:  make final eye color variable and color similarity variable
# ver 2:  make reduction region variable
# ver 3: performance improvement with tighter loop



#eye1 (109,91) , (146,111)
#eye2 (166,90) , (202,107)
def reduceRedEye(pic,startx,starty,endx,endy,endclr,clrthresh):
  for y in range(starty,endy+1):
    for x in range(startx, endx+1):
      px = getPixelAt(pic,x,y)
      clr = getColor(px)
      if distance(clr,red) < clrthresh:
           setColor(px,endclr)
        
        
def main():
  jen = makePicture('jenny-red.jpg')
#  show(jen)
  start = clock()
  # left eye
  reduceRedEye(jen,109,91,202,107,\
  green,150)
  end = clock() - start
  print "left eye time: ", end
#  start = clock()
  # rigth eye
#  reduceRedEye(jen,166,90,202,107,\
#  blue,150)
#  end = clock() - start
#  print "right eye time: ", end
#  repaint(jen)
  
  
  