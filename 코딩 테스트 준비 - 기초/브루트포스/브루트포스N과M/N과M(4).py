def NandM(depth) :
  if (depth == M) :
    for i in range(M) :
      print(answer[i], end=" ")
    print()
    return
  for i in range(1, N + 1) :
    if (depth == 0 or i >= answer[depth - 1]) :
      answer.append(i)
      NandM(depth + 1)
      del answer[-1]
    
N, M = map(int, input().split())
answer = []
NandM(0)
