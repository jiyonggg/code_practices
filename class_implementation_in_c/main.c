#include <stdio.h>
#include "object.c"

int main() {
    Object obj = _object_init();
    obj.method(&obj);

    return 0;
}