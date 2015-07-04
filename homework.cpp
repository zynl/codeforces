/*
*\Question: peak founder
*\Idea: 二分法
*\Algorithm complexity:  
1 3 2 4 5 6 7 8 9 10
*/
#include<iostream>
using namespace std
const int maxn = 10 
int a[maxn];

int main()
{
    for(int i = 0; i < maxn; i++)
    {
        cin >> a[i];
    }
    cout << solve(0, maxn - 1) << endl;    
}

int solve(int start, int end)
{
    int temp = (start + end) / 2
    if(arry[temp] > arry[temp - 1] && arry[temp] > arry[temp + 1])
        return arry[temp]
    else if(arry[temp] > arry[temp - 1] && arry[temp] < arry[temp + 1])
        return solve(temp, end)
    else if(arry[temp] < arry[temp - 1] && arry[temp] > arry[temp + 1])     
        return solve(start, temp)
}