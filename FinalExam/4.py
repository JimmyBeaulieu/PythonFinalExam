# List is mutable. Tuple is immutable. Explain these 2 concepts. (1 points)
# What is slicing on Tuple? (1 point).
# Why does it work? Explain in detail with a code snippet (1 points)
# Tuple and Set have many similarities. Give me a use case for each.
# (in which case you would use Tuple? And in which case Set). (2 points)

# first question:
# Mutable means it can change value directly (you can add and remove elements at will),
# Immutable means that it can't change directly (you can't add or remove elements) and it needs to be copied in another
# memory adress to change value

# second question:
# tuple slicing is a feature that allows you to access a specific sequence of elements within a tuple.

# third question:
# To perform tuple slicing, you need to specify the start and stop indices of the range of elements you want to access
# in the format tuple[start:stop].
# For example, if you have a tuple called my_tuple that contains the elements (1, 2, 3, 4, 5),
# you can access the elements from the second to the fourth position by using: my_tuple[1:4],
# which would return the tuple (2, 3, 4).

# fourth question:
# A tuple is an ordered collection of elements, which means that the elements within a tuple have a specific position
# or index. Tuples are often used to store related data that you want to keep together, such as the coordinates of a
# point on a map or used as keys in a dictionary.

# A set is an unordered collection of unique elements, not stored in any particular order and doesn't allow for
# duplicate elements. Sets are useful for quickly checking whether an element exists in a collection,
# since the lookup time for sets is typically faster than for other data types.
