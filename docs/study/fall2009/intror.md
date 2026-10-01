---
title: "Спецкурс «Введение в обработку данных» (3 курс)"
---

**Место и время проведения:** четверг, вторая пара (11:15-12:50), ауд. 2444-II (дальняя), 2408  
**Преподаватель:** Голяндина Нина Эдуардовна [^1]  
**Преподаватель:** Коробейников Антон Иванович [^2]  
—-

## Программа курса

### Темы состоявшихся занятий

1.  Введение. Краткий обзор. Базовые операции: понятие “workspace”, присваивание, просмотр списка переменных, удаление переменных из workspace’а. Функции c() и seq(). Использование встроенной справки. // (24.09.2009) //
2.  Объекты R. Общие свойства (mode, length). Основные типы объектов: vector, factor, matrix, data frame, list, ts (time series), expression. Конверсия объектов друг в друга. // (24.09.2009, 08.10.2009) //
3.  Основные операции (арифметика, логические операции). Проверка равенства (==, identical, all.equal). Индексирование “векторных” переменных (включая именованные индексы). // (08.10.2009) //
4.  Вызов функций. Правила передачи аргументов. Аргументы по умолчанию. Ellipsis (…) operator. // (15.10.2009) //
5.  Чтение данных из файла и с клавиатуры: функции read.table, scan. Запись данных в файл: функции write, write.table. // (15.10.2009) //
6.  Основные встроенные “скалярные” функции: sum, prod, max, min, which.max, which.min, range, length // (15.10.2009, 22.10.2009) //
7.  Основные встроенные “векторные” функции: round, rev, sort, rank, scale, pmin, pmax, cum{sum, prod, min, max}, diff, match, which // (22.10.2009) //
8.  Группировка, категоризующие переменные, функции над блоками данных: rowsum, aggregate, subset, lapply, sapply, replicate // (22.10.2009) //
9.  Операции с матрицами: cbind, rbind, t, diag, solve, qr, eigen, svd // (22.10.2009) //
10. Графические устройства (функции dev.*). Разбиение устройства на блоки. Понятие о графических параметрах. // (29.10.2009) //
11. Высокоуровневые графические функции: plot, curve, coplot, pairs, density // (29.10.2009, частично) //
12. Высокоуровневые графические функции: barplot, hist, boxplot. // (29.10.2009) //
13. Низкоуровневые графические функции: points, line, abline, axis, legend // (29.10.2009) //
14. Отладка. Функции debug, browser, traceback. // (12.11.2009) //
15. Распределения. Функции распределения, плотности. Моделирование. Функции “d”, “p”, “q”, “r”. Функция sample. // (12.11.2009) //
16. Метод наименьших квадратов. Линейная регрессия. // (12.11.2009) //
17. Пакет lattice. Введение. // (19.11.2009) // [intro.R](../../assets/study/fall2009/intror/intro.r.txt)
18. Пакет lattice. Изображение одномерных данных. // (26.11.2009) // [univariate.R](../../assets/study/fall2009/intror/univariate.r.txt)
19. Пакет lattice. Изображение двумерных данных: скаттерплоты, матрицы скаттерплотов, parallel plot’ы. Стили линий и т.п. // (03.12.2009, 10.12.2009) // [xyplot.R](../../assets/study/fall2009/intror/xyplot.r.txt), [splom.R](../../assets/study/fall2009/intror/splom.r.txt)
20. Пакет lattice. Функции типа identify(). Пакеты playwith и latticist. // (10.12.2009) // [parallel.R](../../assets/study/fall2009/intror/parallel.r.txt), [lattice.identify.R](../../assets/study/fall2009/intror/lattice.identify.r.txt)

### Темы будущих занятий

1.  Пакет lattice. Изображение двумерных данных и данных большей размерности. Разное.

## Prerequisites

Дистрибутив R:

