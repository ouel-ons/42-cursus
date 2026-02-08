/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 13:44:05 by ouel-ons          #+#    #+#             */
/*   Updated: 2025/10/26 15:41:39 by ouel-ons         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	count_words(const char *s, char c)
{
	int	i;
	int	count;

	i = 0;
	count = 0;
	while (s[i])
	{
		while (s[i] && s[i] == c)
			i++;
		if (s[i] && s[i] != c)
		{
			count++;
			while (s[i] && s[i] != c)
				i++;
		}
	}
	return (count);
}

static char	*word_dup(const char *s, int start, int end)
{
	char	*word;
	int		i;

	word = (char *)malloc(sizeof(char) * (end - start + 1));
	if (!word)
		return (NULL);
	i = 0;
	while (start < end)
		word[i++] = s[start++];
	word[i] = '\0';
	return (word);
}

static void	free_all(char **res, int i)
{
	while (res[i])
		free(res[i++]);
	free(res);
}

static int	fill_words(char **res, const char *s, char c)
{
	int	i;
	int	j;
	int	start;
	int	end;

	i = 0;
	j = 0;
	start = 0;
	while (s[start])
	{
		while (s[start] && s[start] == c)
			start++;
		end = start;
		while (s[end] && s[end] != c)
			end++;
		if (end > start)
		{
			res[j] = word_dup(s, start, end);
			if (!res[j++])
				return (-1);
			start = end;
		}
	}
	return (j);
}

char	**ft_split(char const *s, char c)
{
	char	**res;
	int		word_count;
	int		filled;

	if (!s)
		return (NULL);
	word_count = count_words(s, c);
	res = (char **)malloc(sizeof(char *) * (word_count + 1));
	if (!res)
		return (NULL);
	filled = fill_words(res, s, c);
	if (filled == -1)
	{
		free_all(res, 0);
		return (NULL);
	}
	res[word_count] = NULL;
	return (res);
}
