
addLibPath('/home/jlmayfield/repos/MonmCourses/MC-COMP151/src')
import waveGen as wg

def main():
  a4 = wg.sineWave(440.0,10000,spb/2)
  a4_sq = wg.squareWave(440.0,10000,spb/2)
  a4_tri = wg.triangleWave(440.0,10000,spb/2)
  no = wg.whiteNoise(10000,spb/2)
