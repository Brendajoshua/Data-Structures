Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
    0(1)

2. What is the runtime complexity of `dequeue`?
    0(1)

3. What is the runtime complexity of `len`?
    0(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`? 

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`? 

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
    0(1)

2. What is the runtime complexity of `ListNode.insert_before`?
    0(1)

3. What is the runtime complexity of `ListNode.delete`?
    0(1)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
    0(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
    0(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
    0(1)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
    0(1)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
    0(1)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
    0(1)

10. What is the runtime complexity of `DoublyLinkedList.delete`?
    0(1)

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    `Array.splice` in JavaScript has a worst-case runtime of O(n), which is worse than the `delete` method in the doubly linked list. When used to delete items from an array, `Array.splice` has the possibility of shifting all the elements over.