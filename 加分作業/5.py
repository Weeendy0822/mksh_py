#選擇敘述撰寫,判斷它是否為閏年（leap year）或平年
#每四年一閏，每百年不閏，但每四百年也一閏
f=int(input('輸入西元年份:'))
if f%400 == 0:
    print(f,'是閏年')#每四百年一閏
elif f%100 == 0:
    print(f,'不是閏年') #每百年不閏
elif f%4 == 0:
    print(f,'是閏年') #每四年一閏   
else:
   print(f,'是平年')#平年    
    
    