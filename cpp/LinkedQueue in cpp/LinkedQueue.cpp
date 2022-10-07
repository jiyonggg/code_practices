#include <iostream>
#include "Node.cpp"

class LinkedQueue {
    public:
        Node *front;
        Node *rear;
        LinkedQueue() {
            this->front = nullptr;
            this->rear = nullptr;
        }
        ~LinkedQueue() {
            while (!this->isEmpty()) {
                this->dequeue();
            }
        }
        bool isEmpty() {
            return this->front == nullptr;
        }
        void enqueue(int data) {
            Node *node = new Node;
            node->data = data;
            node->link = nullptr;

            if (this->isEmpty()) {
                this->front = node;
            } else {
                this->rear->link = node;
            }
            this->rear = node;
        }
        int dequeue() {
            if (!this->isEmpty()) {
                Node *node = this->front;
                int result = node->data;
                this->front = node->link;

                if (this->front == nullptr) {
                    this->rear = nullptr;
                }
                delete node;
                return result;
            }
        }
        int peek() {
            if (!this->isEmpty()) {
                return this->front->data;
            }
        }
        void display() {
            std::cout << "Queue: ";
            Node *node = this->front;
            while (node != nullptr) {
                std::cout << node->data << " ";
                node = node->link;
            }
            std::cout << std::endl;
        }
};