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