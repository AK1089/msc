.. _lists:

Lists
=====

Lists are ordered sequences of elements of the same type. They allow you to store and manipulate collections of values. In MSC, list indices are zero-based, meaning the first element is at index 0, the second at index 1, and so on.

.. contents:: Contents
   :local:

Creating Lists
--------------

Lists are defined using ``T[]``, where ``T`` is the element type. For example, ``Int[]`` is a list of integers and ``String[]`` is a list of strings.

To create a list with initial values, use the syntax ``T[value1, value2, ...]``:

.. code-block:: msc

    @define Int[] numbers = Int[5, 10, 15]
    @define String[] names = String["Alice", "Bob", "Charlie"]
    @define Boolean[] flags = Boolean[true, false, true]
    @player {{numbers}}
    @player {{names}}

.. code-block:: output

    [5, 10, 15]
    [Alice, Bob, Charlie]

To create an empty list, use ``T[]`` with no values:

.. code-block:: msc

    @define Int[] empty = Int[]
    @player {{empty}}
    @player Length: {{empty.length()}}

.. code-block:: output

    []
    Length: 0

Accessing Elements
------------------

Use square brackets with an index to access elements. Remember that indices start at 0:

.. code-block:: msc

    @define String[] names = String["Alice", "Bob", "Charlie"]
    @player First: {{names[0]}}
    @player Second: {{names[1]}}
    @player Last: {{names[2]}}

.. code-block:: output

    First: Alice
    Second: Bob
    Last: Charlie

You can also modify elements by assigning to an index:

.. code-block:: msc

    @define Int[] numbers = Int[5, 10, 15]
    @var numbers[1] = 99
    @player {{numbers}}

.. code-block:: output

    [5, 99, 15]

Accessing an index outside the list bounds will tell you that the index is out of bounds for your list size, causing an error.

List Methods
------------

All lists have the following methods:

.. list-table::
    :widths: 40 60
    :header-rows: 1

    * - Method
      - Description
    * - ``length()``
      - Returns the number of elements in the list.
    * - ``append(value)``
      - Adds a value to the end of the list.
    * - ``remove(index)``
      - Removes the element at the specified index.
    * - ``clear()``
      - Removes all elements from the list.
    * - ``pop()``
      - Removes and returns the last element.
    * - ``reverse()``
      - Reverses the order of elements in place.
    * - ``shuffle()``
      - Randomizes the order of elements in place.
    * - ``contains(value)``
      - Returns true if the list contains the value.
    * - ``find(value)``
      - Returns the index of the first occurrence of value. Returns -1 if not found.

Example using these methods:

.. code-block:: msc

    @define Int[] nums = Int[1, 2, 3]
    @var nums.append(4)
    @player After append: {{nums}}
    @var nums.reverse()
    @player After reverse: {{nums}}
    @player Contains 2? {{nums.contains(2)}}
    @define Int last = nums.pop()
    @player Popped: {{last}}, remaining: {{nums}}

.. code-block:: output

    After append: [1, 2, 3, 4]
    After reverse: [4, 3, 2, 1]
    Contains 2? true
    Popped: 1, remaining: [4, 3, 2]

Numeric lists (``Int[]``, ``Long[]``, ``Float[]``, ``Double[]``) have additional methods:

.. list-table::
    :widths: 40 60
    :header-rows: 1

    * - Method
      - Description
    * - ``sum()``
      - Returns the sum of all elements.
    * - ``avg()``
      - Returns the average of all elements.

.. code-block:: msc

    @define Int[] scores = Int[85, 90, 78, 92]
    @player Total: {{scores.sum()}}
    @player Average: {{scores.avg()}}

.. code-block:: output

    Total: 345
    Average: 86.25

String lists (``String[]``) have methods for joining:

.. list-table::
    :widths: 40 60
    :header-rows: 1

    * - Method
      - Description
    * - ``concat()``
      - Concatenates all strings together.
    * - ``join(delimiter)``
      - Joins all strings with a delimiter between them.

.. code-block:: msc

    @define String[] words = String["hello", "world"]
    @player {{words.concat()}}
    @player {{words.join(" ")}}
    @player {{words.join(", ")}}

.. code-block:: output

    helloworld
    hello world
    hello, world

The inverse operation is ``String.split()``, which splits a string into a list:

.. code-block:: msc

    @define String[] parts = "one,two,three".split(",")
    @player {{parts}}

.. code-block:: output

    [one, two, three]

The list Namespace
------------------

The ``list`` namespace provides the ``range()`` function, which generates a list of consecutive integers:

.. code-block:: msc

    @player {{list::range(0, 5)}}
    @player {{list::range(3, 7)}}

.. code-block:: output

    [0, 1, 2, 3, 4]
    [3, 4, 5, 6]

The first argument is inclusive (included in the result) and the second is exclusive (not included). This is useful for generating index sequences.

For Loops
---------

The ``@for`` loop iterates over lists. The syntax is ``@for <Type> <variable> in <list>`` and the loop ends with ``@done``:

.. code-block:: msc

    @for String name in String["Alice", "Bob", "Charlie"]
        @player Hello, {{name}}!
    @done

.. code-block:: output

    Hello, Alice!
    Hello, Bob!
    Hello, Charlie!

You can iterate over any list, including ones stored in variables or generated by ``list::range()``:

.. code-block:: msc

    @define Int[] numbers = Int[10, 20, 30]
    @for Int n in numbers
        @player {{n}}
    @done

.. code-block:: output

    10
    20
    30

To iterate with an index, use ``list::range()`` with the list's length:

.. code-block:: msc

    @define String[] items = String["sword", "shield", "potion"]
    @for Int i in list::range(0, items.length())
        @player {{i}}: {{items[i]}}
    @done

.. code-block:: output

    0: sword
    1: shield
    2: potion
