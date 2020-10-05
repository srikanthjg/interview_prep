class Solution(object):


    def __init__(self):
        self.output = []
        self.charDict = {}
        self.charDict[2] = "abc"
        self.charDict[3] = "def"
        self.charDict[4] = "ghi"
        self.charDict[5] = "jkl"
        self.charDict[6] = "mno"
        self.charDict[7] = "pqrs"
        self.charDict[8] = "tuv"
        self.charDict[9] = "wxyz"

    def getChars(self, digit):
        if digit in self.charDict:
            return self.charDict[digit]

    def LCHelper(self, str_list):

        print "called with str_list: %r"%str_list
        list_lens = [len(i) for i in str_list]
        #print list_lens
        multi_char_index = -1
        is_base = True
        for i in range(len(list_lens)):
          if list_lens[i] > 1:
            is_base = False
            multi_char_index = i
            break

        if is_base:
          #print "%r"%str_list
          self.output.append("".join(str_list))
          return

        #print "multi_char_index: %d"%multi_char_index


        for i in str_list[multi_char_index]:

            new_ele = []
            new_ele.append(i)

            new_list = str_list[:multi_char_index] + new_ele + str_list[multi_char_index+1:]

            print new_list
            self.LCHelper(new_list)



    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        nums = list(digits)

        str_list = []
        for n in nums:
            str_list.append(list(self.getChars(int(n))))

        print(str_list)

        self.LCHelper(str_list)
        print self.output
        return self.output


class Solution1:
    output = []
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if digits:
            self.backtrack("", digits)
        return self.output

    def backtrack(self,combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                self.output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map
                # the next available digit
                for letter in self.phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    self.backtrack(combination + letter, next_digits[1:])




#sol= Solution()
#sol.letterCombinations("23")
sol1= Solution1()
print sol1.letterCombinations("234")
