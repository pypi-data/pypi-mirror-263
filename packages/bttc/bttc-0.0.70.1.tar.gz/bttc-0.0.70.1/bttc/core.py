"""Module to put core class or settings."""
from functools import partial, update_wrapper
from mobly.controllers import android_device
from typing import Any, TypeAlias


ANDROID_DEVICE: TypeAlias = android_device.AndroidDevice


class UtilBase:
  """Utility base class."""

  NAME: str = 'Unknown'
  DESCRIPTION: str = '?'

  def __init__(self, ad: ANDROID_DEVICE):
    """Initializes the GModule utility class.

    Args:
        ad:  The Android device object to control.
    """
    self._ad: ANDROID_DEVICE = ad

  def _bind(self, target_func: Any, method_name: str | None = None):
    if not method_name:
      method_name = target_func.__name__

    setattr(self, method_name, partial(target_func, self._ad))
    update_wrapper(getattr(self, method_name), target_func)
