from urllib.parse import urlparse
import re

class Validator:
    def valid(self, value: str):
        raise NotImplementedError("You must implement valid() in your validator class")


class Validators:
    class BlankValidator(Validator):
        def valid(self, value: str):
            return True
        
    """
    A validator for boolean values. Accepts the following values (case-insensitive):
    true, false, 1, 0, yes, no, y, n, t, f
    """
    class BooleanValidator(Validator):
        hint = "y/n"

        def valid(self, value: str):
            return value.lower() in ["true", "false", "1", "0", "yes", "no", "y", "n", "t", "f"]

    """
    A validator for integer values. Accepts any integer value.
    """
    class IntValidator(Validator):
        hint = "integer"

        def valid(self, value: str):
            try:
                int(value)
                return True
            except ValueError:
                return False

    """
    A validator for float values. Accepts any float value.
    """
    class FloatValidator(Validator):
        hint = "float"

        def valid(self, value: str):
            try:
                float(value)
                return True
            except ValueError:
                return False

    """
    A validator for email addresses. Accepts any valid email address.
    """
    class EmailValidator(Validator):
        hint = "email"
        regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        p = re.compile(regex)

        def valid(self, value: str):
            return self.p.match(value) is not None

    """
    A validator for URLs. Accepts any valid URL.
    """
    class URLValidator(Validator):
        hint = "url"

        def valid(self, value: str):
            parsed = urlparse(value)
            return parsed.scheme != "" and parsed.netloc != ""
        
    """
    A validator for ranges. Accepts any value within a given range.
    """
    class RangeValidator(Validator):
        def __init__(self, min: float | int, max: float | int, mode: int | float = int) -> None:
            self.mode = mode
            self.min = self.mode(min)
            self.max = self.mode(max)

            self.hint = f"{self.min} - {self.max}"

        def valid(self, value: str):
            try:
                return self.min <= self.mode(value) <= self.max
            except ValueError:
                return False
    
    """
    A validator for lengths. Accepts any value with a length within a given range.
    """
    class LengthValidator(Validator):
        def __init__(self, min: int, max: int | None = None) -> None:
            self.min = min
            self.max = max

            self.hint = f"{self.min} - {self.max}" if self.max is not None else f"{self.min}+"

        def valid(self, value: str):
            return self.min <= len(value) <= (self.max if self.max is not None else len(value))
