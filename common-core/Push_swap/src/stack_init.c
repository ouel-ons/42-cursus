/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_init.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/15 17:13:36 by ouel-ons          #+#    #+#             */
/*   Updated: 2026/01/16 23:11:32 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	free_stacks(t_node *a, t_node *b, char **args, int to_free)
{
	int	i;

	if (to_free)
	{
		i = 0;
		while (args[i] != 0)
			free(args[i++]);
		free(args[i]);
		free(args);
	}
	if (a != NULL)
		free(a);
	if (b != NULL)
		free(b);
}

t_node	*init_stack_memory(int argc, char **argv, int is_empty)
{
	t_node	*tab;
	int		i;

	tab = malloc(sizeof(t_node) * (argc + 1));
	if (tab == NULL)
		return (NULL);
	i = 0;
	while (i < argc - 1)
	{
		if (!is_empty)
		{
			tab[i].val = ft_atoi(argv[i]);
			tab[i].filled = 1;
		}
		else
		{
			tab[i].val = 0;
			tab[i].filled = 0;
		}
		tab[i].index = i;
		i++;
	}
	tab[i].index = -1;
	return (tab);
}
