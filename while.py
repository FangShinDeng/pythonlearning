# break斷點, 直接跳出整個迴圈
# contiune換迭代, 跳出當次迴圈繼續執行

i = 0
while i<10:
    i+=1
    if i == 3:
        print('跳出此次迴圈')
        # break
        pass
    pass
    print(i)

# while可以搭配else用法
j = 0
while j<=5:
    j+=1
else:
    print(format(j)+'已超過5')
