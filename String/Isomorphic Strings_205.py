class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):     
            return False    
        s_map = {}
        t_map = {}
        for s_char,t_char in zip(s,t):
            if (s_char not in s_map) and (t_char not in t_map):
                s_map[s_char] = t_char
                t_map[t_char] = s_char
            elif s_map.get(s_char)!=t_char and t_map.get(t_char)!=s_char: 
                return False
        return True
