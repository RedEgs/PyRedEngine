# PyRedEngine

Check out the package on PyPi: https://pypi.org/project/pyredengine/ 				
Check out the roadmap on Trello: https://trello.com/b/310qwZMs
Check out the documentation: 

## Todo

### Important 
- [ ] Create first documentation page on "Read the docs"
- [ ] Move to trello board
- [ ] Configure repo
- [x] Make the engine independent of citrus cats
- [x] Publish to PYPI
- [ ] Upgrade to support for python 3.9+
### GUI
- [ ] Maybe add hardware accel if realistic
- [ ] Look at notes for researched optimisation techniques
- [ ] Use faster rendering techniques
- [ ] Make use of dirty loading etc
- [ ] Try decorators etc
- [ ] Do research upon JIT 
- [x] Add Text inputs
	- [x] Add a password input option to hide passwords
	- [ ] Text align
- [ ] Add Dropdowns 
- [ ] Add Windows 
	- [ ] Allow for passing data between windows etc
- [x] Add Subwindows
	- [ ] Fix resizing issues so they scale to the corner
	- [ ] figure out how to close them
- [ ] Add support for undrawing and drawing widgets 
- [ ] Fix subwindows
- [ ] Add support for tinkinter pop ups
- [ ] Fix triple input in scene events
- [ ] Add Status Bars
- [x] Add Sliders
- [x] Add Text Input
	- [ ] Tween unfocused text smoothly
- [x] Button hover size bounce animation
- [ ] Text outlines and strokes (semi, due to broken thickness controls) 
	- [ ] Refactor strokes to be internal to text
- [ ] Add support for CSS and HTML #SCRAPPED
## Backend
- [ ] Basic networking
- [ ] Always figure out ways to optimise
- [ ] Make game loops less repetive ( Make use of globals & class methods) #WIP
- [x] Create app options, see [[App Options]]
- [ ] Add vertical parameters for `calculate_index_spacing()` 
	- [ ] Fix vertical parameters, past 5 elements.
- [x] Refactor scene classes to pass in extra data if needed, make it optional
	- [ ] Document it cuz its kinda complicated to figure out
- [x] Refactor utils to make misc features 
- [x] Make dedicated gui element and sprite group 
- [x] Refactor all scenes with buttons and tweens to work properly
- [x] Add more parameters for tweens like, `self.start(reverse_on_finshed=bool)` #WIP  
- [x] Add a `wait(secs)` to utils for delaying in pygame 
- [x] Refactor tweening on EVERYTHING (Use dataclasses) 
	- [x] Improve interaction between buttons and tweens #COULD-BE-IMPROVED 
	- [x] Try to get tweens to stop checking once they are finished 
	- [x] Make a tween manager to render all tweens in a group.
	- [x] Try to make tweens easier to use. #COULD-BE-IMPROVED
- [x] ↑ Refactor buttons (specifically add group rendering, improve tweening) #WIP 
	- [x] Fix buttons holding down when pressed but not hovered. #NEEDS-TESTING 
	- [x] Fix surface buttons collision
	- [x] Fix buttons not tweening back when they reach max progress
	- [x] Make a variant to buttons which allows for surfaces to be passed #SEMI-FINISHED 
	- [ ] Try to remove the input delay
