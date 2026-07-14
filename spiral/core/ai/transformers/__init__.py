"""
The project's transformer implementations: positioned steps in the agent loop
that reshape what the run carries, without ever denying a call.

The truncate transformer is re-exported here, so it can be reached from the short
package path ```spiral.core.ai.transformers``` as well as its own module.
"""

from spiral.core.ai.transformers.truncate import SpiralAiTruncateTransformer

__all__ = [
    'SpiralAiTruncateTransformer',
]
