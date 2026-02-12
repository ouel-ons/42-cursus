#include "stack.h"

int stack_rotate(t_stack *s)
{
    t_node *first;
    if (!s || s->size < 2)
        return 0;
    first = s->top;
    s->top = s->top->next;
    first->next = NULL;
    s->bottom->next = first;
    s->bottom = first;
    return 1;
}

int stack_rev_rotate(t_stack *s)
{
    t_node *pre;
    t_node *cur;
    if (!s || s->size < 2)
        return 0;
    cur = s->top;
    pre = NULL;
    while (cur->next)
    {
        pre = cur;
        cur = cur->next;
    }
    pre->next = NULL;
    cur->next = s->top;
    s->top = cur;
    s->bottom = pre;
    return 1;
}