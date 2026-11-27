#python中的數學運算符號應用

apples = 1
apples = apples + 1 #在apples的基礎值1上面再加一次1 python會輸出結果為2
apples += 1 #使用簡化符號去執行相同的加法程序(+=)

orages = 1
orages = orages * 2
orages *= 2 #使用簡化符號去執行相同的乘法程序(*=)

bananas = 1
bananas = bananas / 1
bananas /= 1 #使用簡化符號去執行相同的除法程序(/=)

#指數 (平方/三次方)
water = 2
water = water ** 2 #在water的基礎上乘以water基礎數的2次方
water **= 2 #使用簡化符號去執行相同的方程程序(**=)

water = water ** 3 #在water的基礎上乘以water基礎數的3次方
water **= 3 #使用簡化符號去執行相同的方程程序(**=)

#模數 mod % (與除法不同的是模數是專門計算餘數的除法程式)
print (10 % 3) #10除以3會得餘數為1 所以使用10 % 3得出的數字為1 python就會輸出餘數1
print (11 % 3)
print (12 % 3)

#python內置數學函數

#次方 pow
print (pow(3,2)) #與前面的**是相同的意思 只不過pow可以直接使用在print裡直接計算完輸出

#最大值 Max 與最小值 Min
x3 = 1
y3 = 2
z3 = 3
print (max(x3,y3,z3)) #使用max語法去取得x3,y3,z3中的最大值
print (min(x3,y3,z3)) #使用min語法去取得x3,y3,z3中的最小值

#四捨五入 round
x4 = 3.14159265
y4 = 6.66666666
print (round(x4)) #因為使用round這個語法所以輸出的數字會四捨五入
print (round(y4))

#絕對值 abs
a = -666
b = 777
print ("絕對值:",abs(a))
print ("絕對值:",abs(b))

#python的數學模塊
#四捨五入 round, 無條件進位 math.ceil, 無條件捨去 math.floor
import math #因為無條件進位/無條件捨去都是使用math模塊的語法 所以要先在python中載入 "math"
c = 777.666
print (math.ceil(c)) #math模塊的無條件進位語法
print (math.floor(c)) #math模塊的無條件捨去語法
print (round(c)) #因為round這個語法是python內建的所以不需要使用到math模塊

#圓周率 π math.pi 圓周率一樣需要使用到math語法
print (math.pi)

#計算圓的周長 2πR
print ("歡迎來到最強的圓周長計算機")
radius = float(input("請輸入圓的半徑:"))
perimeter = 2 * math.pi * radius
print (f"圓的周長等於:{round(perimeter,2)}")

#計算圓的面積 πR²
print ("歡迎來到最強的圓面積計算機")
radius2 = float(input("請輸入圓的半徑:"))
area = radius2 ** 2 * math.pi
print (f"圓的面積等於:{round(area,2)}")