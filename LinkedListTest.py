import unittest
from LinkedList import LinkedList

class LinkedListTest(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()
        for i in range(10):
            self.linked_list.append(i)
        
        self.python_list = [i for i in range(10)]

        self.one_item_linked_list = LinkedList()
        self.one_item_linked_list.append(1)
        self.one_item_python_list = [1]

        self.empty_linked_list = LinkedList()
        self.empty_python_list = []

    def test_constructor(self):
        test = LinkedList()
        self.assertIsNone(test.head)
        self.assertIsNone(test.tail)
        self.assertEqual(test.size, 0)

    def test_append(self):
        test = LinkedList()
        test.append(1)
        self.assertEqual(test.head.data, 1)
        self.assertEqual(test.tail.data, 1)
        self.assertEqual(test.size, 1)

        test.append(2)
        test.append(3)
        self.assertEqual(test.head.data, 1)
        self.assertEqual(test.tail.data, 3)
        self.assertEqual(test.size, 3)

    def test_prepend(self):
        test = LinkedList()
        test.prepend(1)
        self.assertEqual(test.head.data, 1)
        self.assertEqual(test.tail.data, 1)
        self.assertEqual(test.size, 1)

        test.prepend(2)
        test.prepend(3)
        self.assertEqual(test.head.data, 3)
        self.assertEqual(test.tail.data, 1)
        self.assertEqual(test.size, 3)

    def test_remove_first(self):
        self.assertEqual(self.linked_list.size, 10)
        
        self.linked_list.remove_first()
        self.assertEqual(self.linked_list.head.data, 1)
        self.assertEqual(self.linked_list.tail.data, 9)
        self.assertEqual(self.linked_list.size, 9)
        
        # List has 1 element
        for _ in range(8):
            self.linked_list.remove_first()
        self.assertEqual(self.linked_list.head.data, 9)
        self.assertEqual(self.linked_list.tail.data, 9)
        self.assertEqual(self.linked_list.size, 1)
        
        # Empty List
        self.linked_list.remove_first()
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)
        self.assertEqual(self.linked_list.size, 0)

        # Delete from empty list
        self.assertRaises(IndexError, self.linked_list.remove_first)

    def test_remove_last(self):
        self.assertEqual(self.linked_list.size, 10)

        self.linked_list.remove_last()
        self.assertEqual(self.linked_list.head.data, 0)
        self.assertEqual(self.linked_list.tail.data, 8)
        self.assertEqual(self.linked_list.size, 9)

        # List has 1 element
        for _ in range(8):
            self.linked_list.remove_last()
        self.assertEqual(self.linked_list.head.data, 0)
        self.assertEqual(self.linked_list.tail.data, 0)
        self.assertEqual(self.linked_list.size, 1)

        # Empty List
        self.linked_list.remove_last()
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)
        self.assertEqual(self.linked_list.size, 0)

        self.assertRaises(IndexError, self.linked_list.remove_last)

    def test_accessing_single_index(self):
        self.assertRaises(IndexError, self.empty_linked_list.__getitem__, 0)
        self.assertRaises(IndexError, self.empty_linked_list.__getitem__, -1)
        self.assertRaises(IndexError, self.empty_linked_list.__getitem__, 1)

        self.assertRaises(TypeError, self.linked_list.__getitem__, "a")
        self.assertRaises(TypeError, self.linked_list.__getitem__, None)
        self.assertRaises(TypeError, self.linked_list.__getitem__, Exception)

        self.assertRaises(IndexError, self.linked_list.__getitem__, 10)
        self.assertRaises(IndexError, self.linked_list.__getitem__, -11)

        self.assertEqual(self.linked_list[0], 0)
        self.assertEqual(self.linked_list[9], 9)
        self.assertEqual(self.linked_list[-10], 0)
        self.assertEqual(self.linked_list[-1], 9)
        self.assertEqual(self.linked_list[3], 3)
        self.assertEqual(self.linked_list[-3], 7)        

    def test_accessing_with_slice(self):
        self.assertEqual(self.linked_list[:1], self.python_list[:1])
        self.assertEqual(self.linked_list[3:10], self.python_list[3:10])
        self.assertEqual(self.linked_list[-5:1], self.python_list[-5:1])
        self.assertEqual(self.linked_list[-50:1], self.python_list[-50:1])
        self.assertEqual(self.linked_list[:100], self.python_list[:100])
        self.assertEqual(self.linked_list[:-9], self.python_list[:-9])
        self.assertEqual(self.linked_list[4:], self.python_list[4:])
        self.assertEqual(self.linked_list[4:-2], self.python_list[4:-2])
        self.assertEqual(self.linked_list[100:2], self.python_list[100:2])
        self.assertEqual(self.linked_list[100:-2], self.python_list[100:-2])
        self.assertEqual(self.linked_list[100:200], self.python_list[100:200])

    def test_setting_single_index(self):
        self.assertRaises(IndexError, self.empty_linked_list.__setitem__, 0, 1)
        self.assertRaises(IndexError, self.empty_linked_list.__setitem__, -1, 1)
        self.assertRaises(IndexError, self.empty_linked_list.__setitem__, 1, 1)

        self.assertRaises(TypeError, self.linked_list.__setitem__, "a", 1)
        self.assertRaises(TypeError, self.linked_list.__setitem__, None, 1)
        self.assertRaises(TypeError, self.linked_list.__setitem__, Exception, 1)

        self.assertRaises(IndexError, self.linked_list.__setitem__, 10, 1)
        self.assertRaises(IndexError, self.linked_list.__setitem__, -11, 1)

        self.linked_list[0] = 'a'
        self.python_list[0] = 'a'
        self.linked_list[-2] = 4
        self.python_list[-2] = 4
        self.linked_list[9] = False
        self.python_list[9] = False

        self.assertEqual(self.linked_list[0], self.linked_list[0])
        self.assertEqual(self.linked_list[-2], self.linked_list[-2])
        self.assertEqual(self.linked_list[9], self.linked_list[9])
        self.assertEqual(str(self.linked_list), str(self.linked_list))

    def test_setting_with_slice(self):
        self.linked_list[:2] = [9, 9]
        self.python_list[:2] = [9, 9]
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))

        self.linked_list[5:] = [9, 9]
        self.python_list[5:] = [9, 9]
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))

        self.linked_list[3:3] = [9, 9]
        self.python_list[3:3] = [9, 9]
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))

        self.linked_list[:2] = [9, 9]
        self.python_list[:2] = [9, 9]
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))

        self.linked_list[2:5] = [2, 2]
        self.python_list[2:5] = [2, 2]
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))

        self.linked_list[2:5] = [3, 3, 3]
        self.python_list[2:5] = [3, 3, 3]
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))

        self.linked_list[5:2] = [3, 3, 3]
        self.python_list[5:2] = [3, 3, 3]
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))

        self.linked_list[-3:3] = [3, 3, 3]
        self.python_list[-3:3] = [3, 3, 3]
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))

        self.linked_list[-9:5] = [3, 3, 3]
        self.python_list[-9:5] = [3, 3, 3]
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))

        self.linked_list[100:5] = [4, 4, 4]
        self.python_list[100:5] = [4, 4, 4]
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))

        # Check if head and tail are set properly
        self.linked_list.append('zz')
        self.linked_list.prepend('aa')
        self.python_list.append('zz')
        self.python_list.insert(0, 'aa')
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))

    def test_delete_single_index(self):
        self.assertRaises(IndexError, self.empty_linked_list.__delitem__, 0)
        self.assertRaises(IndexError, self.empty_linked_list.__delitem__, -1)
        self.assertRaises(IndexError, self.empty_linked_list.__delitem__, 1)

        self.assertRaises(TypeError, self.linked_list.__delitem__, "a")
        self.assertRaises(TypeError, self.linked_list.__delitem__, None)
        self.assertRaises(TypeError, self.linked_list.__delitem__, Exception)

        self.assertRaises(IndexError, self.linked_list.__delitem__, 10)
        self.assertRaises(IndexError, self.linked_list.__delitem__, -11)

        del self.one_item_linked_list[0]
        self.assertEqual(str(self.one_item_linked_list), str(self.empty_linked_list))
        self.assertEqual(self.one_item_linked_list.size, 0)

        del self.linked_list[4]
        del self.python_list[4]
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))

        del self.linked_list[-4]
        del self.python_list[-4]
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))

        del self.linked_list[0]
        del self.python_list[0]
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))

        del self.linked_list[-1]
        del self.python_list[-1]
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))

        # Check if head and tail are set properly
        self.linked_list.append('zz')
        self.linked_list.prepend('aa')
        self.python_list.append('zz')
        self.python_list.insert(0, 'aa')
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))

    def test_delete_with_slice(self):
        del self.linked_list[:4]
        del self.python_list[:4]
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))
        self.linked_list.append('zz')
        self.linked_list.prepend('aa')
        self.python_list.append('zz')
        self.python_list.insert(0, 'aa')
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))

        self.setUp()
        del self.linked_list[4:]
        del self.python_list[4:]
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))
        self.linked_list.append('zz')
        self.linked_list.prepend('aa')
        self.python_list.append('zz')
        self.python_list.insert(0, 'aa')
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))

        self.setUp()
        del self.linked_list[2:5]
        del self.python_list[2:5]
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))
        self.linked_list.append('zz')
        self.linked_list.prepend('aa')
        self.python_list.append('zz')
        self.python_list.insert(0, 'aa')
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))

        self.setUp()
        del self.linked_list[4:4]
        del self.python_list[4:4]
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))
        self.linked_list.append('zz')
        self.linked_list.prepend('aa')
        self.python_list.append('zz')
        self.python_list.insert(0, 'aa')
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))

        self.setUp()
        del self.linked_list[-4:1]
        del self.python_list[-4:1]
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))
        self.linked_list.append('zz')
        self.linked_list.prepend('aa')
        self.python_list.append('zz')
        self.python_list.insert(0, 'aa')
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))

        self.setUp()
        del self.linked_list[1:-2]
        del self.python_list[1:-2]
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))
        self.linked_list.append('zz')
        self.linked_list.prepend('aa')
        self.python_list.append('zz')
        self.python_list.insert(0, 'aa')
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))

        self.setUp()
        del self.linked_list[2:100]
        del self.python_list[2:100]
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))
        self.linked_list.append('zz')
        self.linked_list.prepend('aa')
        self.python_list.append('zz')
        self.python_list.insert(0, 'aa')
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))

        self.setUp()
        del self.linked_list[100:2]
        del self.python_list[100:2]
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))
        self.linked_list.append('zz')
        self.linked_list.prepend('aa')
        self.python_list.append('zz')
        self.python_list.insert(0, 'aa')
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(self.linked_list.size, len(self.python_list))

    def test_iteration(self):
        self.linked_list = iter(self.linked_list)
        self.python_list = iter(self.python_list)
        self.assertEqual(next(self.linked_list), next(self.python_list))

        next(self.linked_list)
        next(self.linked_list)
        next(self.python_list)
        next(self.python_list)
        self.assertEqual(next(self.linked_list), next(self.python_list))

        self.one_item_linked_list = iter(self.one_item_linked_list)
        self.one_item_python_list = iter(self.one_item_python_list)
        self.assertEqual(next(self.one_item_linked_list), next(self.one_item_python_list))
        self.assertRaises(StopIteration, next, self.one_item_linked_list)
        self.assertRaises(StopIteration, next, self.one_item_python_list)

        self.empty_linked_list = iter(self.empty_linked_list)
        self.assertRaises(StopIteration, next, self.empty_linked_list)

    def test_str(self):
        self.assertEqual(str(self.linked_list), str(self.python_list))
        self.assertEqual(str(self.empty_linked_list), str(self.empty_python_list))
        self.assertEqual(str(self.one_item_linked_list), str(self.one_item_python_list))

if __name__=="__main__":
    unittest.main()
