#include "lists.h"

/**
 * check_cycle - This function checks if a
 * singly linked list has a cycle in it.
 * @list: The list to check.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp = NULL, *tmp2 = NULL;

	tmp = list;
	tmp2 = list;
	while (tmp && tmp2)
	{
		tmp = tmp->next;
		tmp2 = tmp2->next->next;
		if (tmp == tmp2)
			return (1);
	}
	return (0);
}
