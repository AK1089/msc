.. _appendix_namespaces:

Built-in Namespaces
===================

Quick reference for built-in namespace functions. For creating and using namespaces, see :ref:`Namespaces <namespaces>`.

.. contents::
   :local:
   :depth: 2

system
------

Miscellaneous system functions, such as time.

**Variables:** None

**Functions:**

.. list-table::
   :widths: 35 15 50
   :header-rows: 1

   * - Function
     - Return Type
     - Description
   * - ``currentTimeMillis()``
     - Long
     - Returns the current time in milliseconds since Unix epoch (January 1, 1970).
   * - ``getTPS()``
     - Double[]
     - Returns a list of 3 values: average TPS over the last 1, 5, and 15 minutes.

math
----

Common mathematical operations.

**Variables:** None

**Functions:**

.. list-table::
   :widths: 40 15 45
   :header-rows: 1

   * - Function
     - Returns
     - Description
   * - ``sqrt(Double value)``
     - Double
     - Positive square root of value.
   * - ``abs(Double value)``
     - Double
     - Absolute value.
   * - ``pow(Double value, Double exp)``
     - Double
     - Value raised to the power of exp.
   * - ``randomInt()``
     - Int
     - Random integer (full Int range).
   * - ``randomLong()``
     - Long
     - Random long (full Long range).
   * - ``randomFloat()``
     - Float
     - Random float between 0.0 and 1.0.
   * - ``randomDouble()``
     - Double
     - Random double between 0.0 and 1.0.
   * - ``random(Double min, Double max)``
     - Double
     - Random double between min and max.
   * - ``sin(Double x)``
     - Double
     - Sine of x (degrees).
   * - ``cos(Double x)``
     - Double
     - Cosine of x (degrees).
   * - ``tan(Double x)``
     - Double
     - Tangent of x (degrees).
   * - ``arcsin(Double x)``
     - Double
     - Arcsine of x (returns degrees).
   * - ``arccos(Double x)``
     - Double
     - Arccosine of x (returns degrees).
   * - ``arctan(Double x)``
     - Double
     - Arctangent of x (returns degrees).
   * - ``radsin(Double x)``
     - Double
     - Sine of x (radians).
   * - ``radcos(Double x)``
     - Double
     - Cosine of x (radians).
   * - ``radtan(Double x)``
     - Double
     - Tangent of x (radians).
   * - ``radarcsin(Double x)``
     - Double
     - Arcsine of x (returns radians).
   * - ``radarccos(Double x)``
     - Double
     - Arccosine of x (returns radians).
   * - ``radarctan(Double x)``
     - Double
     - Arctangent of x (returns radians).
   * - ``rad(Double x)``
     - Double
     - Convert degrees to radians.
   * - ``deg(Double x)``
     - Double
     - Convert radians to degrees.

For special cases (NaN, infinity, etc.), see `Java Math documentation <https://docs.oracle.com/javase/10/docs/api/java/lang/Math.html>`_.

util
----

Utility functions.

**Variables:** None

**Functions:**

.. list-table::
   :widths: 45 15 40
   :header-rows: 1

   * - Function
     - Returns
     - Description
   * - ``executeAndQuerySuccess(String cmd)``
     - Boolean
     - Run an ``/execute`` command and return whether it succeeded.
   * - ``executeAndQueryResult(String cmd)``
     - Int
     - Run an ``/execute`` command and return its result value.
   * - ``randomUUID()``
     - String
     - Generate a random UUID string.

format
------

String formatting utilities.

**Variables:** None

**Functions:**

.. list-table::
   :widths: 50 15 35
   :header-rows: 1

   * - Function
     - Returns
     - Description
   * - ``formatDate(Long millis, String format)``
     - String
     - Format a Unix timestamp (milliseconds) using the given format string.

timer
-----

Timer management functions for maps and challenges.

**Variables:** None

**Functions:**

.. list-table::
   :widths: 50 15 35
   :header-rows: 1

   * - Function
     - Returns
     - Description
   * - ``getMapTimer(Player p, String mapcode)``
     - Timer
     - Get a player's timer for a map.
   * - ``getChallengeTimer(Player p, String code)``
     - Timer
     - Get a player's timer for a challenge.
   * - ``getCustomTimer(Player p, String tag)``
     - Timer
     - Get a player's custom timer by tag.
   * - ``getSpecialTimer(Player p, String tag)``
     - Timer
     - Get a player's special timer.
   * - ``removeCustomTimer(Player p, String tag)``
     - (void)
     - Remove a custom timer.
   * - ``formatTime(Long time)``
     - String
     - Format a time value as a human-readable string.

.. warning::

   Never store Timer instances in namespace variables, as they will break silently. Always use ``timer::getCustomTimer(...)`` to retrieve a fresh reference each time.

list
----

List utility functions.

**Variables:** None

**Functions:**

.. list-table::
   :widths: 40 15 45
   :header-rows: 1

   * - Function
     - Returns
     - Description
   * - ``range(Int start, Int end)``
     - Int[]
     - Generate a list of consecutive integers from start (inclusive) to end (exclusive).
