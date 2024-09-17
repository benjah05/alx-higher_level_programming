#include "lists.h"
/**
 * is_palindrome - check if a list is palindrome
 * @head: pointer to the first element in the list
 * Return: 1 if True, 0 if False
 */
int is_palindrome(listint_t **head)
{
	listint_t *prev = NULL, *current, *next = NULL;
	listint_t *slow, *fast;

	if (head == NULL || *head == NULL)
		return (1);
	current = *head;
	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	slow = *head;
	fast = *head;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	return (1);

}
