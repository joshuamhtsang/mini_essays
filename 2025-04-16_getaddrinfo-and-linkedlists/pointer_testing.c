#include <stdio.h>
#include <stdlib.h>

typedef struct Person {
    // Data
    char *name;
    int age;

    // Pointer to next object
    struct Person *next;
} Person;

void printLinkedListUsingWhileLoop(Person *head) {
    Person *current = head;

    while (current != NULL) {
        printf("Name : %s\n", current->name);
        printf("Age : %d\n", current->age);
        current = current->next;
    }
}

void printLinkedListUsingForLoop(Person *head) {
    Person *ptr;

    for (ptr=head; ptr!= NULL; ptr = ptr->next) {
        printf("Name : %s\n", ptr->name);
        printf("Age : %d\n", ptr->age);
    }
}

int main(int argc, char *argv[])
{
    // Some pointer basics
    int a = 10;
    int *ptr = &a;

    printf("Address of a: %p\n", (void*)&a);
    printf("Address of a (via pointer): %p\n", ptr);
    printf("Size of a pointer: %zu bytes\n", sizeof(void *));
    printf("Value of a: %d\n", a);
    printf("Value of a (via dereference of pointer): %d\n", *ptr);

    // Linked list example

    Person *person1 = malloc(sizeof(Person)); // malloc() returns the starting address of a contiguous block of memory allocated
    person1->name = "Joshua"; // 'X->Y' means "the member Y of what is pointed to by X" (Accelerated C++ book)
    person1->age = 25;
    printf("Name: %s\n", person1->name);
    printf("Age: %d\n", person1->age);

    Person *person2 = malloc(sizeof(Person));
    person2->name = "Elsie";
    person2->age = 22;
    printf("Name: %s\n", person2->name);
    printf("Age: %d\n", person2->age);

    // Link Elsie to Josh
    person1->next = person2;

    // It is convention to end a linked list with a NULL
    person2->next = NULL;

    // Print the entire linked list 2 different ways
    printLinkedListUsingWhileLoop(person1); // You pass in the 'head' of the linked list
    printLinkedListUsingForLoop(person1);

    // Free up memory
    free(person1);
    free(person2);

    return 0;
}