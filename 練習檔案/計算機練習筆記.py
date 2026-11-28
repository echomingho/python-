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
