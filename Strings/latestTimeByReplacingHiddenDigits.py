class Solution:
    def maximumTime(self, time: str) -> str:
        ans=""
        if time[0]=='?':
            if time[1]=='?':
                ans+='23'
            else:
                if time[1]<='3':
                    ans+='2'
                else:
                    ans+='1'
                ans+=time[1]
        else:
            ans+=time[0]
            if time[1]=='?':
                if time[0]=='2':
                    ans+='3'
                else:
                    ans+='9'
            else:
                ans+=time[1]
        ans+=':'
        if time[3]=='?':
            ans+='5'
        else:
            ans+=time[3]
        if time[4]=='?':
            ans+='9'
        else:
            ans+=time[4]
        return ans