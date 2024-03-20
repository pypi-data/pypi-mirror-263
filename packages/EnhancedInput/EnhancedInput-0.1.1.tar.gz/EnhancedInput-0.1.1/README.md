*work in progress*

# EnhancedInput
### The easiest way to deal with input in Python
It's as easy as this!
```python
from enhancedinput import EnhancedInput

# Create an EnhancedInput object
inp = EnhancedInput(theme=Themes.fancy)

# Get input from the user, with a length validator 1-20 characters
name = inp.get("What is your name?", validators=[Validators.LengthValidator(1, 20)])

# Get input from the user, with a range validator 0-120,
# which will automatically be valited to an int and returned as an int
age = inp.get("What is your age?", input_type=int,
              validators=[Validators.RangeValidator(0, 120)])
```