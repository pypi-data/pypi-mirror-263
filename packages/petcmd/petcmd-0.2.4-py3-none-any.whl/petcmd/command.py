import logging
import re
from typing import Callable

from .utils import get_signature

type string_collection = list[str] | tuple[str] | set[str]

class Command:

	def __init__(self, cmd: str | string_collection, func: Callable):
		self.cmd = cmd
		self.func = func
		self.__logger = logging.getLogger("petcmd.command")
		self.aliases = self.__generate_aliases()

	def match(self, cmd: str | string_collection):
		if isinstance(cmd, str):
			if isinstance(self.cmd, str):
				return cmd == self.cmd
			return cmd in self.cmd
		if isinstance(self.cmd, str):
			return self.cmd in cmd
		return any(c in cmd for c in self.cmd)

	def __generate_aliases(self) -> dict[str, str]:
		"""Returns {alias: argument}"""
		positionals, keyword, *_ = get_signature(self.func)
		aliases = {}
		for arg in [*positionals, *keyword]:
			aliases[arg] = arg
			aliases[arg.replace('_', '-')] = arg
			first_letter = re.search(r"[a-zA-Z]", arg).group(0)
			if first_letter.lower() not in aliases:
				aliases[first_letter.lower()] = arg
			elif first_letter.upper() not in aliases:
				aliases[first_letter.upper()] = arg
		self.__logger.debug(f"generated aliases for {self.cmd}: {", ".join(aliases.keys())}")
		return aliases
