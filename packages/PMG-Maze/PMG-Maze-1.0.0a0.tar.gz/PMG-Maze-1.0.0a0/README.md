# English Version
To read the English version, use [Google translate](https://translate.google.com/), just paste the link to this site into the field for translation from Russian to English and follow the link that Google gives you.
# PMG-Maze Документация

## Вступление

Библиотека PMG-Maze предназначена для генерации, сохранения, загрузки и визуализации лабиринтов. Она обеспечивает инструменты для создания и манипуляции лабиринтами в Python. Можно регулировать размеры лабиринта и визуализировать его в режиме отладки.

## API Библиотеки

### Методы Генератора Лабиринтов

#### `generate(width: int, height: int, debug: bool = False) -> List[List[str]]`

Генерирует лабиринт размером 'width' x 'height'.

##### Аргументы:

- **width (int):** Ширина лабиринта.
- **height (int):** Высота лабиринта.
- **debug (bool, optional):** Если установлено значение True, информация для отладки будет напечатана.
##### Возвращает:

2D список представляющий лабиринт.

##### Пример:

```python
import pmg_maze as pmg

maze = pmg.generate_maze(10, 10)  # Генерация лабиринта размером 10x10.
```
#### `print(maze: List[List[str]]) -> None`

Выводит лабиринт 'maze' в консоль.

##### Аргументы:

- **maze (List[List[str]]):** 2D список представляющий лабиринт.

##### Пример:

```python
pmg.print(maze)  # Выводит лабиринт в консоль.
```

#### `maze2x_y(maze: List[List[str]], debug: bool = False) -> Tuple[np.ndarray, np.ndarray]`

Преобразует лабиринт в два массива координат: один для x-координат, другой для y-координат.

##### Аргументы:

- **maze (List[List[str]]):** 2D список представляющий лабиринт.
- **debug (bool, optional):** Если установлено значение True, информация для отладки будет напечатана.
##### Возвращает:

Два массива NumPy x и y, содержащие координаты стен лабиринта.

#### `maze2matrix(maze: List[List[str]], debug: bool = False) -> np.ndarray`

Преобразует лабиринт в матрицу, где 1 обозначает стену, а 0 - свободное пространство.

##### Аргументы:

- **maze (List[List[str]]):** 2D список представляющий лабиринт.
- **debug (bool, optional):** Если установлено значение True, информация для отладки будет напечатана.
##### Возвращает:

NumPy-массив, представляющий лабиринт.

```python
matrix = pmg.maze2matrix(maze)  # Конвертирует лабиринт в матрицу NumPy.
print(matrix)  # Выводит матрицу в консоль.
```

### Операции с файлами

#### `save_maze(maze: List[List[str]], filename: str) -> None`

Сохраняет лабиринт в файл с именем 'filename'. Изображение сохраняется в формате numpy.

##### Аргументы:

- **maze (List[List[str]]):** 2D список представляющий лабиринт.
- **filename (str):** Путь и имя файла для сохранения лабиринта.

##### Пример:

```python
pmg.save_maze(maze, 'my_maze.npy')  # Сохраняет лабиринт в файл 'my_maze.npy'.
```
#### `load_maze(filename: str, debug: bool = False) -> List[List[str]]`

Загружает лабиринт из файла с именем 'filename'. Файл должен быть в формате numpy.

##### Аргументы:

- **filename (str):** Путь и имя файла для загрузки лабиринта.
- **debug (bool, optional):** Если установлено значение True, информация для отладки будет напечатана.
##### Возвращает:

2D список представляющий лабиринт.

##### Пример:

```python
maze = pmg.load_maze('my_maze.npy')  # Загружает лабиринт из файла 'my_maze.npy'.
```

#### `save_maze(maze: List[List[Cell]], filename: str, debug: bool = False) -> None`

Сохраняет лабиринт в файл с именем 'filename'. Файл будет в формате numpy.

##### Аргументы:

- **maze (List[List[Cell]]):** 2D список представляющий лабиринт.
- **filename (str):** Путь и имя файла для сохранения лабиринта.
- **debug (bool, optional):** Если установлено значение True, информация для отладки будет напечатана.
##### Пример:

```python
pmg.save_maze(maze, 'my_maze.npy')  # Сохраняет лабиринт в файл 'my_maze.npy'.
```

# Copyright
Used MIT License
Copyright © Arigadam, 2024
