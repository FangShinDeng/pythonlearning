# 學習python基本語法
透過w3schools.com學習python的基本用法https://www.w3schools.com/python/python_file_handling.asp
將這邊的練習題都做完後，就能掌握python大致的語法

## 重點筆記
1. python具有縮排性質，一定要對齊<br>
2. 註解的符號為#, 多排註解需在上下行各加"""三個雙引號, comment.py<br>
3. variable.py<br>
    變數定義規則<br>
    a. 變量名稱必須以字母或下劃線字符開頭<br>
    b. 變量名不能以數字開頭<br>
    c. 變量名稱只能包含字母數字字符和下劃線（Az，0-9和_）<br>
    d. 變量名稱區分大小寫（age，Age和AGE是三個不同的變量）<br>
    e. 若需要全局變數加上global, ex: global x<br>
4. datatype.py<br>
    Data Type, 可以用print(type(x)), 去看出變數類型<br>
    a. Text Type:	str<br>
    b. Numeric Types:	int, float, complex<br>
    c. Sequence Types:	list, tuple, range<br>
    d. Mapping Type:	dict<br>
    e. Set Types:	set, frozenset<br>
    f. Boolean Type:	bool<br>
    g. Binary Types:	bytes, bytearray, memoryview<br>
    補充1: list與tuple的差別主要在於tuple裡面的元素值不能修改<br>
5. numbers.py<br>
    nubmers共有三種, int, float, complex<br>
    若要新增random亂數, 可以用內建 import random<br>
6. strings.py<br>
    a. 多行字串, 透過三個單引號或雙引號<br>
    b. Slice 取出特定字串內的內容, Nagative Slice從尾取內容<br>
    c. String Length 取長度<br>
    d. Strip 去除頭尾空格<br>
    e. upper, lower 將字體變成大寫小寫<br>
    f. Replace 取代<br>
    g. 分割 split<br>
    h. x in txt 檢查字串<br>
    i. 字串跟數字不能一起用, 用format來帶入動態參數,並將不同類型的參數轉換成str<br>
    j. 當遇到字串裡面有單引號或雙引號時, 在雙引號貨單引號前加上\<br>
    k. 還有很多其他內建用法 具體請參考https://www.w3schools.com/python/python_strings.asp的下方內容
7. boolean.py<br>
    使用bool()去判斷不同的內容，回傳True or False<br>
    使用內建函數 isinstance(x,int)去判斷是否為整數<br>
8. operatorlearning.py<br>
    加減乘除,餘數,次方,取整數位,邏輯閘,基本邏輯式判斷,is and in用法<br>
9. list.py<br>
    使用list學習列表的處理函式,包含新增,刪除,插入,修改,打印<br>
    list常用函式, append, insert, remove, pop, del, clear, copy, extend<br>
10. sets.py<br>
    set跟list最大的差別在於set不能接受重複值,list可以, set是無序的, list為有序的, 參考文獻: https://www.itread01.com/content/1517808043.html<br>
11. dictionaries.py<br>
    dictionaries 跟API接口是密不可分, 要好好學習<br>
    主要函式大多都相同,但要特別注意key跟value的概念!<br>
12. elseif.py<br>
    要會使用縮寫法<br>
13. while.py<br>
    a. break斷點, 直接跳出整個迴圈<br>
    b. contiune換迭代, 跳出當次迴圈繼續執行<br>
    c. 注意while可以跟else搭配使用!<br>
14. function.py<br>
    要特別注意,function(*arg)及function(**arg)的用法<br>
    *為tuple, **為dict的不同資料類型<br>
    參考文獻: https://blog.csdn.net/u010758410/article/details/71727822<br>
    遞迴性,函式裡能用自己的函示去遞減, Recursion<br>
15. lambda.py<br>
    匿名函式<br>
16. class.py<br>
    創建類別、建立實例<br>
17. inheritance.py<br>
    創建父子類別,用子類別繼承父類別的定義<br>
18. iterator.py<br>
    迭代器，先定義類別建成實例後，用iter(class)定義迭代,然後再去打印迭代內內容<br>
    若要停止迭代則使用raise StopInteration<br>