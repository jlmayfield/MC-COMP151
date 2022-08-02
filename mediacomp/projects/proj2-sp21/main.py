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

# one echo, 100% volume, begin delay samples from 0
def echo(sound,delay):  
  result = duplicateSound(sound)
  src = getSamples(sound)
  tar = getSamples(result)
  for i in range(delay,len(tar)):
    cur = getSampleValue(tar[i])
    rep = getSampleValue(src[i-delay])
    setSampleValue(tar[i],cur+rep)
  return result

# N echos, decreasing by 1/N vol, separate by delay samples
# does not feedback, echos are copies of original, echos don't echo    
def echoN(sound,delay,N):  
  result = duplicateSound(sound)
  src = getSamples(sound)
  tar = getSamples(result)
  vol = 1.0/N
  for n in range(1,N+1):
    start = n*delay
    for i in range(start,len(tar)):
      cur = getSampleValue(tar[i])
      rep = getSampleValue(src[i-start])
      setSampleValue(tar[i],cur+int(vol*rep))
  return result  

def synth1(freq,amp,sec):
  note = sineWave(freq,amp,sec)
  for i in range(1,12):
    harm = sineWave(freq,amp,sec)
    note = blend(note,harm,1,0.5)
  return note

def testsong():  
  bpm = 180 #tempo beats per minute
  rate = 22050.0 #audio sampling rate (samples per sec)
  secpb = 60.0 / bpm # seconds per beat
  sampspb = int(rate * secpb) #samples per beat
  ## Start song construction
  numbeats = 8
  songlen = int(math.ceil(numbeats * sampspb))
  song = makeEmptySound(songlen, int(rate))
  A4 = synth1(440.0,5000,secpb / 2)
  A5 = synth1(880.0,5000,secpb / 2)
  #A4 = sineWave(440.0,5000,secpb / 2)
  #  print( secpb, sampspb, getLength(song), getLength(A4))
  for b in range(0,numbeats):
    copy(A5,song,int((0.5+b)*sampspb))
  copy(A4,song,0)
  copy(A4,song,4*sampspb)
  blockingPlay(song)