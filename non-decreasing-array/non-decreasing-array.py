class Solution(object):
    def checkDecreasing(self , checklist ):# return true if delta one element will lead to a non-decreasing array
        problemcont = 0
        # for idx , val in enumerate(checklist):
        #     if idx + 1 < len (checklist):
        #         if val > checklist[idx + 1]:
        #             problemcont += 1
        #             checklist[idx] = checklist[idx + 1]        
        for idx in range(0 , len(checklist)-1):
            if idx + 1 < len (checklist):
                if checklist[idx] > checklist[idx + 1]:
                    problemcont += 1
                    checklist[idx] = checklist[idx + 1]
        if problemcont > 1:
            return False
        else:
            return True


mylist = [1 , 1, 1, 2, 3, 4 , 4 , 3 , 3, 6]
solution = Solution()
print solution.checkDecreasing(mylist)