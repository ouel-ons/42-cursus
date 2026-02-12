#include "stack.h"
#include <stdio.h>

static void	del_int(void *p)
{
	free(p);
}

int main(void)
{
	t_stack	*s = NULL;

	int *x = malloc(sizeof(int));
	int *y = malloc(sizeof(int));
	*x = 42;
	*y = 7;

	ft_stack_push(&s, x);
	ft_stack_push(&s, y);

	printf("peek = %d\n", *(int *)ft_stack_peek(s));  // 7
	printf("size = %d\n", ft_stack_size(s));          // 2

	int *popped = (int *)ft_stack_pop(&s);
	printf("pop = %d\n", *popped);                    // 7
	free(popped);

	ft_stack_clear(&s, del_int);                      // frees remaining int*
}
