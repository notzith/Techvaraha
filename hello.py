arr1 = [1, 2, 3, 7, 5]
n1, s1 = 5, 12


def subArraySum(arr, n, s):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            print(i,j)
            arrb = arr[i:j:]
            c = sum(arrb)
            if s == c:
                return(str(i)+" "+str(j))


print(subArraySum(arr1, n1, s1))
