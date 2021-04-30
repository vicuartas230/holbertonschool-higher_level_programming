#include "lists.h"

/**
 * free_dlistint - This function frees a dlistint_t list.
 * @head: The start of the linked list.
 * Return: Nothing.
 */

void free_dlistint(dlistint_t *head)
{
	dlistint_t *tmp = head;

	while (tmp)
	{
		tmp = tmp->next;
		free(head);
		head = tmp;
	}
}
