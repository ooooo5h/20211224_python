from book import Book   # book.py 파일안에서 Book클래스를 main.py에 가져오기
from user import User

# 만들어둔 클래스들을 활용해서 실제 동작 관련 코드 작성

# 책의 인스턴스 하나를 생성 + 변수에 담아줘야지 접근이 가능함
book1 = Book('타짜', 700, 19)    # Book 클래스의 생성자에서는 파라미터 3개를 요구(하도록 수정됨), 메인에서 사용시에는 arguments를 안보내고있다 => 형태가 안맞아서 에러가 남

# 방금 만든 책의 데이터 설정(타짜, 700, 19)

# set_data메쏘드의 self 파라미터에는 => book1이 대입됨
# book1.set_data('타짜', 700, 19)   # 전달인자(=arguments)들을, self 파라미터만 제외하고 작성하면됨

book1.print_book_info()


# 두번째 책의 인스턴스를 추가로 생성
book2 = Book()

# 두번째 책의 데이터 설정 (드래곤볼, 1000, 15)
book2.set_data('드래곤볼', 1000, 15)

# 두번째 책의 정보 출력
book2.print_book_info()


# 연습문제 : 연령제한이 0 => 그때는 전체 이용가로 나타나도록 수정
#           그 외의 숫자 => ?세 이용가로 나타나도록 해보기
book3 = Book()
book3.set_data('뽀로로', 500, 0)
book3.print_book_info()

test02 = '테스트 변수'
            
def add_and_print(num1, num2):
    print(num1 + num2)
    print(test02)
    test = 10

add_and_print(5,11)        

book1.is_rent_available(2005)


num = 10
if num > 5:
    result = '5보다 크다.'
    
print(result)

# 연습문제 클래스 추가 - User
# set_data 메쏘드 추가해서 이름/출생년도/보유포인트를 받아서 저장
# print_user_info 메쏘드 추가해서 위의 3가지 정보 출력


# 사용자 한 명 생성 '본인이름', 출생년도, 포인트로 데이터 세팅
# 정보 출력하기

# 사용자 정보 출력
user1 = User()
user1.set_data('전은형', 1991, 777777)

print(f'사용자1의 이름 : {user1.point}')
user1.print_user_info()


user2 = User()

user2.name = '김학생'
user2.birth_year = 2005
user2.point = 5000

user2.print_user_info()

# 사용자 클래스에도 생성자 추가, 이름 / 출생년도 / 포인트 한꺼번에 입력
# 기존 기본생성자() 유지해보자

user3 = User('이아동', 2012, 1000)
user3.print_user_info()

# boo1의 정보 출력
book1.print_book_info()