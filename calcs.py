import math


class Calculate():
    def __init__(self, list_nums, percentile):
        self.list_nums = list_nums
        self.percentile = percentile

    def calculate_percentile(self):
        # locator
        locator = (self.percentile / 100) * len(self.list_nums)
        # if float or not... if float take ceiling... if not take mean to xn/2 and xn+1/2
        if locator % 1 != 0:
            locator_round = math.ceil(locator)
            equation_percentile = self.list_nums[locator_round - 1]
            return f"{self.percentile} percentile is {equation_percentile}"
        elif locator % 1 == 0:
            ans_float = (self.list_nums[locator - 1] + self.list_nums[locator]) / 2
            return f"{self.percentile} percentile is {ans_float}"

    def calculate_q(self):

        # locators for each mark

        locator_1 = (self.percentile / 100) * len(self.list_nums)

        # same if functionality as above

        if locator_1 % 1 != 0:

            l_1 = math.ceil(locator_1)

            q = self.list_nums[l_1 - 1]

            return q

        elif locator_1 % 1 == 0:

            # return percentile

            q_int = (self.list_nums[math.floor(locator_1) - 1] + self.list_nums[math.floor(locator_1)]) / 2
            return q_int

