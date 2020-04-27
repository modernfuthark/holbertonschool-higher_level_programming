#include "lists.h"
/**
 * check_cycle - Check for a loop in a linked list
 * @list: Head of list
 * Return: 0 if no loop, 1 if a loop is found
 */

int check_cycle(listint_t *list)
{
	int i, flag = 0; /*If found, set to 1*/
	listint_t *copy;
	listint_t *copy2;

	if (!list)
		return (0);
	/*Save 2 copies of the list, one moves 1 ahead of the other*/
	copy = list;
	copy2 = list;

	for (i = 0; copy; i++)
	{
		copy = copy->next;

		if (copy)
		{
			copy = copy->next;

			copy2 = copy2->next;
		}
		/*If they line up, that means copy went back to the head of the lsit*/
		if (copy == copy2)
		{
			flag = 1;
			break;
		}
	}
	return (flag);
}

/*Whiteboarding description of code (shoutout to Bryant)*/
/*This'll be used for like, self reminding how I came to this conclusion*/
/*If the list ends, copy and copy2 should NEVER be the same value until null*/
/*But, if they do equal, that means copy has looped back to the start...*/
/*And caught up to copy2, revealing a loop in the list*/
/*Refer to 'Whiteboard for linked list' in Pictures for a 'drawing'*/
