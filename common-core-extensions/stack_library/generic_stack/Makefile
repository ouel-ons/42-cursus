NAME    = libgstack.a

CC      = cc
CFLAGS  = -Wall -Wextra -Werror
AR      = ar -rcs
RM      = rm -f

# Colors
GREEN  = \033[0;32m
RED    = \033[0;31m
YELLOW = \033[0;33m
BLUE   = \033[0;34m
RESET  = \033[0m

# Auto-detect sources (future-proof)
SRCS    = $(wildcard *.c)
OBJS    = $(SRCS:.c=.o)

all: $(NAME)

$(NAME): $(OBJS)
	@$(AR) $(NAME) $(OBJS)
	@printf "$(GREEN)✔ libgstack archived successfully!$(RESET)\n"

%.o: %.c ft_stack.h
	@$(CC) $(CFLAGS) -c $< -o $@
	@printf "$(BLUE)➜ Compiled:$(RESET) $(GREEN)$<$(RESET)\n"

clean:
	@$(RM) $(OBJS)
	@printf "$(YELLOW)✖ Object files cleaned$(RESET)\n"

fclean: clean
	@$(RM) $(NAME)
	@printf "$(RED)✖ Library removed$(RESET)\n"

re: fclean all
	@printf "$(GREEN)✔ Rebuilt successfully!$(RESET)\n"

OUTPUT = program

test:
	@$(CC) $(CFLAGS) main.c Libgstack.a -o $(OUTPUT)
	@printf "$(GREEN)-> OUTPUT: $(OUTPUT)$(RESET)\n"

.PHONY: all clean fclean re
