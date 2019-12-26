#Find Out OS Name
import os
import sys
import optparse


def ErrOut(text):
  sys.stderr.write(text + '\n')
  sys.exit(1)
  


def GetPlatform():
  if sys.platform.startswith('cygwin') or sys.platform.startswith('win'):
    return 'Windows'

  if sys.platform.startswith('darwin'):
    return 'Apple MAC'

  if sys.platform.startswith('linux'):
    return 'LINUX'
  return None

def main(args):
 
  platform = GetPlatform()
  if platform is None:
    print 'Unknown platform.'
    return 1

  if len(args) == 1:
    print platform
    return 0

if __name__ == '__main__':
  sys.exit(main(sys.argv))
