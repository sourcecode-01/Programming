class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        
        chartoWord = {}
        wordtoChar = {}
        
        for p,w in zip(pattern, words):
            if p in chartoWord and chartoWord[p] != w:
                return False
            if w in wordtoChar and wordtoChar[w] != p:
                return False
            chartoWord[p] = w
            wordtoChar[w] = p
            
        return True
