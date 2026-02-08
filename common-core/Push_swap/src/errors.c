/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   errors.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/15 17:13:53 by ouel-ons          #+#    #+#             */
/*   Updated: 2026/01/16 23:33:19 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

long	ft_atol(const char *str)
{
	long	res;
	int		sign;
	int		i;

	res = 0;
	sign = 1;
	i = 0;
	if (str[i] == '-' || str[i] == '+')
	{
		if (str[i] == '-')
			sign = -1;
		i++;
	}
	while (str[i] >= '0' && str[i] <= '9')
	{
		res = res * 10 + (str[i] - '0');
		i++;
	}
	return (res * sign);
}

static int	is_valid_format(int argc, char **argv)
{
	int	i;
	int	j;

	i = 0;
	while (i < argc - 1)
	{
		j = 0;
		while (argv[i][j])
		{
			if (ft_isdigit(argv[i][j]) == 0)
			{
				if (!(j == 0 && (argv[i][j] == '-' || argv[i][j] == '+')
						&& argv[i][1] != '\0'))
					return (-1);
			}
			j++;
		}
		i++;
	}
	return (1);
}

static int	is_duplicate(int argc, char **argv)
{
	int		i;
	int		j;
	long	tmp;
	long	tmp_j;

	i = 0;
	while (i < argc - 1)
	{
		tmp = ft_atol(argv[i]);
		if (tmp > 2147483647 || tmp < -2147483648)
			return (-1);
		j = i + 1;
		while (j < argc - 1)
		{
			tmp_j = ft_atol(argv[j]);
			if (tmp == tmp_j)
				return (-1);
			j++;
		}
		i++;
	}
	return (0);
}

int	check_input_errors(int argc, char **argv)
{
	if (argc == 1)
		return (0);
	if (is_valid_format(argc, argv) == -1)
	{
		ft_putstr_fd("Error\n", 2);
		return (-1);
	}
	if (is_duplicate(argc, argv) == -1)
	{
		ft_putstr_fd("Error\n", 2);
		return (-1);
	}
	return (1);
}
