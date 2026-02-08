/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/14 10:12:42 by ouel-ons          #+#    #+#             */
/*   Updated: 2025/11/18 19:42:00 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>

int		ft_printf(const char *format, ...);
int		process_format(const char *format, va_list args);
int		handle_conversion(char specifier, va_list args);

int		handle_char(va_list args);
int		handle_string(va_list args);
int		handle_pointer(va_list args);
int		handle_int(va_list args);
int		handle_unsigned(va_list args);
int		handle_hex_lower(va_list args);
int		handle_hex_upper(va_list args);
int		handle_percent(void);

int		ft_putchar(char c);
int		ft_putstr(char *s);
size_t	ft_strlen(const char *s);
void	ft_putnbr_base(unsigned long n, unsigned int base,
			int uppercase, int *count);
void	ft_putnbr(int n, int *count);

#endif
