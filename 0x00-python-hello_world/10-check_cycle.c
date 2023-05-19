#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"
/**
 * check_cycle - check function
 * DESCRIPTION: a function that check if the singly linked
 *				list has a cycle, if so it returns 1
 *				otherwise it returns 0
 * @list: pointer to first node passed to the function
 * Return: 1 if it has a cycle or 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1 = list;
	listint_t *ptr2 = list;

	while (ptr2 != NULL && ptr2->next != NULL)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;
		if (ptr1 == ptr2)
		{
			return (1);
		}
	}
	return (0);
}

