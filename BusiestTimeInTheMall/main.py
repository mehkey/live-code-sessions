
from aenum import Enum
from collections import defaultdict

class Change(int,Enum):
  Enter = 1
  Exit = 0
  pass

class Epoch:
  def __init__(self,epoch):
    self.epoch  = epoch
    self.visitor  = 0

  def apply_change(self,change, count):
    if change == Change.Enter:
      self.visitor +=  count 

    if change == Change.Exit:
      self.visitor -= count

def find_busiest_period(data):
  
  
  epochs = defaultdict(Epoch)
  
  for epoch in data:
    
    time = epoch[0]
    if time not in epochs:
        epochs[time] = Epoch(Epoch(epoch[0]))

    epochs[time].apply_change(epoch[2],epoch[1])

    

    old_time = epoch_change.epoch

    current_count = epoch_change.apply_change(current_count)

    if i < len(data) -1 and epoch_change.epoch != data[i+1][0]  and current_count > max_count:
      max_count = current_count
      max_time = epoch_change.epoch
      
    if i ==  len(data) -1 and current_count > max_count:
      max_time = epoch_change.epoch


  return max_time



'''
Old Way



class Change(int):
  Enter = 1
  Exit = 0
  pass

class Epoch(int):
  pass

class EpochChange:
  def __init__(self,epoch,visitor,change):
    self.epoch  = epoch
    self.visitor  = visitor
    self.change = change
  
  def apply_change(self,count):
    if self.change == Change.Enter:
      return count + self.visitor
      
    if self.change == Change.Exit:
      return count - self.visitor

def find_busiest_period(data):
  max_time = 0
  max_count = 0
  current_count = 0
  old_time = 0
  
  
  
  for i,epoch in enumerate(data):
    
    epoch_change = EpochChange(Epoch(epoch[0]),epoch[1],Change(epoch[2]))

    
    old_time = epoch_change.epoch

    current_count = epoch_change.apply_change(current_count)

    if i < len(data) -1 and epoch_change.epoch != data[i+1][0]  and current_count > max_count:
      max_count = current_count
      max_time = epoch_change.epoch
      
    if i ==  len(data) -1 and current_count > max_count:
      max_time = epoch_change.epoch


  return max_time



'''