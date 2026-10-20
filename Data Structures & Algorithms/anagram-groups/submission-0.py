class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matches = {}

        for i in range(len(strs)):
            sortedString = "".join(sorted(strs[i]))
            if sortedString in matches:
                matches[sortedString].append(i)
            else:
                matches[sortedString] = [i]

        output = []

        for key in matches:
            group = []

            for value in matches[key]:
                group.append(strs[value])

            output.append(group)
        
        return output
