dict1 = {}
print("dict1 = ",dict1)

dict2 = {'key1':123,'name':"woo",'objKey':[1,2,3]}
print("dict2 = ",dict2)
for key in dict2.keys():
    print("key=%s, value=%s "%(key,dict2[key]))
#Your task will be to write a function can_be_composed(word1, word2) to check if word1 can be composed from word2 
# Example usages: • can_be_composed("python", "pantyhose") returns True • can_be_composed("python", "ponytail") returns False • can_be_composed("code", "docent") returns True • can_be_composed("messy", "reassembly") returns True • can_be_composed("computational", "alphanumeric") returns False • can_be_composed("linguistics", "criminologists") returns False
def can_be_composed(word1,world2):
    for i in word1:
        if i in world2:
            world2 = world2.replace(i,"",1)
            continue
        else:
            return False
    return True

def reverse(x):
    ret = 0
    if x < 0:
        flag = -1
        x = abs(x)
    else:
        flag = 1
    while x != 0:
        ret = ret * 10
        if ret*flag < - 2**31 or ret*flag > 2**31-1:
            return 0
        ret = ret + x % 10
        x = x // 10
    return ret*flag

w1 = "python"
w2 = "pantyhose"
w3 = "ponytail"
w4 = "hello"
w5 = "helpos"
w6 = "kellyoh"
print(can_be_composed(w1,w2))
print(can_be_composed(w1,w3))
print(can_be_composed(w4,w5))
print(can_be_composed(w4,w6))


print(reverse(-123))
