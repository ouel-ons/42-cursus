#include "stack.h"

t_node  *node_new(int v)
{
    t_node  *n;
    n = (t_node *)malloc(sizeof(t_node));
    if (!n)
        return (NULL);
    n->v = v;
    n->idx = -1;
    n->next = NULL;
    return (n);
}