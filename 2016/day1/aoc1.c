#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

struct direction {
    char *dir[4];
};

int main(int argc, char *argv[])
{
    FILE *ptr_file = fopen("aoc1.txt", "r");
    char buf[1000];

    if(!ptr_file){
        return 1;
    }

    while (fgets(buf, 1000, ptr_file) != NULL) {
        printf("%s", buf);
    }

    fclose(ptr_file);
    return 0;
}
