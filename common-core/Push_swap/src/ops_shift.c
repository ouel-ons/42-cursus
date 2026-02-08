/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ops_shift.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/15 17:13:40 by ouel-ons          #+#    #+#             */
/*   Updated: 2026/01/15 17:13:41 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	do_shift_up(t_node *stack, char *msg)
{
	int	start;
	int	end;
	int	temp;
	int	temp2;
	int	i;

	start = 0;
	while (stack[start].index != -1 && stack[start].filled != 1)
		start++;
	end = 0;
	while (stack[end].index != -1)
		end++;
	end--;
	i = end;
	temp = stack[i].val;
	while (i > start)
	{
		temp2 = stack[i - 1].val;
		stack[i - 1].val = temp;
		temp = temp2;
		i--;
	}
	stack[end].val = temp;
	ft_putstr_fd(msg, 1);
}

void	do_shift_down(t_node *stack, char *msg)
{
	int	start;
	int	end;
	int	temp;
	int	temp2;
	int	i;

	start = 0;
	while (stack[start].index != -1 && stack[start].filled != 1)
		start++;
	end = 0;
	while (stack[end].index != -1)
		end++;
	end--;
	i = start;
	temp = stack[i].val;
	while (i < end)
	{
		temp2 = stack[i + 1].val;
		stack[i + 1].val = temp;
		temp = temp2;
		i++;
	}
	stack[start].val = temp;
	ft_putstr_fd(msg, 1);
}

void	do_double_shift(t_node *a, t_node *b, int dir)
{
	if (dir == 1)
	{
		do_shift_down(a, "");
		do_shift_down(b, "");
		ft_putstr_fd("rrr\n", 1);
	}
	else
	{
		do_shift_up(a, "");
		do_shift_up(b, "");
		ft_putstr_fd("rr\n", 1);
	}
}
