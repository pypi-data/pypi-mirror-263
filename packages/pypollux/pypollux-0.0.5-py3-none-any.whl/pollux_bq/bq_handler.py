
import json
from typing import List, Dict, Any
from pathlib import Path

class Unicode2StringConverter:
    @staticmethod
    def convert(input_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Converts Unicode escape sequences in a list of dictionaries to normal strings."""
        def decode_string(s: str) -> str:
            return s.encode('utf-16', 'surrogatepass').decode('utf-16')
        
        def decode_values(d: Dict[str, Any]) -> Dict[str, Any]:
            for key, value in d.items():
                if isinstance(value, str):
                    d[key] = decode_string(value)
                elif isinstance(value, dict):
                    d[key] = decode_values(value)
                elif isinstance(value, list):
                    d[key] = [decode_values(item) if isinstance(item, dict) else item for item in value]
            return d
        
        return [decode_values(item) for item in input_data]
    
    def toJson(self, input_data: List[Dict[str, Any]]) -> str:
        """Converts the input data to a JSON string."""
        converted_data = self.convert(input_data)
        return json.dumps(converted_data, ensure_ascii=False, indent=2)
    
    def toJsonFile(self, input_data: List[Dict[str, Any]], path: Path) -> None:
        """Saves the converted JSON to a file."""
        json_str = self.toJson(input_data)
        with path.open('w', encoding='utf-8') as file:
            file.write(json_str)
