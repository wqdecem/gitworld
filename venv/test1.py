import unittest

class Cla(object):

    def __init__(self):
        print('hello world!')

    def bigger(self,a,b):
        if a > b:
            return a
        else:
            return b
        




class Test_test1(unittest.TestCase):
    def __init__(self, methodName = 'runTest'):
        self.C = Cla()
        return super().__init__(methodName)

    def test_A(self):
        self.assertEqual(3,self.C.bigger(3,2))
        

if __name__ == '__main__':
    T = Test_test1()
    T.test_A()
    