/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/14 10:13:03 by ouel-ons          #+#    #+#             */
/*   Updated: 2025/11/19 09:07:06 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printf(const char *format, ...)
{
	va_list	args;
	int		count;

	va_start(args, format);
	count = process_format(format, args);
	va_end(args);
	return (count);
}

int	process_format(const char *format, va_list args)
{
	int	i;
	int	count;
	int	result;

	i = 0;
	count = 0;
	while (format[i])
	{
		if (format[i] == '%' && format[i + 1])
		{
			result = handle_conversion(format[++i], args);
			if (result == -1)
				return (-1);
			count += result;
		}
		else if (format[i] != '%')
		{
			if (ft_putchar(format[i]) == -1)
				return (-1);
			count++;
		}
		i++;
	}
	return (count);
}

int	handle_conversion(char specifier, va_list args)
{
	if (specifier == 'c')
		return (handle_char(args));
	else if (specifier == 's')
		return (handle_string(args));
	else if (specifier == 'p')
		return (handle_pointer(args));
	else if (specifier == 'd' || specifier == 'i')
		return (handle_int(args));
	else if (specifier == 'u')
		return (handle_unsigned(args));
	else if (specifier == 'x')
		return (handle_hex_lower(args));
	else if (specifier == 'X')
		return (handle_hex_upper(args));
	else if (specifier == '%')
		return (handle_percent());
	else
		return (ft_putchar(specifier));
}
