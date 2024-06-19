# 뒤집기
# s5
# 문자열

import sys
s = sys.stdin.readline().rstrip()

cnt = [0, 0]
prev = s[0]

for i in range(1, len(s)):
  if prev == s[i]:
    continue
  else:
    cnt[int(prev)] += 1
    prev = s[i]
cnt[int(prev)] += 1

print(min(cnt))

