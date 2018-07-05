# RPG Game Design Document

### Resources:
Some info from here: http://www.darkshire.net/jhkim/rpg/systemdesign/dice-methods.html


## Dice Rolls 
_bell-curve(`3d6`) vs linear(`1d20`)_  
linear is going to have totally even distribution;
bell curve has more focused on the high end and low end.

from Darkshire:  

Die|1|2|3|4|5|6|7|8|9|10|...
:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:
**1d20**|5%|10%|15%|20%|25%|30%|35%|40%|45%|50%|...
**3d6**|-|-|0.5%|1.9%|4.6%|9.3%|16.2%|25.9%|37.5%|50%|...

#### Rolling Mechanics 
Roll-and-add: roll the dice, add it to the stat, and see if the roll is over the difficulty.

I'd like to have a system that allows you to use resources to make certain rolls better, like in Fate.  
avoids a trivial roll having the same exact chances as a vital one, as realistically you would try harder if it was life threatening.

I like the PbtA system of `2d6`, `7`+ is success. But I'd want to modify it a bit to be able to accomplish the above.

Another possibility is step-dice, where the actual die being rolled is modified. 
> If high rolls are good, then in a step-die system experts have much more random results than beginners do 
(i.e. larger variance). If low rolls are good, then experts have less random results than beginners -- 
which is usually considered more sensible.   

I like the idea of the latter, complete beginners roll `d20`, up to an expert rolling `d4`-`d6` for the same task.
This would probably mean that the actual player stats would just be the die they use to roll it. ex: `pow 12`, `brn 6` 
for a character that is smart and a little strong. Lower = better feels wrong though.  
Could this work with another system? Maybe a difficulty system? If low is better, we could set the difficulty as a number 
where higher = harder.

## Character Attributes
I was first going to go with the classic `str`, `int`, `chr`, and `wis`. But `str` and `int` are reserved words in Python,
and it could be fun to mix it up. Right now I'm thinking Power (`pow`), Brain (`brn`), Social (`soc`), and Agility (`agi`)