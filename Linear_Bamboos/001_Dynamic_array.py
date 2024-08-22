import ctypes
import time
import sys

class DynamicArray:

    def __init__(self, elm_type, capacity=1, resize_factor=2):
        self._n = 0                                    # count actual elements
        self._capacity = capacity                      # default array capacity
        self._A = self._make_array(self._capacity)     # low-level array
        self.resize_factor = resize_factor
        self.elm_type = {'int':ctypes.c_int, 'float':ctypes.c_float, 'double':ctypes.c_double, 'char':ctypes.c_char, '':ctypes.py_object}
    
    def __len__(self):
        return self._n
    
    def resize(self):
        array = (self.capacity * self.resize_factor * self.elm_type)()
        for i in range(self._size):
            array[i] = self._A[i]
        self._A=array
        self._capacity *=self.resize_factor
    
    def getItem(self, k):
        if not 0<=k<=self._n:
            raise IndexError("Index not found")
        return self._A[k]
    
    def append(self, ele):
        if self._n == self._capacity:
            self.resize()
    
    def average_append_time(self, num_elements):
        start_time=time.time()
        for i in range(num_elements):
            self.append(i)
        end_time = time.time()
        return (end_time - start_time) / num_elements
    
    def memory_allocated(self):
        return ctypes.sizeof(self._A)

    def address_allocated(self):
        return ctypes.addressof(self._A)
            