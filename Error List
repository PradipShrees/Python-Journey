# This shows all built-in exceptions in Python. You can raise any of these exceptions in your code to indicate that an error has occurred. You can also create your own custom exceptions by subclassing the Exception class.
""" 
ArithmeticError
BufferError
LookupError

AssertionError
AttributeError
BlockingIOError
BrokenPipeError
ChildProcessError
ConnectionAbortedError
ConnectionError
ConnectionRefusedError
ConnectionResetError
DeprecationWarning
EOFError
EnvironmentError
Exception
FileExistsError
FileNotFoundError
FloatingPointError
FutureWarning
GeneratorExit
ImportError
ImportWarning
IndentationError
IndexError
InterruptedError
IsADirectoryError
KeyError
KeyboardInterrupt
MemoryError
ModuleNotFoundError
NameError
NotADirectoryError
NotImplementedError
OSError
OverflowError
PendingDeprecationWarning
PermissionError
ProcessLookupError
RecursionError
ReferenceError
ResourceWarning
RuntimeError
RuntimeWarning
StopAsyncIteration
StopIteration
SyntaxError
SyntaxWarning
SystemError
SystemExit
TabError
TimeoutError
TypeError
UnboundLocalError
UnicodeDecodeError
UnicodeEncodeError
UnicodeError
UnicodeTranslateError
UnicodeWarning
UserWarning
ValueError
Warning
ZeroDivisionError
"""

# Ways to "implement" (work with) exceptions in Python

# 1) Raise a built-in exception
raise ValueError("Invalid value")

# 2) Raise your own custom exception
class AgeTooLowError(Exception):
    pass

raise AgeTooLowError("Age must be >= 18")

# 3) Raise based on a condition (manual validation)
x = -5
if x < 0:
    raise ValueError("x cannot be negative")

# 4) assert (raises AssertionError if condition is False)
n = 10
assert n > 0, "n must be positive"

# 5) try / except (catch an exception)
try:
    num = int("abc")
except ValueError:
    print("That was not a number")

# 6) try / except as e (capture exception object)
try:
    1 / 0
except ZeroDivisionError as e:
    print("Error:", e)

# 7) Catch multiple exceptions (tuple)
try:
    d = {}
    print(d["x"])
except (KeyError, TypeError):
    print("Key missing or wrong type")

# 8) Multiple except blocks (best practice: specific first)
try:
    x = int("abc")
except ValueError:
    print("ValueError")
except Exception:
    print("Something else happened")

# 9) else (runs only if NO exception happened in try)
try:
    x = int("123")
except ValueError:
    print("bad")
else:
    print("parsed OK:", x)

# 10) finally (runs ALWAYS, error or no error)
f = None
try:
    f = open("data.txt", "r")
    data = f.read()
except FileNotFoundError:
    print("file not found")
finally:
    if f:
        f.close()

# 11) Re-raise the same exception (bubble it up)
try:
    int("abc")
except ValueError:
    print("Logging it, then re-raising...")
    raise

# 12) Raise a different exception while keeping the original cause (exception chaining)
try:
    int("abc")
except ValueError as e:
    raise RuntimeError("Failed to parse number") from e

# 13) Suppress the cause (hide chaining) with 'from None'
try:
    int("abc")
except ValueError:
    raise RuntimeError("Failed to parse number") from None

# 14) with (context manager) automatically handles cleanup, even if exception happens
try:
    with open("data.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("file not found")

# 15) Define your own exception hierarchy (clean for big projects)
class AppError(Exception):
    """Base error for the app."""

class ConfigError(AppError):
    pass

raise ConfigError("Missing config")

# 16) Use built-in helpers that raise exceptions (common pattern)
# dict.get doesn't raise, but indexing does:
d = {}
# d["missing"]  # KeyError

# 17) Handle exceptions in loops (skip bad items, continue)
items = ["10", "x", "30"]
nums = []
for item in items:
    try:
        nums.append(int(item))
    except ValueError:
        continue  # skip bad item