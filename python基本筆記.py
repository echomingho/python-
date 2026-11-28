#字串+數字變數容器會產生錯誤 需要先將變數轉換成字串 str(math)
#integer(int) 整數 #float 浮點數(小數點) #string 字串(中文/可以把數字的變數容器轉換成字串)
age = 18
name = "米豪"
school = "僑光科技大學"
print (f"我的名字叫做 {name} 我今年 {age} 歲 我現在就讀 {school}") #print(f) f=帶入我們所創造的變數

#print ("我今年" + age) #因為我們的age這個變數是數字,再轉換成字串前無法跟字串相加,所以我們需要先將變數轉換成字串 str(age)

print("我今年" + str(age)) #用str將age轉換成字串之後就能夠做相加了

#boolean 布林值 布林值只有兩個值 一個是 "true(真)"" 一個是 "false(假)""
night = True #布林值的值第一個英文"一定要是大寫" 不然python會"不知道" 你是想使用"布林值還是只想新增一個容器變數"
print (f"現在是晚上嗎? {night}")

#type 是使用在"確認字組的型別" 例如你不知道這個容器是"字串"或是"浮點數" 你可以使用type去做確認
x = int(1)
y = float(1)
z = str("20個傻逼")
print (type (x)) #type顯示x這個容器為"int"
print (type (y)) #type顯示y這個容器為"float"
print (type (z)) #type顯示z這個容器為"str"

#型別轉換 分為"顯示" 以及 "隱示"

#顯示型別轉換範例如下:
x1 = 1 # x1為int
y1 = 1.0 # y1為float
z1 = "傻逼" # z1為str
xy = True # xy為bool

x1 = float (1) #將x1轉換成float型別
y1 = int (y1) #將y1轉換成int型別
z1 = bool (1) #將z1轉換成bool型別
xy = str (xy) #將xy轉換成str型別 "當布林值轉換成其他型別時 依然會繼續顯示True or False"

print (x1)
print (type (x1))
print (y1)
print (type (y1))
print (z1)
print (type (z1))
print (xy)
print (type (xy))

#隱示轉換是指在沒有宣告轉換的時候 電腦自動轉換型別 顯示轉換需要使用宣告 "x1 = int(x1)"

#隱示轉換範例如下:
x2 = 250
y2 = 20.5
x2 = x2/y2
print (x2)
print (type (x2)) #因為x2被重新宣告為x2/y2所以會繼承y2的flaot型別 這就是隱示轉換

#input 取得使用者輸入

#第一個範例 填詞遊戲:
print ("題目:我今天去了 (名詞) ,正在參觀的時候我看到非常 (形容詞) 的樹,當我正在觀看這顆非常 (形容詞) 的樹時,有個阿嬤 (動詞) 過來跟我說一句話,阿嬤:你是不是丟搞?")
noun = input("輸入一個名詞:")
adj = input("輸入一個形容詞:")
verb = input("輸入一個動詞:")
print (f"我今天去了一個{noun},正在參觀的時候我看到非常{adj}的樹,當我正在觀看這顆非常{adj}的樹時,有個阿嬤{verb}過來跟我說一句話,阿嬤:你是不是丟搞")

#第二個範例 數學計算 矩形面積:
print ("歡迎來到最強的計算機系統")
long = float(input("請輸入你要計算的矩形面積長度:")) #記得計算數學時要使用float去宣告為浮點數 使用者輸入的浮點數才不會被視作整數
width = float(input("請輸入你要計算的矩形面積寬度"))
area = long * width
print (f"你的矩形面積為 {area} 平方公分")

#第三個範例 購物系統:
buy = input("請輸入你今天想買的物品:")
price = float(input("請輸入這件商品的價格:"))
many = int(input("請輸入你需要購買幾件商品:"))
total = price * many
print (f"親愛的客戶您今天購買的商品為 {buy},您總共購買了 {many} 件商品,總價為 {total}")

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

#if else elif 控制流程
for_sale = True #for_sale如果為True那python會認定這件物品為真 如果為Flase則為假
if for_sale:
    print ("此項目正在售出")
else:
    print("此項目未開放售出")

#if else
#詢問是否年滿18系統
age = int(input("請輸入你的年齡:"))
if age < 18:
    print ("很抱歉您的年紀未達18周歲")
else:
    print("恭喜通過驗證您已經滿18周歲了!")   

#elif >= else if的簡寫 elif是使用在if else的判斷式不夠時所使用的額外判斷
age2 = int(input("請輸入您的年紀:"))
if age2 >= 100:
    print("您的年齡過大無法註冊此帳戶")
elif age2 >= 18:
    print ("您已經年滿18歲了,可以註冊此app帳戶")
elif age2 <= 0:
    print ("您輸入的年齡還未出生,請檢查後再次重新輸入")
else :
    print ("很抱歉您未滿18歲,無法註冊該帳戶")

#python 計算機練習程式
operator = (input("請輸入您今天使用的計算符號:"))
num1 = float(input("請輸入你想要計算的第一個數字:"))
num2 = float(input("請輸入你想要計算的第二的數字:"))
if operator == "-":
    answer = num1 - num2
