#include <stdio.h>

#define bool int
#define False 0
#define True 1
#define Max_Digits_Scale 10
int getSquaresSum(int digits[], int length);
void getDigits(int number, int digits[], int *length);

bool isHappy(int n) {
    int digits[Max_Digits_Scale];
    int number = n;
    int length = 0;
    int sum;
    int count = 0;
    int max_count = Max_Digits_Scale * 9 * 9;
    bool ret = True;
    do {
        getDigits(number, digits, &length);
        sum = getSquaresSum(digits, length);
        count++;
        if (count >= max_count) {
            ret = False;
            break;
        }
        number = sum;
    } while (sum != 1);
    return ret;
}

int getSquaresSum(int digits[], int length) {
    int sum = 0;
    for (int i = 0; i < length; i++) {
        int digit = digits[i];
        sum += digit * digit;
    }
    return sum;
}

void getDigits(int number, int digits[], int *length) {
    int index = 0;
    while (number > 0) {
        digits[index++] = number % 10;
        number = number / 10;
    }
    *length = index;
}

int main(int argc, char *argv[]) {
    int n;
    while (1) {
        scanf("%d", &n);
        printf("current number: %d\n", n);
        bool happy = isHappy(n);
        if (happy == True) {
            printf("number %d is happy number\n", n);
        } else {
            printf("number %d is not happy number\n", n);
        }
    }
}
