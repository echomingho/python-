import sys

chinese = float(input("請輸入國文成績："))
english = float(input("請輸入英文成績："))
math = float(input("請輸入數學成績："))

scores = [chinese, english, math]

if any(score < 0 or score > 100 for score in scores):
    print("請輸入有效的成績（0-100）")
    sys.exit()

total = sum(scores)
average = total / len(scores)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("您的評級為：", grade)
print("您的平均分數為：", average)
'''
                    【問題】
               計算學生成績與評級
                       │
                       ↓
                  【問題拆解】
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
       輸入成績      檢查成績      計算平均
          │            │            │
     國、英、數      0～100？     總分 ÷ 3
                       │            │
                  ┌────┴────┐       ↓
                  │         │    平均分數
                 合法     不合法     ┼──┐
                  │         │          ↓
                  ↓         ↓      【條件判斷】
                 繼續     顯示錯誤       │
                  │         ↓           │
                  │       結束      ┌────┼────┐
                  │                 ↓    ↓    ↓
                  │              A / B / C / D /F
                  │                   │
                  └──────────┬────────┘
                             ↓
                         【輸出結果】
                             │
                       平均分數＋評級
'''