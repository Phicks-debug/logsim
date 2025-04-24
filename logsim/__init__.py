from .logger import CustomLogger, CustomFormatter

# Create a default instance for quick access
get_logger = CustomLogger

__all__ = ["CustomLogger", "CustomFormatter", "get_logger"]
