# Brain Games

Набор математических игр для тренировки мозга. Проект включает в себя пять различных игр, каждая из которых проверяет различные математические навыки.

## Описание проекта

Brain Games — это коллекция консольных игр, разработанных на Python, которые помогают развивать математические способности и логическое мышление. Каждая игра предлагает серию вопросов, на которые нужно дать правильные ответы. Для победы необходимо правильно ответить на 3 вопроса подряд.

### Доступные игры:

- **brain-even** — определение четных чисел
- **brain-calc** — вычисление результата арифметических выражений
- **brain-gcd** — нахождение наибольшего общего делителя
- **brain-progression** — поиск пропущенного числа в арифметической прогрессии
- **brain-prime** — определение простых чисел

## Зависимости

Проект использует следующие зависимости:

- **Python** >= 3.12
- **prompt** >= 0.4.1 — библиотека для ввода данных от пользователя

Для разработки также используется:
- **ruff** >= 0.12.10 — линтер и форматтер кода

## Установка

### Требования

- Python 3.12 или выше
- [uv](https://github.com/astral-sh/uv) — современный менеджер пакетов Python

### Инструкция по установке

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd devops-engineer-from-scratch-project-49
```

2. Установите зависимости:
```bash
make install
```

Или напрямую:
```bash
uv sync
```

3. (Опционально) Соберите пакет и установите его:
```bash
make build
make package-install
```

## Запуск

### Основная команда

Запуск приветственного экрана:
```bash
make brain-games
```

Или:
```bash
uv run brain-games
```

### Игры

#### brain-even
Определите, является ли число четным:
```bash
make brain-even
```
или
```bash
uv run brain-even
```

#### brain-calc
Вычислите результат арифметического выражения:
```bash
make brain-calc
```
или
```bash
uv run brain-calc
```

#### brain-gcd
Найдите наибольший общий делитель двух чисел:
```bash
make brain-gcd
```
или
```bash
uv run brain-gcd
```

#### brain-progression
Найдите пропущенное число в арифметической прогрессии:
```bash
make brain-progression
```
или
```bash
uv run brain-progression
```

#### brain-prime
Определите, является ли число простым:
```bash
make brain-prime
```
или
```bash
uv run brain-prime
```

## Примеры использования

### Пример игры brain-even

```
Welcome to the Brain Games!
May I have your name?
John
Hello, John!
Answer "yes" if the number is even, otherwise answer "no".
Question: 15
Your answer:
no
Correct!
Question: 42
Your answer:
yes
Correct!
Question: 7
Your answer:
no
Correct!
Congratulations, John!
```

### Пример игры brain-calc

```
Welcome to the Brain Games!
May I have your name?
Alice
Hello, Alice!
What is the result of the expression?
Question: 5 + 3
Your answer:
8
Correct!
Question: 10 - 4
Your answer:
6
Correct!
Question: 7 * 2
Your answer:
14
Correct!
Congratulations, Alice!
```

## Структура команд

Проект использует Makefile для упрощения работы с командами:

| Команда | Описание |
|---------|----------|
| `make install` | Установка зависимостей проекта |
| `make brain-games` | Запуск приветственного экрана |
| `make brain-even` | Запуск игры brain-even |
| `make brain-calc` | Запуск игры brain-calc |
| `make brain-gcd` | Запуск игры brain-gcd |
| `make brain-progression` | Запуск игры brain-progression |
| `make brain-prime` | Запуск игры brain-prime |
| `make build` | Сборка пакета |
| `make package-install` | Установка собранного пакета |
| `make lint` | Проверка кода линтером |

## Структура проекта

```
brain_games/
├── __init__.py
├── cli.py              # Функции для взаимодействия с пользователем
├── constants.py        # Константы проекта
├── game_engine.py      # Универсальный движок для запуска игр
├── utils.py            # Вспомогательные функции
├── game_logic/         # Логика отдельных игр
│   ├── brain_calc.py
│   ├── brain_even.py
│   ├── brain_gcd.py
│   ├── brain_prime.py
│   └── brain_progression.py
└── scripts/            # Точки входа для запуска игр
    ├── brain_games.py
    ├── brain_even.py
    ├── brain_calc.py
    ├── brain_gcd.py
    ├── brain_progression.py
    └── brain_prime.py
```

- installation - https://asciinema.org/a/Ai9jpPAlMYGLTBCAf8Y4YTFkU
- brain-even launch game - https://asciinema.org/a/F1CfVWYBnkTjNGUfrTKrzgvN9
- brain-even won game - https://asciinema.org/a/YNIIXXrmrkwhc79wG9rKL0fJM
- brain-even lost game - https://asciinema.org/a/JtqK1bFjQHzX0ahbaPSVbB7po
- brain-calc won game - https://asciinema.org/a/TOgArXeGkBPturU5yphamYQJP
- brain-calc lost game - https://asciinema.org/a/8gFqaddWhmbMnOD75sG3dwA9N
- brain-gcd won game - https://asciinema.org/a/7d249n38DG8sJIdZCql01im8P
- brain-gcd lost game - https://asciinema.org/a/EbTt974aKVXsvp1f5V266Z8vX
- brain-progression won game - https://asciinema.org/a/i24aEtahiC6zijVAcB1GVuqqV
- brain-progression lost game - https://asciinema.org/a/5jdNqIHFvUKXnAsv3cjan5U12
- brain-prime won game - https://asciinema.org/a/JG0emCFUa8gHZ5IjVv7vNVQyc
- brain-prime lost game - https://asciinema.org/a/VuEACndCuI3unWEHHQ57P9RVe

## Статус проекта

### Hexlet tests and linter status:
[![Actions Status](https://github.com/kimdeun/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/kimdeun/devops-engineer-from-scratch-project-49/actions)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=kimdeun_devops-engineer-from-scratch-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=kimdeun_devops-engineer-from-scratch-project-49)

[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=kimdeun_devops-engineer-from-scratch-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=kimdeun_devops-engineer-from-scratch-project-49)

[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=kimdeun_devops-engineer-from-scratch-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=kimdeun_devops-engineer-from-scratch-project-49)

[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=kimdeun_devops-engineer-from-scratch-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=kimdeun_devops-engineer-from-scratch-project-49)

[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=kimdeun_devops-engineer-from-scratch-project-49&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=kimdeun_devops-engineer-from-scratch-project-49)

[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=kimdeun_devops-engineer-from-scratch-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=kimdeun_devops-engineer-from-scratch-project-49)

[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=kimdeun_devops-engineer-from-scratch-project-49&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=kimdeun_devops-engineer-from-scratch-project-49)

[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=kimdeun_devops-engineer-from-scratch-project-49&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=kimdeun_devops-engineer-from-scratch-project-49)

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=kimdeun_devops-engineer-from-scratch-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=kimdeun_devops-engineer-from-scratch-project-49)

[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=kimdeun_devops-engineer-from-scratch-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=kimdeun_devops-engineer-from-scratch-project-49)
