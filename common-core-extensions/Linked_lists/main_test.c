#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"

/* ===================== tiny test helpers ===================== */

#define ASSERT(msg, cond) do { \
	if (!(cond)) { \
		printf("❌ FAIL: %s (line %d)\n", msg, __LINE__); \
		exit(1); \
	} else { \
		printf("✅ %s\n", msg); \
	} \
} while (0)

static int	*mkint(int v)
{
	int *p = (int *)malloc(sizeof(int));
	if (!p) exit(1);
	*p = v;
	return p;
}

static void	del_int(void *p) { free(p); }

static void	print_int(void *p)
{
	if (!p) { printf("(null)\n"); return; }
	printf("%d\n", *(int *)p);
}

static int	cmp_int(void *a, void *b)
{
	int ia = *(int *)a;
	int ib = *(int *)b;
	return (ia - ib);
}

static void	*dup_int(void *p)
{
	int *x = (int *)p;
	return mkint(*x);
}

/* for ft_lstmap: create NEW allocated int = old * 10 */
static void	*map_x10(void *p)
{
	int *x = (int *)p;
	return mkint((*x) * 10);
}

static void	iter_add1(void *p)
{
	int *x = (int *)p;
	(*x)++;
}

static int	sum_list(t_list *lst)
{
	int s = 0;
	while (lst)
	{
		s += *(int *)lst->content;
		lst = lst->next;
	}
	return s;
}

static void	free_nodes_only(t_list *lst)
{
	while (lst)
	{
		t_list *n = lst->next;
		free(lst);
		lst = n;
	}
}

/* useful to build list of allocated ints */
static t_list	*push_back_ints(int *vals, int n)
{
	t_list *lst = NULL;
	for (int i = 0; i < n; i++)
	{
		t_list *node = ft_lstnew(mkint(vals[i]));
		ASSERT("ft_lstnew != NULL", node != NULL);
		ft_lstadd_back(&lst, node);
	}
	return lst;
}

/* check list equals expected int array */
static void	assert_list_eq(const char *msg, t_list *lst, int *exp, int n)
{
	for (int i = 0; i < n; i++)
	{
		ASSERT(msg, lst != NULL);
		ASSERT(msg, *(int *)lst->content == exp[i]);
		lst = lst->next;
	}
	ASSERT(msg, lst == NULL);
}

/* ===================== tests ===================== */

static void	test_standard_libft(void)
{
	printf("\n==== test_standard_libft ====\n");

	int vals[] = {1,2,3};
	t_list *lst = NULL;

	/* ft_lstadd_front + ft_lstnew */
	ft_lstadd_front(&lst, ft_lstnew(mkint(vals[2]))); /* 3 */
	ft_lstadd_front(&lst, ft_lstnew(mkint(vals[1]))); /* 2 3 */
	ft_lstadd_front(&lst, ft_lstnew(mkint(vals[0]))); /* 1 2 3 */
	{
		int exp[] = {1,2,3};
		assert_list_eq("add_front builds 1 2 3", lst, exp, 3);
	}

	ASSERT("ft_lstsize == 3", ft_lstsize(lst) == 3);
	ASSERT("ft_lstlast == 3", *(int *)ft_lstlast(lst)->content == 3);

	/* ft_lstadd_back */
	ft_lstadd_back(&lst, ft_lstnew(mkint(4)));
	ASSERT("ft_lstsize == 4", ft_lstsize(lst) == 4);
	ASSERT("last == 4", *(int *)ft_lstlast(lst)->content == 4);

	/* ft_lstdelone */
	{
		t_list *node = ft_lstnew(mkint(999));
		ft_lstdelone(node, del_int);
		ASSERT("ft_lstdelone doesn't crash", 1);
	}

	/* ft_lstiter */
	ft_lstiter(lst, iter_add1); /* list becomes 2 3 4 5 */
	{
		int exp[] = {2,3,4,5};
		assert_list_eq("ft_lstiter (+1) works", lst, exp, 4);
	}

	/* ft_lstmap */
	{
		t_list *mapped = ft_lstmap(lst, map_x10, del_int); /* 20 30 40 50 */
		int exp[] = {20,30,40,50};
		assert_list_eq("ft_lstmap x10 works", mapped, exp, 4);

		/* ensure original unchanged after map */
		{
			int exp2[] = {2,3,4,5};
			assert_list_eq("original unchanged after map", lst, exp2, 4);
		}

		ft_lstclear(&mapped, del_int);
		ASSERT("mapped cleared == NULL", mapped == NULL);
	}

	ft_lstclear(&lst, del_int);
	ASSERT("ft_lstclear sets NULL", lst == NULL);
}

static void	test_find_get_at(void)
{
	printf("\n==== test_find_get_at ====\n");

	int v[] = {10,20,30,40};
	t_list *lst = push_back_ints(v, 4);

	int key30 = 30;
	t_list *f = ft_lstfind(lst, &key30, cmp_int);
	ASSERT("ft_lstfind finds 30", f && *(int *)f->content == 30);

	t_list *g2 = ft_lstget(lst, 2);
	ASSERT("ft_lstget index 2 is 30", g2 && *(int *)g2->content == 30);

	t_list *a3 = ft_lstat(lst, 3);
	ASSERT("ft_lstat index 3 is 40", a3 && *(int *)a3->content == 40);

	ASSERT("ft_lstget negative -> NULL", ft_lstget(lst, -1) == NULL);
	ASSERT("ft_lstat out of range -> NULL", ft_lstat(lst, 99) == NULL);

	ft_lstclear(&lst, del_int);
}

