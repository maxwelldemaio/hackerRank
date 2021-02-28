from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Make auxiliary array to store pascal triangle values
        arr = []
        for amount in range(1, numRows + 1):
            arr.append([0 for x in range(amount)])
        
        # Iterate through every line
        # and populate integer(s) in it
        for line in range(numRows):

            # Every line has number of
            # integers equal to line number
            for i in range(0, line + 1):
                # First and last values
                # in every row are 1
                if i == 0 or i == line:
                    arr[line][i] = 1
                # Other values are sum of values
                # just above and left of above
                else:
                    arr[line][i] =(arr[line - 1][i - 1] + arr[line - 1][i])
        return arr

