#include "lists.h"

/**
 * dlistint_len - This function returns the number of
 * elements in a linked list.
 * @h: The start of the linked list.
 * Return: The number of nodes
 */

size_t dlistint_len(const dlistint_t *h)
{
	size_t i = 0;

	while (h)
	{
		i++;
		h = h->next;
	}
	return (i);
}
