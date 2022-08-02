# COMP151 - Project 2 - SP21
# Starter Code

# provide frequency (freq), amplitude (amp), and 
# duration (sec)
def sineWave(freq,amp,sec):
  rate = 22050.0
  dur = int(math.ceil(rate*sec))
  result = makeEmptySound(dur)
  # length of note's cycle
  cycleLength = 1.0/freq
  # number of samples in a cycle
  sampPerCycle = cycleLength*rate
  #Compute the wave
  samps = getSamples(result)
  for i in range(0,len(samps)):
    # find point on +/- 1 sin wave
    raw = math.sin((i/sampPerCycle) * 2 * math.pi)
    value = raw * amp
    setSampleValue(samps[i],value)  
  return result
  
# produce static white noise at the given 
# amplitude (amp) and duration (sec)
def whiteNoise(amp,sec):
  rate = 22050
  dur = int(math.ceil(rate*sec))
  noise = makeEmptySound(dur)
  samples = getSamples(noise)
  # generate random samples that are more or less
  # in the +/- 1 range, then scale up amplitude
  for i in range(0,len(samples)):
    samp = samples[i]
    value = amp*random.normalvariate(0,0.75)
    setSampleValue(samp,value)
  return noise
 

# copy source into target beginning at sample number start
# Assumes target can accomodate (is long enough for) source.
def copy(source,target,start):
  if(start == getLength(target)):
    return
  s_samps = getSamples(source)
  t_samps = getSamples(target)
  targetIndex = start
  for sourceIndex in range(0,len(s_samps)):   
    sourceValue = getSampleValue(s_samps[sourceIndex])
    setSampleValue(t_samps[targetIndex],sourceValue)     
    targetIndex = targetIndex + 1

# combine sound1 and sound2 applying a volume adjustment of 
# v1 and v2 
def blend(sound1,sound2,v1,v2):
  maxlen = max(getLength(sound1),getLength(sound2))
  sharedlen = min(getLength(sound1), getLength(sound2))
  target = makeEmptySound(maxlen)
  t = getSamples(target)
  s1 = getSamples(sound1)
  s2 = getSamples(sound2)
  for i in range(0, sharedlen):
    s1val = getSampleValue(s1[i])
    s2val = getSampleValue(s2[i])
    setSampleValue(t[i], v1*s1val + v2*s2val)
  for i in range(sharedlen,maxlen):
    if sharedlen < len(s2):
      s2val = getSampleValue(s2[i])
      setSampleValue(t[i], v2*s2val)
    elif sharedlen < len(s1):
      s1val = getSampleValue(s1[i])
      setSampleValue(t[i], v1*s1val)      
  return target


def testsong():  
  A4 = sineWave(440.0,5000,.25)
  shhhhh = whiteNoise(2500,0.25)
  blockingPlay(A4)
  blockingPlay(shhhhh)