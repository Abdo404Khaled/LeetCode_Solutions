class Solution(object):
    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        count=collections.defaultdict(int)
        total=0
        count[0]=1
        cur=0
        for idx,c in enumerate(word):
            ci=ord(c)-ord('a')
            cur^=(1<<ci)
            total+=count[cur]
            count[cur]+=1
            for i in range(10):
                d=cur^(1<<i)
                total+=count[d]
        return total        