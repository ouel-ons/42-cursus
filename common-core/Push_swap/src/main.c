/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 23:30:42 by ouel-ons          #+#    #+#             */
/*   Updated: 2026/01/16 23:32:03 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	arr_len(char **arr)
{
	int	i;

	i = 0;
	if (!arr)
		return (0);
	while (arr[i])
		i++;
	return (i);
}

static void	select_algo(t_node *a, t_node *b, int argc)
{
	if (argc == 3)
	{
		if (is_sorted(a) == -1)
			do_swap(a, "sa\n");
	}
	else if (argc == 4)
		solve_three(a);
	else
		run_turk_algo(a, b, argc);
}

static char	*get_joined_args(int argc, char **argv)
{
	char	*str;
	int		len;
	int		i;

	len = 0;
	i = 1;
	while (i < argc)
	{
		len += ft_strlen(argv[i]);
		len += 1;
		i++;
	}
	str = malloc(sizeof(char) * (len + 1));
	if (!str)
		return (NULL);
	str[0] = '\0';
	i = 1;
	while (i < argc)
	{
		ft_strlcat(str, argv[i], len + 1);
		ft_strlcat(str, " ", len + 1);
		i++;
	}
	return (str);
}

char	**parse_args(int *argc, char **argv, int *to_free)
{
	char	**split;
	char	*joined;

	joined = get_joined_args(*argc, argv);
	if (!joined)
		return (NULL);
	split = ft_split(joined, ' ');
	free(joined);
	*argc = arr_len(split) + 1;
	*to_free = 1;
	return (split);
}

int	main(int argc, char **argv)
{
	t_node	*stack_a;
	t_node	*stack_b;
	char	**args;
	int		to_free;
	int		err;

	to_free = 0;
	if (argc < 2)
		return (0);
	args = parse_args(&argc, argv, &to_free);
	if (!args)
		return (0);
	err = check_input_errors(argc, args);
	if (err == -1 || err == 0)
	{
		free_stacks(NULL, NULL, args, to_free);
		return (0);
	}
	stack_a = init_stack_memory(argc, args, 0);
	stack_b = init_stack_memory(argc, args, 1);
	if (is_sorted(stack_a) == -1)
		select_algo(stack_a, stack_b, argc);
	free_stacks(stack_a, stack_b, args, to_free);
	return (0);
}
