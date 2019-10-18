
#np.split(arrayName, num)
#num times split

#np.split(arrayName,[num1,num2])

#split first num1 elements second subarray num1 to num2 and then remaining print as it is
# 1 2 3 4 5 6 7 8 9 10
#np.split(arr,[3,9]) means  (1,2,3) (4,5,6,7,8,9) and then remaining is (10)
x = np.arange(9)

#split 3 elements each 
print(np.split(x, 3))

#[array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]

#split first 3 and then 3 to 7 and then remaining print as it is
print(np.split(x,[3,7]))
#[array([0, 1, 2]), array([3, 4, 5, 6]), array([7, 8])]
                         


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
