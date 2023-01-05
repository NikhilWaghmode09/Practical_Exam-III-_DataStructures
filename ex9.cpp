#include <iostream>
#include <string>

using namespace std;

// Stack implementation using an array
const int MAX_SIZE = 100;

class Stack
{
private:
    char arr[MAX_SIZE];
    int top;

public:
    Stack()
    {
        top = -1;
    }

    bool is_empty()
    {
        return top == -1;
    }

    bool is_full()
    {
        return top == MAX_SIZE - 1;
    }

    void push(char c)
    {
        if (is_full())
        {
            cout << "Error: Stack is full" << endl;
            return;
        }
        arr[++top] = c;
    }

    char pop()
    {
        if (is_empty())
        {
            cout << "Error: Stack is empty" << endl;
            return '\0';
        }
        return arr[top--];
    }
};

// Function to reverse a string using a stack
string reverse_string(string s)
{
    Stack st;
    for (char c : s)
        st.push(c);

    string reversed = "";
    while (!st.is_empty())
        reversed += st.pop();
    return reversed;
}

// Function to check if a string is a palindrome
bool is_palindrome(string s)
{
    string reversed = reverse_string(s);
    return s == reversed;
}

int main()
{
    string s;
    cout << "Enter a string: ";
    getline(cin, s);
    cout << "Original string: " << s << endl;
    cout << "Reversed string: " << reverse_string(s) << endl;
    cout << "Is palindrome: " << boolalpha << is_palindrome(s) << endl;

    return 0;
}
