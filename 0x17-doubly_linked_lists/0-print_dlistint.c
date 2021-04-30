#include "lists.h"

/**
 * print_dlistint - This function prints all the elements of a list.
 * @h: The start of the linked list.
 * Return: The number of nodes.
 */

size_t print_dlistint(const dlistint_t *h)
{
	size_t i = 0;

	while (h)
	{
		printf("%d\n", h->n);
		i++;
		h = h->next;
	}
	return (i);
}
