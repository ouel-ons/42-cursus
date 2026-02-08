/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   algo_cost.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/15 17:14:10 by ouel-ons          #+#    #+#             */
/*   Updated: 2026/01/15 17:14:11 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	calc_dist_to_top(t_node *stack, int index, int real)
{
	int	count;
	int	start;
	int	end;
	int	mid;

	count = 0;
	start = get_start_idx(stack);
	end = get_end_idx(stack);
	mid = start + ((end - start) / 2);
	if (index > mid)
	{
		count = end - index + 1;
		if (real == 1)
			count = -count;
	}
	else if (index <= mid)
		count = index - start;
	return (count);
}

int	get_common_moves(t_node *a, t_node *b, int index)
{
	int	cost_a;
	int	cost_b;
	int	dist;
	int	min_idx;

	cost_a = calc_dist_to_top(a, index, 1);
	if (find_min_node(b).val > a[index].val || \
		find_max_node(b, -1).val < a[index].val)
		cost_b = calc_dist_to_top(b, find_min_node(b).index, 1);
	else
	{
		min_idx = find_min_above(b, a[index].val).index;
		cost_b = calc_dist_to_top(b, min_idx, 1);
	}
	dist = 0;
	if (cost_a > 0 && cost_b > 0)
		dist = ft_min(cost_a, cost_b);
	if (cost_a < 0 && cost_b < 0)
		dist = ft_max(cost_a, cost_b);
	return (dist);
}

int	calc_combined_cost(t_node *a, t_node *b, int index)
{
	int		cost;
	int		common;
	t_node	target;

	cost = 0;
	cost += calc_dist_to_top(a, index, 0);
	if (find_min_node(b).val > a[index].val \
	|| find_max_node(b, -1).val < a[index].val)
		cost += calc_dist_to_top(b, find_min_node(b).index, 0);
	else
	{
		target = find_min_above(b, a[index].val);
		cost += calc_dist_to_top(b, b[target.index].index, 0);
	}
	common = get_common_moves(a, b, index);
	if (common < 0)
		common = -common;
	cost = cost - common;
	return (cost + 1);
}

int	find_cheapest_index(t_node *a, t_node *b, int size)
{
	int		i;
	int		cost;
	int		start;
	t_node	min;

	start = get_start_idx(a);
	i = start;
	min.val = -1;
	while (i < size - 1)
	{
		cost = calc_combined_cost(a, b, i);
		if (cost < min.val || min.val == -1)
		{
			min.val = cost;
			min.index = i;
		}
		i++;
	}
	return (min.index);
}
