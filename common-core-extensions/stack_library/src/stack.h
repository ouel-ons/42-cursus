#ifndef STACK_H
# define STACK_H

# include <unistd.h>
# include <stdlib.h>

typedef struct s_node
{
    int v;
    int idx;
    struct s_node   *next;
}   t_node;

typedef struct s_stack
{
    t_node  *top;
    t_node  *bottom;
    int size;
    char    name;
}   t_stack;

/* ====== core (no printing) ====== */
void	stack_init(t_stack *s, char name);
t_node	*node_new(int v);

int		stack_push_top(t_stack *s, t_node *n);
t_node	*stack_pop_top(t_stack *s);

int		stack_swap_top2(t_stack *s);
int		stack_rotate(t_stack *s);
int		stack_rev_rotate(t_stack *s);

void	stack_clear(t_stack *s);

/* ====== ops (print instruction) ====== */
int		op_sa(t_stack *a);
int		op_sb(t_stack *b);
int		op_ss(t_stack *a, t_stack *b);

int		op_pa(t_stack *a, t_stack *b);
int		op_pb(t_stack *a, t_stack *b);

int		op_ra(t_stack *a);
int		op_rb(t_stack *b);
int		op_rr(t_stack *a, t_stack *b);

int		op_rra(t_stack *a);
int		op_rrb(t_stack *b);
int		op_rrr(t_stack *a, t_stack *b);



#endif