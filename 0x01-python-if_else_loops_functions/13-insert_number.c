#include "lists.h"
/**
 * insert_node - insert a number into a sorted singly linked list
 * @number: the number to be inserted in the list
 * Return: address of the new node, NULL in case of failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *numNode;

	if (head == NULL)
		return (NULL);
	numNode = malloc(sizeof(listint_t));
	if (numNode == NULL)
		return (NULL);
	temp = *head;
	while (temp != NULL)
	{
		if (temp->n < number)
			temp = temp->next;
		else
		{
			numNode->n = number;
			numNode->next = temp->next;
			temp->next = numNode;
			return (numNode);
		}
	}
	return (NULL);
}
