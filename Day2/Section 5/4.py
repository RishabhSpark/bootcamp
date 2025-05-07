from collections import deque

stack = deque()
stack.append(10)
stack.append(2)
stack.append(3)
stack.pop()

print(stack)


queue = deque()
queue.appendleft(2)
queue.appendleft(5)
queue.appendleft(3)
queue.popleft()

print(queue)
