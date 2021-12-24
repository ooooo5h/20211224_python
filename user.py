class User:
    
    def __init__(self, name = '이름없음', birth_year = 0, point = 0):
        self.name = name
        self.birth_year = birth_year
        self.point = point

        
    
    def set_data(self, name, birth_year, point):
        
        # self.변수는, self내부에 달려있는 변수
        # 파라미터로 들어오는 변수와는 전혀 별개의 변수
        
        # self.변수와 파라미터 변수는 이름이 같아도 컴퓨터 자체가 처리가능
        self.name = name
        self.birt_year = birth_year
        self.point = point
        
    
    def print_user_info(self):
        
        # 앞의 set_data에서 설정해둔 변수들을 활용하는 메쏘드의 예시
        print('===== 사용자정보 =====')
        print(f'사용자 이름 : {self.name}')
        print(f'출생년도 : {self.birth_year}')
        print(f'보유포인트 : {self.point}P')
        