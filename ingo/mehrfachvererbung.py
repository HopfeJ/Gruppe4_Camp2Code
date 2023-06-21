class A:
    def stop(self):
        print("stop aus Klasse A")

class B:
    def stop(self):
        print("stop aus Klasse B")

class C(A,B):
    def stop_nutzen(self):
        B.stop(self)

c = C()
c.stop()
c.stop_nutzen()
