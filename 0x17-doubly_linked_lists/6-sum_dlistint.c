#include "lists.h"

/**
 * sum_dlistint - This function  returns the sum of
 * all the data (n) of a dlistint_t linked list.
 * @head: The start of the linked list.
 * Return: The add of all data.
 */

int sum_dlistint(dlistint_t *head)
{
	int sum = 0;
	dlistint_t *tmp = head;

	while (tmp)
	{
		sum += tmp->n;
		tmp = tmp->next;
	}
	return (sum);
}
