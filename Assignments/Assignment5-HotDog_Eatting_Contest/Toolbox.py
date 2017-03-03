def userInt(prompt):
    print prompt,
    num = int(raw_input())
    
    return num
    
def userFloat(prompt):
    print prompt,
    f = float(raw_input())
    
    return f
    
def userString(prompt):
    print prompt,
    s = raw_input()
    
    return s
    
def userList(prompt):
    print promt,
    l = raw_input().split(",")
    return l
    
def kmToMi(km):
    return 0.62 * km
