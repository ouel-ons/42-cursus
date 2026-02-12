NAME = libstack.a

CC = cc
CFLAGS = -Wall -Wextra -Werror
AR = ar -rcs
RM = rm -rf

GREEN = \033[0;32m
RED   = \033[0;31m
YELLOW= \033[0;33m
BLUE  = \033[0;34m
RESET = \033[0m

SRCS = stack_init.c \
       node.c \
       stack_push_pop.c \
       stack_swap.c \
       stack_rotate.c \
       stack_clear.c \
       ops_push.c \
       ops_swap.c \
       ops_rotate.c

OBJS = $(SRCS:.c=.o)

all: $(NAME)

$(NAME): $(OBJS)
	@$(AR) $(NAME) $(OBJS)
	@printf "$(GREEN)✔ Library archived successfully!$(RESET)\n"

%.o: %.c stack.h
	@$(CC) $(CFLAGS) -c $< -o $@
	@printf "$(BLUE)➜ Compiled:$(RESET) $(GREEN)$<$(RESET)\n"

clean:
	@$(RM) $(OBJS)
	@printf "$(YELLOW)✖ Objects cleaned$(RESET)\n"

fclean: clean
	@$(RM) $(NAME)
	@printf "$(RED)✖ Library removed$(RESET)\n"

re: fclean all

OUTPUT = program

test:
	@$(CC) $(CFLAGS) main.c Libstack.a -o $(OUTPUT)
	@printf "$(GREEN)-> OUTPUT: $(OUTPUT)$(RESET)\n"

.PHONY: all clean fclean re
