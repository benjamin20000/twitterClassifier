import json
import numpy as np

class JsonWriter:
    @staticmethod
    def write2json(dic,path):
        try:
            dic = JsonWriter.convert_to_native(dic)
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(dic, f, ensure_ascii=False, indent=4)
        except Exception as e:
            raise RuntimeError("error when trying to write to json") from e

    """this function converting a numpy object
     to native python obj suitable to json"""
    @staticmethod
    def convert_to_native(obj):
        if isinstance(obj, dict):
            return {JsonWriter.convert_to_native(k): JsonWriter.convert_to_native(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [JsonWriter.convert_to_native(i) for i in obj]
        elif isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.bool_):
            return bool(obj)
        else:
            return obj


