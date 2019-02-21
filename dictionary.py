d ={'a' : 1,'b' : 2,'c' :3}
for key in d:
    print(key, d[key])
print(d)
print(d.get("f","bar"))
print(d.setdefault("f","bar"))
print(d)
