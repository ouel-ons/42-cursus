/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   algo_turk.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/15 17:13:59 by ouel-ons          #+#    #+#             */
/*   Updated: 2026/01/16 22:28:44 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	exec_moves_to_top(t_node *stack, int index, char *r, char *rr)
{
	int	moves;
	int	count;
	int	sign;

	count = calc_dist_to_top(stack, index, 1);
	sign = count;
	if (count < 0)
		count = -count;
	moves = count;
	if (count != 0)
	{
		while (count > 0)
		{
			if (sign > 0)
				do_shift_up(stack, r);
			else
				do_shift_down(stack, rr);
			count--;
		}
	}
	if (sign > 0)
		return (moves);
	return (-moves);
}

static void	exec_common_moves(t_node *a, t_node *b, int index)
{
	int	dist;

	dist = get_common_moves(a, b, index);
	if (dist > 0)
	{
		while (dist > 0)
		{
			do_double_shift(a, b, 0);
			dist--;
		}
	}
	else if (dist < 0)
	{
		dist = -dist;
		while (dist > 0)
		{
			do_double_shift(a, b, 1);
			dist--;
		}
	}
}

static void	move_cheapest(t_node *src, t_node *dst, int index, int size)
{
	int	start;
	int	common;

	start = get_start_idx(src);
	common = get_common_moves(src, dst, index);
	exec_common_moves(src, dst, index);
	if (common != 0)
		index -= common;
	if (index >= size - 2)
		index = start + (index - (size - 1));
	else if (index < start)
		index = get_end_idx(src) + index;
	index -= exec_moves_to_top(src, index, "rb\n", "rrb\n");
	if (index >= size - 2)
		index = start + (index - (size - 1));
	if (find_min_node(dst).val > src[index].val \
	|| find_max_node(dst, -1).val < src[index].val)
		exec_moves_to_top(dst, find_min_node(dst).index, "ra\n", "rra\n");
	else
		exec_moves_to_top(dst, \
		find_min_above(dst, src[index].val).index, "ra\n", "rra\n");
	do_push(src, dst, "pa\n");
}

static int	get_stack_median(t_node *stack)
{
	int	start;
	int	end;

	start = get_start_idx(stack);
	end = get_end_idx(stack);
	while (start <= end)
	{
		if (is_median(stack, stack[start].val))
			return (stack[start].val);
		start++;
	}
	return (-1);
}

void	run_turk_algo(t_node *a, t_node *b, int size)
{
	int	i;
	int	median;

	i = get_start_idx(a);
	median = get_stack_median(a);
	while (i < size - 4)
	{
		do_push(a, b, "pb\n");
		if (b[get_start_idx(b)].val > median && \
			get_end_idx(a) - get_start_idx(a) + 1 > 3)
			do_shift_up(b, "rb\n");
		i++;
	}
	solve_three(a);
	i = get_start_idx(b);
	while (i < get_end_idx(b))
	{
		move_cheapest(b, a, find_cheapest_index(b, a, size), size);
		i++;
	}
	exec_moves_to_top(a, find_min_above(a, b[i].val).index, "ra\n", "rra\n");
	do_push(b, a, "pa\n");
	exec_moves_to_top(a, find_min_node(a).index, "ra\n", "rra\n");
}
