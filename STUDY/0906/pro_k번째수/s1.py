def solution(array, commands):
  answer = []

  for i in range(len(commands)):
    # [i][0]번째부터 [i][1]까지 짜른다
    arr_list = array[commands[i][0]-1:commands[i][1]]
    arr_list.sort()

    # 3번째 숫자를 append
    answer.append(arr_list[commands[i][2]-1])

  return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))