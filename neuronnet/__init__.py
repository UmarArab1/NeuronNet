import os
import importlib

# Получаем список всех файлов в папке библиотеки
modules = [f[:-3] for f in os.listdir(os.path.dirname(__file__)) if f.endswith(".py") and f != "__init__.py"]

# Динамически импортируем их
for module in modules:
    imported_module = importlib.import_module(f".{module}", package=__name__)
    globals().update({name: getattr(imported_module, name) for name in dir(imported_module) if not name.startswith("_")})