elif operator == "+":
    answer = num1 + num2
elif operator == "*":
    answer = num1 * num2
elif operator == "/":
    answer = num1 / num2
else:
    print ("您輸入的計算符號是錯誤的,請重新檢查後再次輸入")

print (f"您的運算結果為:{answer})")

#python 體重轉換器
weight = float(input("請輸入您的體重:"))
unit = input("請輸入您的體重單位為公斤還是磅(KG/LB)").upper()
print (f"您輸入的體重為:{weight}{unit}")

if unit == "KG":
    weight *= 2.2
    new_unit = "LB(磅)"
elif unit == "LB":
    weight /= 2.2
    new_unit = "KG(公斤)"
else:
    print ("很抱歉無法計算,您輸入的單位錯誤")
    exit()

print (f"您的體重為: {round(weight)} {new_unit}")

#python 溫度轉換程式
unit1 = input("請輸入當前的溫度單位,華氏(F)或者攝氏(C):")
temperature = float(input("請輸入您想轉換的溫度:"))

if unit1 == "F":
    temperature = ((temperature - 32) * 5 / 9)
    print (f"您轉換後的溫度為: {temperature} C")
elif unit1 == "C":
    temperature = ((temperature * 9 / 5) + 32)
    print (f"您轉換後的溫度為: {temperature} F")
else:
    print("很抱歉,您的單位輸入錯誤,請確認後再次重新輸入")
    exit()

#python 中的邏輯運算子(運算符)

#and / or / not
temp = float(input("請輸入當前溫度:"))
unit2 = input("請輸入當前的溫度單位,為攝氏(C)或華氏(F):")
print (f"您輸入的溫度及單位為: {temp} {unit2}")

if temp >= 30 or temp<=0: #or的用法是只要左右兩邊有一個條件為true輸出就會等於true
    print (f"現在的溫度為:{temp} {unit2} , 現在的溫度不適宜出門!")
else:
    print (f"當前的溫度為: {temp} {unit2} , 現在的溫度適宜出門!")
    exit()

temp2 = float(input("請輸入當前溫度:"))
unit3 = input("請輸入當前的溫度單位,為攝氏(C)或華氏(F):")
print (f"您輸入的溫度及單位為: {temp} {unit3}")

if temp < 30 and temp>0: #and的用法是需要左右兩邊的條件都為true輸出才會等於true
    print (f"現在的溫度為:{temp} {unit2} , 現在的溫度適宜出門!")
else:
    print (f"當前的溫度為: {temp} {unit2} , 現在的溫度不適宜出門!")
    exit()

#python 字串方法

#`len()` , `find()` , `capitalize()` , `upper()` , `lower()` , `count()` , `replace()`

#help(str) 查詢所有字串

#使用者全名
name1 = "米豪 MiHao"

#查詢全名有幾個字元
length = len(name1)
print ("您的全名總共有",length,"個字元")

#查詢全名中的第一個空格
space_pos = name1.find (" ")
print ("你一個空格出現在第",space_pos,"個字元")

#capitalize() , upper() , lower() 函數用法

#capitalize 將字母的第一個單字轉換成大寫
name_capitalize = name1.capitalize()
print ("您的全名為:",name_capitalize,("第一個字為大寫"))

#upper 將所有英文字母轉換成大寫
name_upper = name1.upper()
print ("您的全名為:",name_upper,("全部轉換為大寫"))

#lower 將所有英文字母轉換成小寫
name_lower = name1.lower()
print ("您的全名為:",name_lower,("全部轉換成小寫"))

#count() , replace() 函數用法

#count 跟find不同的是 count可以找出一個字串裡總共有幾個你要找的字元
phone_num = str(input("請輸入您的電話號碼:"))
phone_count = phone_num.count("-") #尋找使用者輸入的電話號碼裡共有幾個 "-" 符
print ("您的電話號碼為:",phone_num,"總共有:",phone_count,"個-符")

#replace 將輸入者輸入後的字元轉換成另一個字元
phone_num1 = str(input("請輸入您的電話號碼:"))
phone_replace = phone_num1.replace(" ","-")
print ("您的電話號碼為:",phone_replace)

#程式練習:驗證使用者輸入的合法性
# - 您的使用者名稱不能超過 12 個字元
# - 您的使用者名稱不能包含空格
# - 您的使用者名稱不能包含數字
# - 如果都符合的話,顯示: 歡迎 + 使用者名稱

print ("您的使用者名稱不能超過 12 個字元" , "您的使用者名稱不能包含空格" ,  "您的使用者名稱不能包含數字" )

user_name = input("請輸入您的使用者名稱:")

if len(user_name) > 12:
    print("您輸入的字元超過12個字")
elif " " in user_name:
    print("您的使用者名稱不可使用空格")
elif not user_name.isalpha(): #isalpha這個函數是指在使用者輸入的字串裡尋找不是英文字的其他字元
    print("您的使用者名稱不可包含數字")
else:
    print("歡迎:",user_name,"您的加入")

#python 字串索引

