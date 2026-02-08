/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap_bonus.h                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/17 00:04:43 by ouel-ons          #+#    #+#             */
/*   Updated: 2026/01/17 00:05:27 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_BONUS_H
# define PUSH_SWAP_BONUS_H

# include "push_swap.h"
# include "../libft/libft.h"

void	exec_instruction(t_node *a, t_node *b, char *line);

void	bs_sa(t_node *a);
void	bs_sb(t_node *b);
void	bs_ss(t_node *a, t_node *b);
void	bs_pa(t_node *a, t_node *b);
void	bs_pb(t_node *a, t_node *b);
void	bs_ra(t_node *a);
void	bs_rb(t_node *b);
void	bs_rr(t_node *a, t_node *b);
void	bs_rra(t_node *a);
void	bs_rrb(t_node *b);
void	bs_rrr(t_node *a, t_node *b);

#endif
