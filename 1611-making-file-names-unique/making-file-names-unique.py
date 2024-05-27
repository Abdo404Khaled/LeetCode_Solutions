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
                new_name = "{}({})".format(name, str(k))
                while new_name in words:
                    k += 1
                    new_name = "{}({})".format(name, str(k))

                words[new_name] = 1
                words[name] = k + 1
                res.append(new_name)
        
        return res
        