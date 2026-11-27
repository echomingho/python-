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