// In quest for how object can be implemented in C lang...

#include <stdio.h>
#include <string.h>

struct _Object;
typedef void (*method_ptr)(struct _Object *_self);

typedef struct _Object {
    char name[300];
    method_ptr method;
} Object;

void _object_method(Object *_self) {
    printf("Hello, Object (%s)!\n", _self->name);
}

// Class Constructor
Object _object_init() {
    Object obj;
    strcpy(obj.name, "Test");

    obj.method = _object_method;
    return obj;
}