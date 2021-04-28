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
	unsigned int i = 0;

	tmp = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	while (i < 4)
	{
		tmp = tmp->next;
		i++;
	}
	new->next = tmp->next;
	tmp->next = new;
	return (new);
}
