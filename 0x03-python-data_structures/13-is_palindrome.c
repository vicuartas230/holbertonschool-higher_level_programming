#include "lists.h"

/**
 * is_palindrome - This function checks if
 * a singly linked list is a palindrome.
 * @head: The start of the linked list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	unsigned int i = 0, j = 0, acum = 0, idx = 0;
	int arr[BUFSIZ];

	while (tmp)
	{
		arr[idx++] = tmp->n;
		tmp = tmp->next;
	}
	i = idx - 1;
	while (j < idx)
	{
		if (arr[i--] == arr[j++])
			acum++;
	}
	if (acum == idx)
		return (1);
	else
		return (0);
}
