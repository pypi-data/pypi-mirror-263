## Install

- via pip: pip install PyGymFormat
- from source: git clone PATH \n pip install .

## Use

PyGymFormater creates widgets for everything which are latter combined to a 
game class. Those widgets are sorted into submodules named after their 
properties, like invisible and visible. When creating new entities like the 
player, another submodule with multiple base  class options, you create a
class that inherits from the correct abstract base class.