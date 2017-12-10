// THIS IS NOT MINE, I FOUND THIS ON REDDIT AND WANTED TO REFERENCE IT LATER
#include <stdio.h>

enum State {
    NONE, GARBAGE, IGNORE,
};

int main(int argc, char ** argv) {
    FILE * file = fopen("input.txt", "r");

    char * feed = nullptr;
    size_t len = 0;
    getline(&feed, &len, file);

    State state = NONE;
    int sum = 0;
    int level = 0;
    int chars = 0;
    for (int i = 0; i < len; ++i) {
        char ch = feed[i];
        if (state == NONE) {
            if (ch == '<') {
                state = GARBAGE;
            } else if (ch == '{') {
                level += 1;
            } else if (ch == '}') {
                sum += level;
                level -= 1;
            }
        } else if (state == GARBAGE) {
            if (ch == '!') {
                state = IGNORE;
            } else if (ch == '>') {
                state = NONE;
            } else {
                chars += 1;
            }
        } else if (state == IGNORE) {
            state = GARBAGE;
        }
    }

    printf("%d\n", sum);
    printf("%d\n", chars);

    return 0;
}
