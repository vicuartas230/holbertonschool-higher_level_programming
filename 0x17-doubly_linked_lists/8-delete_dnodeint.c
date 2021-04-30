#include "lists.h"

/**
 * delete_dnodeint_at_index - This function deletes the node
 * at index index of a dlistint_t linked list.
 * @head: The start of the linked list.
 * @index: The number of node to delete.
 * Return: 1 if it succeeded, -1 if it failed.
 */

int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	unsigned int i = 0;
	dlistint_t *tmp = *head;

	if (!*head)
		return (-1);
	if (!tmp->next)
	{
		free(tmp);
		*head = NULL;
		return (1);
	}
	if (index == 0)
	{
		tmp->next->prev = NULL;
		*head = tmp->next;
		free(tmp);
		return (1);
	}
	while (tmp)
	{
		if (i == index - 1)
		{
			tmp->next = tmp->next->next;
			free(tmp->next->prev);
			tmp->next->prev = tmp;
			return (1);
		}
		i++;
		tmp = tmp->next;
	}
	if (index > i)
		return (-1);
	return (-1);
}
