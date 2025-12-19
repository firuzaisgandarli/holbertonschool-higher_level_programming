#!/usr/bin/python3
import pickle


class CustomObject:
    def __init__(self, name="", age=0, is_student=False):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print object attributes in required format"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize current instance to a file"""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize object from a file"""
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except Exception:
            return None
