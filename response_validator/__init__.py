"""
response-validator - Validate and verify LLM responses

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import ResponseValidator, validate, process, main

__all__ = ["ResponseValidator", "validate", "process", "main"]
