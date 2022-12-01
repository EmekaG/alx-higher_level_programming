#include "lists.h"
#include <stdlib.h>

/**
 * _realloc - reallocates a memeory block
 * @ptr: pointer to the previous memory block
 * @prev: the size of the previous memory block
 * @new: the size of the current memory block
 *
 * Return: The pointer to the new memory block otherwise NULL
 */
void *_realloc(void *ptr, unsigned int prev, unsigned int new)
{
	void *newptr;
	unsigned int mini = prev < new ? prev : new;
	unsigned int i;

	if (new == prev)
		return (ptr);
	if (ptr != NULL)
	{
		if (new == 0)
		{
			free(ptr);
			return (NULL);
		}
		newptr = malloc(new);
		if (newptr != NULL)
		{
			for (i = 0; i < mini; i++)
				*((char *)new_ptr + i) = *((char *)ptr + i);
			free(ptr);
			return (newptr);
		}
		free(ptr);
		return (NULL);
	}
	else
	{
		newptr = malloc(new);
		return (newptr);
	}
}

/**
 * check_cycle - check if a linked list has a cycle in it
 * @list: list head
 *
 * Return: 1 if true, 0 if false
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow = list;

	if (list == NULL)
		return (0);

	fast = list->next;
	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
