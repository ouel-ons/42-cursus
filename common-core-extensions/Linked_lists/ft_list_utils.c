#include "list.h"

/* ===================== Standard libft ===================== */

t_list	*ft_lstnew(void *content)
{
	t_list	*n;

	n = (t_list *)malloc(sizeof(t_list));
	if (!n)
		return (NULL);
	n->content = content;
	n->next = NULL;
	return (n);
}

void	ft_lstadd_front(t_list **lst, t_list *new)
{
	if (!lst || !new)
		return ;
	new->next = *lst;
	*lst = new;
}

int	ft_lstsize(t_list *lst)
{
	int	c;

	c = 0;
	while (lst)
	{
		c++;
		lst = lst->next;
	}
	return (c);
}

t_list	*ft_lstlast(t_list *lst)
{
	if (!lst)
		return (NULL);
	while (lst->next)
		lst = lst->next;
	return (lst);
}

void	ft_lstadd_back(t_list **lst, t_list *new)
{
	t_list	*last;

	if (!lst || !new)
		return ;
	if (!*lst)
	{
		*lst = new;
		return ;
	}
	last = ft_lstlast(*lst);
	last->next = new;
}

void	ft_lstdelone(t_list *lst, void (*del)(void *))
{
	if (!lst)
		return ;
	if (del)
		del(lst->content);
	free(lst);
}

void	ft_lstclear(t_list **lst, void (*del)(void *))
{
	t_list	*tmp;

	if (!lst)
		return ;
	while (*lst)
	{
		tmp = (*lst)->next;
		ft_lstdelone(*lst, del);
		*lst = tmp;
	}
}

void	ft_lstiter(t_list *lst, void (*f)(void *))
{
	if (!f)
		return ;
	while (lst)
	{
		f(lst->content);
		lst = lst->next;
	}
}

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*out;
	t_list	*node;
	void	*new_content;

	if (!f)
		return (NULL);
	out = NULL;
	while (lst)
	{
		new_content = f(lst->content);
		node = ft_lstnew(new_content);
		if (!node)
		{
			if (del)
				del(new_content);
			ft_lstclear(&out, del);
			return (NULL);
		}
		ft_lstadd_back(&out, node);
		lst = lst->next;
	}
	return (out);
}

/* ===================== Extras ===================== */

t_list	*ft_lstfind(t_list *lst, void *data_ref, int (*cmp)(void *, void *))
{
	if (!cmp)
		return (NULL);
	while (lst)
	{
		if (cmp(lst->content, data_ref) == 0)
			return (lst);
		lst = lst->next;
	}
	return (NULL);
}

t_list	*ft_lstget(t_list *lst, int index)
{
	int	i;

	if (index < 0)
		return (NULL);
	i = 0;
	while (lst)
	{
		if (i == index)
			return (lst);
		i++;
		lst = lst->next;
	}
	return (NULL);
}

t_list	*ft_lstat(t_list *lst, size_t index)
{
	size_t	i;

	i = 0;
	while (lst)
	{
		if (i == index)
			return (lst);
		i++;
		lst = lst->next;
	}
	return (NULL);
}

/* shallow copy: duplicates nodes only, content pointers are shared */
t_list	*ft_lstcopy(t_list *src)
{
	t_list	*out;
	t_list	*n;

	out = NULL;
	while (src)
	{
		n = ft_lstnew(src->content);
		if (!n)
		{
			ft_lstclear(&out, NULL);
			return (NULL);
		}
		ft_lstadd_back(&out, n);
		src = src->next;
	}
	return (out);
}

/* dup via callback: creates new nodes + new content via dup_content */
t_list	*ft_lstdup(t_list *lst, void *(*dup_content)(void *))
{
	t_list	*out;
	t_list	*n;
	void	*cpy;

	if (!dup_content)
		return (NULL);
	out = NULL;
	while (lst)
	{
		cpy = dup_content(lst->content);
		n = ft_lstnew(cpy);
		if (!n)
		{
			/* We can only free nodes here; caller should ensure dup_content
			   returns heap allocations if they want deep cleanup. */
			free(cpy);
			ft_lstclear(&out, free);
			return (NULL);
		}
		ft_lstadd_back(&out, n);
		lst = lst->next;
	}
	return (out);
}

t_list	*ft_lstfrom_array(void **arr, size_t n)
{
	size_t	i;
	t_list	*out;
	t_list	*node;

	out = NULL;
	i = 0;
	while (i < n)
	{
		node = ft_lstnew(arr[i]);
		if (!node)
		{
			ft_lstclear(&out, NULL);
			return (NULL);
		}
		ft_lstadd_back(&out, node);
		i++;
	}
	return (out);
}

