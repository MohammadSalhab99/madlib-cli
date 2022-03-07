import re


def read_template(path):
    """ function that takes in a path to text file and
     returns a stripped string of the files contents.
    """ 
    try:
      f=open(path)
      return f.read()
    except:
        raise FileNotFoundError(
         'the file does not exist')  
