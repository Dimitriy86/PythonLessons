import copy

# ------------------------------------------------------------------------------------------------

# class MyClass:
#     def __init__(self, value):
#         self.value = value
    
#     def __copy__(self):
#         print("Викликано __copy__")
#         return MyClass(self.value)
    
#     def __deepcopy__(self, memo=None):
#         print("Викликано __deepcopy__")
#         return MyClass(copy.deepcopy(self.value, memo))
    
# # Поверхневе копіювання
# obj = MyClass(5)
# obj_copy = copy.copy(obj)
# obj_copy.value = 10

# # Глибоке копіювання
# obj_deepcopy = copy.deepcopy(obj)
# obj_deepcopy.value = 20
# print(obj.value, obj_copy.value, obj_deepcopy.value)

# ------------------------------------------------------------------------------------------------

# class SimpleObject:
#     def __init__(self, greeting: str):
#         self.greeting = greeting
    
# class ComplexObject:
#     def __init__(self, value: int, nested_obj: SimpleObject):
#         self.value = value
#         self.nested_obj = nested_obj
    
#     def __copy__(self):
#         print("Викликано __copy__ для ComplexObject")
#         # Поверхеневе копіювання не копіює вкладені об'єкти глибоко
#         return ComplexObject(self.value, self.nested_obj)
    
#     def __deepcopy__(self, memo=None):
#         print("Викликано __deepcopy__ для ComplexObject")
#         return ComplexObject(
#             copy.deepcopy(self.value, memo),
#             copy.deepcopy(self.nested_obj, memo)
#         )

# nested_obj = SimpleObject("Hello")
# complex_obj = ComplexObject(5, nested_obj)

# # Створюємо копію та глибоку копію
# complex_obj_copy = copy.copy(complex_obj)
# complex_obj_deepcopy = copy.deepcopy(complex_obj)

# # Змінюємо значення вкладеного об'єкту nested_obj
# nested_obj.greeting = "Hello!!!"

# # Дивимось зміни у об'єктах
# print(f"Copy jbject: {complex_obj_copy.nested_obj.greeting}")
# print(f"Deepcopy object: {complex_obj_deepcopy.nested_obj.greeting}")

# ------------------------------------------------------------------------------------------------

class UserSettings:
    def __init__(self, preferences, large_data_reference):
        self.preferences = preferences
        self.large_data_reference = large_data_reference
    
    def __deepcopy__(self, memo):
        print("Кастомізоване глибокке копіювання для UsersSettings")
        # Припустимо, що preferences - це невеликий словник, який можна безпечно скопіювати,
        # а large_data_reference - це посилання на великий об'єкт даних, яке ми не хочемо дублювати
        new_preferences = copy.deepcopy(self.preferences, memo)
        # Передаємо посилання на ті ж великі дані замість їх копіювання
        new_obj = UserSettings(new_preferences, self.large_data_reference)
        return new_obj

# Створення укземпляра UserSettings
original_settings = UserSettings({"language": "uk"}, large_data_reference="LargeDataID")

# Глибоке копіювання з кастомізованою логікою
settings_copy = copy.deepcopy(original_settings)
