#include "stack.h"

void	ft_stack_push(t_stack **stack, void *data)
{
	t_stack	*n;

	if (!stack)
		return ;
	n = (t_stack *)malloc(sizeof(t_stack));
	if (!n)
		return ;
	n->data = data;
	n->next = *stack;
	*stack = n;
}

void	*ft_stack_pop(t_stack **stack)
{
	t_stack	*top;
	void	*data;

	if (!stack || !*stack)
		return (NULL);
	top = *stack;
	data = top->data;
	*stack = top->next;
	free(top);
	return (data);
}

void	*ft_stack_peek(t_stack *stack)
{
	if (!stack)
		return (NULL);
	return (stack->data);
}

int	ft_stack_size(t_stack *stack)
{
	int	n;

	n = 0;
	while (stack)
	{
		n++;
		stack = stack->next;
	}
	return (n);
}

int	ft_stack_is_empty(t_stack *stack)
{
	return (stack == NULL);
}

void	ft_stack_clear(t_stack **stack, void (*del)(void *))
{
	void	*data;

	if (!stack)
		return ;
	while (*stack)
	{
		data = ft_stack_pop(stack);
		if (del)
			del(data);
	}
}
