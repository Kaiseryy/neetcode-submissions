class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetop = { ")":"(","]":"[","}":"{"}

        for c in s:
            if c in closetop:

                if stack and stack[-1]== closetop[c]:
                    stack.pop()
                
                else:
                    return False
            
            else:
                stack.append(c)
        
        return True if not stack else False

                
            

        