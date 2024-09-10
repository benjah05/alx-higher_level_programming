#include "lists.h"
/**
 * check_cycle - check if a singly linked list has a cycle in it
 * @list: pointer to the first element in the signly linked list
 * Return: 1 if there is a cycle, 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *temp;

	current = list;
	while (current != NULL)
	{
		temp = list;
		while (temp != NULL)
		{
			if (temp == current)
				return (1);
			temp = temp->next;
		}
		current = current->next;
	}
	return (0);
}
