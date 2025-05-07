from collections import deque

# Rotate a deque by 2 positions
dq = deque([1, 2, 3, 4, 5])
print("Original deque:", dq)
dq.rotate(2)
print("Deque after rotating 2 positions:", dq)
