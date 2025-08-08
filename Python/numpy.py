import Python.numpy as np

#print(np.__version) #to check version

#create a list of number in python
#my_list = [1, 2, 3, 4] ## [1, 2, 3, 4]
#my_list = my_list * 2 ## [1, 2, 3, 4, 1, 2, 3, 4]
#print(my_list)

#numpy array is faster
#array = np.array([1, 2, 3, 4]) ## [1 2 3 4]
#array = array * 2 ## [2 4 6 8]
#print(type(array)) ## <class 'numpy.ndarray'>
#print(array)

###########################
#Multi dimensational in numpy
#array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']], ## layer 0
#                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']], ## layer 1
#                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]]) ## layer 2
#print(array.ndim) ## 3
#print(array.shape) ## (3, 3, 3)

#Multidimensional indexing is faster than chain indexing
#print(array[layer, row, column])
#print(array[2, 0, 2]) # U

#string concantation with multidimensatinal array
#word = array[0, 0, 0] + array[2, 0, 0] + array[2, 0, 0] ## ASS

############################
#SLICING
#array = np.array([[1, 2, 3, 4],
#                  [5, 6, 7, 8],
#                  [9, 10, 11, 12],
#                  [13, 14, 15, 16]])
# array[start:end(exclusive):step]
# array[row, column]
#print(array[2:, 2:]) ## [[11 12] [15 16]]

############################
#ARITHMETIC

#array = np.array([1, 2, 3])

#Scalar arithmetic
#linear algebraic terms, basically a single value

#print(array + 1) ## [2 3 4]
#print(array - 2) ## [-1  0  1]
#print(array * 3) ## [3 6 9]
#print(array / 4) ## [0.25 0.5  0.75]
#print(array ** 5) ## [  1  32 243]

#Vectorized math funcs
#another linear algebra term, a vector is a single dimension such as 1D list
#whereas in a scalar is a single value
#we can apply a function to an entire array without a loop

#print(np.sqrt(array))
#print(np.ceil(array))
#print(np.pi)

# EXERCISE
#radii = np.array([1, 2, 3])
#print(np.pi * radii ** 2)

#Elemet-wise arithmetic
#can apply operation between single elements between arrays
#array1 = np.array([1, 2, 3])
#array2 = np.array([4, 5, 6])

#print(array1 + array2) ## [5 7 9]
#print(array1 - array2) ## [-3 -3 -3]
#print(array1 * array2) ## [ 4 10 18]
#print(array1 / array2) ## [0.25 0.4  0.5 ]
#print(array1 ** array2) ## [  1  32 729]

#Comparison operators
#we can create boolean arrays, filter data, use elementwise comparisons

#scores = np.array([91, 55, 100, 73, 82, 64])
#scores[scores < 60] = 0
#print(scores)

############################
#BROADCASTING
# broadcasting allows NumPy to perform operaation on arrays
# with different shapes by virtually expanding dimensions
# so they match the larger array's shape.

# the dimensions have the same size
# OR
# one of the dimensions has a size of 1

#array1 = np.array([[1, 2, 3, 4],
#                   [5, 6, 7, 8],
#                   [9, 10, 11, 12],
#                   [13, 14, 15, 16]])
#array2 = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
#print(array1.shape)
#print(array2.shape)
#print(array1 * array2)

#EXERCISE
#array1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
#array2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

#print(array1.shape)
#print(array2.shape)
#print(array1 * array2)

############################
#AGGREGATE FUNCTIONS

# aggregate functions  = summarize data and typically
#                       return a single value

#array = np.array([[1, 2, 3, 4, 5],
#                  [6, 7, 8, 9, 10]])

#print(np.sum(array))
#print(np.mean(array))
#print(np.std(array))
#print(np.var(array))
#print(np.min(array))
#print(np.max(array))
#print(np.argmin(array))
#print(np.argmax(array))
#print(np.sum(array, axis=1))

############################
#FILTERING
# refers to the process of selecting elements from an array that match a given condition

#ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
#                 [39, 22, 15, 99, 18, 19, 20, 21]])

#teenagers = ages[ages < 18]
#adults = ages[(ages >= 18) & (ages < 65)]
#seniors = ages[ages >= 65]
#evens = ages[ages % 2 == 0]
#odds = ages[ages % 2 != 0]
#print(odds)

#np.where(conditions, array, fill value
#adults = np.where(ages >= 18, ages, 0)
#print(adults)

############################
#RANDOM NUMBERS

#rng = np.random.default_rng() ## only set seed if wanna reproduce the same result
#print(rng.integers(low = 1, high = 101, size = (3, 2)))

#Floating point
#np.random.seed(seed=1)
#print(np.random.uniform(low = -1, high = 1, size = (3, 2)))

#Shuffling an array

rng = np.random.default_rng()
#array = np.array([1, 2, 3, 4, 5])
#rng.shuffle(array)
#print(array)

#Random Choice
fruits = np.array(["🍎", "🍊", "🍌", "🥥", "🍍"])
fruits = rng.choice(fruits, size = (3, 3))
print(fruits)