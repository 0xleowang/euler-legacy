#include <stdio.h>
#include <math.h>

long int P(int n);
int check_P(long int p);

int
main(int argc, char *argv[]) {
    int a, b, finded = 0;

    for(a = 1; !finded; a++) {
        for(b = 1; b < a && !finded; b++) {
            if(check_P(P(a) + P(b)) && check_P(P(a) - P(b))) {
                printf("%ld\n", P(a) - P(b));
                finded = 1;
            }
        }
    }

    return 0;
}

long int
P(int n) {
    return n * (3 * n - 1) / 2;
}

int
check_P(long int p) {
    double n;

    n = (1 + sqrt(1 + 24 * p)) / 6;

    if((int)n == n) { 
        return 1;
    } else {
        return 0;
    }
}
