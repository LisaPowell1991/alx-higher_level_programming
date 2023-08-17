#include "lists.h"

/**
 * dlistint_len - function that returns
 * the number of elements in a linked list.
 * @h: Pointer to the head of the doubly link list
 *
 * Return: the number of elements.
 */

size_t dlistint_len(const dlistint_t *h)
{
	size_t count = 0;

	while (h != NULL)
	{
		h = h->next;
		count++;
	}
	return (count);
}
