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