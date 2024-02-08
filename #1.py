#solution of #1
import numpy as np

def solution(x,y):
  if len(x) < len(y):
    x , y = y , x

  for i in range(len(x)):
    token = False
    for j in range(len(y)):
      if x[i]==y[j]:
        token = True
    if not token:
      return x[i]

#Test
#if __name__ == "__main__":
  # Example arrays
  #array1 = np.array([10, 20, 30, 40])
  #array2 = np.array([10, 20, 30, 40, 50])
  #print(solution(array1, array2))
