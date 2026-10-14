"""
VIDYA-X AI — Content Processors Package
Provides modular extraction processors for PDF and PPT/PPTX files.
"""

from .pdf_processor import process_pdf
from .ppt_processor import process_ppt

__all__ = ["process_pdf", "process_ppt"]
