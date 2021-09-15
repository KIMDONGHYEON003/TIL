n = int(input())
cnt = 0
for _ in range(n):
    word = input()
    error = 0

    for idx in range(len(word)-1):
        if word[idx] != word[idx+1]:
            new_word = word[idx+1:]
            if new_word.count(word[idx]) > 0:
                error += 1

    if error == 0:
        cnt += 1

print(cnt)            