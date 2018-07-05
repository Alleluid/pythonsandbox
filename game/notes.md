# RPG Game Design Document

## Resources:
Some info from here: http://www.darkshire.net/jhkim/rpg/systemdesign/dice-methods.html


### Base dice rolls? 
_bell-curve(3d6) vs linear(1d20)_  
linear is going to have totally even distribution;
bell curve has more focused on the high end and low end.

Die|1|2|3|4|5|6|7|8|9|10|...
:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:
**1d20**|5%|10%|15%|20%|25%|30%|35%|40%|45%|50%|...
**3d6**|-|-|0.5%|1.9%|4.6%|9.3%|16.2%|25.9%|37.5%|50%|...



### Roll-and-add:
roll the dice, add it to the stat, and see if the roll is over the difficulty

I'd like to have a system that allows you to use resources to make certain rolls better, like in Fate.  
avoids a trivial roll having the same exact chances as a vital one, as realistically you would try harder if it was life threatening.