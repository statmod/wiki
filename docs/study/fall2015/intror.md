---
title: "Спецкурс «Введение в обработку данных» (3 курс)"
---

 **Место и время проведения:** вторник, первая пара (09:30-11:05), ауд. 2444-II  
**Преподаватель:** Голяндина Нина Эдуардовна [^1]  
**Преподаватель:** Коробейников Антон Иванович [^2]  


---

## Программа курса


### Темы состоявшихся занятий


1.  Введение. Краткий обзор. Базовые операции: понятие “workspace”, присваивание, просмотр списка переменных, удаление переменных из workspace’а. Функции c() и seq(). Использование встроенной справки. // (29.09.2015) //
2.  Объекты R. Общие свойства (mode, length). Основные типы объектов: vector, factor, matrix, data frame, list, ts (time series), expression. Конверсия объектов друг в друга. // (29.09.2015) //
3.  Основные операции (арифметика, логические операции). Проверка равенства (==, identical, all.equal). Индексирование “векторных” переменных (включая именованные индексы). // (06.10.2015) //
4.  Вызов функций. Правила передачи аргументов. Аргументы по умолчанию. Ellipsis (…) operator. // (13.10.2015) //
5.  Основные встроенные “скалярные” функции: sum, prod, max, min, which.max, which.min, range, length. // (13.10.2015) //
6.  Основные встроенные “векторные” функции: round, rev, sort, rank, scale, pmin, pmax, cum{sum, prod, min, max}, diff, match, which // (13.10.2015) //
7.  Чтение данных из файла и с клавиатуры: функции read.table, scan. Запись данных в файл: функции write, write.table. // (20.10.2015) //
8.  Группировка, категоризующие переменные, функции над блоками данных: rowsum, aggregate, subset, lapply, sapply, replicate // (13.10.2015, 20.10.2015) //
9.  Операции с матрицами: cbind, rbind, t, diag, solve, qr, eigen, svd // (20.10.2015) //
10. Графические устройства (функции dev.*). Разбиение устройства на блоки. Понятие о графических параметрах // (10.11.2015) //
11. Высокоуровневые графические функции: plot, curve, coplot, pairs, density // (10.11.2015) //
12. Низкоуровневые графические функции: points, line, abline, axis, legend // (10.11.2015) //
13. Высокоуровневые графические функции: barplot, hist, boxplot // (10.11.2015) //
14. Распределения. Функции распределения, плотности. Моделирование. Функции “d”, “p”, “q”, “r”. // (10.11.2015) //
15. Функция sample // (10.11.2015) //
16. Отладка. Функции debug, browser, traceback, recover // (17.11.2015) //
17. Преобразование данных. Пакет plyr // (17.11.2015) // [golfdata.Rdata](../../assets/study/fall2011/intror/golfdata.rdata.zip), [sac-basic.R](../../assets/study/fall2011/intror/sac-basic.r.txt), [sac-plyr.R](../../assets/study/fall2011/intror/sac-plyr.r.txt),[reshape.R](../../assets/study/fall2011/intror/reshape.r.txt)
18. Пакет lattice. Введение. // (24.11.2015) // [intro.R](../../assets/study/fall2009/intror/intro.r.txt)
19. Пакет lattice. Изображение одномерных данных. // (24.11.2015)// [univariate.R](../../assets/study/fall2009/intror/univariate.r.txt)
20. Пакет lattice. Изображение двумерных данных: скаттерплоты, матрицы скаттерплотов, parallel plot’ы. Стили линий и т.п. // (01.12.2015) // [xyplot.R](../../assets/study/fall2009/intror/xyplot.r.txt), [splom.R](../../assets/study/fall2009/intror/splom.r.txt), [parallel.R](../../assets/study/fall2009/intror/parallel.r.txt)
21. Пакет lattice. Функции типа identify(). // (08.12.2015) // [lattice.identify.R](../../assets/study/fall2009/intror/lattice.identify.r.txt)


### Темы будущих занятий


1.  Метод наименьших квадратов. Линейная регрессия


## Prerequisites

 Дистрибутив R:

1.  [Windows](http://cran.r-project.org/bin/windows/base/R-3.2.2-win.exe)
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

|                   | Task 1 | Task 2 |   Data   |
|:-----------------:|:------:|:------:|:--------:|
|   Арцыман Илья    |   \+   |   \+   |  Oscar   |
|  Зотиков Дмитрий  |   \+   |   \+   | Airlines |
|  Сазыкин Дмитрий  |   \+   |   \+   |   SES    |
| Суровикина Тамара |   \+   |   \+   |   UFO    |
| Федорченко Сергей |   \+   |   \+   |   STAR   |


## Разное


1.  [Intro to R](http://www.youtube.com/playlist?list=PLOU2XLYxmsIK9qQfztXeybpHvru-TrqAP)

[^1]: в сентябре

[^2]: октябрь-декабрь