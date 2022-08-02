
import math
from media import *

# provide frequency (freq), amplitude (amp), and 
# duration 
def sineWave(freq,amp,sec):
  result = makeEmptySoundBySeconds(sec)
  rate = getSamplingRate(result)
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


if __name__ == '__main__':
  A4 = sineWave(440.0,5000,1)
  blockingPlay(A4)