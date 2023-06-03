"""HTML dialog to provide an alternative modal."""

from pynecone.components.libs.chakra import ChakraComponent
from pynecone.vars import Var


class Dialog(ChakraComponent):
    """A dialog component."""

    tag = "dialog"

    open: Var[bool]
