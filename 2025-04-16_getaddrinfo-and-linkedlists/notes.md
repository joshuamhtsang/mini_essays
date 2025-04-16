# getaddrinfo() and Linked Lists

## getaddrinfo()

This is a function provided by `<netdb.h>` available on Unix systems that works with a struct called `addrinfo` that is also provided by the same header file.

https://beej.us/guide/bgnet/html/split-wide/system-calls-or-bust.html#getaddrinfoprepare-to-launch

`showip.c` demonstrates how to use `getaddrinfo()`.  Note that this function returns an error code, and the interesting information is filled in a linked list of `addrinfo` structs:

1. A pointer to a 'hint' addrinfo struct that tells (or hints!) `getaddrinfo()` what we want
2. A pointer to a linked list of results (**res), this is where our results will be if execution succeeds

The function signature is as follows:
~~~
#include <netdb.h>

int getaddrinfo(const char *node,     // e.g. "www.example.com" or IP
                const char *service,  // e.g. "http" or port number
                const struct addrinfo *hints,
                struct addrinfo **res);
~~~

To compile and run:
~~~
$ gcc showip.c -o showip
$ ./showip
~~~

## Linked Lists

Since the results of `getaddrinfo` are returned as a linked list, its instructive to know how linked lists work.  `pointer_testing.c` contains some pointer basics and an example of a linked lists.  It shows two different ways of iterating though a linked list.

To compile and run:
~~~
$ gcc pointer_testing.c -o pointer_testing
$ ./pointer_testing
~~~