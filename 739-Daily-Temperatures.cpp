#include <stack>
using namespace std;

class Solution {
private:
    vector<int> vec;
    stack<int> stk;

public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        this->vec = vector<int>(temperatures.size(), 0);

        for (int i = 0; i < temperatures.size(); ++i) {
            while (!this->stk.empty() and temperatures[this->stk.top()] < temperatures[i]) {
                int j = this->stk.top();
                this->stk.pop();
                this->vec[j] = i - j;
            }
            this->stk.push(i);
        }

        return this->vec;
    }
};