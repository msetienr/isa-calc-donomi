import os, sys

path = os.path.abspath('.')
sys.path.insert(1, path)

from calc import unirCalculator as uc

def test_sum():
    assert uc.sum(1, 2) == 3
    assert uc.sum(2, 1) == 3