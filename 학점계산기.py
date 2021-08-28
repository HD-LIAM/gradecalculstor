print("=====================================================")

name = input("이름을 입력하세요: ")  #input은 입력되는 모든것을 문자열로 취급한다.
grade = int(input("점수를 입력하세요: "))

if grade < 60:
    print("학점: F") 
elif grade <= 64:
    print("학점: D")
elif grade <= 69:
    print("학점: D+")
elif grade <= 74:
    print("학점: C")
elif grade <= 79:
    print("학점: C+")
elif grade <= 84:
    print("학점: B")
elif grade <= 89:
    print("학점: B+")
elif grade <= 94:
    print("학점: A")
elif grade <= 100:
    print("학점: A+")

print("=====================================================")