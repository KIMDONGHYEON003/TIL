# dfs나 bfs를 사용해야할거 같음 (없어도 가능할지도)

# X, Y를 합치거나 합치지 않거나의 경우로
# s에 주어진 숫자만큼 나누어서 생각해보자

# 초기에 s를 기준으로 나뉜 배열을 요소 하나하나씩 나눈다.
# [[1], [1], [1], [1]]
# 왼쪽의 세포와 같다면 합친다.
# 다르면 합치지 않고 넘어간다.
# 합칠때마다 c를 하나씩 증가시킨다.

# result 리스트에 c를 하나씩 append한다.