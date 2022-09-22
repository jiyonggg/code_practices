#include <stdio.h>
#include "object.h"

int main() {
    Object obj = _object_init();
    obj.method(&obj);

    return 0;
}