1.  [Windows](http://cran.r-project.org/bin/windows/base/R-2.9.2-win32.exe)
2.  [Linux](http://cran.r-project.org/bin/linux)
3.  [MacOS X](http://cran.r-project.org/bin/macosx/)

Редакторы и оболочки:

1.  [Tinn-R (Windows)](http://www.sciviews.org/Tinn-R/)
2.  [SciViews-K (Windows, Linux, MacOS X)](http://www.sciviews.org/SciViews-K/index.html)
3.  [RKWard (Linux)](http://rkward.sourceforge.net/)

‘Must-have’ пакеты:

1.  [playwith](http://cran.r-project.org/web/packages/playwith/index.html)
2.  [latticist](http://cran.r-project.org/web/packages/latticist/index.html)

## Рекомендуемая литература

### Книги

1.  **Peter Dalgaard**. *Introductory Statistics with R*. Springer, 2002.
2.  **John Maindonald and John Braun**. *Data Analysis and Graphics Using R*. Cambridge University Press, Cambridge, 2003.
3.  **John Verzani**. *Using R for Introductory Statistics*. Chapman & Hall/CRC, Boca Raton, FL, 2005.
4.  **Paul Murrell**. *R Graphics*. Chapman & Hall/CRC, Boca Raton, FL, 2005.

### Статьи

1.  **John Maindonald**. *Using R for Data Analysis and Graphics - Introduction, Examples and Commentary*. [PDF](http://cran.r-project.org/doc/contrib/usingR.pdf)
2.  **John Verzani**. *Simple R*. [PDF](http://cran.r-project.org/doc/contrib/Verzani-SimpleR.pdf)
3.  **Petra Kuhnert and Bill Venables**. *An Introduction to R: Software for Statistical Modelling & Computing*. [ZIP](http://cran.r-project.org/doc/contrib/Kuhnert+Venables-R_Course_Notes.zip)
4.  **David Rossiter**. *Introduction to the R Project for Statistical Computing for Use at the ITC*. [PDF](http://cran.r-project.org/doc/contrib/Rossiter-RIntro-ITC.pdf)
5.  **Е.М. Балдин, А.И. Коробейников, А.Б. Шипунов** *Анализ данных с R* [www](http://www.inp.nsk.su/~baldin/DataAnalysis/)

## Задачи

Условные обозначения:

1.  Цифра в клетке - порядковый номер “подхода”. Наличие цифры означает, что решение было получено, **проверено**, и результат отослан обратно.
2.  Решетка - задание запрошено и выдано, плюс - зачтено, звездочка - штраф, минус - хм, незачет ;-)

Кроме того, пишется дата и время.

|                 |                       |        |          |       |       |
|:---------------:|:---------------------:|:------:|:--------:|:-----:|:------|
|                 |        Task 1         | Task 2 |  Task 3  | Task4 | Зачет |
|  Векличева М.   |          \+           |   \+   |    \+    |       | ✘     |
|  Горбунова И.   |          \+           |   \+   |    \+    |  \+   | ✘     |
| Притыковская Н. |          *+          |  *+   | [star.zip](../../assets/study/fall2009/intror/star.zip)  |  \+   | ✘     |
| Галиаскарова Н. |          \+           |   \+   | [young.txt](../../assets/study/fall2009/intror/young.txt)  |  \+   | ✘     |
|    Сенов А.     |          \+           |   \+   | [middle.txt](../../assets/study/fall2009/intror/middle.txt)  |  \+   | ✘     |
|    Бояров А.    | 3 (20.12.2009, 18:10) |  *+   | [w300.txt](../../assets/study/fall2009/intror/w300.txt)  |  \+   | ✘     |
|  Сукманская К.  |          \+           |   \+   | [m300.txt](../../assets/study/fall2009/intror/m300.txt) |  \+   | ✘     |

[Названия переменных (для Task 3)](../../assets/study/fall2009/intror/names.xls)

[Полные расшифровки названий (для Task 3)](../../assets/study/fall2009/intror/films101_psypar99.txt)

[Жанры фильмов (исходно прилагалось к данным) (для Task 3)](../../assets/study/fall2009/intror/films_101_type.txt)

## Разное

FIXME

— *[Anton Korobeynikov](mailto:asl@math.spbu.ru) 2009/08/31 20:32*

[^1]: в сентябре

[^2]: октябрь-декабрь
