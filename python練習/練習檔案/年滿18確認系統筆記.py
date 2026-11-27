#if else
#詢問是否年滿18系統
age = int(input("請輸入你的年齡:"))
if age < 18:
    print ("很抱歉您的年紀未達18周歲")
else:
    print("恭喜通過驗證您已經滿18周歲了!")   

#elif >= else if的簡寫 elif是使用在if else的判斷式不夠時所使用的額外判斷
age2 = int(input("請輸入您的年紀:"))
if age2 >= 100:
    print("您的年齡過大無法註冊此帳戶")
elif age2 >= 18:
    print ("您已經年滿18歲了,可以註冊此app帳戶")
elif age2 <= 0:
    print ("您輸入的年齡還未出生,請檢查後再次重新輸入")
else :
    print ("很抱歉您未滿18歲,無法註冊該帳戶")