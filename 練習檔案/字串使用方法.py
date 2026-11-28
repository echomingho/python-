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