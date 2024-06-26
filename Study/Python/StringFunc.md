# 문자열 함수 모음

```python
# 문자열에서 문자 치환
text.replace('a', 'b', [바꿀 횟수])

# 문자열에서 특정 문자 개수 세기
text.count('a')

# 문자열 소문자로 전환
text.lower()

# 문자열 대문자로 전환
text.upper()

# 문자열 인덱스를 사용할 수 있지만, = 으로 할당할 수는 없다.

# 문자 아스키 코드로 변환
ord("A")

# 아스키 코드를 문자로 변환
chr(45)

# 문자열 정렬
sorted(s) # 정렬된 배열로 나옴. 기준 소문자
sorted(s.split()) # 단어별 대문자 우선 정렬
sorted(s.split(), key=s.lower) # 단어별 소문자 우선 정렬

# 문자열 숫자인지 확인하는 방법
text.isdigit()

# 문자열이 알파벳(한글) 또는 숫자인지 확인
text.isalnum()

# 문자열이 알파벳(한글) 인지 확인
text.isalpha()

# 문자열 뒤집기
text = text[::-1]

# 문자열에 원하는 크기까지 0채우기
text.zfill(10)

# 문자열에 원하는 크기까지 문자 채우기
text.rjust(10, '*')

# 문자열이 특정 문자로 시작하는지 확인
str = 'banana'
result = str.startswith('ba')

# 문자열이 특정 문자로 끝나는지 확인
str = 'banana'
result = str.endswith('na')

# 문자열 하나씩 끊어서 리스트로
list(srt)

```

### 정규 표현식

> 정규 표현식은 문자열을 처리할 때 사용하는 기법
> [정규 표현식 살펴보기](https://wikidocs.net/1642)

**메타 문자**

> 메타 문자란, 원래 그 문자가 가진 뜻이 아니라 특별한 의미를 가진 문자를 말함.

1. [] 문자 - 문자 클래스
   > 사이의 문자들과 매치

- 정규 표현식이 `[abc]` 라면, a, b, c 중 한 개의 문자와 매치
- 정규 표현식이 `[a-c]` 라면, a 부터 c 사이의 한 개의 문자와 매치
- 문자 클래스 안에 `^` 메타 문자를 사용할 경우 반대의 의미를 갖는다.

- [0-9] 숫자인 경우, [a-zA-Z] 문자열인 경우 와 같이 많이 쓰이는 정규 표현식은 별도의 표기법으로 표현할 수 있다.
  - `\d` - `[0-9]` 숫자
  - `\D` - `[^0-9]` 숫가 아닌 것
  - `\s` - `[ \t\n\r\f\v]` 화이트스페이스
  - `\S` - `[^ \t\n\r\f\v]` 화이트 스페이스가 아닌 것
  - `\w` - `[a-zA-Z0-9_]` 문자와 숫자
  - `\W` - `[^a-zA-Z0-9_]` 문자와 숫자가 아닌 것

<br>

2. 문자 - \n을 제외한 모든 문자
   > 줄바꿈 문자를 제외한 모든 문자와 매치

- 정규 표현식이 `a.b` 라면, a와 b 사이에 어떤 문자가 들어가도 매치 된다는 의미이다.
- 정규 표현식이 `a[.]b` 라면, . 는 메타 문자가 아니라 . 문자 그자체를 의미한다.

<br>

3. `*` 문자

   > 0부터 2억개(메모리 용량상 무한대)까지 반복

- 정규 표현식이 `ca*t` 라면, c와 t 사이에 a가 0번 이상 반복되면 매치

4. `+` 문자
   > 최소 1번 이상의 반복을 나타냄.

- 정규 표현식이 `ca+t` 라면, c와 t 사이에 a가 1번이상 반복되면 매치

<br>

5. `{}`문자와 `?` 문자
   > {}는 사이 값을 나타내는 것, ?는 있어도되고 없어도 된다는 것

- 정규 표현식이 `ca{2}t` 라면, c와 t 사이에 a가 반드시 두번 반복되면 매치
- 정규 표현식이 `ca{2,5}t` 라면, c와 t 사이에 2~5번 반복되면 매치
- 정규 표현식이 `ca?t` 라면, c와 t 사이에 a의 유무에 관계없이 매치

**파이썬 정규 표현식 모듈**

```
import re
p = re.complie(`[a-z]+`)

# 문자열의 처음 문자부터 정규식과 매치 되는지
m = p.match("3three") # None

if m:
  print("문자열이 매치됨")
else:
  print("문자열이 매치되지 않음")

# 문자열 전체를 검색하여 정규식과 매치 되는지
m = p.search("3three") # 매치됨

# 정규식과 매치되는 모든 문자열을 리스트로 리턴
result = p.findall("life is too short")
["life", "is", "too", "short"]


```

**문자열 소비가 없는 메타 문자**

1. |

   > or과 동일한 의미

2. ^
   > 문자열의 맨 처음과 일치, re.MULTILINE을 사용하면 여러 줄의 문자열일 때 각 줄의 처음과 일치

```
re.search('^Life', 'Life is too short') # 매치
```

3. $
   > 문자열의 끝과 일치

```
re.search('short$', 'Life is too short') # 매치
```

4. \A

   > 문자열의 처음과 매치

5. \Z

   > 문자열의 끝과 매치

6. \b
   > 단어 구분자, 화이트 스페이스

```
p = re.complie(r'\bclassn')
p.search('no class at all') # 매치
```

- `\b`는 파이썬 리터럴 규칙에 따르면 백스페이스를 의미하므로, 단어 구분자라는 것을 알려주기 위해 `r`을 반드시 붙여야 한다.

7. \B
   > 화이트 스페이스로 구분된 단어가 아닌 경우

```
p = re.compile(r'\Bclass\B')
p.search('no class at all') # 불일치
```

**그루핑**

```
p = re.complie('(ABC)+')
m = p.search('ABCABCABC OK?') # 매치
m.group() # ABCABCABC

P = re.compile(r'(\w+)\s+(\d+[-]\d+[-]\d+)')
m = p.search('park 010-1234-1234')
m.group(1)   # park
m.group(2)   # 010-1234-1234

p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
m.group("name")    # park

```
