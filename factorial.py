facto=lambda x: 1 if x==0 else x*facto(x-1)
print(facto(3))
