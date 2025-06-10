#請使用迴圈敘述撰寫一程式，要求使用者輸入一個正整數 n（n<10），顯示 n*n 乘法表。
#每個運算子及運算元輸出的欄寬為 2，而每項乘積輸出的欄寬為 4，皆靠左對齊不跳行
a = int(input('輸入一個正整數 n（n<10）:'))
if a<10:
    for i in range(1,a+1):#起始值,終止值
        for j in range(1,a+1):
            print("{:<2}*{:<2}={:<4}".format(j,i,i*j),end="")#課本p32
        print()
else:
    print('不能')