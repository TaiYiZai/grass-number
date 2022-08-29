#產生一個隨機整數1~100(不要印出來)
#讓使用者重複輸入去猜
#猜對的話，告訴使用者"終於猜到了!"
#猜錯的話，告訴使用者"比答案大/小"
import random

r = random.randint(1, 100)
while True:
	number = input("請猜數字: ")
	number = int(number)
	if number == r:
		print("終於猜對了!")
		break
	elif number > r:
		print("猜錯了，比答案大")
	else:
		print("猜錯了，比答案小")
