"""
The project's guard implementations: positioned steps in the agent loop
that observe, govern, mask, or shorten what the run carries.

The truncate guard is re-exported here, so it can be reached from the short
package path ```spiral.core.ai.guards``` as well as its own module.
"""

from spiral.core.ai.guards.truncate import SpiralAiTruncateGuard

__all__ = [
    'SpiralAiTruncateGuard',
]
