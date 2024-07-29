#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a, b, c;

    printf("Enter the first integer (a): ");
    scanf("%d", &a);
    printf("Enter the second integer (b): ");
    scanf("%d", &b);
    printf("Enter the third integer (c): ");
    scanf("%d", &c);

    if (a >= 2 && b <= 0) {
        printf("The value range fits in the domain\n");
    } else {
        printf("The value range is out of the domain\n");
    }


    if (a < 15 || c > -4) {
        printf("Values are ok\n");
    } else {
        printf("Values are not okay\n");
    }


    if (a % 2 != 0) {
        printf("The value is odd\n");
    } else {
        printf("The value is even\n");
    }


    printf("\nAdditional Boolean Operations:\n");

    printf("a AND b: %d && %d = %d\n", a, b, a && b);


    printf("a OR b: %d || %d = %d\n", a, b, a || b);


    printf("NOT a: !%d = %d\n", a, !a);
    printf("NOT b: !%d = %d\n", b, !b);
    printf("NOT c: !%d = %d\n", c, !c);


    printf("\nCombination of Boolean Operators:\n");

    printf("a AND (NOT b): %d && !%d = %d\n", a, b, a && !b);
    printf("(NOT a) OR b: !%d || %d = %d\n", a, b, !a || b);
    printf("(a AND b) OR (NOT a): (%d && %d) || !%d = %d\n", a, b, a, (a && b) || !a);
    printf("(a OR b) AND (NOT c): (%d || %d) && !%d = %d\n", a, b, c, (a || b) && !c);





    return 0;
}
