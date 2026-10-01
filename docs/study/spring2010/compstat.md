---
title: "Спецкурс «Выч. методы и пакеты в статистическом исследовании» (4 курс)"
---

**Место и время проведения:** 1-2 пары, ауд 4526; 3 пара, ауд 2446  
**Преподаватель:** Коробейников Антон Иванович, Усевич Константин Дмитриевич  
—-

## Программа курса

### Темы состоявшихся занятий

1.  Введение. Краткий обзор. Базовые операции: понятие “workspace”, присваивание, просмотр списка переменных, удаление переменных из workspace’а. Функции c() и seq(). Использование встроенной справки. *(10.02.2010)*
2.  Объекты R. Общие свойства (mode, length). Основные типы объектов: vector, matrix, data frame, list, expression. Конверсия объектов друг в друга. *(10.02.2010)*
3.  Основные операции (арифметика, логические операции). Проверка равенства (==, identical, all.equal). Индексирование “векторных” переменных (включая именованные индексы). *(10.02.2010)*
4.  Вызов функций. Правила передачи аргументов. Аргументы по умолчанию. Ellipsis (…) operator. *(10.02.2010, 17.02.2010)*
5.  Основные встроенные “скалярные” функции: sum, prod, max, min, which.max, which.min, range, length *(17.02.2010)*
6.  Основные встроенные “векторные” функции: round, rev, sort, rank, scale, pmin, pmax, cum{sum, prod, min, max}, diff, match, which *(17.02.2010)*
7.  Функции над блоками данных: lapply, sapply, replicaten *(17.02.2010)*
8.  Операции с матрицами: cbind, rbind, t, diag, solve, qr, eigen, svd *(17.02.2010)*
9.  Графические устройства (функции dev.*). Разбиение устройства на блоки. Понятие о графических параметрах. *(24.02.2010)*
10. Высокоуровневые графические функции: plot, curve, coplot, pairs, density *(24.02.2010)*
11. Распределения. Функции распределения, плотности. Моделирование. Функции “d”, “p”, “q”, “r”. Функция sample. *(24.02.2010)*
12. Низкоуровневые графические функции: points, line, axis, legend. *(24.02.2010)*
13. Отладка. Функции debug, browser, traceback. *(17.02.2010)*
14. Векторизация. Эффективная работа с памятью. *(17.02.2010)*
15. Нахождение (локальных) экстремумов функций *(24.02.2010)*

### Темы будущих занятий

### Задачи

1.  Вычисление стационарного распределения марковской цепи (Problem 0)
2.  Моделирование. Адаптивный метод отбора (Problem 1)
3.  Вычисление интеграла методом Монте-Карло (Problem 2)
4.  Оценки максимального правдоподобия (Problem 3)
5.  EM-алгоритм. Построение ОМП для смеси нормально распределенных случайных величин (Problem 4)
6.  Support Vector Machines (Problem 5)
7.  Метод Гусеница-SSA (Problem 6)
8.  Кластерный анализ (Problem 7)
9.  Линейная регрессия (Problem 8)
10. Нейронные сети (Problem 9)

### (Возможные) будущие задачи

1.  Линейная, логистическая и нелинейная регрессия
2.  Планирование эксперимента
3.  …

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

1.  Решетка - задание запрошено и выдано, плюс - зачтено, звездочка - штраф, минус - хм, незачет

Кроме того, пишется дата и время.

|  |  |  |  |  |  |  |  |  |  |  |  |
|:--:|---:|:--:|:--:|:--:|:--:|:--:|----|----|:--:|:--:|:---|
|  | Problem 0 | Problem 1 | [Problem 2](../../assets/study/spring2010/compstat/task2.pdf) | [Problem 3](../../assets/study/spring2010/compstat/task3.pdf) | [Problem 4](../../assets/study/spring2010/compstat/task4.pdf) | Problem 5 | [Problem 6](../../assets/study/spring2010/compstat/task6.pdf) | [Problem 7](../../assets/study/spring2010/compstat/task7.pdf) | Problem 8 | Problem 9 | Допуск |
| Антонов А. | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

+

 |
| Егорова О. | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

+

 |
| Жукова М. | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

+

 |
| Матвеева Ю. | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

+

 |
| Шлемов А. | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

+

 |
| Яковенко А. | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

+

 |
| Болотов Ю. | \+ | \+ | \+ | \+ | \+ | \+ | 10 | \+ |  | \# | 

3

 |
| Голяндина А. | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

+

 |
| Евстафьева Н. | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

+

 |
| Кубасова Ю. | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

+

 |

|  |  |  |  |  |  |  |  |  |  |  |  |
|:--:|---:|:--:|:--:|:---|:--:|:--:|----|----|:--:|:--:|:--:|
|  | Problem 0 | Problem 1 | [Problem 2](../../assets/study/spring2010/compstat/task2.pdf) | [Problem 3](../../assets/study/spring2010/compstat/task3.pdf) | [Problem 4](../../assets/study/spring2010/compstat/task4.pdf) | Problem 5 | [Problem 6](../../assets/study/spring2010/compstat/task6.pdf) | [Problem 7](../../assets/study/spring2010/compstat/task7.pdf) | Problem 8 | Problem 9 | Допуск |
| Александров А. | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

+

 |
| Дмитриев А. | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

+

 |
| Васильев Д. | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

+

 |
| Бонько Е. | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

+

 |
| Титоренко А. | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

+

 |
| Фидельман Д. | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

+

 |
| Аношина Т. | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

+

 |
| Сизов А. | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

+

 |
| Натекин А. | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

+

 |
| Дерягин Е. | \+ | \+ | \+ | \# | \# | \# | \# | \# | \# | \# | 

7

 |
| Тамазян Г. | \+ | \+ | \+ | 10 | 2, [cross.txt](../../assets/study/spring2010/compstat/cross.txt) | \+ | 2 | \+ | \# | \+ | 

4

 |

** Внимание:** Если напротив Вашей фамилии отсутствует назначенное задание, то для его получения Вам следует отправить запрос по почте.

## Разное

Список рассылки: [http://groups.google.com/a/statmod.ru/group/r-spring-2010](http://groups.google.com/a/statmod.ru/group/r-spring-2010)

### Запись на первую часть беседы по программе экзамена

27.05.2010, с 11:00. Аудитория будет известна позднее. Необходимым условием для записи является наличие допуска. Не более 12 человек.

1.  Егорова О.
2.  Жукова М.
3.  Александров А.
4.  Дмитриев А.

### Запись на вторую часть беседы по программе экзамена

08.06.2010, с 11:00. Аудитория будет известна позднее. Необходимым условием для записи является наличие допуска. Не более 10 человек.

1.  Васильев Д.
2.  Кубасова Ю.
3.  Антонов А.
