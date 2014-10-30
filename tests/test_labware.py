import unittest
from itctools import labware


class TestLabware(unittest.TestCase):
    """Validation of the labware submodule."""

    def test_labware(self):
        """Ensure that Labware has correct parameter assignment."""
        itcplate = labware.Labware('DestinationPlate', 'ITC Plate', '123abc')
        self.assertEqual([itcplate.RackLabel, itcplate.RackType, itcplate.RackID], ['DestinationPlate', 'ITC Plate', '123abc'])

    def test_pipettinglocation(self):
        """Ensure that PipettingLocation has correct parameter asignment."""
        pipettinglocation = labware.PipettingLocation('Buffer', 'Trough 100 ml', 1)
        self.assertEqual([pipettinglocation.RackLabel, pipettinglocation.RackType, pipettinglocation.Position], ['Buffer', 'Trough 100 ml', 1])

if __name__ == '__main__':
    unittest.main()
