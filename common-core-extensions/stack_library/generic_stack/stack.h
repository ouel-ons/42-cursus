#ifndef FT_STACK_H
# define FT_STACK_H

# include <stdlib.h>

typedef struct s_stack
{
	void			*data;
	struct s_stack	*next;
}	t_stack;

void	ft_stack_push(t_stack **stack, void *data);
void	*ft_stack_pop(t_stack **stack);
void	*ft_stack_peek(t_stack *stack);
int		ft_stack_size(t_stack *stack);
int		ft_stack_is_empty(t_stack *stack);
void	ft_stack_clear(t_stack **stack, void (*del)(void *));

#endif
