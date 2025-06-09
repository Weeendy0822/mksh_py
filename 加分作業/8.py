#選擇敘述，輸入三個邊長，是否可以組成一個三角形。若可以，則輸出該三角形之周長；否則顯示【Invalid】。 提示：檢查方法 = 任意兩個邊長之總和大於第三邊長
a=int(input('輸入三角形1邊長:'))
s=int(input('輸入三角形1邊長:'))
d=int(input('輸入三角形1邊長:'))
if (a+s)>d and (a+d)>s and (s+d)>a :#任意兩個邊長之總和大於第三邊長
    print('三角形周長:',a+s+d)
else:
    print('【Invalid】')



