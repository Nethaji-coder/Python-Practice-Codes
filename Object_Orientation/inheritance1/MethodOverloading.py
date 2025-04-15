#Python cannot accept methodoverloading as shown below first two methods will not get exceuted the last method will only get excecuted
class Demo:
    def disp(self):
        print('Inside disp1 with 0 parameter')
    def disp(self, a):
        print('Inside disp with 1 parameter')
    def disp(self, a, b):
        print('Inside disp with 2 parameters')
d = Demo()
#d.disp()--Error
#d.disp(10)--Error
d.disp(10, 20)
