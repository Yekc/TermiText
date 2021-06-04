# TermiText

[Github page](https://github.com/Yekc/TermiText)

Color and format text you print in the terminal!
Here is an example on how to use TermiText:
```python
from termitext import *

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
```  
**LIST OF COLORS:**  
- Text: lightred, red, orange, yellow, lightgreen, green, lightcyan, cyan, lightblue, blue, pink, purple, black, darkgrey,    lightgrey  
- Highlight: red, orange, green, cyan, blue, purple, black, lightgrey  

**LIST OF FORMATS:**  
- Styles: bold, underline, strikethrough, invisible, reverse, disable  

