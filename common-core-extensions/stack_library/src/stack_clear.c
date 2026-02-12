#include "stack.h"

void    stack_clear(t_stack *s)
{
    t_node  *cur;
    t_node  *next;
    if (!s)
        return;
    cur = s->top;
    while (cur)
    {
        next = cur->next;
        free(cur);
        cur = next;
    }
    s->top = NULL;
    s->bottom = NULL;
    s->size = 0;
}