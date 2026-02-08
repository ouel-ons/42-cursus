/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   math_utils.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/15 17:13:46 by ouel-ons          #+#    #+#             */
/*   Updated: 2026/01/15 17:13:47 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_min(int a, int b)
{
	if (a <= b)
		return (a);
	return (b);
}

int	ft_max(int a, int b)
{
	if (a >= b)
		return (a);
	return (b);
}

int	is_sorted(t_node *stack)
{
	int	i;

	i = 0;
	while (stack[i + 1].index != -1)
	{
		if (stack[i].val > stack[i + 1].val)
			return (-1);
		i++;
	}
	return (1);
}

int	is_median(t_node *stack, int num)
{
	int	curr;
	int	end;
	int	high;
	int	low;

	curr = get_start_idx(stack);
	end = get_end_idx(stack);
	high = 0;
	low = 0;
	while (curr <= end)
	{
		if (stack[curr].val > num)
			high++;
		else if (stack[curr].val < num)
			low++;
		curr++;
	}
	if ((high - low) >= -1 && (high - low) <= 1)
		return (1);
	return (0);
}
