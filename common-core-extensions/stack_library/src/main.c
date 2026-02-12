#include "stack.h"
/* compile with your library just to test */
int main(void)
{
	t_stack	a, b;

	stack_init(&a, 'a');
	stack_init(&b, 'b');
	stack_push_top(&a, node_new(3));
	stack_push_top(&a, node_new(2));
	stack_push_top(&a, node_new(1)); /* A = 1 2 3 */

	op_ra(&a);   /* A = 2 3 1 */
	op_rra(&a);  /* A = 1 2 3 */
	op_pb(&a, &b); /* A=2 3, B=1 */
	op_sa(&a);     /* A=3 2 */

	stack_clear(&a);
	stack_clear(&b);
}
