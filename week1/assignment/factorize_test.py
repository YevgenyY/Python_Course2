import unittest


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        with self.subTest(x=1):
            self.assertRaises(TypeError, factorize, 'string')

        with self.subTest(x=2):
            self.assertRaises(TypeError, factorize, 1.5)

    def test_negative(self):
        with self.subTest(x=1):
            self.assertRaises(ValueError, factorize, -1)

        with self.subTest(x=2):
            self.assertRaises(ValueError, factorize, -10)

        with self.subTest(x=3):
            self.assertRaises(ValueError, factorize, -100)

    def test_zero_and_one_cases(self):
        with self.subTest(x=1):
            a = 0
            b = factorize(a)
            self.assertTrue(isinstance(b, tuple))
            self.assertCountEqual(b, (0,))

        with self.subTest(x=2):
            a = 1 
            b = factorize(a)
            self.assertTrue(isinstance(b, tuple))
            self.assertCountEqual(b, (1,))

    def test_simple_numbers(self):
        with self.subTest(x=1):
            a = 3 
            b = factorize(a)
            self.assertTrue(isinstance(b, tuple))
            self.assertCountEqual(b, (3,))

        with self.subTest(x=2):
            a = 13 
            b = factorize(a)
            self.assertTrue(isinstance(b, tuple))
            self.assertCountEqual(b, (13,))

        with self.subTest(x=3):
            a = 29 
            b = factorize(a)
            self.assertTrue(isinstance(b, tuple))
            self.assertCountEqual(b, (29,))

    def test_two_simple_multipliers(self):
         with self.subTest(x=1):
            a = 6 
            b = factorize(a)
            self.assertTrue(isinstance(b, tuple))
            self.assertCountEqual(b, (2,3))

         with self.subTest(x=2):
            a = 26
            b = factorize(a)
            self.assertTrue(isinstance(b, tuple))
            self.assertCountEqual(b, (2,13))

         with self.subTest(x=3):
            a = 121 
            b = factorize(a)
            self.assertTrue(isinstance(b, tuple))
            self.assertCountEqual(b, (11,11))

    def test_many_multipliers(self):
         with self.subTest(x=1):
            a = 1001 
            b = factorize(a)
            self.assertTrue(isinstance(b, tuple))
            self.assertCountEqual(b, (7,11,13))

         with self.subTest(x=2):
            a = 9699690
            b = factorize(a)
            self.assertTrue(isinstance(b, tuple))
            self.assertCountEqual(b, (2,3,5,7,11,13,17,19))


#if __name__ == "__main__":
#    unittest.main()
