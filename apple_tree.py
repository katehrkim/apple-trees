from apple import Apple

class AppleTree:
    def __init__(self, height=0, age=0, num_apples=0):
        self.height = height
        self.age = age
        self.num_apples = num_apples
        self.apple_list = []
  
    def age_tree(self):
        self.age += 4
        self.height += 1
        self.num_apples += 1
        new_apple = Apple()
        self.apple_list.append(new_apple)
   
    def is_dead(self):
        if self.age >= 100:
            return True
        else:
            return False
    
    def any_apples(self):
        if self.num_apples == 0:
            return False
        else:
            return True

    def pick_an_apple(self):
        if self.num_apples == 0:
            raise Exception('No apples on your tree')
        else:
            self.num_apples -= 1
            return self.apple_list.pop()
        # Read the tests before coding.
