def solution(string):
  res = []
  prev = 0
  for i in range(len(string) + 1):
    odd = i % 2 == 0
    if odd and i != 0:
      temp = string[prev:i]
      prev = i
      res.append(temp)

    if i == len(string) and not odd:

      temp = string[prev:i]
      temp += '_'
      res.append(temp)


  print(res)

solution('vbnfyu6745g')