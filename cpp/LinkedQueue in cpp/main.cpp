#include <iostream>
#include "LinkedQueue.cpp"

int main() {
    std::cout << "Main Function Started" << std::endl;
    LinkedQueue *q = new LinkedQueue;
    std::cout << "isEmpty(): " << q->isEmpty() << std::endl;
    q->enqueue(5);
    q->enqueue(4);
    q->enqueue(7);
    q->enqueue(8);
    q->enqueue(4);
    q->display();
    std::cout << "isEmpty(): " << q->isEmpty() << std::endl;
    std::cout << "dequeue: " << q->dequeue() << std::endl;
    std::cout << "peek: " << q->peek() << std::endl;
    std::cout << "dequeue: " << q->dequeue() << std::endl;
    q->display();
    std::cout << "peek: " << q->peek() << std::endl;
    std::cout << "dequeue: " << q->dequeue() << std::endl;
    std::cout << "dequeue: " << q->dequeue() << std::endl;
    q->display();
    std::cout << "Main Function Finished" << std::endl;
    delete q;
    return 0;
}