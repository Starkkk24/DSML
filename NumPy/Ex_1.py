import numpy as np

arr1 = np.random.random((3,3))
# print(arr1.shape)
arr2 = np.array(([3,1,5], [2,6,7], [9,0,8]))
print(arr2.shape)

arr3 = np.array([1.1, 2.2, 3.3])
arr33 = arr3.astype("int32")
print(arr33)
print(arr33.dtype)
print(arr3.nbytes)

arr4 = np.arange(1,7)
# print(arr4)
print(f"Even in arr4:{arr4[[1,3,5]]}")

arr5 = np.zeros([9])
# print(arr5)
print(arr5.reshape(3,3))

arr6 = np.arange(0,65)
# print(arr6)
mask = arr6 > 50
print(arr6[mask]) 