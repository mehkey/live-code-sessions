import unittest

def find_array_quadruplet(arr, s):
    '''
    Approach 1: 4 Loops

    O(N^4)

    Approach 2: 3 Loops + Binary Search

    O(N^3 Log N)


    Approach 3: 2 Loops + 2 Pointers + Sort

    O(N^3)

    '''
    kuplut = Kuplets(4)

    return kuplut.kuplet_find(arr,s)

class Kuplets:

    def __init__(self, k):
        self.k = k

    def kuplet_find(self, arr, s):
        arr.sort()

        return self.kuplet_k(arr, [] , 0, s, self.k)

    def kuplet_k(self, arr, cur, start, s, k):
        

        #print(cur)
        if k == 2:

            l = start

            r = len(arr) -1

            while l < r:

                if arr[l] + arr[r] == s:
                    cur.append(arr[l])
                    cur.append(arr[r])
                    return cur
                elif arr[l] + arr[r] < s:
                    l += 1
                else:
                    r -= 1
            
            return cur
        else:

            for i in range(start, len(arr)):

                cur.append(arr[i])

                res = self.kuplet_k(arr, cur, i + 1, s - arr[i], k-1 )

                if len(res) == self.k:
                    return res

                cur.pop()
        
        return []


class TestKuplets(unittest.TestCase):


    def test_default(self):
        kuplut = Kuplets(4)

        res = kuplut.kuplet_find([2, 7, 4, 0, 9, 5, 1, 3],20)

        self.assertEqual(res , [0, 4, 7, 9] )


#unittest.main(verbosity=2)