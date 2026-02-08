/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   number_utils.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/14 10:15:11 by ouel-ons          #+#    #+#             */
/*   Updated: 2025/11/14 10:36:26 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../ft_printf.h"

void	ft_putnbr_base(unsigned long n, unsigned int base,
			int uppercase, int *count)
{
	char	*digits;

	if (uppercase)
		digits = "0123456789ABCDEF";
	else
		digits = "0123456789abcdef";
	if (n >= base)
		ft_putnbr_base(n / base, base, uppercase, count);
	if (*count == -1)
		return ;
	if (ft_putchar(digits[n % base]) == -1)
		*count = -1;
	else
		(*count)++;
}

void	ft_putnbr(int n, int *count)
{
	if (n == -2147483648)
	{
		if (ft_putstr("-2147483648") == -1)
		{
			*count = -1;
			return ;
		}
		*count += 11;
		return ;
	}
	if (n < 0)
	{
		if (ft_putchar('-') == -1)
		{
			*count = -1;
			return ;
		}
		(*count)++;
		n = -n;
	}
	ft_putnbr_base(n, 10, 0, count);
}
