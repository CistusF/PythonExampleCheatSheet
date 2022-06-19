# 파일 불러와서 읽기
파일 = open("ex1.txt", "r", encoding="utf-8") # ex1.txt를 utf-8의 형식으로 인코딩하여 읽어오라는 명령
print(파일.read())
파일.close()