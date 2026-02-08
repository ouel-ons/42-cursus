/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   checker.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 23:58:56 by ouel-ons          #+#    #+#             */
/*   Updated: 2026/01/16 23:58:59 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap_bonus.h"

static int	is_stack_empty(t_node *stack)
{
	int	i;

	i = 0;
	while (stack[i].index != -1)
	{
		if (stack[i].filled == 1)
			return (0);
		i++;
	}
	return (1);
}

static void	check_solution(t_node *a, t_node *b)
{
	if (is_sorted(a) == 1 && is_stack_empty(b))
		ft_putstr_fd("OK\n", 1);
	else
		ft_putstr_fd("KO\n", 1);
}

// New helper to fix TOO_MANY_LINES in main
static void	process_instructions(t_node *a, t_node *b)
{
	char	*line;

	line = get_next_line(0);
	while (line)
	{
		exec_instruction(a, b, line);
		free(line);
		line = get_next_line(0);
	}
}

int	main(int argc, char **argv)
{
	t_node	*a;
	t_node	*b;
	char	**args;
	int		to_free;

	to_free = 0;
	if (argc < 2)
		return (0);
	args = parse_args(&argc, argv, &to_free);
	if (!args)
		return (0);
	if (check_input_errors(argc, args) <= 0)
	{
		free_stacks(NULL, NULL, args, to_free);
		return (0);
	}
	a = init_stack_memory(argc, args, 0);
	b = init_stack_memory(argc, args, 1);
	process_instructions(a, b);
	check_solution(a, b);
	free_stacks(a, b, args, to_free);
	return (0);
}
