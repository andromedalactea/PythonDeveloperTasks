# Python Misc Questions

1. **To indicate and propagate errors: use try/except or return an error value?**

   I prefer using `try/except` to handle errors because it provides a clear and explicit way to manage exceptions, especially when dealing with unexpected errors or operations that might fail due to conditions beyond our control. However, in simple functions where expected errors can be logically and directly handled, returning an error value can be a valid option.

2. **Explain the difference between mutable and immutable types.**

   - **Mutable Types:**
     - These types allow modification of their content after creation.
     - Examples: lists (`list`), dictionaries (`dict`), sets (`set`).

     ```python
     my_list = [1, 2, 3]
     my_list[0] = 4  # Modifies the list
     print(my_list)  # Output: [4, 2, 3]
     ```

   - **Immutable Types:**
     - These types do not allow modification of their content after creation.
     - Examples: strings (`str`), tuples (`tuple`), numbers (`int`, `float`).

     ```python
     my_tuple = (1, 2, 3)
     my_tuple[0] = 4  # Will raise an error because tuples are immutable
     ```


3. **Define lambda, iterator, generator; and give examples how to use them.**

   - **Lambda:**
     - A small anonymous function defined using the `lambda` keyword.
     - Used to define short, one-time-use functions.

     ```python
     sum = lambda x, y: x + y
     print(sum(2, 3))  # Output: 5
     ```

   - **Iterator:**
     - An object that allows traversing a collection of elements one at a time.
     - Defined with the methods `__iter__()` and `__next__()`.

     ```python
     my_list = [1, 2, 3]
     my_iterator = iter(my_list)
     print(next(my_iterator))  # Output: 1
     print(next(my_iterator))  # Output: 2
     print(next(my_iterator))  # Output: 3
     ```

   - **Generator:**
     - A function that produces a sequence of results using the `yield` keyword.
     - Used to create iterators in a simpler and more memory-efficient way, especially for large data volumes.

     ```python
     def counter(max):
         n = 0
         while n < max:
             yield n
             n += 1

     for number in counter(3):
         print(number)  # Output: 0 1 2
     ```

4. **What do you use for testing? Linting? Debugging? Type enforcement?**

   - **Testing:**
     - I use `pytest` for unit and integration testing due to its simplicity and extensibility.

     ```sh
     pip install pytest
     pytest
     ```

   I currently use unit tests primarily and am not advanced in the field of testing, but I would love to delve deeper into this competency.
