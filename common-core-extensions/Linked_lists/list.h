#ifndef LIST_H
# define LIST_H

# include <stdlib.h>
# include <stddef.h>

typedef struct s_list
{
	void			*content;
	struct s_list	*next;
}	t_list;

/* ===== Standard libft ===== */
t_list	*ft_lstnew(void *content);
void	ft_lstadd_front(t_list **lst, t_list *new);
int		ft_lstsize(t_list *lst);
t_list	*ft_lstlast(t_list *lst);
void	ft_lstadd_back(t_list **lst, t_list *new);
void	ft_lstdelone(t_list *lst, void (*del)(void *));
void	ft_lstclear(t_list **lst, void (*del)(void *));
void	ft_lstiter(t_list *lst, void (*f)(void *));
t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *));

/* ===== Extras ===== */
t_list	*ft_lstfind(t_list *lst, void *data_ref, int (*cmp)(void *, void *));
t_list	*ft_lstget(t_list *lst, int index);
t_list	*ft_lstat(t_list *lst, size_t index);

t_list	*ft_lstcopy(t_list *src); /* shallow copy */
t_list	*ft_lstdup(t_list *lst, void *(*dup_content)(void *)); /* deep-ish via callback */

t_list	*ft_lstfrom_array(void **arr, size_t n);
void	**ft_lstto_array(t_list *lst); /* NULL-terminated */

void	ft_lstremove_if(t_list **lst, void *ref, int (*cmp)(void *, void *),
			void (*del)(void *));
void	ft_lstinsert_after(t_list *node, t_list *new);
void	ft_lstinsert_before(t_list **lst, t_list *target, t_list *new);

t_list	*ft_lstpop_front(t_list **lst);
t_list	*ft_lstpop_back(t_list **lst);
t_list	*ft_lstprepend(t_list **lst, void *content);

void	ft_lstswap_nodes(t_list *a, t_list *b); /* swaps CONTENT only */
void	ft_lstsort(t_list **lst, int (*cmp)(void *, void *));
void	ft_lstreverse(t_list **lst);

void	ft_lstprint(t_list *lst, void (*print)(void *));

#endif
