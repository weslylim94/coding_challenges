########################
# FOR TESTING PURPOSES #
########################
# import time
# start_time = time.time()

file = open("input.txt", "r")
vals = file.readline().replace('\n', '').split(' ')
vals = map(int, vals)
inputs = file.readline().split(' ')
inputs = map(int, inputs)

n = vals[0]
k = vals[1]

# initial call 
def homeVal(n, k, list):
  for i in range(n - k + 1):
    print homeValHelper(list[i:i + k])
    
# helper function to work on each sublist
def homeValHelper(list):
  #return value for current sublist
  counter = 0

  # counting consecutive increases or decreases
  next = 0
  for i in range(len(list) - 1):

    # checking if next element is increasing 
    if list[i] < list[i + 1]:
      if next > 0:
        next = next + 1
      else:
        next = 1

    # checking if next element is decreasing
    elif list[i] > list[i + 1]:
      if next < 0:
        next = next - 1
      else:
        next = -1

    # checking if next element is the same
    else:
      next = 0
    counter = counter + next

  return counter



homeVal(n, k, inputs)



########################
# FOR TESTING PURPOSES #
########################
# import random
# l = []
# for i in range(200000):
#   l.append(random.randint(1000, 1000000))
# homeVal(5, 3, [188930, 194123, 201345, 154243, 154243])
# homeVal(200000, 150000, l)
# print "My program took", time.time() - start_time, "to run"