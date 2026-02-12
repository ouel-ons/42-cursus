#include "stack.h"

int stack_push_top(t_stack  *s, t_node  *n)
{
    if (!n || !s)
        return 0;
    n->next = s->top;
    s->top = n;
    if (s->size == 0)
        s->bottom = n;
    s->size++;
    return 1;
}

t_node *stack_pop_top(t_stack   *s)
{
    t_node  *n;
    if (!s || s->size == 0)
        return (NULL);
    n = s->top;
    s->top = s->top->next;
    n->next = NULL;
    s->size--;
    if (s->size == 0)
        s->bottom = NULL;
    return n;
}