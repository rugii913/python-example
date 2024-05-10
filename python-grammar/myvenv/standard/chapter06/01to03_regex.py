# 정규표현식?

## 목적: 문자열 추출(특정 패턴 찾기), 유효성 검사 - 많은 언어에서 지원

## 단점: 가독성 떨어짐, 유지보수 어려움, 처리 느림 - 꼭 필요한 상황에서 사용

## 연습 예제: https://regexr.com/639t5 - 왼쪽 Cheatsheet 메뉴 참고

# ----------------------------- #

# 정규표현식 사용 방법

## expression flags
### g(Global)  →  가장 처음 match되는 문자열 뿐만 아니라 전체에서 match되는 문자열 확인
### i(case Insensitive)
### m(Multiline)  →  anchors 관련, m flag가 있어야 개행문자를 구분하여 각 줄마다 anchors에 의해 시작, 끝에 대해서 match되는 것을 바라는 대로 확인 가능함
### s(Single line(dotall))
### u(Unicode)
### y(stickY)

## character classes
### .  →  any character except newline: 개행 문자를 제외하고 모든 character 하나하나

### \w  →  any word character(alphanumeric & underscore): 알파벳, 숫자, _에 match되는 모든 character 하나하나
### \d  →  any digit character (0-9): 숫자에 match되는 모든 character 하나하나
### \s  →  any whitespace character (spaces, tabs, line breaks): whitespace 문자(스페이스바, 탭, 개행) character 하나하나
### \W  →  any character that is not a word character
### \D  →  any character that is not a digit character
### \S  →  any character that is not a whitespace character

### 두 character class를 연속으로 적은 경우
### → ex. \w\d 첫번째 character가 alphanumeric이고 두번째 character가 digit인 조건에 match되는 문자열을 찾음
###       예를 들어 33, m3 등

### [abc]  →  chracter set - any character in the set: [abc] 예시에서는 a, b, c 세트에 속하도록 match되는 character 하나하나
### [^abc]  →  negated set - any character that is not in the set: [^abc] 예시에서는 a, b, c 세트에 속하지 않도록 match되는 character 하나하나
### [a-g]  →  character set range - a character in the range "a" to "g" (char code 97 to 103), case sensitive
### → ex. [a-zA-Z] 알파벳 character [가-힣] 한글 character
### cf. 결론적으로, []로 묶이면 character 하나

## anchors
### ^https  →  beginning - Matches the beginning of the string, or the beginning of a line if the multiline flag (m) is enabled. This matches a position, not a character.
#### cf. set에서 negate의 의미로 사용되는 ^와 구분할 것
### com$  →  end - Matches the end of the string, or the end of a line if the multiline flag (m) is enabled. This matches a position, not a character.
### \b \B  →  word boundary - Matches a word boundary position between a word character and non-word character or position (start / end of string).
#### - \bapple 단어의 앞 부분인 apple만
#### - \Bapple 단어의 앞 부분이 아닌 apple만
#### - apple\b 단어의 뒷 부분인 apple만
#### - apple\B 단어의 뒷 부분이 아닌 apple만

## escaped characters
### \. \* \\ \t \n \r \[ \( 등

## quantifiers & alternation
### 예를 들어 rait, rabit, rabbit, rabbbit, rabbbbit 문자열이 있다고 하면
### *  →  0 or more - ex. rab*it - rait, rabit, rabbit, rabbbit, rabbbbit 모두 match
### +  →  1 or more - ex. rab+it - rait은 match되지 않음
### ?  →  0 or 1 - ex. rab?it - rait, rabit
### b{4}  →  exactly five - ex. rab{4}it - rabbbbit
### b{2,}  →  two or more - ex. rab{2,}it - rabbit, rabbbit, rabbbbit
### b{1,3}  →  between one & three - ex. rab{1,3}it - rabit, rabbit, rabbbit
### ra.+?t  →  lazy - Makes the preceding quantifier lazy, causing it to match as few characters as possible. By default, quantifiers are greedy, and will match as many characters as possible.
### - ex. ra.+t일 경우, rait, rabit, rabbit, rabbbit, rabbbbit 전체 문자열 추출
### - ex. ra.+?t일 경우, rait rabit rabbit rabbbit rabbbbit 각각의 문자열 추출
### - ex. ra.{4:}?t일 경우, rait rabit 하나 rabbit, rabbbit 하나 rabbbbit 하나 이렇게 추출
### (b|bb)  →  capturing group과 함께 쓰인 alternation
###            - Acts like a boolean OR. Matches the expression before or after the |.
###            - It can operate within a group, or on a whole expression. The patterns will be tested in order.
### - ex. ra(b|bb)it일 경우, rabit, rabbit 추출

## groups & lookaround
### 예를 들어 #좋아요, #좋아요반사, #팔로우, #맞팔, 문자열이 있다고 하면
### #(.+?),  →  capturing group - Groups multiple tokens together and creates a capture group for extracting a substring or using a backreference.
###             # , 제외하고 (.+?)로 gorup 묶은 부분만 추출 가능

### 예를 들어 pen pineapple apple pen 문자열이 있다고 하면
### (\b.+)\s.*\1  →  numeric reference - Matches the results of a capture group. For example \1 matches the results of the first capture group & \3 matches the third.
###              첫번째로 묶인 pen group을 \1로 역참조해서 pen pineapple apple pen 전체를 뽑아냄

### (?:abc)  →  non-capturing group - Groups multiple tokens together without creating a capture group.
###             group으로 추출까지 하진 않고 검색 조건으로 사용하고 싶을 때 사용
###             ex. \[(?:특가할인|품절)].*
### (?=abc)  →  positive lookahead(긍정형 전방 탐색)
###             검색 조건에는 포함되나 추출 결과에는 포함되지 않도록 함
###             ex. .*(?=-레몬스토어)
### (?!abc)  →  negative lookahead(부정형 전방 탐색)
###             해당 문자열이 포함되지 않는 검색 조건으로 전방 탐색
###             ex. .*(?= -(?!레몬).*스토어)
### cf. (?<=abc) positive look behind  (?<!ABC) negative lookbehind
