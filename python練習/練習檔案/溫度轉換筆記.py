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