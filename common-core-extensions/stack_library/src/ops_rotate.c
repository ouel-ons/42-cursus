#include "stack.h"

static void	putop2(const char *s)
{
	write(1, s, 2);
	write(1, "\n", 1);
}

static void	putop3(const char *s)
{
	write(1, s, 3);
	write(1, "\n", 1);
}

int	op_ra(t_stack *a)
{
	if (stack_rotate(a))
		return (putop2("ra"), 1);
	return (0);
}

int	op_rb(t_stack *b)
{
	if (stack_rotate(b))
		return (putop2("rb"), 1);
	return (0);
}

int	op_rr(t_stack *a, t_stack *b)
{
	int	xa;
	int	xb;

	xa = stack_rotate(a);
	xb = stack_rotate(b);
	if (xa || xb)
		return (putop2("rr"), 1);
	return (0);
}

int	op_rra(t_stack *a)
{
	if (stack_rev_rotate(a))
		return (putop3("rra"), 1);
	return (0);
}

int	op_rrb(t_stack *b)
{
	if (stack_rev_rotate(b))
		return (putop3("rrb"), 1);
	return (0);
}

int	op_rrr(t_stack *a, t_stack *b)
{
	int	xa;
	int	xb;

	xa = stack_rev_rotate(a);
	xb = stack_rev_rotate(b);
	if (xa || xb)
		return (putop3("rrr"), 1);
	return (0);
}
