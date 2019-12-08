from stack_impl_linked_list import Stack
from queue_impl_linked_list import Queue


def reverse_queue(queue):
    """
    Returns the reversed queue for a queue input. Creates a separate queue that is reverse of the original queue, doesn't modify the original queue in place
        :params: -
            queue - queue to reverse
        :output: -
            queue - reversed queue
    Time complexity - 
    """
    stack = Stack()
    original_queue = Queue()
    rev_queue = Queue()

    # creating the stack
    while not queue.is_empty():
        element = queue.dequeue()
        stack.push(element)
        original_queue.enqueue(element)

    # creating the reverse stack
    while not stack.is_empty():
        element = stack.pop()
        rev_queue.enqueue(element)

    # reinstating the original queue
    queue = original_queue
    return rev_queue


queue = Queue()
queue.enqueue("I am deadshot")
queue.enqueue(", and you are dust")
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)


print(queue)
print(reverse_queue(queue))
print(queue)
