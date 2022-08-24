from datetime import datetime
import sys
import yaml
import os
from src.genetic_algorithm import run
  
  
if __name__ == '__main__':
  os.system('clear')
  input_n = sys.argv[1]
  run(input_n)