#include "lists.h"

/**
 * get_dnodeint_at_index - This function  returns
 * the nth node of a linked list.
 * @head: The start of the linked list.
 * @index: The node to look for.
 * Return: The nth node of the linked list.
 */

dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *tmp = head;
	unsigned int i = 0;

	while (tmp)
	{
		if (i == index)
			return (tmp);
		i++;
		tmp = tmp->next;
	}
	return (NULL);
}
