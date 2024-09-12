#include "lists.h"
/**
 * insert_node - insert a number into a sorted singly linked list
 * @number: the number to be inserted in the list
 * Return: address of the new node, NULL in case of failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *slow, *fast, *numNode;

	slow = *head;
	fast = *head;
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
	while (slow && fast && fast->next && fast->n < number)
	{
		slow = fast;
		fast = fast->next;
	}
	if (fast == NULL)
	{
		slow->next = numNode;
		return (numNode);
	}
	slow->next = numNode;
	numNode->next = fast;
	return (numNode);
}
