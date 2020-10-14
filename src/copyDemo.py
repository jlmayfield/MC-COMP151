

setMediaPath('/home/jlmayfield/repos/CourseRepos/MC-COMP151/bookmedia/')

swan = makePicture('swan.jpg')
# bounding box of swan: ul:(71,71)  lr:(397,288)

# source, source coordiantes, target
def makeCropCopy(source,sx,sy,ex,ey,t_w,t_h,pin_x,pin_y):  
  #make canvas as per user supplied size 
  target = makeEmptyPicture(t_w,t_h)
  # setup target coordinates 
  t_x = pin_x 
  # for every source column
  for x in range(sx,ex+1):
    # reset target y coordinate
    t_y = pin_y
    #for every source row (in each column)
    for y in range(sy,ey+1):
      # get pixels
      src_px = getPixel(source,x,y)
      tar_px = getPixel(target,t_x,t_y) 
      # get new color 
      newclr = getColor(src_px)
      # copy
      setColor(tar_px,newclr)
      # advance target y coord.
      t_y = t_y + 1    
    # advance target x coordinate
    t_x = t_x + 1
   
  # ya done!
  return target
  
other_swan = makeCropCopy(swan,71,68,397,288,1000,1000,200,400)



def scale(source):
  t_w = getWidth(source)/2
  t_h = getHeight(source)/2
  target = makeEmptyPicture(t_w,t_h)
  t_x = 0
  for x in range(0,getWidth(source),2):
    t_y = 0
    for y in range(0,getHeight(source),2):
      src_px = getPixel(source,x,y)
      tar_px = getPixel(target,t_x,t_y)
      setColor(tar_px,getColor(src_px))
      t_y = t_y + 1      
    t_x = t_x + 1 
  return target

small_swan = scale(swan)

  