// linear congruential generator


#include <stdio.h>

#define A 1103515245
#define C 12345
#define M 2147483648

int main() {
    // Set the initial value for the LCG algorithm
    long int prev = 1;
    
    // Generate 10 random numbers between 1 and 100 using the LCG algorithm
    for (int i = 0; i < 10; i++) {
        // Generate a random number using the LCG algorithm
        long int rand_num = (A * prev + C) % M;
        // Scale the random number to the range 1-100
        rand_num = rand_num % 100 + 1;
        // Update the previous value for the LCG algorithm
        prev = rand_num;
        // Print the generated number
        printf("%ld\n", rand_num);
    }
    
    return 0;
}
