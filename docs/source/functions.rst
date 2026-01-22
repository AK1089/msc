.. _functions:

Functions
=========

Functions are reusable pieces of code that can be called from scripts or other functions. Unlike scripts, which are triggered by events, functions must be called explicitly. Functions can accept parameters, perform operations, and optionally return a value.

.. contents:: Contents
   :local:

Why Use Functions?
------------------

Functions serve several purposes:

When you find yourself writing the same code in multiple scripts, extract it into a function. Change it once, and all callers benefit.

Functions can break complex scripts into manageable pieces. A script that handles a puzzle might call ``checkSolution()``, ``giveReward()``, and ``resetPuzzle()`` as separate functions.

Functions are required for ``@chatscript``, which needs to call a function when the player clicks a chat message.

Defining Functions
------------------

Functions are defined with the ``/function define`` command:

.. code-block:: console

    /function define <namespace> <ReturnType> <name>(<parameters>)

For a function that returns nothing, omit the return type (or use ``Void``):

.. code-block:: console

    /function define mymap greet()
    /function define mymap Void greet()

For a function that returns a value:

.. code-block:: console

    /function define mymap Int double(Int x)
    /function define mymap String formatScore(Int score, String name)

After defining the function, add its body using the script command:

.. code-block:: console

    /script create function mymap greet @player Hello!

Or import from paste.minr.org:

.. code-block:: console

    /script import function mymap greet <paste-id>

Parameters
----------

Parameters allow functions to work with different values each time they're called. Each parameter has a type and a name:

.. code-block:: console

    /function define mymap givePoints(Player target, Int amount)

When called, the values are copied into the function. Modifying a parameter inside the function does not affect the original variable:

.. code-block:: msc

    @define Int x = 5
    @var mymap::tryToChange(x)
    @player x is still {{x}}

.. code-block:: output

    x is still 5

Even if ``tryToChange`` sets its parameter to a different value, ``x`` remains 5.

Parameters must match the expected types. Calling ``givePoints("hello", 10)`` would fail because ``"hello"`` is not a Player.

Return Values
-------------

Functions can return a value using the ``@return`` operator:

.. code-block:: console

    /function define mymap Int add(Int a, Int b)

.. code-block:: msc

    @return a + b

The returned value can be used in expressions:

.. code-block:: msc

    @define Int result = mymap::add(3, 4)
    @player 3 + 4 = {{result}}
    @player Doubled: {{mymap::add(3, 4) * 2}}

.. code-block:: output

    3 + 4 = 7
    Doubled: 14

A function without a return type (or with ``Void``) cannot return a value, and its result cannot be used in expressions:

.. code-block:: msc

    @var mymap::greet()                    # OK - standalone call
    @define String x = mymap::greet()      # Error - greet returns nothing

If a function with a return type doesn't explicitly return, it returns ``null``.

Calling Functions
-----------------

Functions in the current namespace (set by ``@using``) can be called directly:

.. code-block:: msc

    @using mymap
    @var greet()
    @define Int x = add(1, 2)

Functions in other namespaces use the ``::`` specifier:

.. code-block:: msc

    @var mymap::greet()
    @define Int x = mymap::add(1, 2)

Built-in namespace functions work the same way:

.. code-block:: msc

    @define Double root = math::sqrt(16.0D)
    @define Int floor = math::floor(3.7D)

Methods are functions that belong to a type. They're called with dot notation:

.. code-block:: msc

    @define String name = player.getName()
    @define String upper = "hello".toUpperCase()
    @var player.sendMessage("Hi!")

Functions and Script Flow
-------------------------

Functions can use the same operators as scripts, including delays and prompts. Be aware that these affect the calling script:

.. code-block:: msc

    # In a function
    @player Starting countdown...
    @delay 3s
    @player Done!

When this function is called, the calling script pauses for 3 seconds.

Cooldowns in functions work differently. If a function has a ``@cooldown`` and is on cooldown when called, the calling script terminates immediately. This can be useful for rate-limiting, but can also cause unexpected behavior.

Functions do not have access to the ``player``, ``block``, or ``entity`` parameters that scripts have. If a function needs to work with a player, pass it as a parameter:

.. code-block:: console

    /function define mymap healPlayer(Player p)

.. code-block:: msc

    @var p.setHealth(20.0D)
    @var p.sendMessage("&aYou have been healed!")

Call it from a script:

.. code-block:: msc

    @var mymap::healPlayer(player)

Command Reference
-----------------

.. list-table::
    :widths: 40 60
    :header-rows: 1

    * - Command
      - Description
    * - ``/function define <namespace> [ReturnType] <name>(<params>)``
      - Creates a new function.
    * - ``/function remove <namespace> <name>``
      - Deletes a function.
    * - ``/function info <namespace> <name>``
      - Shows function details.
    * - ``/script create function <namespace> <name> <@operator> ...``
      - Adds a line to the function body.
    * - ``/script view function <namespace> <name>``
      - Views the function body.
    * - ``/script import function <namespace> <name> <id>``
      - Imports from paste.minr.org.
    * - ``/script export function <namespace> <name>``
      - Exports to paste.minr.org.

Example
-------

A complete example: a function that formats a player's stats.

.. code-block:: console

    /function define mymap String formatStats(Player p, Int score)

.. code-block:: msc

    @define String name = p.getName()
    @define Double health = p.getHealth()
    @return "&b" + name + "&r: " + score + " points, " + health + " hearts"

Using it in a script:

.. code-block:: msc

    @using mymap
    @player {{formatStats(player, score)}}

.. code-block:: output

    &brickyboy320&r: 42 points, 20.0 hearts
