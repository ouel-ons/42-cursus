/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   exec_bonus.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/17 00:00:16 by ouel-ons          #+#    #+#             */
/*   Updated: 2026/01/17 00:00:21 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap_bonus.h"

static int	ft_strcmp(const char *s1, const char *s2)
{
	size_t	i;

	i = 0;
	while (s1[i] || s2[i])
	{
		if (s1[i] != s2[i])
			return ((unsigned char)s1[i] - (unsigned char)s2[i]);
		i++;
	}
	return (0);
}

static void	error_exit(t_node *a, t_node *b)
{
	ft_putstr_fd("Error\n", 2);
	free_stacks(a, b, NULL, 0);
	exit(1);
}

void	exec_instruction(t_node *a, t_node *b, char *line)
{
	if (ft_strcmp(line, "sa\n") == 0)
		bs_sa(a);
	else if (ft_strcmp(line, "sb\n") == 0)
		bs_sb(b);
	else if (ft_strcmp(line, "ss\n") == 0)
		bs_ss(a, b);
	else if (ft_strcmp(line, "pa\n") == 0)
		bs_pa(a, b);
	else if (ft_strcmp(line, "pb\n") == 0)
		bs_pb(a, b);
	else if (ft_strcmp(line, "ra\n") == 0)
		bs_ra(a);
	else if (ft_strcmp(line, "rb\n") == 0)
		bs_rb(b);
	else if (ft_strcmp(line, "rr\n") == 0)
		bs_rr(a, b);
	else if (ft_strcmp(line, "rra\n") == 0)
		bs_rra(a);
	else if (ft_strcmp(line, "rrb\n") == 0)
		bs_rrb(b);
	else if (ft_strcmp(line, "rrr\n") == 0)
		bs_rrr(a, b);
	else
		error_exit(a, b);
}
