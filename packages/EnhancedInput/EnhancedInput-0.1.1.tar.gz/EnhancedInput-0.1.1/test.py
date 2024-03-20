from src.enhancedinput import EnhancedInput, Themes, Validators

inp = EnhancedInput(theme=Themes.fancy)

name = inp.get("What is your name?", validators=[Validators.LengthValidator(1, 20)])

print(f"Hello, {name}!")

age = inp.get("What is your age?", input_type=int, validators=[Validators.IntValidator(), Validators.RangeValidator(0, 140)])
