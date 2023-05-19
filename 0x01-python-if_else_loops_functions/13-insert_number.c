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
	node->next = NULL;
	if (*head == NULL)
	{
		*head = node;
		return (node);
	}
	if ((*head)->n > number)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	current = *head;
	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}
	temp = current->next;
	current->next = node;
	node->next = temp;
	return (node);
}
