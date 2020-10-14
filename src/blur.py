# A riff on program 85 'blur' 

# Change this to the path to your media directory 
setMediaPath('/home/jlmayfield/repos/CourseRepos/MC-COMP151/bookmedia/')

def blur(source):
  target = duplicatePicture(source)
  for y in range(1, getHeight(source)-1):
    for x in range(1,getWidth(source)-1):
      r = 0
      g = 0
      b = 0
      for i in range(y-1,y+2):
        for j in range(x-1,x+2):
          px = getPixel(source,j,i)
          r = r + getRed(px)
          g = g + getGreen(px)
          b = b + getBlue(px)
      curr = getPixel(target,x,y)
      setColor(curr,makeColor(r/9,g/9,b/9))
  return target


orig = makePicture('horse.jpg')
blurred1 = blur(orig)
blurred2 = blur(blurred1)
#explore(orig)
#explore(blurred1)
#explore(blurred2)

#fuzzy = makePicture('horse.jpg')
#for n in range(0,5):
#  fuzzy = blur(fuzzy)
#show(fuzzy)


       