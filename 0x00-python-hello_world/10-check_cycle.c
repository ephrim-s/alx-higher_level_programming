#include "lists.h"
/**
 * check_cycle - find out if there is singly linked list inthe cycle
 * @list: list of links
 * Return: 1 on sucess and 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *chck_1, *chck_2;

	if (list == NULL || list->next == NULL)
		return (0);

	chck_1 = list->next;
	chck_2 = list->next->next;

	while (chck_1 && chck_2 && chck_2->next)
	{
		if (chck_1 == chck_2)
			return (1);
		chck_1 = chck_1->next;
		chck_2 = chck_2->next;
	}
	return (0);
}
