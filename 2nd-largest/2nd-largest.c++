#include <stdio.h>
#include <conio.h>

int main () {
    int arr[8] = [25, 16, 38, 10, 35, 48, 20, 50];
    int n = 8;

    int max_1, max_2;
    
    if(arr[0] > arr[1])
        {
            max_1 = arr[0];
            max_2 = arr[1];
        } else {
            max_1 = arr[1];
            max_2 = arr[0];
        }
    
    for (int i = 2; i<= n-1; i++)
    {
        if (arr[i] > max_1)
        {
            max_2 = max_1;
            max_1 = arr[i];
        } else if (arr[i] > max_2){
            max_2 = arr[i];
        }
    }     
    printf("2nd Largest: %d", max_2);
}
