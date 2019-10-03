#!/usr/bin/python
import unittest
import disjoint

class Disjoint:

    def __init__(self):
        self._sets = []
		
    def createSet(self, repr):
        self._sets.apend(repr)         #
		
	def mergeSets(self, repr1, repr2):
        set1 = self.findset(repr1)
        set2 = sefl.findSet(repr2)
        if set1 != set2:
            set1.extend(set2)
            self._sets.remove(set2)

    def findSet(self, repr1):
        for oneSet in self._sets:
            if repr1 in oneSet:
                return oneSet
				
    def getSets(self):             # python convention is to expose attributs directly 
        return self._sets

# test class :
class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        pass
		
    def test_empty(self):
        dis = disjoint.Disjoint()
        self.assertEqual([], dis.getSets())
		self.assertEqual(None, dis.findSet(1))
		
    def test_init(self):
        dis = disjoint.Disjoint();
		for i in range(1, 6):
            dis.createSet(i)
        for i in range(1, 6):
            found = dis.findSet(i)
            self.assertEqual(1, len(found))
			self.assertEqual(i, found[0])
        expected = [[i] for i in range(1, 6)]
        self.assertEqual(expected, dis.getSets())
		
	def test_simple(self):
        dis = disjoint.Disjoint()
        for i in range(1, 6):
            dis.createSet(i)
        pairs = [[1, 2], [2, 4], [4, 5]]
        for p in pairs:
            p1 = p[0]
            p2 = p[1]
			
			if dis.findSet(p1) != dis.findSet(p2):
                dis.mergeSets(p1, p2)

        expectedSets = [[1, 2, 4, 5], [3]]
        self.assertEqual(expectedSets, dis.getSets())

if __name__ == '__main__':
    unittest.main()
			
			
# Note that there is cameCase here and that is not part of pep - 8

# Note 2 - The getSets method is unnecessarry - 
			
			