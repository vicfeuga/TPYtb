import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
 
from fonctions import read_input

def test_read_input():
    assert read_input('input.json') != None