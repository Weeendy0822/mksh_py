#使用者輸入一個十進位整數 num(0 ≤ num ≤ 15)，將 num 轉換成十六進位值
#轉換規則 = 十進位 0~9 的十六進位值為其本身，十進位 10~15 的十六進位值為 A~F
f=int(input('輸入一個十進位整數:'))
if f >= 0 and f <= 15:
    print(f)#本身
elif f == 10:
    print('A')
elif f == 11:
    print('B')
elif f == 12:
    print('C')
elif f == 13:
    print('D')
elif f == 14:
    print('E')
elif f == 15:
    print('F')






