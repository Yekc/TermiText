# TermiText

Color and format text you print in the terminal, or create text animations!  
Here are examples on how to use TermiText:
```python
from termitext import *

#--------------------TEXT MODIFICATION
#Print green text with orange highlight
print(color("Hello world!", color = "green", highlight = "orange"))

#Print on the same line
slprint("This text is all ")
slprint(" on the same line!")

#Print bold text
print(format("Hello world!", style = "bold"))

#Clear the terminal
clear()

#Print one character at a time with 1 second between each character
slowprint("Hello", 1)

#--------------------TEXT ANIMATIONS
#Create an animation with 0.5 seconds between each frame
animation.create("myAnimation", 0.5)

#Add frames to the animation
animation.frame("myAnimation", "frame1")
animation.frame("myAnimation", "frame2")

#Play the animation
animation.play("myAnimation")
```  
**LIST OF COLORS:**  
- Text: lightred, red, orange, yellow, lightgreen, green, lightcyan, cyan, lightblue, blue, pink, purple, black, darkgrey,    lightgrey  
- Highlight: red, orange, green, cyan, blue, purple, black, lightgrey  

**LIST OF FORMATS:**  
- Styles: bold, underline, strikethrough, invisible, reverse, disable  

*PyPi README.md file is in TermiText folder, this one is just for Github*
