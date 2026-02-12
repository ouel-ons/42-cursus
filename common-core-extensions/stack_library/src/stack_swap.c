#include "stack.h"

int stack_swap_top2(t_stack *s)
{
    t_node  *first;
    t_node  *second;
    if (!s || s->size == 0)
        return (0);
    first = s->top;
    second = s->top->next;
    first->next = second->next;
    second->next = first;
    s->top = second;
    if (s->size == 2)
        s->bottom = first;
    return 1;
}