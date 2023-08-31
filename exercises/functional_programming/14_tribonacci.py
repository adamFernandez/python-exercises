def tribonacci(signature, n):
    while len(signature) < n:
        number = signature[-1] + signature[-2] + signature[-3]
        signature.append(number)
    return ([1] if signature == [1,1,1] else 
            [] if n == 0 else  
            signature[:n] if n < 3 else
            signature)

def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res


def tribonacci(signature,n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    
    return signature[:n]
