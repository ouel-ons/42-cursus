/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   format_handers2.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/14 10:34:57 by ouel-ons          #+#    #+#             */
/*   Updated: 2025/11/14 10:35:17 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../ft_printf.h"

int	handle_hex_lower(va_list args)
{
	unsigned int	n;
	int				count;

	n = va_arg(args, unsigned int);
	count = 0;
	ft_putnbr_base(n, 16, 0, &count);
	return (count);
}

int	handle_hex_upper(va_list args)
{
	unsigned int	n;
	int				count;

	n = va_arg(args, unsigned int);
	count = 0;
	ft_putnbr_base(n, 16, 1, &count);
	return (count);
}

int	handle_percent(void)
{
	return (ft_putchar('%'));
}
