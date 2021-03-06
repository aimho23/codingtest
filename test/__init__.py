a = [input()]

b == ["1","2","3","4","5","6","7","8"]
if b == a :
    print("ascending")

elif b == a.reverse() :
    print("descending")

elif b != a:
    print("mixed")
