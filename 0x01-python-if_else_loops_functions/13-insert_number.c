#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - insert function
 * DESCRIPTION: a function that inserts a new
 *				node in a sorted linked list
 * @head: pointer to the first node passed to the function
 * @number: the node data
 * Return: address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *temp, *current;

	if (head == NULL)
		return (NULL);
	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	current = *head;
	if (*head == NULL)
	{
		node->next = NULL;
		*head = node;
		return (node);
	}
	if (current->n > number)
	{
		node->next = current;
		*head = node;
		return (node);
	}
	while (current != NULL)
	{
		if (current->next->n > number || current->next == NULL)
		{
			temp = current->next;
			current->next = node;
			node->next = temp;
			return (node);
		}
		if (current->next == NULL)
		{
			current->next = node;
			node->next = NULL;
			return (node);
		}
	current = current->next;
	}
	free(node);
	return (NULL);
}
