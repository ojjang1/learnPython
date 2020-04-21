#### 클래스 상속 ####
class Parent:
    def can_sing(self):
        print("Sing a song")

father = Parent()
father.can_sing()

class LuckyChild(Parent):
    pass

child1 = LuckyChild()
child1.can_sing()


class UnLuckyChild:
    pass

child2 = UnLuckyChild()
'''
오류발생
child2.can_sing()
상속을 안받아 내부에 함수가 없다.
'''

class LuckyChild2(Parent):
    def can_dance(self):
        print("Shuffle Dance")

child2 = LuckyChild2()
child2.can_sing()
child2.can_dance()


    
