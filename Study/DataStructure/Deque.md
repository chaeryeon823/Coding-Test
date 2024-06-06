### DEQUE

```python
from collections import deque

# 삽입
dq.append()
dq.appendleft()

# 삭제
dq.pop() # 마지막 요소
dq.popleft()

# 좌우 반전
dq.reverse()
```

- 큐도 deque를 사용해서 구현
- deque는 list보다 속도가 빠르다.
- `pop(0)` 와 같은 메서드를 수행할때 리스트의 경우 `O(N)` 연산을 수행하지만, deque는 `O(1)` 연산을 수행한다.
- push와 pop이 빈번한 알고리즘의 경우, list 보다 deque를 사용하는 것이 효율적이며 속도가 더 빠르다.
