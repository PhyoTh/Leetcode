#include <stack>
#include <limits>
#include <algorithm>
#include <utility>
using namespace std;

class MinStack {
private:
    stack<pair<int, int>> stk;
    int minimum;

public:
    MinStack() {
        this->minimum = numeric_limits<int>::max();
    }

    void push(int value) {
        int minSoFar = value;
        if (!this->stk.empty()) {
            pair<int, int> p = this->stk.top();
            minSoFar = min(minSoFar, p.second);
        }
        this->stk.push({value, minSoFar});
        this->minimum = min(this->minimum, minSoFar);
    }
    
    void pop() {
        if (this->stk.empty())
            return;

        this->stk.pop();
        if (this->stk.empty())
            this->minimum = numeric_limits<int>::max();
        else
            this->minimum = this->stk.top().second;
    }
    
    int top() {
        if (this->stk.empty())
            return -1;
        return this->stk.top().first;
    }
    
    int getMin() {
        return this->minimum;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(value);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */