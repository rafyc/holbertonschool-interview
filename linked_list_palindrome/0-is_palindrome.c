#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - function that check if a linked list is a palindrome
 * @head: the beginning of the linked list
 * Return: 1 if it is a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev = NULL, *next;
    listint_t *first_half = *head, *second_half;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        second_half = slow->next;
    }
    else
    {
        second_half = slow;
    }

    prev->next = NULL;

    while (second_half != NULL)
    {
        next = second_half->next;
        second_half->next = prev;
        prev = second_half;
        second_half = next;
    }

    second_half = prev;

    while (second_half != NULL)
    {
        if (first_half->n != second_half->n)
            return (0);

        first_half = first_half->next;
        second_half = second_half->next;
    }

    return (1);
}
