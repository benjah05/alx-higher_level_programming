#include "lists.h"
/**
 * insert_node - insert a number into a sorted singly linked list
 * @number: the number to be inserted in the list
 * Return: address of the new node, NULL in case of failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *slow, *fast, *numNode;

	numNode = malloc(sizeof(listint_t));
	if (numNode == NULL)
		return (NULL);
	numNode->n = number;
	numNode->next = NULL;
	if (*head == NULL && (*head)->n >= number)
	{
		numNode->next = *head;
		*head = numNode;
		return (numNode);
	}
	slow = *head;
	fast = (*head)->next;
	while (fast != NULL && fast->n < number)
	{
		slow = fast;
		fast = fast->next;
	}
	slow->next = numNode;
	numNode->next = fast;
	return (numNode);
}
