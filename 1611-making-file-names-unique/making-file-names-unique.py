class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        words = defaultdict(int)
        res = []
        for name in names:
            if name not in words:
                words[name] = 1
                res.append(name)
            else:
                k = 1
                while f"{name}({k})" in words:
                    k += 1
                words[f"{name}({k})"] = 1
                res.append(f"{name}({k})")
        
        return res