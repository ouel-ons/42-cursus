/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/15 17:49:44 by ouel-ons          #+#    #+#             */
/*   Updated: 2026/01/16 23:35:21 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include "../libft/libft.h"
# include <stdlib.h>
# include <unistd.h>

typedef struct s_node
{
	int	val;
	int	filled;
	int	index;
}	t_node;

t_node	*init_stack_memory(int argc, char **argv, int is_empty);
void	free_stacks(t_node *a, t_node *b, char **args, int to_free);
char	**parse_args(int *argc, char **argv, int *to_free);

int		get_start_idx(t_node *stack);
int		get_end_idx(t_node *stack);
t_node	find_min_node(t_node *stack);
t_node	find_max_node(t_node *stack, int threshold);
t_node	find_min_above(t_node *stack, int threshold);

int		ft_min(int a, int b);
int		ft_max(int a, int b);
int		is_sorted(t_node *stack);
int		is_median(t_node *stack, int num);

void	do_push(t_node *src, t_node *dst, char *msg);
void	do_shift_up(t_node *stack, char *msg);
void	do_shift_down(t_node *stack, char *msg);
void	do_swap(t_node *stack, char *msg);
void	do_double_shift(t_node *a, t_node *b, int dir);

int		check_input_errors(int argc, char **argv);

void	run_turk_algo(t_node *a, t_node *b, int size);
int		exec_moves_to_top(t_node *a, int index, char *r, char *rr);

void	solve_three(t_node *stack);
long	ft_atol(const char *str);
int		calc_dist_to_top(t_node *a, int index, int real_cost);
int		calc_combined_cost(t_node *a, t_node *b, int index);
int		get_common_moves(t_node *a, t_node *b, int index);
int		find_cheapest_index(t_node *a, t_node *b, int size);

#endif