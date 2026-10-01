---
title: "Спецкурс «Введение в обработку данных» (3 курс)"
---

**Место и время проведения:** четверг, вторая пара (11:15-12:50), ауд. 2444-II (дальняя).  
**Преподаватель:** Голяндина Нина Эдуардовна [^1]  
**Преподаватель:** Коробейников Антон Иванович [^2]  
—-

## Программа курса

### Темы состоявшихся занятий

1.  Введение. Краткий обзор. Базовые операции: понятие “workspace”, присваивание, просмотр списка переменных, удаление переменных из workspace’а. Функции c() и seq(). Использование встроенной справки. // (25.09.2008) //
2.  Объекты R. Общие свойства (mode, length). Основные типы объектов: vector, factor, matrix, data frame, list, ts (time series), expression. Конверсия объектов друг в друга. // (25.09.2008, 02.10.2008) //
3.  Основные операции (арифметика, логические операции). Проверка равенства (==, identical, all.equal). Индексирование “векторных” переменных (включая именованные индексы). // (02.10.2008) //
4.  Вызов функций. Правила передачи аргументов. Аргументы по умолчанию. Ellipsis (…) operator. // (02.10.2008) //
5.  Чтение данных из файла и с клавиатуры: функции read.table, scan. Запись данных в файл: функции write, write.table. // (09.10.2008)

//

1.  Основные встроенные “скалярные” функции: sum, prod, max, min, which.max, which.min, range, length // (16.10.2008) //
2.  Основные встроенные “векторные” функции: round, rev, sort, rank, scale, pmin, pmax, cum{sum, prod, min, max}, diff, match, which // (16.10.2008) //
3.  Группировка, категоризующие переменные, функции над блоками данных: rowsum, aggregate, subset, lapply, sapply, replicate // (16.10.2008) //
4.  Операции с матрицами: cbind, rbind, t, diag, solve, qr, eigen, svd // (16.10.2008, 23.10.2008) //
5.  Графические устройства (функции dev.*). Разбиение устройства на блоки. Понятие о графических параметрах. // (23.10.2008) //
6.  Высокоуровневые графические функции: plot, curve, coplot, pairs, density // (23.10.2008) //
7.  Высокоуровневые графические функции: barplot, hist, boxplot. // (30.10.2008) //
8.  Отладка. Функции debug, browser, traceback. // (30.10.2008) //
9.  Распределения. Функции распределения, плотности. Моделирование. Функции “d”, “p”, “q”, “r”. Функция sample. // (30.10.2008) //
10. Низкоуровневые графические функции: points, line, abline, axis, legend // (06.11.2008) //
11. Метод наименьших квадратов. Линейная регрессия. // (06.11.2008) //
12. Пакет lattice. Введение. Изображение одномерных данных. // (13.11.2008) // [intro.R](../../assets/study/fall2008/intror/intro.r.txt), [univariate.R](../../assets/study/fall2008/intror/univariate.r.txt)
13. Пакет lattice. Изображение двумерных данных: скаттерплоты, матрицы скаттерплотов, parallel plot’ы. Стили линий и т.п. // (20.11.2008) // [xyplot.R](../../assets/study/fall2008/intror/xyplot.r.txt), [splom.R](../../assets/study/fall2008/intror/splom.r.txt), [parallel.R](../../assets/study/fall2008/intror/parallel.r.txt)
14. Пакет lattice. Функции типа identify(). Пакеты playwith и latticist. // (27.11.2008) // [lattice.identify.R](../../assets/study/fall2008/intror/lattice.identify.r.txt)

### Темы будущих занятий

1.  Пакет lattice. Изображение двумерных данных и данных большей размерности. Разное.

## Prerequisites

Дистрибутив R:

1.  [Windows](http://cran.r-project.org/bin/windows/base/R-2.8.0-win32.exe)
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
2.  Плюс - зачет, звездочка - штраф, минус - хм, незачет ;-)

Кроме того, пишется дата и время.

|              |        |        |          |       |       |
|:------------:|:------:|:------:|:--------:|------:|:------|
|              | Task 1 | Task 2 |  Task 3  | Task4 | Зачет |
|  Антонов А.  |   \+   |   \+   |    \+    |    \+ | ✔     |
|  Болотов Ю.  |   \+   |   \+   | [w300-2.txt](../../assets/study/fall2008/intror/w300_norm.txt)  |    \+ | ✔     |
| Голяндина А. |   \+   |   \+   | [young.txt](../../assets/study/fall2008/intror/young.txt)  |    \+ | ✔     |
|  Егорова О.  |   \+   |   \+   | [w300.txt](../../assets/study/fall2008/intror/w300.txt)  |    \+ | ✔     |
|  Жукова М.   |   \+   |   \+   | [midlle2.txt](../../assets/study/fall2008/intror/middle_norm.txt)  |    \+ | ✔     |
| Матвеева Ю.  |   \+   |   \+   | [middle.txt](../../assets/study/fall2008/intror/middle.txt) |    \+ | ✔     |
| Русинова М.  |   \+   |   \+   | [m300.txt](../../assets/study/fall2008/intror/m300.txt) |    \+ | ✔     |
|  Шлемов А.   |   \+   |   \+   | [egsingle.zip](../../assets/study/fall2008/intror/egsingle.zip) |    \+ | ✔     |
| Яковенко А.  |  +*   |   \+   | [young2.txt](../../assets/study/fall2008/intror/young_norm.txt) |    \+ | ✔     |

[Названия переменных (для Task 3)](../../assets/study/fall2008/intror/names.xls)

[Полные расшифровки названий (для Task 3)](../../assets/study/fall2008/intror/films101_psypar99.txt)

[Жанры фильмов (исходно прилагалось к данным) (для Task 3)](../../assets/study/fall2008/intror/films_101_type.txt)

## Разное

FIXME

— *[Anton Korobeynikov](mailto:asl@math.spbu.ru) 2008/10/30 01:53*

[^1]: в сентябре

[^2]: октябрь-декабрь
