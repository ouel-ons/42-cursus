/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_utils.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/15 17:13:31 by ouel-ons          #+#    #+#             */
/*   Updated: 2026/01/15 17:13:33 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	get_start_idx(t_node *stack)
{
	int	i;

	i = 0;
	while (stack[i].filled != 1)
		i++;
	if (stack[i].index == -1)
		i--;
	return (i);
}

int	get_end_idx(t_node *stack)
{
	int	i;

	i = 0;
	while (stack[i].index != -1)
		i++;
	i--;
	return (i);
}

t_node	find_min_node(t_node *stack)
{
	int	curr;
	int	end;
	int	min;

	curr = get_start_idx(stack);
	end = get_end_idx(stack);
	min = stack[curr].index;
	while (curr <= end)
	{
		if (stack[curr].val < stack[min].val)
			min = stack[curr].index;
		curr++;
	}
	return (stack[min]);
}

t_node	find_max_node(t_node *stack, int limit)
{
	int	curr;
	int	end;
	int	max;

	curr = get_start_idx(stack);
	end = get_end_idx(stack);
	max = -1;
	while (curr <= end)
	{
		if (max == -1 || ((stack[curr].val > stack[max].val || \
		stack[max].filled == -1) && (limit == -1 || \
		stack[curr].val < limit)))
			max = stack[curr].index;
		curr++;
	}
	return (stack[max]);
}

t_node	find_min_above(t_node *stack, int limit)
{
	int	curr;
	int	end;
	int	min;

	curr = get_start_idx(stack);
	end = get_end_idx(stack);
	min = -1;
	while (curr <= end)
	{
		if (stack[curr].val > limit && \
		(min == -1 || stack[curr].val < stack[min].val))
			min = stack[curr].index;
		curr++;
	}
	if (min == -1)
		return (find_min_node(stack));
	return (stack[min]);
}
