import time
import multiprocessing
#======================================Singlemode====================================================
def factorize(*number):

    lst2 = []
    for i in number:
        lst = []
        for j in range(1, i + 1):
            if i % j == 0:
                lst.append(j)
            if i == j:
                break
        lst2.append(lst)
    return lst2

x1 = time.time()
a, b, c, d = factorize(128, 255, 99999, 10651060)
print (time.time()- x1)


assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395,
             532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]


#===============================Multimode===============================================================
def mulfactorize(*numbers):

    ls = []
    ls2 = []
    for i in numbers:        
        for j in range(1, i + 1):
            if i % j == 0:
                ls.append(j)
            if i == j:
                break
        ls2.append(ls)
    return ls


w = x = y = z = None

if __name__ == '__main__':    
    pool = multiprocessing.Pool(processes=2) 
    y1 = time.time()    
    w, x, y, z = pool.map(mulfactorize, (128, 255, 99999, 10651060))    
    print (time.time()- y1)


assert w == [1, 2, 4, 8, 16, 32, 64, 128]
assert x == [1, 3, 5, 15, 17, 51, 85, 255]
assert y == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert z == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395,
             532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

        
        
