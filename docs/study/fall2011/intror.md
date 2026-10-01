---
title: "Спецкурс «Введение в обработку данных» (3 курс)"
---

**Место и время проведения:** четверг, вторая пара (11:15-12:50), ауд. 2444-II (дальняя)  
**Преподаватель:** Голяндина Нина Эдуардовна [^1]  
**Преподаватель:** Коробейников Антон Иванович [^2]  
—-

## Программа курса

### Темы состоявшихся занятий

1.  Введение. Краткий обзор. Базовые операции: понятие “workspace”, присваивание, просмотр списка переменных, удаление переменных из workspace’а. Функции c() и seq(). Использование встроенной справки. // (29.09.2011) //
2.  Объекты R. Общие свойства (mode, length). Основные типы объектов: vector, factor, matrix, data frame, list, ts (time series), expression. Конверсия объектов друг в друга. // (29.09.2011, 06.10.2011) //
3.  Основные операции (арифметика, логические операции). Проверка равенства (==, identical, all.equal). Индексирование “векторных” переменных (включая именованные индексы). // (06.10.2011, 13.10.2011) //
4.  Вызов функций. Правила передачи аргументов. Аргументы по умолчанию. Ellipsis (…) operator. // (13.10.2011) //
5.  Чтение данных из файла и с клавиатуры: функции read.table, scan. Запись данных в файл: функции write, write.table. // (20.10.2011) //
6.  Основные встроенные “скалярные” функции: sum, prod, max, min, which.max, which.min, range, length. // (20.10.2011) //
7.  Основные встроенные “векторные” функции: round, rev, sort, rank, scale, pmin, pmax, cum{sum, prod, min, max}, diff, match, which // (20.10.2011) //
8.  Группировка, категоризующие переменные, функции над блоками данных: rowsum, aggregate, subset, lapply, sapply, replicate // (27.10.2011) //
9.  Операции с матрицами: cbind, rbind, t, diag, solve, qr, eigen, svd // (27.10.2011) //
10. Графические устройства (функции dev.*). Разбиение устройства на блоки. Понятие о графических параметрах // (03.11.2011) //
11. Высокоуровневые графические функции: plot, curve, coplot, pairs, density // (03.11.2011, 10.11.2011) //
12. Низкоуровневые графические функции: points, line, abline, axis, legend // (03.11.2011) //
13. Высокоуровневые графические функции: barplot, hist, boxplot // (10.11.2011) //
14. Отладка. Функции debug, browser, traceback. // (17.11.2011) //
15. Распределения. Функции распределения, плотности. Моделирование. Функции “d”, “p”, “q”, “r”. Функция sample. // (17.11.2011) //
16. Метод наименьших квадратов. Линейная регрессия. // (17.11.2011) //
17. Преобразование данных. Пакеты plyr и reshape2. // (24.11.2011, 01.12.2011) // [golfdata.Rdata](../../assets/study/fall2011/intror/golfdata.rdata.zip), [sac-basic.R](../../assets/study/fall2011/intror/sac-basic.r.txt), [sac-plyr.R](../../assets/study/fall2011/intror/sac-plyr.r.txt),[reshape.R](../../assets/study/fall2011/intror/reshape.r.txt)
18. Пакет lattice. Введение. // (08.12.2011) // [intro.R](../../assets/study/fall2009/intror/intro.r.txt)
19. Пакет lattice. Изображение одномерных данных. // (08.12.2011, частично) // [univariate.R](../../assets/study/fall2009/intror/univariate.r.txt)
20. Пакет lattice. Изображение двумерных данных: скаттерплоты, матрицы скаттерплотов, parallel plot’ы. Стили линий и т.п. // (15.12.2011, 22.12.2011) // [xyplot.R](../../assets/study/fall2009/intror/xyplot.r.txt), [splom.R](../../assets/study/fall2009/intror/splom.r.txt), [parallel.R](../../assets/study/fall2009/intror/parallel.r.txt)
21. Пакет lattice. Функции типа identify(). // (22.12.2011) // [lattice.identify.R](../../assets/study/fall2009/intror/lattice.identify.r.txt)

### Темы будущих занятий

1.  Пакет lattice. Изображение двумерных данных и данных большей размерности. Разное.

## Prerequisites

Дистрибутив R:

1.  [Windows](http://cran.r-project.org/bin/windows/base/R-2.13.1-win.exe)
2.  [Linux](http://cran.r-project.org/bin/linux)
3.  [MacOS X](http://cran.r-project.org/bin/macosx/)
4.  [Revolution-R](http://info.revolutionanalytics.com/free-academic.html)

Редакторы и оболочки:

1.  [R Studio (Windows, Linux, MacOS X)](http://www.rstudio.org)
2.  [Tinn-R (Windows)](http://www.sciviews.org/Tinn-R/)
3.  [SciViews-K (Windows, Linux, MacOS X)](http://www.sciviews.org/SciViews-K/index.html)
4.  [RKWard (Linux)](http://rkward.sourceforge.net/)

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

3 курс: ^ ^ Task 1 ^ Task 2 ^ Task 3 ^  
^ Артишевская Юлия \| 3 (03.01.2012, 22:08) \| 1 (03.01.2012, 22:13) \| UFO# \|  
^ Гученко Роман \| + \| + \| Airlines# \|  
^ Есипенко Евгений \| + \| + \| STAR# \|  
^ Майер Роман \| + \| + \| SES# \|  
^ Тросиненко Анатолий \| + \| + \| ATUS# \|  
^ Яковлева Ольга \| + \| 2 (06.02.2012, 14:35) \| Oscar# \|  

## Разное

FIXME

— *[Anton Korobeynikov](mailto:anton@korobeynikov.info) 2011/09/28 00:13*

[^1]: в сентябре

[^2]: октябрь-декабрь
