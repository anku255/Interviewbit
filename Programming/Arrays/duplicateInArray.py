class Solution():
    # def repeatedNumber(self, A):
    #     hashMap = [0 for _ in range(len(A) + 1)]

    #     for i in A:
    #         if hashMap[i] == 1:
    #             return i
    #         else:
    #             hashMap[i] = 1
    #     return -1

    def repeatedNumber(self, A):
        s = sum(A)
        n = len(A)
        missing = s - (n*(n-1))/2
        return missing


s = Solution()
arr = [3, 4, 1, 4, 1]

print(s.repeatedNumber(arr))
