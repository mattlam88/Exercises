class py_solution:
   def is_valid_parenthese(self, str1):
      brackets,container = [], {"(": ")", "{": "}", "[": "]"}
      
      for paranthese in str1:
         if paranthese in container:
            brackets.append(paranthese)
         elif len(brackets) == 0 or container[brackets.pop()] != paranthese:
            return False

      return len(brackets) == 0