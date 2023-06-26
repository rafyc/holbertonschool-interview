#include "binary_trees.h"

/**
sorted_array_to_avl -function that builds an AVL tree from an array
@array: pointer to the first element of the array to be converted
@size: the number of element in the array
*/

binary_tree_t *create(binary_tree_t *parent, int value)
{
    binary_tree_t *new;

    new = malloc(sizeof(binary_tree_t));
    if(new == NULL)
        return (NULL);
    new->parent = parent;
    new->left = NULL;
    new->right = NULL;
    new->n = value;
    return (new);
}

avl_t *sorted_array_to_avl(int *array, size_t size)
{
    if (array == NULL || size == 0)
        return NULL;

    // Implementation logic to construct the AVL tree from the sorted array

    return NULL;  // Return the root node of the constructed AVL tree
}
