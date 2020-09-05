import mymodule as mym # 用as來縮寫其他模組

a = mym.person1["age"]

print(a)

# print(mym)

import platform
x = platform.system()
print(x)
print(platform)

# 使用dir列出模塊中的所有內建函數
print(dir(platform))
print(dir(mym))

from mymodule import person1 # 僅匯入person1

print(mym.person1["age"])
print(mym.person1)