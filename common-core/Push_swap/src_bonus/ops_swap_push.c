/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ops_swap_push.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/17 00:02:21 by ouel-ons          #+#    #+#             */
/*   Updated: 2026/01/17 00:02:24 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap_bonus.h"

void	bs_sa(t_node *a)
{
	do_swap(a, "");
}

void	bs_sb(t_node *b)
{
	do_swap(b, "");
}

void	bs_ss(t_node *a, t_node *b)
{
	do_swap(a, "");
	do_swap(b, "");
}

void	bs_pa(t_node *a, t_node *b)
{
	do_push(b, a, "");
}

void	bs_pb(t_node *a, t_node *b)
{
	do_push(a, b, "");
}
