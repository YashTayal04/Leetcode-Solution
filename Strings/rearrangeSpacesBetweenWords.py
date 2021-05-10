class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces=0
        word=0
        for i in range(len(text)):
            if text[i]==' ':
                spaces+=1
            else:
                if i==0 or text[i-1]==' ':
                    word+=1 
        ans=""
        if word==1:
            for i in text:
                if i!=" ":
                    ans+=i
            for i in range(spaces):
                ans+=" "
            return ans
        else:
            s=spaces//(word-1)
            for i in range(len(text)):
                if text[i]!=" ":
                    if len(ans)==0 or text[i-1]!=" ":
                        ans+=text[i]
                    else:
                        for j in range(s):
                            ans+=" "
                        ans+=text[i]
            for i in range(spaces%(word-1)):
                ans+=" "
            return ans
                    