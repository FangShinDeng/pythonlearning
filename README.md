## 學習python基本語法
透過w3schools.com學習python的基本用法https://www.w3schools.com/python/python_file_handling.asp
將這邊的練習題都做完後，就能掌握python大致的語法

重點筆記
1. python具有縮排性質，一定要對齊
2. 註解的符號為#, 多排註解需在上下行各加"""三個雙引號, comment.py
3. 變數定義規則, variable.py
    a. 變量名稱必須以字母或下劃線字符開頭
    b. 變量名不能以數字開頭
    c. 變量名稱只能包含字母數字字符和下劃線（Az，0-9和_）
    d. 變量名稱區分大小寫（age，Age和AGE是三個不同的變量）
    e. 若需要全局變數加上global, ex: global x
4. Data Type, 可以用print(type(x)), 去看出變數類型, datatype.py
    Text Type:	str
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type:	dict
    Set Types:	set, frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray, memoryview
    ### list與tuple的差別主要在於tuple裡面的元素值不能修改
5. nubmers共有三種, int, float, complex, numbers.py
    ### 若要新增random亂數, 可以用內建 import random
6. strings.py
    ### 多行字串, 透過三個單引號或雙引號
    ### Slice 取出特定字串內的內容, Nagative Slice從尾取內容
    ### String Length 取長度
    ### Strip 去除頭尾空格
    ### upper, lower 將字體變成大寫小寫
    ### Replace 取代
    ### 分割 split
    ### x in txt 檢查字串
    ### 字串跟數字不能一起用, 用format來帶入動態參數,並將不同類型的參數轉換成str
    ### 當遇到字串裡面有單引號或雙引號時, 在雙引號貨單引號前加上\
    ### 還有很多其他內建用法 具體請參考https://www.w3schools.com/python/python_strings.asp的下方內容