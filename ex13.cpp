#include<bits/stdc++.h>
using namespace std;
int front;
int rear=front=-1;
string order_no;
bool isfull(int n)
{
    if((rear==n-1 && front==0) || (rear==(front-1)%(n-1)))
    {
        return true;
    }
    else
    {
        return false;
    }
}
bool isempty(int n)
{
    if(front==-1)
    {
        return true;
    }
    else
    {
        return false;
    }
}
void push(string arr[], int n)
{
    if(isfull(n)==true)
    {
        cout<<"The order is reached to its maximum limit."<<endl;
    }
    else if (rear==n-1)
    {
        rear=0;
        cout<<"Enter the order number : ";
        cin>>order_no;
        arr[rear]=order_no;
    }
    else if (isempty(n)==true)
    {
        rear=front=0;
        cout<<"Enter the order number : ";
        cin>>order_no;
        arr[rear]=order_no;
    }
    else
    {
        rear++;
        cout<<"Enter the order number : ";
        cin>>order_no;
        arr[rear]=order_no;
    }
}

void display(string arr[],int n)
{
    cout<<"**DISPLAY**\n";
            if(front<=rear)
            {
                for(int i=front;i<=rear;i++)
                {
                    cout<<arr[i]<<" ";
                }
            }
            else if (rear<=front)
            {
                for(int i=rear;i<=front;i++)
                {
                    cout<<arr[i]<<" ";
                }
            }
            cout<<endl;
            
}
int main()
{
    int n, choice;
    int start=0;
    cout<<"Enter the maximum number of order : ";
    cin>>n;
    string arr[n];
    while(start==0)
    {
        cout<<"**MENUE**"<<endl;
        cout<<"Press 1: To place the order."<<endl

        <<"Press 2: To exit."<<endl;
        cout<<"Enter your choice : ";
        cin>>choice;
        switch(choice)
        {
            case 1:
            push(arr, n);
            display(arr, n);
            break;

        

            case 2:
            start++;
            break;

            default:
            cout<<"You have entered a wrong choice."<<endl;
        }
    }

    return 0;
}

/*Traffic Light is also a real-time application of circular queue.*/
