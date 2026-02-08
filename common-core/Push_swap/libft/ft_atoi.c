/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 12:58:30 by ouel-ons          #+#    #+#             */
/*   Updated: 2025/10/26 17:40:58 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	check_overflow(unsigned long r, int sign, char c)
{
	if (r > (9223372036854775807ul - (c - '0')) / 10)
	{
		if (sign == 1)
			return (-1);
		return (0);
	}
	return (1);
}

int	ft_atoi(const char *str)
{
	int				i;
	int				sign;
	unsigned long	r;
	int				check;

	i = 0;
	sign = 1;
	r = 0;
	while ((str[i] >= 9 && str[i] <= 13) || str[i] == ' ')
		i++;
	if (str[i] == '-' || str[i] == '+')
	{
		if (str[i] == '-')
			sign = -1;
		i++;
	}
	while (str[i] >= '0' && str[i] <= '9')
	{
		check = check_overflow(r, sign, str[i]);
		if (check != 1)
			return (check);
		r = r * 10 + (str[i++] - '0');
	}
	return ((int)(r * sign));
}
