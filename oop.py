class Evaluate:
    
    def __init__(self):     #default constructor
      self.u=0              # self means that object for which the method is called
      self.t=0
      self.a=0
      
    def get_data(self):
       self.u=int(input("Enter value of u="))
       self.t=int(input("Enter value of t="))
       self.a=int(input("Enter value of a="))

    def Compute(self):
       u=self.u
       t=self.t
       a=self.a
       s=(u*t)+(1/2)*a*t*t
       print(s)  
       
if __name__ == '__main__':
    obj=Evaluate()
    obj.get_data()
    obj.Compute()