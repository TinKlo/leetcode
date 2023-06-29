import random
from tqdm import tqdm

random_numbers = random.sample(range(500), 250)
targeted = random.randint(0,6000)
print(random_numbers)
print(targeted)
nums = []

class Solution_1:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
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
                    continue

        print(f"This was List: { nums }")
        print(f"This was target: { target }")
        print(f"this is solution: { a }")
        if a == []:
            print("no solution possible.")

samples = Solution_1()

samples.twoSum(random_numbers, targeted)
