class calc:
  def __init__(self,f = 0):
    self.val = 0
    self.f = f
    
  def add(self,val):
    self.val += val
    print(self.val)

  def sub(self,val):
    self.val -= val
    print(self.val)

  def mul(self,val):
    self.val *= val
    print(self.val)

  def div(self,val):
    if self.f != 0 : 
      self.val /= val
    else :
      self.val //= val
      
    print(self.val)

