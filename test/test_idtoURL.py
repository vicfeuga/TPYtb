import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
 
from fonctions import idtoURL

id_test = idtoURL('od_PmtmMDV0')

def test_idtoURL():
    assert  id_test == 'https://www.youtube.com/watch?v=od_PmtmMDV0'
