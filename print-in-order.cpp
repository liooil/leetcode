#include <condition_variable> 

class Foo {
public:
    Foo()
        :
        printMutexs{} {
        printMutexs[0].lock();
        printMutexs[1].lock();
    }

    void first(function<void()> printFirst) {
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        printMutexs[0].unlock();
    }

    void second(function<void()> printSecond) {
        printMutexs[0].lock();
        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        printMutexs[1].unlock();
    }

    void third(function<void()> printThird) {
        printMutexs[1].lock();
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
    }
private:
    std::mutex printMutexs[2];
};