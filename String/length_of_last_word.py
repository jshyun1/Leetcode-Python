def lengthOfLastWord(s: str):
    s= s.strip()
    list = s.split(' ')
    return len(list[-1])

