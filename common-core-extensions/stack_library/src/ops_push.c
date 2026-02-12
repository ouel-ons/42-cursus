#include "stack.h"

static void	putop(const char *s)
{
	write(1, s, 2);
	write(1, "\n", 1);
}

int	op_pa(t_stack *a, t_stack *b)
{
	t_node	*n;

	n = stack_pop_top(b);
	if (!n)
		return (0);
	stack_push_top(a, n);
	putop("pa");
	return (1);
}

int	op_pb(t_stack *a, t_stack *b)
{
	t_node	*n;

	n = stack_pop_top(a);
	if (!n)
		return (0);
	stack_push_top(b, n);
	putop("pb");
	return (1);
}
