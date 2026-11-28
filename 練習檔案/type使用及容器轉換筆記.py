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