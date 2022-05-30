# Nuke GUI Toggler
*About
Python tool using the Nuke library. This tool disables nodes while working within the nuke GUI. Come render time the nodes are turned back to produce the desired image. This is to help speed up workflow from memory intensive nodes.*

## GETTING STARTED
The first thing to do is to locate your .nuke folder. *(It is hidden by default.)*

- **Windows:** C:\ Users\< username >\.nuke
 
- **Mac:** /Users/< username >/.nuke

Look for a menu.py file.

### Installation

1. Paste the below code into the **menu.py** file located in your .nuke directory

```
# Import Custom Modules
from gui_toggler import *

m = nuke.menu("Nuke")
m.addCommand("Python Tools/GUI Toggler", "node = Toggler()")
```

2. Paste the below code into the **init.py** file located in your .nuke directory

```
# Make sure you use the correct version
nuke.pluginAddPath('./gui_toggler')
```

3. Place the gui_toggler folder into your .nuke directory
4. Restart Nuke.

## HOW TO USE
1. Create node from the custom drop down pannel 'Python Tools'
2. Link Nodes by;
    i. Selecting nodes and click 'Link Selected' in properties pannel
    ii. Input the node group you want to link and click 'Link Classes' in properties pannel
3. Repeat same process to remove links and using the alternate button.
4. Disable GUI by disabling the Toggler_GUI Node



## Requirements
- The Foundry - Nuke Licence


## Contact
#### Damien England
#### damien.england@icloud.com
#### [Website](http://www.damienengland.com.au) 
