


# 2번
## 0을 앞에 채워 길이를 맞추는 작업
def func_a(string, length):
	padZero = ""
	padSize = length - len(string)
	print(padSize)
	for i in range(padSize):
		padZero += "0"
	return padZero + string

def solution(binaryA, binaryB):
	max_length = max(len(binaryA), len(binaryB))
	binaryA = func_a(binaryA, max_length)
	binaryB = func_a(binaryB, max_length)

	hamming_distance = 0
	for i in range(max_length):
		if binaryA[i] != binaryB[i] :
			hamming_distance += 1
	return hamming_distance

binaryA = "10010"
binaryB = "110"
ret = solution(binaryA, binaryB)

print("solution 함수의 반환 값은", ret, "입니다.")


# 3번 계산기 by 문자열
def func_a(numA, numB, exp):								# 13. 123, 12, +
	if exp == '+':											# 14. exp가 + 이므로 123+12 = 135
		return numA + numB
	elif exp == '-':
		return numA - numB
	elif exp == '*':
		return numA * numB

def func_b(exp):											# 3. '123+12' 받음
	for index, value in enumerate(exp):						# 4. enumerate : 순서 , 값 가져옴
		if value == '+' or value == '-' or value == '*':	# 5. value가 연산자면 index값 리턴
			return index									# 6 나오는 값 : 3 을 다시 solution 함수로

print()
def func_c(exp, idx):										# 8. '123+12' , 3 받음
	numA = int(exp[:idx])									# 9.  123+12[:3] -> 123
	numB = int(exp[idx + 1:])								# 10. 123+12[4:] -> 12

	return numA, numB										# 11. 123 과 12 리턴

print()
def solution(expression):									# 1. 123+12 str형태로 넣음
	exp_index = func_b(expression) 							# 2. '123+12' 를 func_b로 	-> 3 +
	first_num, second_num = func_c(expression , exp_index)	# 7. '123+12' , 3 을 func_c로-> 123, 12
	result = func_a(first_num, second_num, expression[exp_index]) #12. 123, 12, + 을 func_a로
	return result											# 15. func_a 값 (135) 리턴


a = "123+12"
ret = solution(a)											# 16. solution 함수의 값 리턴
print("solution 함수의 반환 값은", ret, "입니다.")				# 17. soultion 함수 값 출력




# 5번 소용돌이 수

n = 4
nn = n * n
r = [0 , 1 , 0 , -1]	# 행 변화
c = [1 , 0 , -1 , 0]	# 렬 변화

a = []
for i in range(nn) :
	i += 1
	a.append(i)
print(a)

def recursive_function(i) :
	if i == 5 :
		return
	print(i, i+1)
	recursive_function(i + 1)
	print(i)

#recursive_function(1)


## dfs
def dfs(graph , v , visited) :
	visited[v] = True
	print(v , end=" ")
	for i in graph[v] :
		if not visited[i] :
			dfs(graph, i , visited)
graph = [
	[],
	[2,3,8],
	[1,7],
	[1,4,5],
	[3,5],
	[3,4],
	[7],
	[2,6,8],
	[1,7]
]
visited = [False] * 9
dfs(graph , 1, visited)


print()
from collections import deque
def bfs(graph , start , visited) :

	queue = deque([start])

	visited[start] = True

	while queue :
		v = queue.popleft()
		print(v, end=' ')
		for i in graph[v] :
			if not visited[i] :
				queue.append(i)
				visited[i] = True

graph = [
	[],
	[2,3,8],
	[1,7],
	[1,4,5],
	[3,5],
	[3,4],
	[7],
	[2,6,8],
	[1,7]
]
visited = [False] * 9
bfs(graph , 1, visited)




