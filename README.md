

# NeuronNet

Лёгкая библиотека для коллективного обучения нейросетей

## Описание

NeuronNet — это простая и эффективная библиотека для коллективного обучения нейросетей. Она позволяет моделям обучаться не только независимо, но и обмениваться знаниями, что ускоряет обучение и повышает качество предсказаний. Это идеальный инструмент для тех, кто хочет исследовать и развивать новые методы обучения.

### Возможности

Коллективное обучение: несколько моделей могут обмениваться знаниями, что ускоряет и улучшает процесс обучения.

Лёгкость в использовании: библиотека имеет минимальные зависимости и проста в интеграции.

Гибкость: поддерживает различные типы задач и легко адаптируется под нужды пользователя.


#### Установка

Для использования библиотеки в своём проекте:

pip install neuronnet  # Если библиотека будет доступна через PyPI

# Или клонируйте репозиторий:

git clone https://github.com/UmarArab1/NeuronNet  
cd neuronnet

#### Пример использования

import numpy as np
from neuronnet import CollectiveLearningModel, collective_training

#### Создание случайных данных для обучения
X = np.random.randn(100, 5)  # 100 примеров, 5 признаков
y = np.random.randn(100, 1)  # 100 целевых значений

# Создание моделей для коллективного обучения
models = [CollectiveLearningModel(5, 10, 1) for _ in range(3)]

# Обучение моделей
collective_training(models, X, y, epochs=1000, learning_rate=0.01)

# Проверка предсказаний
for i, model in enumerate(models):
    predictions, _ = model.forward(X[:10])
    print(f"Model {i+1} predictions:\n", predictions)

Лицензия

Проект распространяется под лицензией MIT с дополнительными ограничениями. Подробности см. в файле LICENSE.

Автор

Разработчик: Умар
Контакты: [umarfrost2011@gmail.com]

```mermaid
classDiagram
    class CollectiveLearningModel {
        +int input_size
        +int hidden_size
        +int output_size
        +weights_input_hidden
        +weights_hidden_output
        +bias_hidden
        +bias_output
        +forward(X)
        +backward(X, y, output, hidden_output, learning_rate)
    }

    class Training {
        +collective_training(models, X, y, epochs, learning_rate)
    }

    class NeuronNet {
        +CollectiveLearningModel models[]
        +train(X, y, epochs, learning_rate)
    }

    CollectiveLearningModel --> Training : uses
    Training --> NeuronNet : interacts

