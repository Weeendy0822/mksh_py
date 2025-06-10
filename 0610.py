def fab(a):
    if a == 0:return 0
    if a == 1:return 1
    return fab(a-1)+fab(a-2)
for i in range(20):
    print(fab(i), ' ', end='')
    