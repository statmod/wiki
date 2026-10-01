---
title: "Спецкурс «Введение в обработку данных» (3 курс)"
---

 **Место и время проведения:** четверг, вторая пара (11:15-12:50), ауд. 3357  
**Преподаватель:** Голяндина Нина Эдуардовна [^1]  
**Преподаватель:** Коробейников Антон Иванович [^2]  


---

## Программа курса


### Темы состоявшихся занятий


1.  Введение. Краткий обзор. Базовые операции: понятие “workspace”, присваивание, просмотр списка переменных, удаление переменных из workspace’а. Функции c() и seq(). Использование встроенной справки. // (09.10.2014) //
2.  Объекты R. Общие свойства (mode, length). Основные типы объектов: vector, factor, matrix, data frame, list, ts (time series), expression. Конверсия объектов друг в друга. // (09.10.2014) //
3.  Основные операции (арифметика, логические операции). Проверка равенства (==, identical, all.equal). Индексирование “векторных” переменных (включая именованные индексы). // (16.10.2014) //
4.  Вызов функций. Правила передачи аргументов. Аргументы по умолчанию. Ellipsis (…) operator. // (16.10.2014) //
5.  Основные встроенные “скалярные” функции: sum, prod, max, min, which.max, which.min, range, length. // (16.10.2014) //
6.  Основные встроенные “векторные” функции: round, rev, sort, rank, scale, pmin, pmax, cum{sum, prod, min, max}, diff, match, which // (16.10.2014) //
7.  Чтение данных из файла и с клавиатуры: функции read.table, scan. Запись данных в файл: функции write, write.table. // (23.10.2014) //
8.  Группировка, категоризующие переменные, функции над блоками данных: rowsum, aggregate, subset, lapply, sapply, replicate // (23.10.2014) //
9.  Операции с матрицами: cbind, rbind, t, diag, solve, qr, eigen, svd // (6.11.2014) //
10. Отладка. Функции debug, browser, traceback, recover // (06.11.2014) //
11. Распределения. Функции распределения, плотности. Моделирование. Функции “d”, “p”, “q”, “r”. // (6.11.2014) //
12. Функция sample // (11.11.2014) //
13. Метод наименьших квадратов. Линейная регрессия // (11.11.2014) //
14. Графические устройства (функции dev.*). Разбиение устройства на блоки. Понятие о графических параметрах // (13.11.2014) //
15. Высокоуровневые графические функции: plot, curve, coplot, pairs, density // (13.11.2014) //
16. Низкоуровневые графические функции: points, line, abline, axis, legend // (13.11.2014) //
17. Высокоуровневые графические функции: barplot, hist, boxplot // (13.11.2014) //
18. Преобразование данных. Пакет plyr // (20.11.2014) // [golfdata.Rdata](../../assets/study/fall2011/intror/golfdata.rdata.zip), [sac-basic.R](../../assets/study/fall2011/intror/sac-basic.r.txt), [sac-plyr.R](../../assets/study/fall2011/intror/sac-plyr.r.txt),[reshape.R](../../assets/study/fall2011/intror/reshape.r.txt)
19. Пакет lattice. Введение. // (27.12.2014) // [intro.R](../../assets/study/fall2009/intror/intro.r.txt)
20. Пакет lattice. Изображение одномерных данных. // (27.12.2014, 04.12.2014) // [univariate.R](../../assets/study/fall2009/intror/univariate.r.txt)
21. Пакет lattice. Изображение двумерных данных: скаттерплоты, матрицы скаттерплотов, parallel plot’ы. Стили линий и т.п. // (04.12.2014) // [xyplot.R](../../assets/study/fall2009/intror/xyplot.r.txt), [splom.R](../../assets/study/fall2009/intror/splom.r.txt), [parallel.R](../../assets/study/fall2009/intror/parallel.r.txt)
22. Пакет lattice. Функции типа identify(). // (11.12.2014) // [lattice.identify.R](../../assets/study/fall2009/intror/lattice.identify.r.txt)


### Темы  будущих занятий


1.  Пакет lattice. Введение
2.  Пакет lattice. Изображение одномерных данных
3.  Пакет lattice. Изображение двумерных данных: скаттерплоты, матрицы скаттерплотов, parallel plot’ы. Стили линий и т.п.
4.  Пакет lattice. Функции типа identify()
5.  Пакет lattice. Изображение двумерных данных и данных большей размерности. Разное.


## Prerequisites

 Дистрибутив R:

1.  [Windows](http://cran.r-project.org/bin/windows/base/R-3.1.1-win.exe)
2.  [Linux](http://cran.r-project.org/bin/linux)
3.  [MacOS X](http://cran.r-project.org/bin/macosx/)

Редакторы и оболочки:

1.  [R Studio (Windows, Linux, MacOS X)](http://www.rstudio.org)
2.  [Tinn-R (Windows)](http://www.sciviews.org/Tinn-R/)
3.  [SciViews-K (Windows, Linux, MacOS X)](http://www.sciviews.org/SciViews-K/index.html)
4.  [RKWard (Linux)](http://rkward.sourceforge.net/)


## Рекомендуемая литература

 

### Книги


1.  **Peter Dalgaard**. *Introductory Statistics with R*. Springer, 2002.
2.  **John Maindonald and John Braun**. *Data Analysis and Graphics Using R*. Cambridge University Press, Cambridge, 2003.
3.  **John Verzani**. *Using R for Introductory Statistics*. Chapman & Hall/CRC, Boca Raton, FL, 2005.
4.  **Paul Murrell**. *R Graphics*. Chapman & Hall/CRC, Boca Raton, FL, 2005.
5.  **Шипунов А.Б., Балдин Е.М., Волкова П.А., Коробейников А.И., Назарова С.А., Петров С.В., Суфиянов В.Г.** Наглядная статистика. Используем R! – М.: ДМК Пресс, 2012. – 298 с. [PDF](http://ashipunov.info/shipunov/school/books/rbook.pdf)
6.  **Роберт И. Кабаков** R в действии. Анализ и визуализация данных в R. – М.: ДМК Пресс, 2013. – 280 с.


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

|                    |            1            |           2           | экзамен  |
|:------------------:|:-----------------------:|:---------------------:|----------|
| Черниговская Мария |           \+            |          \+           | Crime    |
|    Суворов Иван    |           *+           |          \+           | UFO      |
|  Коврыга Валерия   |           \+            |          \+           | Films    |
|   Пимахов Кирилл   |           \+            |          \+           | STAR     |
|   Белоусов Юрий    |           \+            | 1 (11.12.2014, 03:19) | SES      |
| Грязнов Святослав  |           *+           |          \+           | ATUS     |
|     Явейн Анна     | *2 (06.12.2014, 12:47) |          \+           | Airlines |
|  Жорникова Полина  |           \+            |          \+           | Oscar    |


## Разное


1.  [Intro to R](http://www.youtube.com/playlist?list=PLOU2XLYxmsIK9qQfztXeybpHvru-TrqAP)

[^1]: в сентябре

[^2]: октябрь-декабрь