"""
What to do if the module is called like this: python -m corpert
"""

from .cli import _parse_cmd_line
from .corpert import Corpert

kwargs = _parse_cmd_line()
corpert = Corpert(**kwargs)
corpert.run()
