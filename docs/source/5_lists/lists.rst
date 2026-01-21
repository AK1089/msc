.. _lists:

Lists
===================================

Lists are an ordered sequence of elements. In MSC, list indices are zero-based.

.. _lists_constructors:

Constructors
-------------------------

Lists are defined using ``T[]``, where ``T`` is the element type (e.g. ``Int[]`` is a list of integers).

Lists can be initialised with ``T[a, b, ..., z]`` where ``a, b, ..., z`` are zero or more instances of type ``T``.

.. code-block:: msc

    @define Int[] xs = Int[5]
    @define Int[] ys = Int[]
    @define Int[] zs = Int[5, 3, 2, 1]

    @player {{xs}}
    @player {{ys}}
    @player {{zs}}

.. code-block:: output

    [5]
    []
    [5, 3, 2, 1]

.. _list_indexing:

Indexing
--------------------

Retrieving a value at an index:

.. code-block:: msc

    @define Int[] xs = Int[5, 10, 15]
    @player {{xs[0]}}
    @player {{xs[2]}}

.. code-block:: output

    5
    15

Setting the value at an index:

.. code-block:: msc

    @define Int[] xs = Int[5, 10, 15]
    @var xs[1] = 99
    @player {{xs}}

.. code-block:: output

    [5, 99, 15]

Both reading and writing in one expression:

.. code-block:: msc

    @define Int[] xs = Int[5, 10]
    @var xs[1] = xs[0] + 1
    @player {{xs}}

.. code-block:: output

    [5, 6]

Accessing an out of bounds index will throw an ``IndexOutOfBoundException`` and terminate the script.

.. _lists_method:

Methods
--------------

All List Types
^^^^^^^^^^^^^^

These methods are available on all list types:

.. list-table::
    :widths: 50 50
    :stub-columns: 0

    * - Int **length**\()
      - Returns the number of items in the list.
    * - **append**\(T value)
      - Appends a value to the end of the list.
    * - **remove**\(Int index)
      - Removes the item at the specified index from the list.
    * - **clear**\()
      - Removes all items from the list.
    * - **reverse**\()
      - Reverses the order of the items in the list.
    * - **shuffle**\()
      - Randomises the order of the items in the list.
    * - T **pop**\()
      - Removes the last element of the list and returns it.
    * - Boolean **contains**\(T value)
      - Returns whether the list contains an element equal to value.
    * - Int **find**\(T value)
      - Returns the first index that matches the value. Throws an
        ``ElementNotFoundException`` if the value is not in the list.
        (Tip: always use ``contains`` before ``find``)

Numeric Lists
^^^^^^^^^^^^^

These methods are available on ``Int[]``, ``Long[]``, ``Float[]``, and ``Double[]``:

.. list-table::
    :widths: 50 50
    :stub-columns: 0

    * - Number **sum**\()
      - Returns the sum of all elements in the list.
    * - Number **avg**\()
      - Returns the average of all elements in the list.

String Lists
^^^^^^^^^^^^

These methods are available on ``String[]``:

.. list-table::
    :widths: 50 50
    :stub-columns: 0

    * - String **concat**\()
      - Concatenates all strings in the list together.
        ``String["hello", "world"].concat()`` yields ``"helloworld"``.
    * - String **join**\(String delimiter)
      - Joins all strings in the list with the delimiter between each.
        ``String["hello", "world"].join(" ")`` yields ``"hello world"``.

Note: The ``String.split(String separator)`` method (on the String type) returns a ``String[]``. For example, ``"hi world".split(" ")`` yields ``["hi", "world"]``.

Appending with Index Assignment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An alternate way to append to a list is to assign a value to an index equal to the current length:

.. code-block:: msc

    @define Int[] x = Int[1, 2, 3]
    @var x[x.length()] = 4
    @player {{x}}

.. code-block:: output

    [1, 2, 3, 4]

.. _lists_namespace:

The list Namespace
------------------

The ``list`` namespace contains the ``range()`` function.

``Int[] list::range(Int start, Int end)`` generates a list of integers from ``start`` (inclusive) to ``end`` (exclusive).

.. code-block:: msc

    @player {{list::range(0, 5)}}
    @player {{list::range(3, 7)}}

.. code-block:: output

    [0, 1, 2, 3, 4]
    [3, 4, 5, 6]

This is particularly useful for iterating through list indices:

.. code-block:: msc

    @define String[] names = String["Alice", "Bob", "Charlie"]
    @for Int i in list::range(0, names.length())
        @player {{i}}: {{names[i]}}
    @done

.. code-block:: output

    0: Alice
    1: Bob
    2: Charlie

.. _lists_for_loops:

For Loops
----------------

For loops iterate over lists. They are defined with ``@for <Type> <item> in <list>`` and terminated with ``@done``.

Iterating directly over elements:

.. code-block:: msc

    @for Int num in Int[1, 2, 3, 4, 5]
        @player {{num}}
    @done

.. code-block:: output

    1
    2
    3
    4
    5

Using ``list::range()`` to iterate by index:

.. code-block:: msc

    @for Int i in list::range(1, 6)
        @player {{i}}
    @done

.. code-block:: output

    1
    2
    3
    4
    5

Iterating through a list by index:

.. code-block:: msc

    @define Int[] values = Int[10, 50, 90]
    @for Int i in list::range(0, values.length())
        @player Index {{i}} = {{values[i]}}
    @done

.. code-block:: output

    Index 0 = 10
    Index 1 = 50
    Index 2 = 90

.. _list_relative_indexing:

Relative Variable Indexing
--------------------------

Relative variables (see :ref:`Variables <variables>`) store a separate value for each player. You can access another player's value using player indexing syntax.

Suppose we have a relative variable defined as:

.. code-block:: console

    /variable define mymap relative Int score = 0

And different players have different scores: rickyboy320 has 3, CreepaShadowz has 7.

To read another player's value:

.. code-block:: msc

    @player {{score[Player("rickyboy320")]}}

.. code-block:: output

    3

.. code-block:: msc

    @player {{score[Player("CreepaShadowz")]}}

.. code-block:: output

    7

Note that looking up a player by name can fail if they're offline. For reliable lookups, use UUIDs:

.. code-block:: msc

    @player {{score[Player("63664a36-a4c4-4541-a337-dd5639600407")]}}

If a relative variable is indexed with a player who has no value set yet, the default value is returned.

Writing to another player's relative variable is also supported:

.. code-block:: msc

    @player Before: {{score[Player("rickyboy320")]}}
    @var score[Player("rickyboy320")] = 8
    @player After: {{score[Player("rickyboy320")]}}

.. code-block:: output

    Before: 3
    After: 8
