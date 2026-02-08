# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ouel-ons <ouel-ons@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/17 16:35:01 by ouel-ons          #+#    #+#              #
#    Updated: 2026/01/17 16:35:02 by ouel-ons         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME        = push_swap
BONUS_NAME  = checker

CC          = cc
CFLAGS      = -Wall -Wextra -Werror
INCLUDES    = -I./includes -I./libft

LIBFT       = ./libft/libft.a

SRC_DIR     = src
BONUS_DIR   = src_bonus
OBJ_DIR     = obj

SRCS        = $(SRC_DIR)/main.c \
              $(SRC_DIR)/stack_init.c \
              $(SRC_DIR)/stack_utils.c \
              $(SRC_DIR)/math_utils.c \
              $(SRC_DIR)/ops_push.c \
              $(SRC_DIR)/ops_shift.c \
              $(SRC_DIR)/errors.c \
              $(SRC_DIR)/algo_turk.c \
              $(SRC_DIR)/algo_tiny.c \
              $(SRC_DIR)/algo_cost.c

BONUS_SRCS  = $(BONUS_DIR)/checker.c \
              $(BONUS_DIR)/exec_bonus.c \
              $(BONUS_DIR)/utils_bonus.c \
              $(BONUS_DIR)/ops_swap_push.c \
              $(BONUS_DIR)/ops_rotate.c \
              $(BONUS_DIR)/ops_rev_rotate.c

OBJS        = $(SRCS:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)
BONUS_OBJS  = $(BONUS_SRCS:$(BONUS_DIR)/%.c=$(OBJ_DIR)/%.o)

SHARED_OBJS = $(OBJ_DIR)/stack_init.o \
              $(OBJ_DIR)/stack_utils.o \
              $(OBJ_DIR)/errors.o \
              $(OBJ_DIR)/math_utils.o \
              $(OBJ_DIR)/ops_push.o \
              $(OBJ_DIR)/ops_shift.o


all: $(NAME)

$(NAME): $(OBJS) $(LIBFT)
	$(CC) $(CFLAGS) $(OBJS) $(LIBFT) -o $(NAME)

bonus: $(BONUS_NAME)

$(BONUS_NAME): $(BONUS_OBJS) $(SHARED_OBJS) $(LIBFT)
	$(CC) $(CFLAGS) $(BONUS_OBJS) $(SHARED_OBJS) $(LIBFT) -o $(BONUS_NAME)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	@mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) $(INCLUDES) -c $< -o $@

$(OBJ_DIR)/%.o: $(BONUS_DIR)/%.c
	@mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) $(INCLUDES) -c $< -o $@

$(LIBFT):
	make -C ./libft

clean:
	rm -rf $(OBJ_DIR)
	make clean -C ./libft

fclean: clean
	rm -f $(NAME) $(BONUS_NAME)
	make fclean -C ./libft

re: fclean all

.PHONY: all clean fclean re bonus