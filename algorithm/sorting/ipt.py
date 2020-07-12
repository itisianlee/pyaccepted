import os
import sys

absp = os.path.abspath('.')
sys.path.append('/' + os.path.join(*absp.split('/')[:-2]))