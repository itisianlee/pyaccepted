import os
import sys

absp = os.path.abspath('.')
sys.path.append(absp)
sys.path.append('/' + os.path.join(*absp.split('/')[:-2]))