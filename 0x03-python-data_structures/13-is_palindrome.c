#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"
/**
 * is_palindrome - check function
 * DESCRIPTION: a function that check if the singly linked
 *				list is a plaindrome, if so it returns 1
 *				otherwise it returns 0
 * @head: pointer to first node passed to the function
 * Return: 1 if it's plaindrome or 0 if not
 */
int is_palindrome(listint_t **head)
{
	int len = 0, first_half, second_half;
	listint_t *current = *head;
	int *arr = NULL;

	while (current != NULL)
	{
		len++;
		arr = realloc(arr, len * sizeof(int));
		if (arr == NULL)
		{
			free(arr);
			return (-1);
		}
		arr[len - 1] = current->n;
		current = current->next;
	}

	first_half = (len / 2) - 1;
	if (len % 2 == 0)
	{
		second_half = first_half + 1;
	}
	else
	{
		second_half = first_half + 2;
	}

	while (second_half < len)
	{
		if (arr[first_half] != arr[second_half])
		{
			free(arr);
			return (0);
		}
		first_half--;
		second_half++;
	}

	free(arr);
	return (1);
}

