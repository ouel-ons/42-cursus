# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/14 10:16:10 by ouel-ons          #+#    #+#              #
#    Updated: 2025/11/19 09:08:51 by ouel-ons         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

CC = cc
CFLAGS = -Wall -Wextra -Werror

NAME = libftprintf.a

SRC_DIR = src

MANDATORY_SRCS = \
	ft_printf.c \
	$(SRC_DIR)/format_handlers1.c \
	$(SRC_DIR)/format_handlers2.c \
	$(SRC_DIR)/number_utils.c \
	$(SRC_DIR)/string_utils.c \
	$(SRC_DIR)/write_utils.c

MANDATORY_OBJS = $(MANDATORY_SRCS:.c=.o)

all: $(NAME)

$(NAME): $(MANDATORY_OBJS)
	ar rcs $(NAME) $(MANDATORY_OBJS)

%.o: %.c ft_printf.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(MANDATORY_OBJS)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: clean
