#include "lists.h"

/**
 * add_dnodeint_end - This function adds a new node at the end of a list.
 * @head: The start of the linked list.
 * @n: The data of the list.
 * Return: The address of the new element, or NULL if it failed.
 */

dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new = NULL, *tmp = *head;

	new = malloc(sizeof(dlistint_t));
	if (!new)
		return (NULL);
	new->n = n;
	if (!*head)
	{
		*head = new;
		new->next = NULL;
		new->prev = NULL;
		return (new);
	}
	else
	{
		while (tmp->next)
			tmp = tmp->next;
		tmp->next = new;
		tmp->next->prev = tmp;
		tmp->next->next = NULL;
		return (new);
	}
	return (NULL);
}
