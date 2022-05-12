class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        pt = {")":"(","}":"{","]":"["}
        
        for i in s:
            if i in pt:
                if st and st[-1] == pt[i]:
                    st.pop()
                else:
                    return False
            else:
                st.append(i)
                
        return True if not st else False
        
