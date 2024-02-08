#solution of #2-1
def convert2decimal(n, k, b):
  r = 0
  for i in range(k):
     r+= int(n[k-i-1])*pow(b,i)
  return r

def convert2origin(decimal, k, b):
  r = ""
  for i in range(k-1):
    decimal, remain = decimal//b , decimal%b
    if decimal:
      r = str(remain) + r
      if decimal < b:
        r = str(decimal) + r
    else:
      r = '0' + r
  return r

#Check for duplicates
def check(z, tmp, result):
  r = 0
  if (z in tmp):
    if len(result) and z==result[0]:
      r = 1
    else:
      result.append(z)
  tmp.append(z)

  return r

#When input is decimal
def loop_decimal(n, k, b, tmp, result):
  x = "".join(sorted(n, reverse=True))
  y = "".join(sorted(n))
  z = str(int(x) - int(y))
  for i in range(k-len(z)):
    z = '0' + z

  if check(z, tmp, result): 
    return len(result)

  return loop_decimal(z, k, b, tmp, result)
  
#When input isn't decimal
def loop_normal(n, k, b, tmp, result):
  x = "".join(sorted(n, reverse=True))
  y = "".join(sorted(n))
  z = convert2origin((convert2decimal(x, k, b) - convert2decimal(y, k, b)), k, b)

  if check(z, tmp, result): 
    return len(result)
    
  return loop_normal(z, k, b, tmp, result)
  
#main fuction
def solution(n, b):
    #Your code here
    k = len(n)
    tmp = []
    result = []
    r = 0
    try:
      if b == 10:
        r = loop_decimal(n, k, b, tmp, result)
      else:
        r = loop_normal(n, k, b, tmp, result)
    except:
      r = 0
    return r

#Test
#if __name__ == '__main__':
  #n = '210022'
  #b = 3
  #solution(n, b)
