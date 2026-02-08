/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ops_rev_rotate.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/17 00:03:08 by ouel-ons          #+#    #+#             */
/*   Updated: 2026/01/17 00:03:10 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap_bonus.h"

void	bs_rra(t_node *a)
{
	do_shift_down(a, "");
}

void	bs_rrb(t_node *b)
{
	do_shift_down(b, "");
}

void	bs_rrr(t_node *a, t_node *b)
{
	do_shift_down(a, "");
	do_shift_down(b, "");
}
