class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        
        for num in nums:
            if(num in elements):
                elements[num] = elements[num] + 1
            else:
                elements[num] = 1
        

        temp = sorted(elements, key = elements.get, reverse = True)

        output = []

        for i in range(k):
            output.append(temp[i])
        
        return output
