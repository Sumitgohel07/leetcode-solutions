class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        dict_p = dict()
        for i in range(len(p)):
            dict_p[p[i]] = dict_p.get(p[i],0) + 1

        ws = len(p)
        dict_s = dict()
        left = 0
        op = []
        for right in range(len(p)):
            dict_s[s[right]] = dict_s.get(s[right],0) + 1
        if dict_s == dict_p:
            op.append(left)
        for right in range(len(p),len(s)):
            dict_s[s[left]]-=1
            if dict_s[s[left]]==0:
                del dict_s[s[left]]
            left+=1

            dict_s[s[right]] = dict_s.get(s[right],0) + 1

            if dict_s == dict_p:
                op.append(left)
        return op  
            
            

