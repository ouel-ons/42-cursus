/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   algo_tiny.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/15 17:14:07 by ouel-ons          #+#    #+#             */
/*   Updated: 2026/01/15 17:14:08 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	solve_three(t_node *stack)
{
	int	start;
	int	end;

	start = get_start_idx(stack);
	end = get_end_idx(stack);
	if (find_min_node(stack).index == start && \
		find_max_node(stack, -1).index == end)
		return ;
	if (find_min_node(stack).index == start && \
		find_max_node(stack, -1).index == end - 1)
	{
		do_swap(stack, "sa\n");
		do_shift_up(stack, "ra\n");
	}
	if (find_max_node(stack, -1).index == start)
		do_shift_up(stack, "ra\n");
	if (stack[start].val > stack[start + 1].val)
		do_swap(stack, "sa\n");
	if (find_min_node(stack).index == end)
		do_shift_down(stack, "rra\n");
}
