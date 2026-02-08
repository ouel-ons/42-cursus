/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   format_handlers.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/14 10:14:25 by ouel-ons          #+#    #+#             */
/*   Updated: 2025/11/19 07:55:15 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../ft_printf.h"

int	handle_char(va_list args)
{
	char	c;

	c = va_arg(args, int);
	return (ft_putchar(c));
}

int	handle_string(va_list args)
{
	char	*str;

	str = va_arg(args, char *);
	if (!str)
		return (ft_putstr("(null)"));
	return (ft_putstr(str));
}

int	handle_pointer(va_list args)
{
	void	*ptr;
	int		count;

	ptr = va_arg(args, void *);
	count = 0;
	if (!ptr)
		return (ft_putstr("0x0"));
	if (ft_putstr("0x") == -1)
		return (-1);
	count += 2;
	ft_putnbr_base((unsigned long)ptr, 16, 0, &count);
	return (count);
}

int	handle_int(va_list args)
{
	int	n;
	int	count;

	n = va_arg(args, int);
	count = 0;
	ft_putnbr(n, &count);
	return (count);
}

int	handle_unsigned(va_list args)
{
	unsigned int	n;
	int				count;

	n = va_arg(args, unsigned int);
	count = 0;
	ft_putnbr_base(n, 10, 0, &count);
	return (count);
}
