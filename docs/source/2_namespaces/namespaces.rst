Namespaces
==============

Namespaces are a way of separating variables, functions and types into logical groups to prevent name collisions. In previous versions of MSC, variables were global and could easily cause collisions when using common names like ``x`` or ``count``. With namespaces, the same variable name can exist in different namespaces without conflict.

Generally, a namespace encapsulates a given project, a module within a project, or a logical module that can be reused in different projects (such as the ``math`` namespace, which provides mathematical functions and constants).

.. _namespace_desc:

The Namespace
-----------------------------

A namespace consists of variables, functions and types. A user can define a namespace using a unique name. Within the namespace, variables can be defined to make them usable within the namespace. These are persistent variables and will be stored to file, meaning they can be re-used across scripts. Functions can also be defined within the namespace, allowing for reusable code blocks that can be called from scripts. Additionally, custom types can be defined within the namespace to create complex data structures.

Before being able to use a variable, function or type, they should be defined as element of a namespace. The definition of the variable requires a type. Persistent variables have to be defined in advance so that the compiler knows where to look and what type they are. See :ref:`Variables <variables>` for more details.

When using variables, functions or types in a script, the script should know what namespace the variable, function or type is in. If the namespace is undefined, it automatically defaults to the **local namespace** which contains variables that are *not persistent*. All variables within the local namespace should therefore be defined locally (that is, within the script). If using an undefined variable, the compiler will throw an error.

The local namespace is also present when using a specified namespace, and always takes precedence over the specified namespace. Any variables defined within the local namespace will shadow (that is, overrule) the variable in the specified namespace. This is to make sure that an addition of a same-named variable in the namespace will not change the functionality of the script. By explicitly accessing the namespace, as described in :ref:`Best Practice <namespace_best_practice>`, you can still target the shadowed variable in the specified namespace by using the temporary namespace specifier (**::**).

The local namespace is created at the start of a script, and deleted when the script terminates. Therefore the variables and types stored within the local namespace are *not persistent*.

.. _namespace_using:

Using Namespaces
-----------------------

When a script starts, it starts out with the **local namespace**. Unless defined, the local namespace contains no variables, functions or types.

A script can switch namespaces at any time using the **@using** script operation. Only one namespace will be active at any time, with the exception of the local namespace, which is always active and its variables always shadow the active namespace.

A variable or function can be temporarily accessed from a different namespace using the namespace specifier. A variable can be accessed using **namespace::variable**, a function using **namespace::function()**, and a type using **namespace::Type**.

Note that when executing a function, the function's namespace will be used. Variables can still be supplied from a different namespace through the parameters, and the function can still access other variables using the **@using** operator and temporary namespace specifier.

.. _namespace_best_practice:

Best Practice
--------------------

When using multiple variables, functions and/or types from one namespace, it is best to use **@using**.

Sometimes it is required to use multiple namespaces at the same time, such as using a variable from one namespace in a function of a different namespace. In this case you can use **@using** for the most frequently used namespace, to limit unnecessary words and characters.

When using a namespace once, it is best to use the temporary namespace specifier (**::**) since adding additional lines would be less clear than adding the specifier.

It can occur that a variable with the same name is both defined in the namespace that is currently set as **@using**, and in the local namespace (that is, earlier in the script). To access the local variable, there is no need to (and you cannot) use a namespace specifier to access the variable. To access the namespace variable, you are required to use the temporary namespace specifier (**::**) to access the variable, because the local namespace shadows the variable within the specified namespace, unless explicitly using the variable from the namespace.

In general, it is best to use the most readable approach. **@using** is intended for repeated usage, while **::** is intended for one-time-use of namespaces.
