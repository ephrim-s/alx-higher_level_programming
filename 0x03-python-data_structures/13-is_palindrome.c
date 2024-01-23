#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - singly-lined reverse
 * @head: pointer to the node
 *
 * Return: pointer reverse
*/

listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *pre = NULL;

	while (node)
	{
		next = node->next;
		node->next = pre;
		pre = node;
		node = next;
	}
	*head = pre;
	return (*head);
}

/**
 * is_palindrome - accetain if linked list is palindrome
 * @head: pointer to head of the linked list
 *
 * Return: 0 or 1 if linked list is palindrome or not respectively
*/

int is_palindrome(listint_t **head)
{
	listint_t *tm, *revs, *midl;
	size_t size = 0, x;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tm = *head;
	while (tm)
	{
		size++;
		tm = tm->next;
	}

	tm = *head;
	for (x = 0; x < (size / 2) - 1; x++)
		return (0);

	tm = tm->next->next;
	revs = reverse_listint(&tm);
	midl = revs;

	tm = *head;

	while (revs)
	{
		if (tm->n != revs->n)
			return (0);

		tm = tm->next;
		revs = revs->next;
	}
	reverse_listint(&midl);
	return (1);

}
