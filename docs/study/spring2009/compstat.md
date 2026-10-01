---
title: "Спецкурс «Выч. методы и пакеты в статистическом исследовании» (4 курс)"
---

**Место и время проведения:** среда, 1 пара (ауд. 2514, по знаменателю), 2 пара (ауд. 2514), 3 пара (ауд. 2446).  
**Преподаватель:** Коробейников Антон Иванович  
—-

## Введение

FIXME

## Программа курса

### Темы состоявшихся занятий

1.  Введение. Краткий обзор. Базовые операции: понятие “workspace”, присваивание, просмотр списка переменных, удаление переменных из workspace’а. Функции c() и seq(). Использование встроенной справки. // (11.02.2009) //
2.  Объекты R. Общие свойства (mode, length). Основные типы объектов: vector, matrix, data frame, list, expression. Конверсия объектов друг в друга. // (11.02.2009, 18.02.2009) //
3.  Основные операции (арифметика, логические операции). Проверка равенства (==, identical, all.equal). Индексирование “векторных” переменных (включая именованные индексы). // (18.02.2009) //
4.  Вызов функций. Правила передачи аргументов. Аргументы по умолчанию. Ellipsis (…) operator. // (18.02.2009) //
5.  Основные встроенные “скалярные” функции: sum, prod, max, min, which.max, which.min, range, length // (18.02.2009) //
6.  Основные встроенные “векторные” функции: round, rev, sort, rank, scale, pmin, pmax, cum{sum, prod, min, max}, diff, match, which // (18.02.2009) //
7.  Функции над блоками данных: lapply, sapply, replicate // (18.02.2008) //
8.  Операции с матрицами: cbind, rbind, t, diag, solve, qr, eigen, svd // (18.02.2009) //
9.  Графические устройства (функции dev.*). Разбиение устройства на блоки. Понятие о графических параметрах. // (25.02.2009) //
10. Высокоуровневые графические функции: plot, curve, coplot, pairs, density // (25.02.2009) //
11. Распределения. Функции распределения, плотности. Моделирование. Функции “d”, “p”, “q”, “r”. Функция sample. // (25.02.2009) //
12. Низкоуровневые графические функции: points, line, axis, legend // (25.02.2009) //
13. Отладка. Функции debug, browser, traceback. // (04.03.2009) //
14. Векторизация. Эффективная работа с памятью. // (04.03.2009) //

### Темы будущих занятий

### Задачи

1.  Вычисление стационарного распределения марковской цепи (Problem 0, 25.02.2009)
2.  Вычисление интеграла методом Монте-Карло (Problem 1, 04.03.2009)
3.  Линейная, логистическая и нелинейная регрессия (Problem 2, 11.03.2009)
4.  Оценки максимального правдоподобия (Problem 3, 18.03.2009)
5.  EM-алгоритм. Построение ОМП для смеси нормально распределенных случайных величин (Problem 4, 25.03.2009)
6.  Support Vector Machines (Problem 5, 01.04.2009)
7.  Метод Гусеница-SSA (Problem 6, 08.04.2009)
8.  Спектральный анализ и фильтрация :) (Problem7, 15.04.2009)
9.  Кластерный анализ (Problem 8, 22.04.2009)

### (Возможные) будущие задачи

1.  Планирование эксперимента
2.  …

## Prerequisites

Дистрибутив R:

