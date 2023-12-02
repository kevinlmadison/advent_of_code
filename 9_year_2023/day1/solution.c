/* 
    $ clang -std=c99 -Wall solution.c -o run_solution
    $ ./run_solution
*/
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <regex.h>

#define MAX_INPUT_LENGTH 50

void strrev(char *str) {
    if (str == NULL) {
        return; // Handle NULL pointer input
    }

    int length = strlen(str);
    int start = 0;
    int end = length - 1;

    while (start < end) {
        // Swap characters at start and end indices
        char temp = str[start];
        str[start] = str[end];
        str[end] = temp;

        // Move start and end pointers towards the center
        start++;
        end--;
    }
}

int part1(char *inputs[], int num_inputs) {
    int total = 0;
    regex_t regex;
    regmatch_t match_f, match_b;

    char *pattern = "[1-9]";
    if (regcomp(&regex, pattern, REG_EXTENDED | REG_ICASE) != 0) {
        fprintf(stderr, "Regex compilation failed\n");
        return -1;
    }

    int i;
    for (i = 0; i < num_inputs; i++) {
        if (regexec(&regex, inputs[i], 1, &match_f, 0) == 0) {
            char first = inputs[i][match_f.rm_so] - '0';

            char *reverse_input = strdup(inputs[i]);
            strrev(reverse_input);

            if (regexec(&regex, reverse_input, 1, &match_b, 0) == 0) {
                char last = reverse_input[match_b.rm_so] - '0';
                total += (first * 10) + last;
            }

            free(reverse_input);
        }
    }

    regfree(&regex);
    return total;
}

int main(int argc, char** argv) {
    FILE *file;
    file = fopen("input", "r");
    if (file == NULL) {
        perror("Error opening file");
        return EXIT_FAILURE;
    }

    int num_inputs = 0;
    char **inputs = NULL;
    char line[MAX_INPUT_LENGTH];

    while (fgets(line, sizeof(line), file) != NULL) {
        line[strcspn(line, "\n")] = '\0'; // Remove newline character
        
        // Dynamically allocate memory for each input
        char *input = strdup(line);
        if (input == NULL) {
            perror("Memory allocation failed");
            return EXIT_FAILURE;
        }

        // Resize the inputs array to accommodate a new input
        char **temp = realloc(inputs, (num_inputs + 1) * sizeof(char *));
        if (temp == NULL) {
            perror("Memory allocation failed");
            free(input); // Free the last allocated input
            return EXIT_FAILURE;
        }
        inputs = temp;
        
        inputs[num_inputs++] = input;
    }

    fclose(file);

    int result = part1(inputs, num_inputs);
    printf("Total: %d\n", result);

    // Free allocated memory for inputs
    for (int i = 0; i < num_inputs; i++) {
        free(inputs[i]);
    }
    free(inputs);

    return 0;
}
