class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for c in tokens:
            if c == '+':
                st.append(st.pop() + st.pop())
            elif c == '*':
                st.append(st.pop() * st.pop())
            elif c == '-':
                a,b = st.pop() , st.pop()
                st.append(b - a)
            elif c == '/':
                a,b = st.pop() , st.pop()
                st.append(int(b / a))
            else:
                st.append(int(c))
        return st[-1]
