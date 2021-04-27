#include "lists.h"

/**
 * check_cycle - This function checks if a
 * singly linked list has a cycle in it.
 * @list: The list to check.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp = NULL, *arr[BUFSIZ];
	int i = 0, j = 0;

	tmp = list;
	while (tmp)
	{
		arr[j] = tmp;
		i = j - 1;
		while (i >= 0)
		{
			if (arr[i] == arr[j])
				return (1);
			i--;
		}
		tmp = tmp->next;
		j++;
	}
	return (0);
}
