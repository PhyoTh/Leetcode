#include <stack>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> Stack;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == ')') {
                if (Stack.empty() || Stack.top() != '(')
                    return false;
                Stack.pop();
            }
            else if (s[i] == '}') {
                if (Stack.empty() || Stack.top() != '{')
                    return false;
                Stack.pop();
            }
            else if (s[i] == ']') {
                if (Stack.empty() || Stack.top() != '[')
                    return false;
                Stack.pop();
            }
            else {
                Stack.push(s[i]);
            }
        }
        if (Stack.empty())
            return true;
        else
            return false;
    }
};