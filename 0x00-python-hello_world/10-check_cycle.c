#include "lists.h"
/**
 * check_cycle - check if a singly linked list has a cycle in it
 * @list: pointer to the first element in the signly linked list
 * Return: 1 if there is a cycle, 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current;
	int n1 = 0, n2;

	if (list == NULL)
		return (NULL);
	current = list;
	while (list != NULL)
	{
		n2 = 0;
		while (current != NULL)
		{
			if (current->next == list->next && n1 != n2)
				return (1);
			current = current->next;
			n2++;
		}
		list = list->next;
		n1++;
	}
	return (0);
}
