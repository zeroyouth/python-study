class Charactor:
  def __init__(self,name,iq=99,hp=100,exp=0,level=1) :
      self.name = name
      self.iq = iq
      self.hp = hp
      self.exp = exp
      self.level = level

  #파이썬 매직매서드 __str__ : 이름 출력
  def __str__(self):
      return f"제 이름은 {self.name}"

  def __sizeof__(self):
      return self.iq

  def study(self, book): #책 경험치
      self.exp += book.exp
      self.hp -= 5
      if (self.exp > 50): #경험치가 50보다 크면
          self.level_up() 

  def level_up(self): 
      self.level += 1
      self.exp = 0 #경험치 초기화

  def rest(self, min):
      self.hp += min
      
class Book:
    def __init__(self, exp):
        self.exp = exp

class Developer(Charactor):
    def __init__(self,name,language,iq=99,hp=100,exp=0,level=1):
        # super() : 상속받은 부모의 값 => charactor
        super().__init__(name,iq,hp,exp,level)
        self.language = language

    def study(self, book):
        super().study(book) # 상속받은 거 다 받고 추가해줌
        print('개발 너무 재밌습니다.') 


    # 오버라이드 : 부모 클래스가 정의한 함수를 덮어씌워 다시 정의하여 사용하는 것 =>  덮어씌우기
    def rest(self, min): 
        self.hp += 0.5*min

youngeun = Charactor('youngeun')
youngeun_pro = Developer('youngeun','python')
django = Book(60)

# print(isinstance(youngeun_pro, Charactor))
# youngeun.study(django)
youngeun_pro.study(django)
print(f'영은 프로의 레벨 {youngeun_pro.level}')
# youngeun_pro.rest(3)
print(f"영은 프로의 hp = {youngeun_pro.hp}") 
# print(youngeun.level)
print(youngeun)
# print(f"제 체력은 {youngeun.hp}")
