#include "lists.h"

/**
  * insert_node - This function inserts a number
  * into a sorted singly linked list.
  * @head: The start of the linked list.
  * @number: The number to insert.
  * Return: the address of the new node, or NULL if it failed.
  */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL, *new = NULL;

	tmp = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (number < 0)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	if (!*head)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	while (tmp)
	{
		if (tmp->next == NULL)
		{
			new->next = NULL;
			tmp->next = new;
			return (new);
		}
		if (tmp->n < number && number <= tmp->next->n)
		{
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
		tmp = tmp->next;
	}
	return (NULL);
}
