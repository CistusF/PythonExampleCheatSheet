# 파일 다중 내용 읽기

# 방법 1
파일 = open("ex2.txt", "r", encoding="utf-8")
txt = 파일.read()
print(txt)
파일.close()

# 방법 2
# 한글자씩 읽기
파일 = open("ex2.txt", "r", encoding="utf-8")
txt = 파일.read(1)
while txt != "":
    print(txt, end="")
    txt = 파일.read(1)
print("")
파일.close()

# 방법 3
# 한줄씩 읽기
파일 = open("ex2.txt", "r", encoding="utf-8")
txt = 파일.readline()
while txt != "":
    print(txt, end="")
    txt = 파일.readline()
print("")
파일.close()