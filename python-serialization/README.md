# Python Serialization

## Task 0: Basic Serialization

Bu modul Python dictionary-ni JSON faylına serialize etmək və JSON faylından deserialize edərək dictionary-ni bərpa etmək üçün yazılıb.

### Fayllar
- `task_00_basic_serialization.py`

### Funksiyalar
#### `serialize_and_save_to_file(data, filename)`
- **Parametrlər:**
  - `data`: Python dictionary
  - `filename`: JSON faylının adı
- **İş prinsipi:** Dictionary-ni JSON formatına çevirir və fayla yazır. Əgər fayl mövcuddursa, üzərinə yazılır.

#### `load_and_deserialize(filename)`
- **Parametrlər:**
  - `filename`: JSON faylının adı
- **İş prinsipi:** JSON faylını oxuyur və Python dictionary kimi qaytarır.

### İstifadə nümunəsi
```python
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

serialize_and_save_to_file(data_to_serialize, 'data.json')
print("Data serialized and saved to 'data.json'.")

deserialized_data = load_and_deserialize('data.json')
print("Deserialized Data:")
print(deserialized_data)
