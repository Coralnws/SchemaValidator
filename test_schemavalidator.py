# test_schemavalidator.py
"""
Tests for SchemaValidator module.
"""

import unittest
from schemavalidator import SchemaValidator

class TestSchemaValidator(unittest.TestCase):
    """Test cases for SchemaValidator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SchemaValidator()
        self.assertIsInstance(instance, SchemaValidator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SchemaValidator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
