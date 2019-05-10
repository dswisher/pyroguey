# Design Notes #

## UI/Simulation Separation ##

I wish to keep the UI and the simulation separate.
An entity component system approach seems like a good idea for the simulation, but it is less clear that it is a good fit for the UI.
At the very least, I would like to have the option of switching out the underlying UI framework without having to change any simulation code.

* The Map - a display-technology agnostic representation of the game world. For example, rather than representing the character as `@`, it would use a constant like `SPRITE_PLAYER`.

The following are scenarios that need to be handled, written as user stories.

* As a player, when I click a movement key, the character should move in that direction.
  * The UI accepts the input key (left arrow, say) and translates it to a `MOVE_LEFT` command and sends it to the simulation.
  * The simulation processes the `MOVE_LEFT` command, which may or may not actually move the character (depending on walls), and updates the state of the map.
  * The render loop draws the updated view by querying the map.
* As a player, when I click the inventory key, the inventory opens up.
  * TODO
* As a player, I can examine the contents of a treasure chest.
  * TODO
* As a player, I can equip/unequip items
  * TODO
* As a player, I can cast a ranged spell that requires choosing a specific target.
  * The UI accepts the "cast" key and requests that the UI open spell chooser.
  * The UI allows the user to select a spell to cast, or cancel the operation.
  * The chosen spell is sent to the simulation as a `CAST` command with appropriate parameters.
  * The simulation sets up to cast the spell, and requests a target from the UI.
  * The UI brings up the "choose target" interface and allows the player to select a target on the map, or cancel.
  * The UI sends a `TARGET` command to the simulation to complete casting of the spell.
  * The simulation completes casting of the spell, updates the state of the map and player inventory.
  * The UI draws the updated views by querying the map and/or inventory.
* As a player, I should be able to see a mini-map of the larger area
  * TODO
* As a developer, I can examine the internal state of the simulation.
  * TODO
* As a developer, I can alter the state of the game (reset the level, jump to a location, jump to a new level, etc)
  * TODO


