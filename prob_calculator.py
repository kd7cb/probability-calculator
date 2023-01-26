import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **balls):
    data = balls
    self.contents = list()
    i = 0
    
    for x in data:
      for i in range(data[x]):
        self.contents.append(x)

  def draw(self,todraw):
    self.drawn = list()
    if todraw > len(self.contents):
      return self.contents
    else:
      for x in range(todraw):
        chosen_ball = random.choice(self.contents)
        self.drawn.append(chosen_ball)
        self.contents.remove(chosen_ball)
    return self.drawn
      
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  expectlst = list()
  drawnlst = list()
  m = 0
  
  for x in expected_balls:
    for i in range(expected_balls[x]):
      expectlst.append(x)
  
  for x in range(num_experiments):
    drawnlst.clear()
    hatcopy = copy.deepcopy(hat)
    drawnlst = hatcopy.draw(num_balls_drawn)
    expected_copy = copy.deepcopy(expected_balls)

    for color in drawnlst:
      if(color in expected_copy):
        expected_copy[color]-=1
    
    if(all(x <= 0 for x in expected_copy.values())):
      m += 1

  return m/num_experiments