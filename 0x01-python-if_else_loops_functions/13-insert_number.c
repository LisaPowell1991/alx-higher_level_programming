#include "lists.h"

/**
 * insert_node - inserts a number into a
 * sorted singly linked list.
 * @head: double pointer
 * @number: integer
 *
 * Return: The address of the new node
 * or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current = *head;

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (current->next && number > current->next->n)
		current = current->next;

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
