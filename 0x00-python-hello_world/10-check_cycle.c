#include "lists.h"
/**
 * check_cycle - checks for cycle in a linked list
 * @list: linked list to check
 * Return: 1 if cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp_1 = NULL, *tmp_2 = NULL;

	tmp_1 = list;
	tmp_2 = list;

	while (list)
	{
		tmp_2 = tmp_2->next;
		if (!tmp_1 || !tmp_2)
			return (0);
		if (tmp_2 == tmp_1)
			return (1);
	}
	return (0);
}
