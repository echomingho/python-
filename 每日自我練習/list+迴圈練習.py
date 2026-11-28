"""
請輸入第 1 科成績：80
請輸入第 2 科成績：90
請輸入第 3 科成績：75
請輸入第 4 科成績：100
請輸入第 5 科成績：85
你的成績列表：[80, 90, 75, 100, 85]
總分：430
平均：86.0
"""
scores = []
for i in range(5):
    score = int(input(f"請輸入第 {i+1} 科成績："))
    scores.append(score)
total = sum(scores)
average = total / len(scores)
print(f"你的成績列表：{scores}")
print(f"總分：{total}")
print(f"平均：{average}")

"""
請輸入第 1 科成績：80
請輸入第 2 科成績：45
請輸入第 3 科成績：92
請輸入第 4 科成績：58
請輸入第 5 科成績：70
最高分：92
最低分：45
不及格共有 2 科：[45, 58]
"""
scores = []
for i in range(5):
    score = int(input(f"請輸入第 {i+1} 科成績："))
    scores.append(score)
print(f"最高分:{max(scores)}")
print(f"最低分:{min(scores)}")

failures = [score for score in scores if score < 60]

"""
【串列生成式邏輯流程圖】
目標語法：failures = [score for score in scores if score < 60]

  [ 1. 資料來源 ]              [ 2. 條件守門員 ]            [ 3. 出貨打包 ]
for score in scores   ───▶    if score < 60     ───▶   最前面的 score
(從 scores 逐一拿出)          (檢查是否小於 60)        (通過檢查，送進新 list)
                                    │
                                    ▼ (大於等於 60)
                               [ 直接丟棄 ]

  ▼ (全部資料跑完後)
組裝成全新的 list ──▶ 存入左邊的 failures 變數
"""

print(f"不及格共有 {len(failures)} 科：{failures}")