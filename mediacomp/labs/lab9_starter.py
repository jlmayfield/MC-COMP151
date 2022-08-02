# Lab 9 Starter

bassC4 = makeSound('/home/jlmayfield/repos/MonmCourses/MC-COMP151/mediasources-4ed/musicsounds/bassoon-c4.wav')
bassG4 = makeSound('/home/jlmayfield/repos/MonmCourses/MC-COMP151/mediasources-4ed/musicsounds/bassoon-g4.wav')


# Sounds must be same length, or longer sound is sound1.
# blend is functional, it returns the combination of sound1 
#  and sound2.
def blend(sound1,sound2):
  target = makeEmptySound(getLength(sound1))
  t = getSamples(target)
  s1 = getSamples(sound1)
  s2 = getSamples(sound2)
  for i in range(0, len(s2)):
    s1val = getSampleValue(s1[i])
    s2val = getSampleValue(s2[i])
    setSampleValue(t[i], s1val + s2val)
  return target
  

bassCG4 = blend(bassC4,bassG4)
blockingPlay(bassCG4)  
blockingPlay(bassC4)
blockingPlay(bassG4)