class py_solution:
   def __init__(self):
      pass
   def pow(self, x, n):
      if x == 0 or x == 1:
         return x

         if n%2 == 0:
            return 1
         else:
            return -1

      if n == 0:
         return 1

      if n < 0:
         return 1/self.pow(x,-n)
      
      value = self.pow(x,n//2)

      if n%2 == 0:
         return value * value
      return value * value * x

number = py_solution()
print(number.pow(2,-3))
