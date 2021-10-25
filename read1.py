data = []
count = 0
with open("reviews.txt", "r") as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:   #每一千筆印一次（因print很耗時間)
            print(len(data))    # %<-- 用來求餘數
print("檔案讀取完了，總共有", len(data), "筆資料")

#myself
index_len = []
for i in data:
    index_len.append(len(i))
print("平均留言長度是：", sum(index_len) / len(data))

#teacher
sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print("平均留言長度是：", sum_len / len(data))

#teacher 篩選
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print("一共有", len(new), "筆留言長度小於100")

#teacher 篩選2
good = []
for d in data:
    if "good" in d:
        good.append(d)
print("一共有", len(good), "筆留言提到good")
print(good[0])


 

# 文字計數

wc = {}
for d in data:
    words = d.split(" ")
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1         

for word in wc:
    if wc[word] >1000000:
        print(word, wc[word])

print(len(wc))

while True:
    word = input("請問你想查什麼字：")
    if word == "q":
        break
    if word in wc:
        print(word, "出現過的次數為：", wc[word])
    else:
        print("沒有這個字出現過")

print("感謝使用本查詢功能")



