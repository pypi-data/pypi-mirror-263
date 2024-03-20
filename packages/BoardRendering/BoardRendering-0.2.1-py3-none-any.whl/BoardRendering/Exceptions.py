class Exceptions:
    """All Exceptions"""
    class InvalidPosition(Exception):
        """Caused by a position value being invalid"""
        pass
    class InvalidBoard(Exception):
        """Caused by Board being Invalid"""
        pass