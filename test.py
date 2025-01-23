num = 10 ** 5
num = str(num)
print(num)

l = {"1":5, "1":6}

print(l.keys())

print(list(num)[0])

dict_test = {}

dict_test = dict(name = "john")
dict_test["name"] = dict(name="john")

print(dict_test)

arr = [1,2,3,4,5,1,7,8,11,9,15,20,16]

def function(a,b):
        # condition1 = a is not None
        condition2 = a == 5
        condition3 = a > b+1
        condition4 = a+3 > b+2
        if condition2 and condition3 and condition4:
            print("Passed")
            print(f"a==>{a} b==>{b}")
        else:
            print("Failed") 
            print(f"a==>{a} b==>{b}")

for i in range(len(arr) - 1):
    function(arr[i], arr[i+1])