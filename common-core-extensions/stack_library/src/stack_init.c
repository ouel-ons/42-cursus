#include "stack.h"

void    stack_init(t_stack  *s, char name)
{
    s->top = NULL;
    s->bottom = NULL;
    s->size = 0;
    s->name = name;
}