/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ops_push.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/15 17:13:43 by ouel-ons          #+#    #+#             */
/*   Updated: 2026/01/15 17:13:44 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	do_push(t_node *src, t_node *dst, char *msg)
{
	int	first;
	int	end;

	first = 0;
	while (src[first].filled != 1)
		first++;
	end = 0;
	while (dst[end].index != -1 && dst[end].filled != 1)
		end++;
	end--;
	dst[end].val = src[first].val;
	src[first].val = 0;
	dst[end].filled = 1;
	src[first].filled = 0;
	ft_putstr_fd(msg, 1);
}

void	do_swap(t_node *stack, char *msg)
{
	int	start;
	int	temp;

	start = get_start_idx(stack);
	temp = stack[start].val;
	stack[start].val = stack[start + 1].val;
	stack[start + 1].val = temp;
	ft_putstr_fd(msg, 1);
}
