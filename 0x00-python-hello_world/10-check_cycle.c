#include "lists.h"
/**
 * check_cycle - check if a singly linked list has a cycle in it
 * @list: pointer to the first element in the signly linked list
 * Return: 1 if there is a cycle, 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *temp;
	int n1 = 0, n2;

	current = list;
	while (current != NULL)
	{
		temp = list;
		n2 = 0;
		while (temp != NULL)
		{
			if (temp == current && n1 != n2)
				return (1);
			temp = temp->next;
			n2++;
		}
		current = current->next;
		n1++;
	}
	return (0);
}
