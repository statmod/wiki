---
title: "Спец. лабораторный выч. практикум (магистры, 2 курс)"
---

**Место и время проведения:** четверг, третья пара (13:40-15:15), ауд. 4399  
**Преподаватель:** Коробейников Антон Иванович  
—-

## Программа курса

### Темы состоявшихся занятий

1.  Введение. Краткий обзор. Базовые операции: понятие “workspace”, присваивание, просмотр списка переменных, удаление переменных из workspace’а. Функции c() и seq(). Использование встроенной справки. // (03.09.2009) //
2.  Объекты R. Общие свойства (mode, length). Основные типы объектов: vector, factor, matrix, data frame, list, ts (time series), expression. Конверсия объектов друг в друга. // (03.09.2009) //
3.  Основные операции (арифметика, логические операции). Проверка равенства (==, identical, all.equal). Индексирование “векторных” переменных (включая именованные индексы). // (03.09.2009, 10.09.2009) //
4.  Вызов функций. Правила передачи аргументов. Аргументы по умолчанию. Ellipsis (…) operator. // (10.09.2009) //
5.  Чтение данных из файла и с клавиатуры: функции read.table, scan. Запись данных в файл: функции write, write.table. // (17.09.2009 //
6.  Основные встроенные “скалярные” функции: sum, prod, max, min, which.max, which.min, range, length // (10.09.2009) //
7.  Основные встроенные “векторные” функции: round, rev, sort, rank, scale, pmin, pmax, cum{sum, prod, min, max}, diff, match, which // (10.09.2009) //
8.  Группировка, категоризующие переменные, функции над блоками данных: rowsum, aggregate, subset, lapply, sapply, replicate // (10.09.2009, 17.09.2009) //
9.  Операции с матрицами: cbind, rbind, t, diag, solve, qr, eigen, svd // (10.09.2009) //
10. Распределения. Функции распределения, плотности. Моделирование. Функции “d”, “p”, “q”, “r”. Функция sample. // (17.09.2009) //
11. Графические устройства (функции dev.*). Разбиение устройства на блоки. Понятие о графических параметрах. // (24.10.2009) //
12. Высокоуровневые графические функции: plot, curve, coplot, pairs, density // (24.10.2009) //
13. Высокоуровневые графические функции: barplot, hist, boxplot. // (24.10.2009) * - Отладка. Функции debug, browser, traceback.* (24.10.2009) //
14. Низкоуровневые графические функции: points, line, abline, axis, legend // (24.10.2009) //
15. Оценки максимального правдоподобия // (08.10.2009) //
16. Линейная регрессия // (15.10.2009) //
17. Проверка гипотез о равенстве средних, гипотез согласия // (22.10.2009) //
18. Метод опорных векторов (Support Vector Machines) // (29.10.2009) //
19. Анализ данных типа времени жизни // (12.11.2009) //
20. Model-based clustering. EM-алгоритм // (19.11.2009) //
21. Кластерный анализ // (26.11.2009) //
22. Ядерные методы // (03.12.2009, 10.12.2009) //

### Темы будущих занятий

1.  Дисперсионный анализ
2.  Факторный анализ и метод главных компонент
3.  Анализ временных рядов. Метод Гусеница-SSA
4.  …

## Задачи

Условные обозначения:

1.  Цифра в клетке - порядковый номер “подхода”. Наличие цифры означает, что решение было получено, **проверено**, и результат отослан обратно.
2.  Решетка - задание запрошено и выдано, плюс - зачтено, звездочка - штраф, минус - хм, незачет ;-)

Кроме того, пишется дата и время.

|              |      |     |           |                  |     |     |         |        |
|:------------:|:----:|:---:|:---------:|:----------------:|:---:|:---:|:-------:|:------:|
|              | Data | ОМП | Регрессия | Проверка гипотез | SVM | EM  | Cluster | Kernel |
| Власьева Е.  |  \+  | \+  |    \+     |        \+        | \+  | \+  |   \+    |   \+   |
| Марудова Н.  |  \+  | \+  |    \+     |        \+        | \+  | \+  |   \+    |   \+   |
| Радионов А.  |  \+  | \+  |    \+     |        \+        | \+  | \+  |   \+    |   \+   |
| Казакова О.  |  \+  | \#  |    \+     |        \+        | \#  | \+  |   \+    |   \+   |
| Кузнецова А. |  \+  | \+  |    \+     |        \+        | \+  | \+  |   \+    |   \+   |

## Prerequisites

Дистрибутив R:

1.  [Windows](http://cran.r-project.org/bin/windows/base/R-2.9.2-win32.exe)
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

### Статьи

1.  **John Maindonald**. *Using R for Data Analysis and Graphics - Introduction, Examples and Commentary*. [PDF](http://cran.r-project.org/doc/contrib/usingR.pdf)
2.  **John Verzani**. *Simple R*. [PDF](http://cran.r-project.org/doc/contrib/Verzani-SimpleR.pdf)
3.  **Petra Kuhnert and Bill Venables**. *An Introduction to R: Software for Statistical Modelling & Computing*. [ZIP](http://cran.r-project.org/doc/contrib/Kuhnert+Venables-R_Course_Notes.zip)
4.  **David Rossiter**. *Introduction to the R Project for Statistical Computing for Use at the ITC*. [PDF](http://cran.r-project.org/doc/contrib/Rossiter-RIntro-ITC.pdf)
5.  **Е.М. Балдин, А.И. Коробейников, А.Б. Шипунов** *Анализ данных с R* [www](http://www.inp.nsk.su/~baldin/DataAnalysis/)
