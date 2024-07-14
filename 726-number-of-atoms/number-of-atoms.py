class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n=len(formula)
        stack=[]
        count=defaultdict(lambda:0)
        c=""
        s=""
        for i in reversed(formula):
            if i.isdigit():
                c=i+c
            elif i==')':
                if c:
                    if not stack:
                        stack.append(int(c))
                    else:
                        top=stack[-1]
                        stack.append(top*int(c))
                    c=""
            elif i=="(":
                if stack:
                    stack.pop()
            elif i.islower():
                s=i+s
            else:
                s=i+s
                if c:
                    if stack:
                        count[s]+=int(c)*stack[-1]
                    else:
                        count[s]+=int(c)
                    c=""
                                                
                else:
                    if stack:
                        count[s]+=stack[-1]
                    else:
                        count[s]+=1
                s=""
        ans=""
        for i in sorted(count):
            if count[i]>1:
                ans+=i+str(count[i])
            else:
                ans+=i
        return ans            