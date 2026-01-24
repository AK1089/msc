.. _appendix_types:

Built-in Types
==============

Quick reference for built-in type constructors and methods. For operator compatibility, see :doc:`operators`.

.. contents::
   :local:
   :depth: 2

Primitives
----------

String
^^^^^^

Represents plain text. Any text surrounded by ``"`` is a String literal.

**Default value:** ``null``

**Constructors:**

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Constructor
     - Description
   * - ``String(String value)``
     - Clone a String.
   * - ``String(Int value)``
     - Convert Int to text.
   * - ``String(Long value)``
     - Convert Long to text.
   * - ``String(Float value)``
     - Convert Float to text.
   * - ``String(Double value)``
     - Convert Double to text.
   * - ``String(Boolean value)``
     - Convert Boolean to text (``"true"`` or ``"false"``).
   * - ``String(Player value)``
     - Get player name.
   * - ``String(Entity value)``
     - Get entity UUID.
   * - ``String(Block value)``
     - Get block coordinates.
   * - ``String(Item value)``
     - Get item as text.

**Methods:**

.. list-table::
   :widths: 45 15 40
   :header-rows: 1

   * - Method
     - Return Type
     - Description
   * - ``contains(String seq)``
     - Boolean
     - True if String contains seq.
   * - ``equalsIgnoreCase(String other)``
     - Boolean
     - Case-insensitive equality check.
   * - ``matches(String regex)``
     - Boolean
     - True if String matches regex pattern.
   * - ``startsWith(String prefix)``
     - Boolean
     - True if String starts with prefix.
   * - ``indexOf(String seq)``
     - Int
     - Index of first occurrence, or -1 if not found.
   * - ``length()``
     - Int
     - Number of characters.
   * - ``replace(String old, String new)``
     - String
     - Replace all occurrences of old with new.
   * - ``substring(Int start, Int end)``
     - String
     - Substring from start (inclusive) to end (exclusive).
   * - ``toLowerCase()``
     - String
     - Convert to lowercase.
   * - ``toUpperCase()``
     - String
     - Convert to uppercase.
   * - ``trim()``
     - String
     - Remove leading/trailing whitespace.
   * - ``split(String delimiter)``
     - String[]
     - Split into a list by delimiter.

Int
^^^

Represents whole numbers. Range: -2,147,483,648 to 2,147,483,647.

**Default value:** ``0``

**Literal:** Any whole number (``42``, ``-7``, ``0``)

**Constructors:**

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Constructor
     - Description
   * - ``Int(Int value)``
     - Clone an Int.
   * - ``Int(Long value)``
     - Cast Long to Int (precision loss).
   * - ``Int(Float value)``
     - Discard decimals.
   * - ``Int(Double value)``
     - Discard decimals.
   * - ``Int(String value)``
     - Parse String to Int. Throws NumberFormatException if invalid.

**Methods:**

.. list-table::
   :widths: 35 15 50
   :header-rows: 1

   * - Method
     - Return Type
     - Description
   * - ``floor(Double x)``
     - Int
     - Floor of a double (static).
   * - ``ceiling(Double x)``
     - Int
     - Ceiling of a double (static).

Long
^^^^

Represents large whole numbers. Range: -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807.

**Default value:** ``0``

**Literal:** Number with ``L`` suffix (``42L``, ``-7L``)

**Constructors:**

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Constructor
     - Description
   * - ``Long(Int value)``
     - Upcast Int to Long.
   * - ``Long(Long value)``
     - Clone a Long.
   * - ``Long(Float value)``
     - Discard decimals.
   * - ``Long(Double value)``
     - Discard decimals.
   * - ``Long(String value)``
     - Parse String to Long. Throws NumberFormatException if invalid.

**Methods:** Same as Int.

Float
^^^^^

Represents decimal numbers with single precision.

**Default value:** ``0.0``

**Literal:** Any decimal number (``3.14``, ``-0.5``, ``1.0``)

**Constructors:**

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Constructor
     - Description
   * - ``Float(Int value)``
     - Cast Int to Float.
   * - ``Float(Long value)``
     - Cast Long to Float (precision loss).
   * - ``Float(Float value)``
     - Clone a Float.
   * - ``Float(Double value)``
     - Cast Double to Float (precision loss).
   * - ``Float(String value)``
     - Parse String to Float. Throws NumberFormatException if invalid.

**Methods:** None.

Double
^^^^^^

Represents decimal numbers with double precision.

**Default value:** ``0.0``

**Literal:** Number with ``D`` suffix (``3.14D``, ``1D``)

