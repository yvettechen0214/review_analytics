data = []
count = 0
with open("reviews.txt", "r") as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:   #每一千筆印一次（因print很耗時間)
            print(len(data))    # %<-- 用來求餘數
