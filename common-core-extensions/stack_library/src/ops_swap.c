#include "stack.h"

static void	putop(const char *s)
{
	write(1, s, 3);
	write(1, "\n", 1);
}

int	op_sa(t_stack *a)
{
	if (stack_swap_top2(a))
		return (putop("sa"), 1);
	return (0);
}

int	op_sb(t_stack *b)
{
	if (stack_swap_top2(b))
		return (putop("sb"), 1);
	return (0);
}

int	op_ss(t_stack *a, t_stack *b)
{
	int	xa;
	int	xb;

	xa = stack_swap_top2(a);
	xb = stack_swap_top2(b);
	if (xa || xb)
		return (putop("ss"), 1);
	return (0);
}