**Constructors:**

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Constructor
     - Description
   * - ``Double(Int value)``
     - Cast Int to Double.
   * - ``Double(Long value)``
     - Cast Long to Double.
   * - ``Double(Float value)``
     - Upcast Float to Double.
   * - ``Double(Double value)``
     - Clone a Double.
   * - ``Double(String value)``
     - Parse String to Double. Throws NumberFormatException if invalid.

**Methods:** None.

Boolean
^^^^^^^

Represents ``true`` or ``false``.

**Default value:** ``false``

**Literal:** ``true`` or ``false``

**Constructors:**

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Constructor
     - Description
   * - ``Boolean(Boolean value)``
     - Copy a Boolean.
   * - ``Boolean(String value)``
     - Parse ``"true"`` or ``"false"``. Defaults to false.

**Methods:** None.

Minecraft Objects
-----------------

Player
^^^^^^

Represents an online Minecraft player.

**Default value:** ``null``

**Constructors:**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Constructor
     - Description
   * - ``Player(String nameOrUUID)``
     - Find player by name or UUID. Returns null if not found.
   * - ``Player(Int x, Int y, Int z, String world)``
     - Find player at coordinates. Returns null if not found.
   * - ``Player(String name, Player visibleTo)``
     - Find player by name, only if visible to visibleTo.

**Methods:**

