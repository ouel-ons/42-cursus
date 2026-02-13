t_list  *ft_lstfind(t_list *lst, void *data_ref, int (*cmp)(void *, void *));
t_list  *ft_lstget(t_list *lst, int index);
t_list  *ft_lstdup(t_list *lst, void *(*dup_content)(void *));
t_list  *ft_lstcopy(t_list *src);                 // shallow copy
t_list  *ft_lstfrom_array(void **arr, size_t n);
void   **ft_lstto_array(t_list *lst);
void    ft_lstremove_if(t_list **lst, void *ref, int (*cmp)(void *, void *), void (*del)(void *));
void    ft_lstinsert_after(t_list *node, t_list *new);
void    ft_lstinsert_before(t_list **lst, t_list *target, t_list *new);
t_list  *ft_lstpop_front(t_list **lst);
t_list  *ft_lstpop_back(t_list **lst);
t_list  *ft_lstprepend(t_list **lst, void *content);
t_list  *ft_lstat(t_list *lst, size_t index);
void    ft_lstswap_nodes(t_list *a, t_list *b);
void    ft_lstsort(t_list **lst, int (*cmp)(void *, void *));
void    ft_lstreverse(t_list **lst);
void    ft_lstprint(t_list *lst, void (*print)(void *));


t_list
ft_lstnew
ft_lstadd_front
ft_lstsize
ft_lstlast
ft_lstadd_back
ft_lstdelone
ft_lstclear
ft_lstiter
ft_lstmap