1.  [Windows](http://cran.r-project.org/bin/windows/base/R-2.8.0-win32.exe)
2.  [Linux](http://cran.r-project.org/bin/linux)
3.  [MacOS X](http://cran.r-project.org/bin/macosx/)

Редакторы и оболочки:

1.  [Tinn-R (Windows)](http://www.sciviews.org/Tinn-R/)
2.  [SciViews-K (Windows, Linux, MacOS X)](http://www.sciviews.org/SciViews-K/index.html)
3.  [RKWard (Linux)](http://rkward.sourceforge.net/)

## Рекомендуемая литература

### Книги

1.  **Peter Dalgaard**. *Introductory Statistics with R*. Springer, 2002.
2.  **John Maindonald and John Braun**. *Data Analysis and Graphics Using R*. Cambridge University Press, Cambridge, 2003.
3.  **John Verzani**. *Using R for Introductory Statistics*. Chapman & Hall/CRC, Boca Raton, FL, 2005.
4.  **Paul Murrell**. *R Graphics*. Chapman & Hall/CRC, Boca Raton, FL, 2005.
5.  **Ермаков С.М.** *Статистическое моделирование, часть II* [PDF](../../assets/study/books/mmm_part2.pdf)
6.  **Голяндина Н.Э.** *Метод «Гусеница»-SSA: анализ временных рядов*: Учеб. пособие. СПб: Изд-во СПбГУ, 2004. 76 с.[PDF](http://www.gistatgroup.com/gus/ssa_an.pdf)

### Статьи

1.  **John Maindonald**. *Using R for Data Analysis and Graphics - Introduction, Examples and Commentary*. [PDF](http://cran.r-project.org/doc/contrib/usingR.pdf)
2.  **John Verzani**. *Simple R*. [PDF](http://cran.r-project.org/doc/contrib/Verzani-SimpleR.pdf)
3.  **Petra Kuhnert and Bill Venables**. *An Introduction to R: Software for Statistical Modelling & Computing*. [ZIP](http://cran.r-project.org/doc/contrib/Kuhnert+Venables-R_Course_Notes.zip)
4.  **David Rossiter**. *Introduction to the R Project for Statistical Computing for Use at the ITC*. [PDF](http://cran.r-project.org/doc/contrib/Rossiter-RIntro-ITC.pdf)
5.  **Е.М. Балдин, А.И. Коробейников, А.Б. Шипунов** *Анализ данных с R* [www](http://www.inp.nsk.su/~baldin/DataAnalysis/)
6.  **А.И. Коробейников** *Оценки максимального правдоподобия в условиях цензурирования на базе EM-алгоритма* [PDF](../../assets/study/spring2008/em.pdf)

## Задачи

Условные обозначения:

1.  Цифра в клетке - порядковый номер “подхода”. Наличие цифры означает, что решение было получено, **проверено**, и результат отослан обратно.
2.  Плюс - зачет, звездочка - штраф, минус - хм, незачет ;-)

Кроме того, пишется дата и время.

|               |           |           |           |                    |                |
|:-------------:|:---------:|:---------:|:---------:|:------------------:|:--------------:|
|               | Problem 0 | Problem 1 | Problem 2 |     Problem 3      | Problem 4 [^1] |
| Андрющенко А. |    \+     |    \+     |    \+     |         \+         |       \+       |
|  Бережная М.  |    \+     |    \+     |    \+     |         \+         |                |
|  Буйнова С.   |    \+     |    \+     |    \+     |         \+         |       \+       |
|  Горбунов С.  |    \+     |    \+     |    \+     |         \+         |                |
|    Ким Е.     |    \+     |    \+     |    \+     |         \+         |       \+       |
|  Ненашева А.  |    \+     |    \+     |    \+     |         \+         |                |
|   Попов С.    |    \+     |    \+     |           | NegBinomial + cens |       \+       |
|  Тимофеев А.  |    \+     |    \+     |    \+     |         \+         |       \+       |
|  Тимофеев И.  |    \+     |    \+     |    \+     |         \+         |                |
| Трубников В.  |    \+     |    \+     |    \+     |         \+         |       \+       |

|               |                |          |           |          |             |
|:-------------:|:--------------:|:--------:|:---------:|:--------:|:-----------:|
|               | Problem 5 [^2] | [Problem 6](../../assets/study/spring2009/compstat/ssatask.pdf) | Problem 7 | [Problem 8](../../assets/study/spring2009/compstat/cltask.pdf) |   Допуск    |
| Андрющенко А. |       \+       |    \+    |    \+     |    \+    |   

✔

   |
|  Бережная М.  |       \+       |   \#3    |    \+     |    \+    | 

✘

 (2) |
|  Буйнова С.   |       \+       |    \+    |    \+     |    \+    |   

✔

   |
|  Горбунов С.  |  [satellite.zip](../../assets/study/spring2009/compstat/satellite.zip), C   |          |           |    \+    | 

✘

 (4) |
|    Ким Е.     |       \+       |    \+    |    \+     |    \+    |   

✔

   |
|  Ненашева А.  |  [splice.zip](../../assets/study/spring2009/compstat/splice.zip), C   |          |           |    \+    | 

✘

 (4) |
|   Попов С.    |  [satellite.zip](../../assets/study/spring2009/compstat/satellite.zip), nu  |   \#2    |    \+     |    \+    | 

✘

 (4) |
|  Тимофеев А.  |       \+       |    \+    |    \+     |    \+    |   

✔

   |
|  Тимофеев И.  |       \+       |   \#1    |    \+     |    \+    | 

✘

 (2) |
| Трубников В.  |       \+       |    \+    |    \+     |    \+    |   

✔

   |

** Внимание:** Если напротив Вашей фамилии отсутствует назначенное задание, то для его получения Вам следует отправить запрос по почте.

[^1]: Моделировать многомерное нормальное распределение можно при помощи функции mvrnorm из пакета MASS. Кроме того, в пакете mvtnorm присутствуют как функция плотности так и моделирующая функция

[^2]: При отсутствии специального тестового массива разделить тренировочный на две части. Метка классификации по-умолчанию является последним столбцом в файле.