.. list-table::
   :widths: 45 15 40
   :header-rows: 1

   * - Method
     - Return Type
     - Description
   * - ``getName()``
     - String
     - Player's Minecraft username.
   * - ``getDisplayName()``
     - String
     - Player's display name (e.g., nickname).
   * - ``getUniqueId()``
     - String
     - Player's UUID.
   * - ``getRank()``
     - String
     - Player's server rank.
   * - ``getLocale()``
     - String
     - Player's client locale.
   * - ``getX()``
     - Double
     - X coordinate.
   * - ``getY()``
     - Double
     - Y coordinate.
   * - ``getZ()``
     - Double
     - Z coordinate.
   * - ``getYaw()``
     - Float
     - Rotation around Y axis.
   * - ``getPitch()``
     - Float
     - Rotation around X axis.
   * - ``getWorld()``
     - String
     - Current world name.
   * - ``getLocation()``
     - Location
     - Player's location.
   * - ``teleport(Position pos)``
     - (void)
     - Teleport player to position.
   * - ``getHealth()``
     - Double
     - Current health (0 = dead).
   * - ``setHealth(Double hp)``
     - (void)
     - Set health (0 to maxHealth).
   * - ``getMaxHealth()``
     - Double
     - Maximum health.
   * - ``setMaxHealth(Double hp)``
     - (void)
     - Set maximum health.
   * - ``damage(Double amount)``
     - (void)
     - Deal damage to player.
   * - ``getFoodLevel()``
     - Float
     - Current food level.
   * - ``setFoodLevel(Int level)``
     - (void)
     - Set food level.
   * - ``getSaturation()``
     - Float
     - Current saturation level.
   * - ``setSaturation(Float level)``
     - (void)
     - Set saturation level.
   * - ``getExp()``
     - Float
     - XP progress toward next level.
   * - ``setExp(Float exp)``
     - (void)
     - Set XP progress.
   * - ``getLevel()``
     - Float
     - Current XP level.
   * - ``setLevel(Int level)``
     - (void)
     - Set XP level.
   * - ``giveExp(Int amount)``
     - (void)
     - Give XP points.
   * - ``giveExpLevels(Int amount)``
     - (void)
     - Give XP levels (negative to take).
   * - ``getFallDistance()``
     - Float
     - Distance fallen.
   * - ``getFireTicks()``
     - Int
     - Ticks until fire stops.
   * - ``setFireTicks(Int ticks)``
     - (void)
     - Set fire ticks.
   * - ``getTimePlayed()``
     - Long
     - Playtime in milliseconds.
   * - ``isDead()``
     - Boolean
     - True if marked for removal.
   * - ``isOnline()``
     - Boolean
     - True if currently online.
   * - ``isOp()``
     - Boolean
     - True if server operator.
   * - ``isFlying()``
     - Boolean
     - True if flying.
   * - ``isOnGround()``
     - Boolean
     - True if on solid ground.
   * - ``isSneaking()``
     - Boolean
     - True if sneaking.
   * - ``isSprinting()``
     - Boolean
     - True if sprinting.
   * - ``isGliding()``
     - Boolean
     - True if gliding.
   * - ``isInsideVehicle()``
     - Boolean
     - True if in a vehicle.
   * - ``leaveVehicle()``
     - Boolean
     - Leave vehicle. Returns true if was in one.
   * - ``hasGravity()``
     - Boolean
     - True if gravity enabled.
   * - ``setGravity(Boolean gravity)``
     - (void)
     - Enable/disable gravity.
   * - ``canSee(Player other)``
     - Boolean
     - True if can see other player.
   * - ``sendMessage(String msg)``
     - (void)
     - Send a chat message.
   * - ``closeInventory()``
     - (void)
     - Close open inventory.
   * - ``getItem(Int slot)``
     - Item
     - Item in inventory slot.
   * - ``setItem(Int slot, Item item)``
     - (void)
     - Set item in slot.
   * - ``getItemInMainHand()``
     - Item
     - Item in main hand.
   * - ``setItemInMainHand(Item item)``
     - (void)
     - Set main hand item.
   * - ``getItemInOffHand()``
     - Item
     - Item in off hand.
   * - ``setItemInOffHand(Item item)``
     - (void)
     - Set off hand item.
   * - ``getHelmet()``
     - Item
     - Helmet slot item.
   * - ``setHelmet(Item item)``
     - (void)
     - Set helmet.
   * - ``getChestplate()``
     - Item
     - Chestplate slot item.
   * - ``setChestplate(Item item)``
     - (void)
     - Set chestplate.
   * - ``getLeggings()``
     - Item
     - Leggings slot item.
   * - ``setLeggings(Item item)``
     - (void)
     - Set leggings.
   * - ``getBoots()``
     - Item
     - Boots slot item.
   * - ``setBoots(Item item)``
     - (void)
     - Set boots.
   * - ``countItem(String id)``
     - Int
     - Count items of type in inventory.
   * - ``dropItem(Boolean dropAll)``
     - Boolean
     - Drop held item (or stack if dropAll).
   * - ``setResourcePack(String url, String hash)``
     - (void)
     - Request resource pack download.
   * - ``getTargetBlock(Int distance)``
     - Block
     - Block player is looking at (max 120).
   * - ``getTargetBlockFace(Int distance)``
     - String
     - Face of target block (NORTH, UP, etc.).
   * - ``getTargetEntity(Int distance)``
     - Entity
     - Entity player is looking at (max 120).
   * - ``getClickedBlockFace()``
     - String
     - Block face clicked (for interact scripts).
   * - ``getBedLocationWorld()``
     - String
     - World where bed is set.
   * - ``getPlayerWeather()``
     - String
     - Player's current weather type.
   * - ``resetPlayerTime()``
     - (void)
     - Sync player time with server.
   * - ``isPlayingMap()``
     - Boolean
     - True if playing a map.
   * - ``getMapTime()``
     - Long
     - Current map time.
   * - ``hasCompletedMap(String tag)``
     - Boolean
     - True if completed the map.
   * - ``isPlayingChallenge()``
     - Boolean
     - True if in a challenge.
   * - ``getCurrentChallenge()``
     - String
     - Current challenge tag (or null).
   * - ``getChallengeTime()``
     - Long
     - Current challenge time (-1 if not in challenge).
   * - ``hasCompletedChallenge(String tag)``
     - Boolean
     - True if completed the challenge.
   * - ``getChallengePoints()``
     - Int
     - Total challenge points.
   * - ``getCurrentCheckpoint()``
     - String
     - Current checkpoint (or null).
   * - ``getPoints()``
     - Int
     - FFA points.
   * - ``getAttempts()``
     - Int
     - Times hit a starting checkpoint.
   * - ``getSpeedrunScore()``
     - Int
     - Speedrun score.
   * - ``getHexaRecord()``
     - Int
     - Hexa stage reached.

Entity
^^^^^^

Represents a moveable object in Minecraft (mobs, arrows, item frames, etc.).

**Default value:** ``null``

**Constructors:**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Constructor
     - Description
   * - ``Entity(String uuid)``
     - Find entity by UUID. Returns null if not found.
   * - ``Entity(Int x, Int y, Int z, String world)``
     - Find entity at coordinates. Returns null if not found.

**Methods:**

