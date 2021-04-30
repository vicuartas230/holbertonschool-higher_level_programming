#include "lists.h"

/**
 * insert_dnodeint_at_index - This function inserts a new node at
 * a given position.
 * @h: The start of the linked list.
 * @idx: The node to look for.
 * @n: The data of the new node.
 * Return: the address of the new node, or NULL if it failed.
 */

dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	unsigned int i = 0;
	dlistint_t *new = NULL, *tmp = *h;

	new = malloc(sizeof(dlistint_t));
	if (!new)
		return (NULL);
	new->n = n;
	if (!*h && idx)
		return (NULL);
	else if (!*h && !idx)
	{
		*h = new, new->next = NULL, new->prev = NULL;
		return (new);
	}
	if (!idx)
	{
		new->prev = NULL, new->next = tmp, tmp->next->prev = new;
		*h = new;
		return (new);
	}
	while (tmp->next)
	{
		if (i == idx - 1)
		{
			new->next = tmp->next, new->prev = tmp, tmp->next->prev = new;
			tmp->next = new;
			return (new);
		}
		i++;
		tmp = tmp->next;
	}
	if (idx == i + 1)
	{
		tmp->next = new, new->prev = tmp, new->next = NULL;
		return (new);
	}
	return (NULL);
}
