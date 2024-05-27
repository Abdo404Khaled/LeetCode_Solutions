class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        words = {}
        res = []
        for name in names:
            if name not in words:
                words[name] = 1
                res.append(name)
            else:
                k = words[name]
                
                while "{}({})".format(name, str(k)) in words:
                    k += 1
                words["{}({})".format(name, str(k))] = 1
                res.append("{}({})".format(name, str(k)))
                words[name] = k + 1
        
        return res
        