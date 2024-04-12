import pytest

from slicetools import reverse_slice, mirror_slice, shift_slice


def test_reverse_slice_1():
    x = slice(None, 3, 1)
    y = reverse_slice(x)
    assert(y.start == 2 and y.stop == None and y.step == -1)
    
    a = [0,1,2,3,4,5]
    
    b = a[x]
    assert(b == [0,1,2])

    c = a[y]
    assert(c == [2,1,0])


def test_reverse_slice_2():
    x = slice(None, 3, -1)
    y = reverse_slice(x)
    assert(y.start == 4 and y.stop == None and y.step == 1)
    
    a = [0,1,2,3,4,5]
    
    b = a[x]
    assert(b == [5, 4])

    c = a[y]
    assert(c == [4, 5])


def test_reverse_slice_3():
    x = slice(-1, 3, -1)
    y = reverse_slice(x)
    assert(y.start == 4 and y.stop == None and y.step == 1)
    
    a = [0,1,2,3,4,5]
    
    b = a[x]
    assert(b == [5, 4])

    c = a[y]
    assert(c == [4, 5])


def test_mirror_slice_1():
    x = slice(0, 2)
    y = mirror_slice(x)
    assert(y.start == None and y.stop == -3 and y.step == -1)
    
    a = [0,1,2,3,4,5]
    
    b = a[x]
    assert(b == [0, 1])

    c = a[y]
    assert(c == [5, 4])


def test_mirror_slice_2():
    x = slice(1, -3, 1)
    y = mirror_slice(x)
    assert(y.start == -2 and y.stop == 2 and y.step == -1)
    
    a = [0,1,2,3,4,5]
    
    b = a[x]
    assert(b == [1, 2])

    c = a[y]
    assert(c == [4, 3])


def test_shift_slice_1():
    x = slice(None, 3, 1)
    y = shift_slice(x, 0)
    assert(y == x)

    a = [0,1,2,3,4,5]
    
    b = a[x]
    assert(b == [0, 1, 2])

    c = a[y]
    assert(c == [0, 1, 2])


def test_shift_slice_2():
    x = slice(None, 3, 1)
    y = shift_slice(x, 2)
    assert(y.start == 2 and y.stop == 5 and y.step == 1)

    a = [0,1,2,3,4,5]
    
    b = a[x]
    assert(b == [0, 1, 2])

    c = a[y]
    assert(c == [2, 3, 4])


def test_shift_slice_3():
    x = slice(None, 3, -1)
    y = shift_slice(x, 2)
    assert(y.start == None and y.stop == 5 and y.step == -1)

    a = [0,1,2,3,4,5]
    
    b = a[x]
    assert(b == [5, 4])

    c = a[y]
    assert(c == [])


def test_shift_slice_4():
    x = slice(-1, 3, -1)
    y = shift_slice(x, 2)
    assert(y.start == None and y.stop == 5 and y.step == -1)

    a = [0,1,2,3,4,5]
    
    b = a[x]
    assert(b == [5, 4])

    c = a[y]
    assert(c == [])


def test_shift_slice_5():
    x = slice(1, 3, 1)
    y = shift_slice(x, -2)
    assert(y.start == None and y.stop == 1 and y.step == 1)

    a = [0,1,2,3,4,5]
    
    b = a[x]
    assert(b == [1, 2])

    c = a[y]
    assert(c == [0])


def test_shift_slice_6():
    x = slice(1, 3, 1)
    y = shift_slice(x, -3)
    assert(y.start == y.stop and y.step == 1)

    a = [0,1,2,3,4,5]
    
    b = a[x]
    assert(b == [1, 2])

    c = a[y]
    assert(c == [])
