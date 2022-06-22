class Solution:
    def calPoints(self, ops: List[str]) -> int:
        st = []
        
        for i in ops:
            if i == "+":
                st.append(st[-1] + st[-2])
            elif i == "D":
                st.append(2*st[-1])
            elif i == "C":
                st.pop()
            else:
                st.append(int(i))
            
        return sum(st)
