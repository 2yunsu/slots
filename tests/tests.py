import sys
from .slots.slots import MAB

# Assuming pytest
sys.path.append('/root/slots')


# Most basic test of defaults
def test_mab():
    mab = MAB()
    mab.run()
