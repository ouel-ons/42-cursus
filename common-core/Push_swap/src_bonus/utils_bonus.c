/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils_bonus.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/17 00:00:08 by ouel-ons          #+#    #+#             */
/*   Updated: 2026/01/17 00:00:09 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap_bonus.h"

static int	arr_len(char **arr)
{
	int	i;

	i = 0;
	if (!arr)
		return (0);
	while (arr[i])
		i++;
	return (i);
}

static char	*get_joined_args(int argc, char **argv)
{
	char	*str;
	int		len;
	int		i;

	len = 0;
	i = 1;
	while (i < argc)
	{
		len += ft_strlen(argv[i]);
		len += 1;
		i++;
	}
	str = malloc(sizeof(char) * (len + 1));
	if (!str)
		return (NULL);
	str[0] = '\0';
	i = 1;
	while (i < argc)
	{
		ft_strlcat(str, argv[i], len + 1);
		ft_strlcat(str, " ", len + 1);
		i++;
	}
	return (str);
}

char	**parse_args(int *argc, char **argv, int *to_free)
{
	char	**split;
	char	*joined;

	joined = get_joined_args(*argc, argv);
	if (!joined)
		return (NULL);
	split = ft_split(joined, ' ');
	free(joined);
	*argc = arr_len(split) + 1;
	*to_free = 1;
	return (split);
}
