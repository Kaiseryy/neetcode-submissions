class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
               strsS = ''.join(sorted(s))
               res[strsS].append(s)
        return list(res.values())

        
     
        
     