static void	test_copy_dup(void)
{
	printf("\n==== test_copy_dup ====\n");

	int v[] = {1,2,3};
	t_list *src = push_back_ints(v, 3);

	/* shallow copy */
	t_list *sh = ft_lstcopy(src);
	ASSERT("ft_lstcopy not NULL", sh != NULL);
	ASSERT("shallow: content pointers are same",
		sh->content == src->content);

	/* deep-ish dup */
	t_list *dp = ft_lstdup(src, dup_int);
	ASSERT("ft_lstdup not NULL", dp != NULL);
	ASSERT("dup: content pointers are different",
		dp->content != src->content);
	ASSERT("dup: values equal",
		*(int *)dp->content == *(int *)src->content);

	/* mutate src first element => shallow reflects, dup does not */
	*(int *)src->content = 999;
	ASSERT("shallow sees change", *(int *)sh->content == 999);
	ASSERT("dup does NOT see change", *(int *)dp->content != 999);

	/* cleanup:
	   - src owns ints
	   - sh nodes only (contents shared with src)
	   - dp owns its duplicated ints
	*/
	ft_lstclear(&dp, del_int);
	free_nodes_only(sh);
	ft_lstclear(&src, del_int);
}

static void	test_array_conversion(void)
{
	printf("\n==== test_array_conversion ====\n");

	void *arr[4];
	arr[0] = mkint(7);
	arr[1] = mkint(8);
	arr[2] = mkint(9);
	arr[3] = mkint(10);

	t_list *lst = ft_lstfrom_array(arr, 4);
	ASSERT("ft_lstfrom_array not NULL", lst != NULL);

	void **back = ft_lstto_array(lst);
	ASSERT("ft_lstto_array not NULL", back != NULL);
	ASSERT("ft_lstto_array NULL-terminated", back[4] == NULL);
	ASSERT("values preserved",
		*(int *)back[0] == 7 && *(int *)back[3] == 10);

	/* cleanup:
	   lst nodes + ints are owned by arr elements
	*/
	free(back);
	ft_lstclear(&lst, del_int); /* frees ints in nodes */
	/* arr pointers are now freed by lstclear */
}

static void	test_insert_pop_prepend(void)
{
	printf("\n==== test_insert_pop_prepend ====\n");

	int v[] = {1,3,4};
	t_list *lst = push_back_ints(v, 3); /* 1 3 4 */

	/* insert_after (after 1 insert 2) */
	{
		t_list *n2 = ft_lstnew(mkint(2));
		ft_lstinsert_after(lst, n2); /* 1 2 3 4 */
		int exp[] = {1,2,3,4};
		assert_list_eq("insert_after works", lst, exp, 4);
	}

	/* insert_before (before 4 insert 99) */
	{
		t_list *target = ft_lstlast(lst); /* 4 */
		t_list *n99 = ft_lstnew(mkint(99));
		ft_lstinsert_before(&lst, target, n99); /* 1 2 3 99 4 */
		int exp[] = {1,2,3,99,4};
		assert_list_eq("insert_before works", lst, exp, 5);
	}

	/* prepend helper */
	ft_lstprepend(&lst, mkint(0)); /* 0 ... */
	{
		int exp[] = {0,1,2,3,99,4};
		assert_list_eq("prepend works", lst, exp, 6);
	}

	/* pop_front */
	{
		t_list *p = ft_lstpop_front(&lst);
		ASSERT("pop_front returns node", p != NULL);
		ASSERT("popped value is 0", *(int *)p->content == 0);
		ft_lstdelone(p, del_int);
		int exp[] = {1,2,3,99,4};
		assert_list_eq("after pop_front", lst, exp, 5);
	}

	/* pop_back */
	{
		t_list *p = ft_lstpop_back(&lst);
		ASSERT("pop_back returns node", p != NULL);
		ASSERT("popped value is 4", *(int *)p->content == 4);
		ft_lstdelone(p, del_int);
		int exp[] = {1,2,3,99};
		assert_list_eq("after pop_back", lst, exp, 4);
	}

	ft_lstclear(&lst, del_int);
}

static void	test_remove_if(void)
{
	printf("\n==== test_remove_if ====\n");

	int v[] = {5,1,5,2,5,3};
	t_list *lst = push_back_ints(v, 6);

	int ref = 5;
	ft_lstremove_if(&lst, &ref, cmp_int, del_int); /* remove all 5 */
	{
		int exp[] = {1,2,3};
		assert_list_eq("remove_if removes all matches", lst, exp, 3);
	}
	ft_lstclear(&lst, del_int);
}

static void	test_swap_sort_reverse(void)
{
	printf("\n==== test_swap_sort_reverse ====\n");

	int v[] = {3,1,4,2};
	t_list *lst = push_back_ints(v, 4);

	/* swap contents between first and last */
	ft_lstswap_nodes(lst, ft_lstlast(lst));
	{
		int exp[] = {2,1,4,3};
		assert_list_eq("swap_nodes (content swap) works", lst, exp, 4);
	}

	/* sort */
	ft_lstsort(&lst, cmp_int);
	{
		int exp[] = {1,2,3,4};
		assert_list_eq("lstsort ascending works", lst, exp, 4);
	}

	/* reverse */
	ft_lstreverse(&lst);
	{
		int exp[] = {4,3,2,1};
		assert_list_eq("lstreverse works", lst, exp, 4);
	}

	/* print (visual check) */
	printf("ft_lstprint output should be: 4 3 2 1 (one per line)\n");
	ft_lstprint(lst, print_int);

	ft_lstclear(&lst, del_int);
}

int	main(void)
{
	printf("===== Linked List Test Suite =====\n");

	test_standard_libft();
	test_find_get_at();
	test_copy_dup();
	test_array_conversion();
	test_insert_pop_prepend();
	test_remove_if();
	test_swap_sort_reverse();

	printf("\n🎉 ALL TESTS PASSED\n");
	return 0;
}
