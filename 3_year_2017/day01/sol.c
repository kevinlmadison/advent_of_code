#include <stdio.h>

int main(int argc, char *argv[]) {
    FILE * file = fopen("input.txt", "r");

    char * feed = NULL;
    size_t len = 0;

    getline(&feed, &len, file);

    int sum = 0;
    int x1;
    int x2;
    for(int i = 0; i < len; i++) {
        x1 = atoi(feed[i]);
        x2 = atoi(feed[(i+1)%len]);
        printf("%d, ", x1);
        if (x1 == x2) {
            sum += x1;
        }
    }

    printf("%d\n",sum);

    return 0;
}
