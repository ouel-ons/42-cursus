/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ops_rotate.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/17 00:02:42 by ouel-ons          #+#    #+#             */
/*   Updated: 2026/01/17 00:02:45 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap_bonus.h"

void	bs_ra(t_node *a)
{
	do_shift_up(a, "");
}

void	bs_rb(t_node *b)
{
	do_shift_up(b, "");
}

void	bs_rr(t_node *a, t_node *b)
{
	do_shift_up(a, "");
	do_shift_up(b, "");
}
