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