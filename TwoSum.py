import random
import time
import timeit

from tqdm import tqdm

random_numbers = random.sample(range(500), 250)
targeted = random.randint(0,6000)
print(random_numbers)
print(targeted)
nums = []

class Solution_1:
    def twoSum_brute_data_draft(self, nums: list[int], target: int) -> list[int]:
        """
        Function responsible for take given values of nums and target
        iterate trough them checking for each valuew if the sum of 
        them is equal to the target value.
        """
        print("twoSum_brute_data_draft")
        start_time = time.time()
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return([i,j])
        end_time = time.time()
        execution_time = end_time - start_time
        print(execution_time)

    def better_solution_data_draft(self, nums: list[int], target: int) -> list[int]:
        """
        Function responsible for take given values of nums and target
        iterate trough them checking for each valuew if the sum of 
        them is equal to the target value. This Uses Dict and is not by brute force.
        """
        print("Better Solution, bight memory usage.")
        start_time = time.time()
        seen = {}

        for i, num in enumerate(nums):
            if target - num in seen:
                return(seen[taerget - num, i])
            elif num not in seen: 
                seen[num] = i

        print(nums)
        print(target)
        print(f"This was List: { nums }")
        print(f"This was target: { target }")
        print(f"this is solution: { seen }")
        if seen == []:
            print("no solution possible.")
        end_time = time.time()
        execution_time = end_time - start_time
        print(execution_time)


    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Function responsible for take given values of nums and target
        iterate trough them checking for each valuew if the sum of 
        them is equal to the target value.
        """
        print("Standard Solution")
        start_time = time.time()
        a=[]
        print(nums)
        print(target)
        for i in tqdm(range(len(nums))):
            for j in range(i+1):
                if nums[i]+nums[j]==target:
                    a.append(i)
                    a.append(j)
                    break
                else:
                    time.sleep(0.0001)
                    continue

        print(f"This was List: { nums }")
        print(f"This was target: { target }")
        print(f"this is solution: { a }")
        if a == []:
            print("no solution possible.")
        end_time = time.time()
        execution_time = end_time - start_time
        print(execution_time)

brute = Solution_1()
brute.twoSum(random_numbers, targeted)


data_draft_brute = Solution_1()
data_draft_brute.twoSum_brute_data_draft(random_numbers, targeted)

data_draft_brute.better_solution_data_draft(random_numbers, targeted)git 