.. list-table::
   :widths: 40 15 45
   :header-rows: 1

   * - Method
     - Return Type
     - Description
   * - ``getEntityType()``
     - String
     - Entity type (magic value, may change).
   * - ``getUniqueId()``
     - String
     - Entity UUID.
   * - ``getX()``
     - Double
     - X coordinate.
   * - ``getY()``
     - Double
     - Y coordinate.
   * - ``getZ()``
     - Double
     - Z coordinate.
   * - ``getYaw()``
     - Float
     - Rotation around Y axis.
   * - ``getPitch()``
     - Float
     - Rotation around X axis.
   * - ``getVelocityX()``
     - Double
     - X velocity.
   * - ``getVelocityY()``
     - Double
     - Y velocity.
   * - ``getVelocityZ()``
     - Double
     - Z velocity.
   * - ``getWorld()``
     - String
     - Current world name.
   * - ``getLocation()``
     - Location
     - Entity's location.
   * - ``teleport(Position pos)``
     - (void)
     - Teleport entity.
   * - ``isDead()``
     - Boolean
     - True if marked for removal.
   * - ``isOnGround()``
     - Boolean
     - True if on solid ground.
   * - ``getHealth()``
     - Double
     - Current health.
   * - ``setHealth(Double hp)``
     - (void)
     - Set health.
   * - ``getMaxHealth()``
     - Double
     - Maximum health.
   * - ``setMaxHealth(Double hp)``
     - (void)
     - Set maximum health.
   * - ``damage(Double amount)``
     - (void)
     - Deal damage.
   * - ``addPassenger(Entity passenger)``
     - Boolean
     - Add passenger. Returns false if failed.
   * - ``ejectPassenger(Entity passenger)``
     - (void)
     - Eject passenger.

Block
^^^^^

Represents a block in the Minecraft world.

**Default value:** ``null``

**Constructors:**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Constructor
     - Description
   * - ``Block(Int x, Int y, Int z, String world)``
     - Get block at coordinates.

**Methods:**

.. list-table::
   :widths: 45 15 40
   :header-rows: 1

   * - Method
     - Return Type
     - Description
   * - ``getBlockType()``
     - String
     - Block type (magic value, may change).
   * - ``getX()``
     - Int
     - X coordinate.
   * - ``getY()``
     - Int
     - Y coordinate.
   * - ``getZ()``
     - Int
     - Z coordinate.
   * - ``getWorld()``
     - String
     - World name.
   * - ``getLocation()``
     - BlockLocation
     - Block's location.
   * - ``getRelative(Int x, Int y, Int z)``
     - Block
     - Block at relative offset.
   * - ``getBlockPower()``
     - Int
     - Redstone power level.
   * - ``getLightLevel()``
     - Int
     - Total light level.
   * - ``getLightFromBlocks()``
     - Int
     - Light from nearby blocks.
   * - ``getLightFromSky()``
     - Int
     - Light from sky.
   * - ``isBlockPowered()``
     - Boolean
     - True if powered by redstone.
   * - ``isBlockIndirectlyPowered()``
     - Boolean
     - True if indirectly powered.
   * - ``isEmpty()``
     - Boolean
     - True if air.
   * - ``isLiquid()``
     - Boolean
     - True if liquid.

Item
^^^^

Represents an item stack.

**Default value:** ``null``

**Constructors:**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Constructor
     - Description
   * - ``Item(String item, Int amount)``
     - Create item by name with stack size. Throws MaterialNotFoundException if invalid.

**Methods:**

.. list-table::
   :widths: 40 15 45
   :header-rows: 1

   * - Method
     - Return Type
     - Description
   * - ``getItemType()``
     - String
     - Item type name.
   * - ``setItemType(String item)``
     - (void)
     - Set item type (resets extra data).
   * - ``getAmount()``
     - Int
     - Stack size.
   * - ``setAmount(Int amount)``
     - (void)
     - Set stack size.
   * - ``getMaxStackSize()``
     - Int
     - Maximum stack size (-1 if unknown).
   * - ``getDisplayName()``
     - String
     - Custom name (null if none).
   * - ``hasDisplayName()``
     - Boolean
     - True if has custom name.
   * - ``isSimilar(Item item)``
     - Boolean
     - True if same type (ignores amount).

Spatial Types
-------------

Location
^^^^^^^^

Represents a position in a world (Double precision).

**Constructors:**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Constructor
     - Description
   * - ``Location(Double x, Double y, Double z, String world)``
     - Create from coordinates and world.
   * - ``Location(Vector3 vec, String world)``
     - Create from vector and world.

**Methods:**

.. list-table::
   :widths: 35 20 45
   :header-rows: 1

   * - Method
     - Return Type
     - Description
   * - ``asBlockLocation()``
     - BlockLocation
     - Convert to block-aligned location.
   * - ``asVector2()``
     - Vector2
     - Convert to XZ vector.
   * - ``asVector3()``
     - Vector3
     - Convert to XYZ vector.
   * - ``getRegions()``
     - Region[]
     - Get all regions at this location.

