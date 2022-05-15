class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        
        for i in s:
            if st and st[-1][0 ] == i:
                st[-1][1] += 1
                if st[-1][1] == k:
                    st.pop()
            else:
                st.append([i,1])
        
        return ''.join(char * count for char,count in st)
