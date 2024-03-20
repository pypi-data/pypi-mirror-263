from .themes import Themes, Theme
from .colors import Colors
from .validator import Validator
import sys

class EnhancedInput:
    def __init__(self, theme: Theme = Themes.default) -> None:
        self.theme: Theme = theme
        self.invalid_input_message: str = Colors.RED + "Invalid input" + Colors.END

    """Get input from the user"""
    def get(self, prompt: str = "", input_type: str | int | float = str, theme: Theme = None, validators: list[Validator] = [], showHint: bool = True) -> str:
        if theme is None:
            theme = self.theme
            
        hints = []
        if showHint:
            for validator in validators:
                try:
                    hints.append(validator.hint)
                except AttributeError:
                    pass

        while True:
            try:
                res = input_type(input(theme.format(prompt, hints)))
            except ValueError:
                print(self.invalid_input_message)
                continue

            if self.validate(res, validators):
                break
            else:
                print(self.invalid_input_message)
    
        sys.stdout.write(Colors.END)
        sys.stdout.flush()

        return res
    
    """Validate any string value"""
    def validate(self, value: str, validators: list[Validator]) -> bool:
        for validator in validators:
            if not validator.valid(value):
                return False
        return True
