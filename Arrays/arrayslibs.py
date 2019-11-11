import copy

A = list(range(10))


if __name__ == "__main__":

    print('General')
    print(len(A))
    print(A)
    A.append(2)
    print(A)
    A.remove(1)
    print(A)
    A.insert(1,3)
    print(A)

    print(2 in A)

    print('Copy')
    #copy, copies the refrence, but deep copy copies the object
    B = copy.copy(A)
    C = copy.deepcopy(A);

    print(B)
    print(C)

    print('Sorting')
    #A.sort() sorts the array in place, while sorted() returns a sorted copy
    A.sort()
    C = sorted(B)
    print(A)
    print(C)

    print('Reverse')
    #A.reverse() is in place reverse
    A.reverse()
    print(A)

    print('Slicing')
    print(A[2:4])
    print(A[2:])
    print(A[:1])
    print(A[:-1])
    print(A[-2:])
    print(A[-3:-1])
    print(A[1:5:2])
    print(A[::-1])