Stringifies to ``"x y z world"``.

BlockLocation
^^^^^^^^^^^^^

Represents a block-aligned position (Int precision).

**Constructors:**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Constructor
     - Description
   * - ``BlockLocation(Int x, Int y, Int z, String world)``
     - Create from coordinates and world.
   * - ``BlockLocation(BlockVector3 vec, String world)``
     - Create from vector and world.

**Methods:**

.. list-table::
   :widths: 35 20 45
   :header-rows: 1

   * - Method
     - Return Type
     - Description
   * - ``set(String block)``
     - BlockLocation
     - Change block at location.
   * - ``asLocation()``
     - Location
     - Convert to Location.
   * - ``asVector2()``
     - Vector2
     - Convert to XZ vector.
   * - ``asVector3()``
     - Vector3
     - Convert to XYZ vector.
   * - ``getRegions()``
     - Region[]
     - Get all regions at this location.

Stringifies to ``"x y z world"``.

Position
^^^^^^^^

Like Location, but includes yaw and pitch.

**Constructors:**

.. list-table::
   :widths: 55 45
   :header-rows: 1

   * - Constructor
     - Description
   * - ``Position(Double x, Double y, Double z, Float yaw, Float pitch, String world)``
     - Create with all parameters.
   * - ``Position(Location loc, Float yaw, Float pitch)``
     - Create from Location with rotation.

**Methods:**

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - Method
     - Return Type
     - Description
   * - ``getYaw()``
     - Float
     - Get yaw rotation.
   * - ``getPitch()``
     - Float
     - Get pitch rotation.
   * - ``asLocation()``
     - Location
     - Convert to Location (loses rotation).

Vector3 / BlockVector3
^^^^^^^^^^^^^^^^^^^^^^

3D vectors for abstract positions.

**Constructors:**

.. list-table::
   :widths: 45 55
   :header-rows: 1

   * - Constructor
     - Description
   * - ``Vector3(Double x, Double y, Double z)``
     - Create continuous vector.
   * - ``BlockVector3(Int x, Int y, Int z)``
     - Create block-aligned vector.

**Methods:**

.. list-table::
   :widths: 40 15 45
   :header-rows: 1

   * - Method
     - Return Type
     - Description
   * - ``length()``
     - Double/Int
     - Vector magnitude.
   * - ``distance(Vector other)``
     - Double/Int
     - Distance to another vector (same type).
   * - ``containedWithin(Vector min, Vector max)``
     - Boolean
     - True if within bounding box (same type).

Stringifies to ``"x y z"``.

Vector2 / BlockVector2
^^^^^^^^^^^^^^^^^^^^^^

2D vectors for XZ plane positions.

**Constructors:**

.. list-table::
   :widths: 45 55
   :header-rows: 1

   * - Constructor
     - Description
   * - ``Vector2(Double x, Double z)``
     - Create continuous vector.
   * - ``BlockVector2(Int x, Int z)``
     - Create block-aligned vector.

**Methods:** Same as Vector3/BlockVector3.

Stringifies to ``"x z"``.

Region
^^^^^^

Wrapper for WorldGuard regions.

**Constructors:**

.. list-table::
   :widths: 55 45
   :header-rows: 1

   * - Constructor
     - Description
   * - ``Region(String id, String world)``
     - Look up existing WorldGuard region. Returns null if not found.
   * - ``Region(BlockVector3 min, BlockVector3 max, String world)``
     - Create transient cuboid region.
   * - ``Region(Int x1, Int y1, Int z1, Int x2, Int y2, Int z2, String world)``
     - Create transient cuboid region.
   * - ``Region(BlockVector2[] points, String world)``
     - Create transient polygonal region.

.. note::

   Transient regions created via script are not saved to WorldGuard and are not visible to ``/region info`` or the spider eye.

**Methods:**

.. list-table::
   :widths: 35 20 45
   :header-rows: 1

   * - Method
     - Return Type
     - Description
   * - ``containsPlayer(Player p)``
     - Boolean
     - True if player is inside region.
   * - ``getPlayersInside()``
     - Player[]
     - All players currently inside.
   * - ``getMinimumPoint()``
     - BlockLocation
     - Minimum corner.
   * - ``getMaximumPoint()``
     - BlockLocation
     - Maximum corner.
   * - ``getMemberPlayers()``
     - Player[]
     - Region members.
   * - ``getMemberGroups()``
     - String[]
     - Member group names.
   * - ``getOwningPlayers()``
     - Player[]
     - Region owners.
   * - ``getOwningGroups()``
     - String[]
     - Owner group names.
