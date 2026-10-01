---
title: "Спецкурс «Введение в обработку данных» (3 курс)"
---

**Место и время проведения:** среда, третья пара (13:40-15:15), ауд. 2444-I (у окна)  
**Преподаватель:** Голяндина Нина Эдуардовна [^1]  
**Преподаватель:** Коробейников Антон Иванович [^2]  
—-

## Программа курса

### Темы состоявшихся занятий

1.  Введение. Краткий обзор. Базовые операции: понятие “workspace”, присваивание, просмотр списка переменных, удаление переменных из workspace’а. Функции c() и seq(). Использование встроенной справки. // (03.10.2012) //
2.  Объекты R. Общие свойства (mode, length). Основные типы объектов: vector, factor, matrix, data frame, list, ts (time series), expression. Конверсия объектов друг в друга. // (03.10.2012, 10.10.2012) //
3.  Основные операции (арифметика, логические операции). Проверка равенства (==, identical, all.equal). Индексирование “векторных” переменных (включая именованные индексы). // (10.10.2012) //
4.  Вызов функций. Правила передачи аргументов. Аргументы по умолчанию. Ellipsis (…) operator. // (17.10.2012) //
5.  Чтение данных из файла и с клавиатуры: функции read.table, scan. Запись данных в файл: функции write, write.table. // (17.10.2012) //
6.  Основные встроенные “скалярные” функции: sum, prod, max, min, which.max, which.min, range, length. // (17.10.2012) //
7.  Основные встроенные “векторные” функции: round, rev, sort, rank, scale, pmin, pmax, cum{sum, prod, min, max}, diff, match, which // (17.10.2012) //
8.  Операции с матрицами: cbind, rbind, t, diag, solve, qr, eigen, svd // (17.10.2012) //
9.  Группировка, категоризующие переменные, функции над блоками данных: rowsum, aggregate, subset, lapply, sapply, replicate // (24.10.2012) //
10. Графические устройства (функции dev.*). Разбиение устройства на блоки. Понятие о графических параметрах // (24.10.2012) //
11. Отладка. Функции debug, browser, traceback. // (24.10.2012) //
12. Высокоуровневые графические функции: plot, curve, coplot, pairs, density // (24.10.2012, 31.10.2012) //
13. Низкоуровневые графические функции: points, line, abline, axis, legend // (31.10.2012) //
14. Высокоуровневые графические функции: barplot, hist, boxplot // (31.10.2012) //
15. Распределения. Функции распределения, плотности. Моделирование. Функции “d”, “p”, “q”, “r”. Функция sample. // (31.10.2012) //
16. Метод наименьших квадратов. Линейная регрессия. // (31.10.2012) //
17. Преобразование данных. Пакет plyr. // (28.11.2012, 05.12.2012) // [golfdata.Rdata](../../assets/study/fall2011/intror/golfdata.rdata.zip), [sac-basic.R](../../assets/study/fall2011/intror/sac-basic.r.txt), [sac-plyr.R](../../assets/study/fall2011/intror/sac-plyr.r.txt),[reshape.R](../../assets/study/fall2011/intror/reshape.r.txt)
18. Пакет lattice. Введение. // (05.12.2012) // [intro.R](../../assets/study/fall2009/intror/intro.r.txt)
19. Пакет lattice. Изображение одномерных данных. // (12.12.2012) // [univariate.R](../../assets/study/fall2009/intror/univariate.r.txt)
20. Пакет lattice. Изображение двумерных данных: скаттерплоты, матрицы скаттерплотов, parallel plot’ы. Стили линий и т.п. // (12.12.2012, 19.12.2012) // [xyplot.R](../../assets/study/fall2009/intror/xyplot.r.txt), [splom.R](../../assets/study/fall2009/intror/splom.r.txt), [parallel.R](../../assets/study/fall2009/intror/parallel.r.txt)
21. Пакет lattice. Функции типа identify(). // (19.12.2012) // [lattice.identify.R](../../assets/study/fall2009/intror/lattice.identify.r.txt)

### Темы будущих занятий

1.  Пакет lattice. Изображение двумерных данных и данных большей размерности. Разное.

## Prerequisites

Дистрибутив R:

1.  [Windows](http://cran.r-project.org/bin/windows/base/R-2.15.1-win.exe)
2.  [Linux](http://cran.r-project.org/bin/linux)
3.  [MacOS X](http://cran.r-project.org/bin/macosx/)
4.  [Revolution-R](http://info.revolutionanalytics.com/free-academic.html)

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
5.  **Шипунов А.Б., Балдин Е.М., Волкова П.А., Коробейников А.И., Назарова С.А., Петров С.В., Суфиянов В.Г.** Наглядная статистика. Используем R! – М.: ДМК Пресс, 2012. – 298 с.

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
^ Андреев \| + \| + \| ATUS \|  
^ Григорян \| + \| + \| \|  
^ Грицай \| + \| + \| \|  
^ Звонарев \| + \| + \| \|  
^ Кипрушкин \| + \| + \| Crime \|  
^ Киселев \| + \| + \| \|  
^ Куликов \| + \| + \| Films - I \|  
^ Тарасов \| + \| + \| Airlines \|  
^ Федяева \| + \| + \| Oscar \|  

## Разное

FIXME

[^1]: в сентябре

[^2]: октябрь-декабрь
