# queue - FIFO(First In First Out)

queue = [3, 4, 6, 8, 9, 1]
print("Original queue is :", queue)
queue.append(7)
print("Queue after insertion is :", queue)
queue.pop(0)
print("Queue after deletion is :", queue)
print("Value obtained after peep operation is :", queue[(len(queue) - 1)])
