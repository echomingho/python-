""""

題目：終極密碼猜數字遊戲

請寫一段 Python 程式，讓電腦心裡隨機想一個 1 到 100 的秘密數字，接著讓玩家一直猜，直到猜中為止：
1. 如果玩家猜的數字比秘密數字大：印出 "太大了！再小一點"
2. 如果玩家猜的數字比秘密數字小：印出 "太小了！再大一點"
3. 如果玩家猜中了：印出 "恭喜答對！"，並結束遊戲（跳出迴圈）
執行畫面範例（假設秘密數字是 68）：
text
請猜一個 1~100 的數字：50
太小了！再大一點
請猜一個 1~100 的數字：80
太大了！再小一點
請猜一個 1~100 的數字：68
恭喜答對！

"""
import random

#引入隨機數字模組

num = random.randint(1, 100)
count = 0
low = 1      # 記錄目前範圍的最小值
high = 100   # 記錄目前範圍的最大值

while True:
    # 直接用 f-string 顯示目前的 low 和 high，不用再寫 if count == 0 分開判斷！
    guess = int(input(f"請猜一個 {low}~{high} 的數字："))
    
    # 防呆條件也跟著變成 low 和 high
    if guess < low or guess > high:
        print(f"請輸入有效的數字（{low}~{high}）")
        continue
        
    count += 1

    if guess < num:
        print("太小了！再大一點")
        low = guess + 1     # 猜太小，把下限更新成剛剛猜的數字
    elif guess > num:
        print("太大了！再小一點")
        high = guess - 1     # 猜太大，把上限更新成剛剛猜的數字
    else:
        print("恭喜答對！")
        print(f"你總共猜了 {count} 次")
        break
