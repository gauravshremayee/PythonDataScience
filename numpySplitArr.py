
x=[1,2,3,99,99,3,2,1] 
x1, x2, x3 = np.split(x, [3, 5])
print(x1, x2, x3) 
#[1 2 3] [99 99] [3 2 1]
#Notice that N split points lead to N + 1 subarrays. The related functions np.hsplit and np.vsplit are similar:
grid = np.arange(16).reshape((4, 4))
            
#array([[ 0,  1,  2,  3],
#                   [ 4,  5,  6,  7],
#                   [ 8,  9, 10, 11],
#                    [12, 13, 14, 15]])

upper, lower = np.vsplit(grid, [2]) print(upper)
print(lower)
