---
title: "322 гр., спец. СМ. Спецкурс «Введение в обработку данных»"
---

**Место и время проведения:** четверг, вторая пара (11:15-12:50), ауд. 4526  
**Преподаватель:** Коробейников Антон Иванович [^1]  


---

## Программа курса


### Темы состоявшихся занятий


1.  Введение. Краткий обзор. Базовые операции: понятие “workspace”, присваивание, просмотр списка переменных, удаление переменных из workspace’а. Функции c() и seq(). Использование встроенной справки.
2.  Объекты R. Общие свойства (mode, length). Основные типы объектов: vector, factor, matrix, data frame, list, ts (time series), expression. Конверсия объектов друг в друга.
3.  Основные операции (арифметика, логические операции). Проверка равенства (==, identical, all.equal). Индексирование “векторных” переменных (включая именованные индексы).
4.  Вызов функций. Правила передачи аргументов. Аргументы по умолчанию. Ellipsis (…) operator.
5.  Основные встроенные “скалярные” функции: sum, prod, max, min, which.max, which.min, range, length.
6.  Основные встроенные “векторные” функции: round, rev, sort, rank, scale, pmin, pmax, cum{sum, prod, min, max}, diff, match, which
7.  Чтение данных из файла и с клавиатуры: функции read.table, scan. Запись данных в файл: функции write, write.table.
8.  Операции с матрицами: cbind, rbind, t, diag, solve, qr, eigen, svd
9.  Группировка, категоризующие переменные, функции над блоками данных: rowsum, aggregate, subset, lapply, sapply, replicate
10. Графические устройства (функции dev.*). Разбиение устройства на блоки. Понятие о графических параметрах
11. Высокоуровневые графические функции: plot, curve, coplot, pairs, density
12. Низкоуровневые графические функции: points, line, abline, axis, legend

<!-- -->

    - 


### Темы будущих занятий


1.  Высокоуровневые графические функции: barplot, hist, boxplot
2.  Распределения. Функции распределения, плотности. Моделирование. Функции “d”, “p”, “q”, “r”.
3.  Функция sample
4.  Отладка. Функции debug, browser, traceback, recover
5.  Преобразование данных. Пакеты tidyr и plyr. [tidyr.pdf](../../assets/study/fall2016/intror/tidyr.pdf)
6.  Пакет lattice. Введение. [intro.R](../../assets/study/fall2009/intror/intro.r.txt)
7.  Пакет lattice. Изображение одномерных данных. [univariate.R](../../assets/study/fall2009/intror/univariate.r.txt)
8.  Пакет lattice. Изображение двумерных данных: скаттерплоты, матрицы скаттерплотов, parallel plot’ы. Стили линий и т.п.[xyplot.R](../../assets/study/fall2009/intror/xyplot.r.txt), [splom.R](../../assets/study/fall2009/intror/splom.r.txt), [parallel.R](../../assets/study/fall2009/intror/parallel.r.txt)
9.  Пакет lattice. Функции типа identify(). [lattice.identify.R](../../assets/study/fall2009/intror/lattice.identify.r.txt)
10. Системы рисования. Пакет ggplot [ggplot.zip](../../assets/study/fall2016/intror/ggplot.zip).
11. Преобразование данных. Пакет plyr
12. Метод наименьших квадратов. Линейная регрессия


## Prerequisites

 Дистрибутив R:

1.  [Windows](https://cran.r-project.org/bin/windows/base/)
2.  [Linux](http://cran.r-project.org/bin/linux)
3.  [MacOS X](http://cran.r-project.org/bin/macosx/)

Редакторы и оболочки:

1.  [R Studio (Windows, Linux, MacOS X)](http://www.rstudio.org)


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

- Task 1: 23:59 02.11
- Task 2: 23:59 22.11
- Task 3:

|                 |  Task 1  |        Task 2         |   Data    |
|:---------------:|:--------:|:---------------------:|:---------:|
|  Хромов Никита  |    \+    |          \+           | Airlines  |
| Олейник Михаил  |    \+    |          \+           |   ATUS    |
|  Потешкин Егор  |    \+    |          \+           |  Crimes   |
| Филатова Арина  |    \+    |          \+           |    UFO    |
|  Кахидзе Элэнэ  |    \+    | 2 (04.12.2022, 14:16) |   IMDB    |
| Подлеснов Яков  |    \+    |          *+          | RoadCrash |
| Булгакова Дарья |    \+    |          \+           |   STAR    |
|   Салова Яна    |    \+    |          \+           |    SES    |
| Киселев Михаил  | [chickweight.txt](../../assets/study/fall2022/intror/chickweight.txt) |       [8](../../assets/study/fall2022/intror/task2-8.pdf)        |           |


## Разное


1.  [Intro to R](http://www.youtube.com/playlist?list=PLOU2XLYxmsIK9qQfztXeybpHvru-TrqAP)

[^1]: сентябрь-декабрь