# 파일 쓰기
파일 = open("ex3.txt", "w", encoding="utf-8")
파일.write("글")
파일.write("쓰기")
파일.write("\n줄바꿈\n\n")
파일.writelines(["나는", "개론이", "싫다."])
파일.close()