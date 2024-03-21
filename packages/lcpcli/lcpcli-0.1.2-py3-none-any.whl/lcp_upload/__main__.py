from .cli import _parse_cmd_line
from .lcp_upload import lcp_upload

kwargs = _parse_cmd_line()

lcp_upload(**kwargs)
