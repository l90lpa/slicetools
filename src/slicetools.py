def _canonicalize_slice(s) -> slice:
    step = 1 if s.step is None else s.step
    assert(step != 0)

    if step > 0 and s.start == 0:
        start = None
    elif step < 0 and s.start == -1:
        start = None
    else:
        start = s.start
    
    return slice(start, s.stop, step)


def mirror_slice(s) -> slice:
    """mirror_slice: returns a slice that is the mirror of the input slice. A mirrored slice 
    represents those elements that are the mirror - about the center of the array - of those 
    of the input slice.
    
    For example, suppose we have,
    
    `x = slice(None, 2, 1)`,

    then the mirrored slice is,

    `y=slice(None,-3,-1)`

    To get a better intutition for how `x` and `y` are different, let,

    `a = [0,1,2,3,4,5,6]`

    Then, `a[x] = [0,1]` while `a[y] = [6,5]`
    """
    s = _canonicalize_slice(s)
    assert(s.start != 0 and s.start != -1 and s.step != 0)

    step = -s.step

    adjustment = step // abs(step)

    return slice(-s.start + adjustment if s.start is not None else None,
                 -s.stop  + adjustment if s.stop  is not None else None,
                 step)


def reverse_slice(s) -> slice:
    """reverse_slice: returns a slice that is the reserve of the input slice. A reversed slice 
    represents the same part of an array but accessed in reverse order.
    
    For example, suppose we have,
    
    `x = slice(None, 2, 1)`,

    then the reversed slice is,

    `y=slice(1,None,-1)`

    To get a better intutition for how `x` and `y` are different, let,

    `a = [0,1,2,3,4,5,6]`

    Then, `a[x] = [0,1]` while `a[y] = [1,0]`
    """
    
    s = _canonicalize_slice(s)

    step = -s.step

    adjustment = step // abs(step)

    return slice(s.stop  + adjustment if s.stop  is not None else None,
                 s.start + adjustment if s.start is not None else None,
                 step)


def shift_slice(s, n) -> slice:
    """shift_slice: returns a slice that is the n-shifted slice of the input slice. A shifted slice
    is one that accesses elements that are positions away from those of the input slice. Some shifts
    can cause the slice to represent less elements than the input slice. For example if the input slice
    represents the whole array and a shift of n is applied then the resulting slice will represent n 
    less elements.
    
    For example, suppose we have,
    
    `x = slice(None, 2, 1)`,

    then the 3-shifted slice is,

    `y=slice(3, 5, 1)`

    To get a better intutition for how `x` and `y` are different, let,

    `a = [0,1,2,3,4,5,6]`

    Then, `a[x] = [0,1]` while `a[y] = [3,4]`
    """
    if n == 0:
        return s
    
    is_reversed = False
    if s.step is not None and s.step < 0:
        is_reversed = True
        s = reverse_slice(s)

    length = abs(n) + 1
    
    if s.start is not None:
        length += abs(s.start)

    if s.stop is not None:
        length += abs(s.stop)

    start = 0 if s.start is None else s.start
    start = start if start >= 0 else length - start
    
    stop = length if s.stop is None else s.stop
    stop = stop if stop >= 0 else length - stop

    start += n
    stop  += n

    if start < 1:
        start = None
    elif start >= length:
        return slice(0,0) # Empty slice
    
    if stop < 1:
        return slice(0,0) # Empty slice
    elif stop >= length:
        stop = None

    s = slice(start, stop, s.step)
    if is_reversed:
        s = reverse_slice(s)

    return s
