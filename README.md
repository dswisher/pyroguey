# Pyroguey - a roguelike experiment in Python #

## Setup ##

Need sdl2 installed:

    brew install sdl2

Using python3:

    python -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install tcod


## TODO ##

* Use key-map defined [here](http://www.roguebasin.com/index.php?title=Preferred_Key_Controls) (RogueBasin)
* Add 1-cell border left and right of map to prep for keyboard targetting
* Allow targeting via keyboard
* Add scrolls that do AOE
* Add rings (new equipment slot)
* Add more weapons
* Add more mobs
* Show equipped items on character screen
* Add ability to go back up stairs
* Add gold
* Add shops (surface level) to buy/sell items
* Loot corpses for gold
* Collapse inventory - one line for all healing potions, with a count
* Limit inventory by weight - can carry lots of healing pots, only a few swords
* Fix libtcod deprecation warnings

## Links ##

* bearlibterminal - [home](http://foo.wyrd.name/en:bearlibterminal) - [api ref](http://foo.wyrd.name/en:bearlibterminal:reference)
* esper - [github](https://github.com/benmoran56/esper)
* libtcod - [github](https://github.com/libtcod/python-tcod) - [docs](https://python-tcod.readthedocs.io/en/latest/)
* Roguelikedev [tutorial revised](https://www.reddit.com/r/roguelikedev/wiki/python_tutorial_series)
  * [part 1](http://rogueliketutorials.com/libtcod/1) - Drawing the '@' symbol and moving it around
  * [part 2](http://rogueliketutorials.com/libtcod/2) - The generic Entity, the render functions, and the map
  * [part 3](http://rogueliketutorials.com/libtcod/3) - Generating a dungeon
  * [part 4](http://rogueliketutorials.com/libtcod/4) - Field of View
  * [part 5](http://rogueliketutorials.com/libtcod/5) - Placing Enemies and kicking them (harmlessly)
  * [part 6](http://rogueliketutorials.com/libtcod/6) - Doing (and taking) some damage
  * [part 7](http://rogueliketutorials.com/libtcod/7) - Creating the Interface
  * [part 8](http://rogueliketutorials.com/libtcod/8) - Items and Inventory
  * [part 9](http://rogueliketutorials.com/libtcod/9) - Ranged Scrolls and Targeting
  * [part 10](http://rogueliketutorials.com/libtcod/10) - Saving and Loading
  * [part 11](http://rogueliketutorials.com/libtcod/11) - Multiple floors
  * [part 12](http://rogueliketutorials.com/libtcod/12) - Tuning the difficulty
  * [part 13](http://rogueliketutorials.com/libtcod/13) - Equipment
  * repos: [official](https://github.com/TStand90/roguelike_tutorial_revised/tree/part1)
    * [toptea](https://github.com/toptea/roguelike_tutorial/tree/part1) - esper
    * [kuraha4](https://github.com/kuraha4/roguelike-tutorial-python) - bearlibterminal
    * [kelte](https://github.com/brianbruggeman/kelte)

