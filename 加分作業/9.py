#迴圈敘述，讓使用者輸入兩個正整數 a、b（a < b），利用迴圈計算從 a 開始連加到 b 的總和
a=int(input('輸入正整數(小)'))
b=int(input('輸入正整數(大)'))
s=0
for i in range(a,b+1):#起始值,終點值
    s+=i
print(s)    


