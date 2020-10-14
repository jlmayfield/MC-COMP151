#





#program 82,
#  This program is a nice, self contained program but this one and done
#  style quickly becomes a problem when the program gets larger there's clear subfunctions (scale down, ex 6.30) that could be 
#    written, in a reusable style, and used. This pays off more if you
#    end up scaling down multiple pictures. It also combines loading pictures
# and showing picture code with modifying picture code

def scaleDown(src,startx,starty,endx,endy):
  w = endx - startx + 1
  h = endy - starty + 1
  c_w = int(w/2)
  c_h = int(h/2)  
  canvas = makeEmptyPicture(c_w,c_h)
  sourceX = startx
  for targetX in range(0, c_w):
    sourceY = starty
    for targetY in range(0,c_h):
      color = getColor(getPixel(src,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      sourceY = sourceY + 2
    sourceX = sourceX + 2
  return canvas
  

 
# version -1:  main will load and show the pictures of the kids and cat.
# version -0.5: maybe posterize all of the image just to get the 8bit stuff
#   figured out
# version 0: modify the 'posterize all' to do 'posterize some'
      
setMediaPath('/home/jlmayfield/repos/CourseRepos/MC-COMP151/bookmedia/')

def main():
  horse = makePicture('horse.jpg')
  dog = makePicture('dog.jpg')
  # horse face only
  smallHorse = scaleDown(horse,107,107,254,428)
  # entire dog picture
  smallDog = scaleDown(dog,0,0,getWidth(dog),getHeight(dog))
  explore(smallHorse)
  explore(smallDog)
  #writePictureTo(smallHorse,'/home/jlmayfield/repos/CourseRepos/MC-COMP151/creations/smallhorse.jpg')
  #writePictureTo(smallHorse,'/home/jlmayfield/repos/CourseRepos/MC-COMP151/creations/smalldog.jpg')
  return smallHorse
  
  
  
  