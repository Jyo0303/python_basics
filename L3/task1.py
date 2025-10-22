dic = {"(": ")", "[": "]", "{": "}"}
        temp = []

        for ch in s:
            if ch in dic:  
                temp.append(ch)
            else: 
                if not temp or dic[temp[-1]] != ch:
                    return False
                temp.pop()

        return len(temp) == 0
