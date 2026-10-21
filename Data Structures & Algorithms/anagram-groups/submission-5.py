class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sublist = []
        answer = []
        for i in range(0, len(strs)):
            ana = ''.join(sorted(strs[i]))
            if ana not in sublist:
                sublist.append(ana)
                answer.append([strs[i]])
            else:
                index = sublist.index(ana)
                answer[index].append(strs[i]) 
        return answer