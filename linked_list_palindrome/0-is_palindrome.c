#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: the head of the linked list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int total_nodes = 1, half_nodes, count = 1;
	listint_t *queue, *current, *prev = NULL, *next, *half_list, *current_head;

	if (!head || !*head || !(*head)->next)
		return (1);

	current_head = *head;
	queue = (*head)->next;
	while (queue)
	{
		queue = queue->next;
		total_nodes++;
	}
	half_nodes = total_nodes / 2;

	current = *head;
	while (count <= half_nodes)
	{
		current = current->next;
		count++;
	}
	half_list = current;

	current = half_list;
	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	half_list->next = prev;

	current = prev;
	queue = *head;
	while (count <= half_nodes && queue)
	{
		if (current_head->n != queue->n)
			return (0);

		current_head = current_head->next;
		queue = queue->next;
		count++;
	}

	return (1);
}
