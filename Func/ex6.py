# 재귀함수

리스트 = [1,1,1,1,1,1,2,1,1,1,1]

def _2찾기(위치값):
    if 리스트[위치값] == 2:
        return 위치값
    else:
        return _2찾기(위치값 + 1)

result = _2찾기(0)

print(result)