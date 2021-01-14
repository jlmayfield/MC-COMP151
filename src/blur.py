# A riff on program 85 'blur' 

# Change this to the path to your media directory 
setMediaPath('/home/jlmayfield/repos/CourseRepos/MC-COMP151/bookmedia/')
horse = makePicture('horse.jpg')
#line 6
def avgcolor(source,x,y):
  r = 0
  g = 0
  b = 0
  for i in range(y-1,y+2):
    for j in range(x-1,x+2):      
      px = getPixel(source,j,i)
      r = r + getRed(px)
      g = g + getGreen(px)
      b = b + getBlue(px)
  avgcolor = makeColor(r/9,g/9,b/9)
  return avgcolor
#line 19
def blur(source):
  target = duplicatePicture(source)
  for y in range(1,getHeight(source)-1,1):
    for x in range(1,getWidth(source)-1,1):
      curr = getPixel(target,x,y)
      avgclr = avgcolor(source,x,y)
      #setBlockColor(source,x,y,avgclr)
      setColor(curr,agvclr)
  return target

setMediaPath('/home/jlmayfield/repos/CourseRepos/MC-COMP151/bookmedia/')
def main():
  horse = makePicture('horse.jpg')  
  blurred_horse = blur(horse)
  blur(horse)
  explore(horse)
  
  explore(blurred_horse)