/* returns a NULL-terminated array: [0..size-1] contents, last = NULL */
void	**ft_lstto_array(t_list *lst)
{
	void	**arr;
	size_t	i;
	size_t	n;

	n = (size_t)ft_lstsize(lst);
	arr = (void **)malloc(sizeof(void *) * (n + 1));
	if (!arr)
		return (NULL);
	i = 0;
	while (lst)
	{
		arr[i++] = lst->content;
		lst = lst->next;
	}
	arr[i] = NULL;
	return (arr);
}

void	ft_lstremove_if(t_list **lst, void *ref, int (*cmp)(void *, void *),
			void (*del)(void *))
{
	t_list	*cur;
	t_list	*prev;
	t_list	*next;

	if (!lst || !cmp)
		return ;
	cur = *lst;
	prev = NULL;
	while (cur)
	{
		next = cur->next;
		if (cmp(cur->content, ref) == 0)
		{
			if (!prev)
				*lst = next;
			else
				prev->next = next;
			ft_lstdelone(cur, del);
		}
		else
			prev = cur;
		cur = next;
	}
}

void	ft_lstinsert_after(t_list *node, t_list *new)
{
	if (!node || !new)
		return ;
	new->next = node->next;
	node->next = new;
}

void	ft_lstinsert_before(t_list **lst, t_list *target, t_list *new)
{
	t_list	*cur;

	if (!lst || !*lst || !target || !new)
		return ;
	if (*lst == target)
	{
		ft_lstadd_front(lst, new);
		return ;
	}
	cur = *lst;
	while (cur && cur->next && cur->next != target)
		cur = cur->next;
	if (cur && cur->next == target)
	{
		new->next = target;
		cur->next = new;
	}
}

t_list	*ft_lstpop_front(t_list **lst)
{
	t_list	*node;

	if (!lst || !*lst)
		return (NULL);
	node = *lst;
	*lst = node->next;
	node->next = NULL;
	return (node);
}

t_list	*ft_lstpop_back(t_list **lst)
{
	t_list	*cur;
	t_list	*prev;

	if (!lst || !*lst)
		return (NULL);
	cur = *lst;
	prev = NULL;
	while (cur->next)
	{
		prev = cur;
		cur = cur->next;
	}
	if (!prev)
		*lst = NULL;
	else
		prev->next = NULL;
	return (cur);
}

t_list	*ft_lstprepend(t_list **lst, void *content)
{
	t_list	*node;

	node = ft_lstnew(content);
	if (!node)
		return (NULL);
	ft_lstadd_front(lst, node);
	return (node);
}

/* This swaps ONLY content pointers (safe without prev pointers). */
void	ft_lstswap_nodes(t_list *a, t_list *b)
{
	void	*tmp;

	if (!a || !b)
		return ;
	tmp = a->content;
	a->content = b->content;
	b->content = tmp;
}

/* ===== sort (merge sort) ===== */

static t_list	*split_mid(t_list *head)
{
	t_list	*slow;
	t_list	*fast;
	t_list	*prev;

	slow = head;
	fast = head;
	prev = NULL;
	while (fast && fast->next)
	{
		prev = slow;
		slow = slow->next;
		fast = fast->next->next;
	}
	if (prev)
		prev->next = NULL;
	return (slow);
}

static t_list	*merge_sorted(t_list *a, t_list *b, int (*cmp)(void *, void *))
{
	t_list	dummy;
	t_list	*tail;

	tail = &dummy;
	dummy.next = NULL;
	while (a && b)
	{
		if (cmp(a->content, b->content) <= 0)
		{
			tail->next = a;
			a = a->next;
		}
		else
		{
			tail->next = b;
			b = b->next;
		}
		tail = tail->next;
	}
	tail->next = (a ? a : b);
	return (dummy.next);
}

static t_list	*merge_sort(t_list *head, int (*cmp)(void *, void *))
{
	t_list	*mid;
	t_list	*left;
	t_list	*right;

	if (!head || !head->next)
		return (head);
	mid = split_mid(head);
	left = merge_sort(head, cmp);
	right = merge_sort(mid, cmp);
	return (merge_sorted(left, right, cmp));
}

void	ft_lstsort(t_list **lst, int (*cmp)(void *, void *))
{
	if (!lst || !*lst || !cmp)
		return ;
	*lst = merge_sort(*lst, cmp);
}

void	ft_lstreverse(t_list **lst)
{
	t_list	*prev;
	t_list	*cur;
	t_list	*next;

	if (!lst)
		return ;
	prev = NULL;
	cur = *lst;
	while (cur)
	{
		next = cur->next;
		cur->next = prev;
		prev = cur;
		cur = next;
	}
	*lst = prev;
}

void	ft_lstprint(t_list *lst, void (*print)(void *))
{
	if (!print)
		return ;
	while (lst)
	{
		print(lst->content);
		lst = lst->next;
	}
}
