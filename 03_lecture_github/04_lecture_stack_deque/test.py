from collections import deque
my_deque = deque()
my_deque.append(1)
my_deque.append(2)
my_deque.append(3)
my_deque.append(4)
my_deque.append(5)
my_deque.append(6)
while my_deque:
	a = my_deque.popleft()
	print(a)
	my_deque.appendleft(a)
	a = my_deque.popleft()

	#
	# my_stack = []
	# my_stack.append(1)
	# my_stack.append(2)
	# my_stack.append(3)
	# my_stack.append(4)
	# my_stack.append(5)
	# my_stack.append(6)
	# while my_stack:
	# 	print(my_stack.pop())
