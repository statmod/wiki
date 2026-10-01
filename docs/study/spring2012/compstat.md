---
title: "Спецкурс «Выч. методы и пакеты в статистическом исследовании» (4 курс)"
---

 **Место и время проведения:** 3 пара, ауд 4399; 4-5 пары, ауд 2414/1412  
**Преподаватель:** Коробейников Антон Иванович  
**Преподаватель:** Шлемов Александр Юрьевич  


---

## Программа курса


### Темы состоявшихся занятий


1.  Введение. Краткий обзор. Базовые операции: понятие “workspace”, присваивание, просмотр списка переменных, удаление переменных из workspace’а. Функции c() и seq(). Использование встроенной справки. // (15.02.2012) //
2.  Объекты R. Общие свойства (mode, length). Основные типы объектов: vector, matrix, data frame, list, expression. Конверсия объектов друг в друга. // (15.02.2012) //
3.  Основные операции (арифметика, логические операции). Проверка равенства (==, identical, all.equal). Индексирование “векторных” переменных (включая именованные индексы). // (15.02.2012) //
4.  Вызов функций. Правила передачи аргументов. Аргументы по умолчанию. Ellipsis (…) operator. Область видимости переменных // (15.02.2012) //
5.  Чтение и запись данных из файла. Функции scan, read.table, write.table и пр. // (22.02.2012) //
6.  Основные встроенные “скалярные” функции: sum, prod, max, min, which.max, which.min, range, length // (22.02.2012) //
7.  Основные встроенные “векторные” функции: round, rev, sort, rank, scale, pmin, pmax, cum{sum, prod, min, max}, diff, match, which // (22.02.2012) //
8.  Операции с матрицами: cbind, rbind, t, diag, solve, qr, eigen, svd // (22.02.2012) //
9.  Функции над блоками данных: lapply, sapply, replicate // (22.02.2012) //
10. Графические устройства (функции dev.*). Разбиение устройства на блоки. Понятие о графических параметрах // (29.02.2012) //
11. Высокоуровневые графические функции: plot, curve, pairs, density // (29.02.2012) //
12. Низкоуровневые графические функции: points, line, axis, legend // (29.02.2012) //
13. Распределения. Функции распределения, плотности. Моделирование. Функции “d”, “p”, “q”, “r”. Функция sample // (29.02.2012) //
14. Отладка. Функции debug, browser, traceback // (29.02.2012) //
15. Векторизация. Эффективная работа с памятью // (29.02.2012) //
16. Нахождение (локальных) экстремумов функций // (14.03.2012) //


### Темы будущих занятий


### Задачи


1.  Вычисление стационарного распределения марковской цепи // (29.02.2012) //
2.  Вычисление интеграла методом Монте-Карло // (07.03.2012) //
3.  Оценки максимального правдоподобия // (14.03.2012) //
4.  EM-алгоритм. Построение ОМП для смеси нормально распределенных случайных величин // (21.03.2012) //
5.  Support Vector Machines // (28.03.2012) //
6.  Линейные модели I // (04.04.2012) //
7.  Линейные модели II // (11.04.2012) //
8.  Бутстреп // (18.04.2012) //
9.  Моделирование. Адаптивный метод отбора // (25.04.2012) //
10. Метод Гусеница-SSA // (03.05.2012) //


### (Возможные) будущие задачи


1.  Проверка статистических гипотез
2.  Кластерный анализ
3.  Нейронные сети
4.  Деревья классификации и регрессии. Методы улучшения классификаторов. Bagging. Boosting. Алгоритм AdaBoost
5.  Моделирование. Markov Chain Monte-Carlo. Метод Метрополиса-Хастингса. Метод Гиббса.
6.  Логистическая и нелинейная регрессия
7.  Планирование эксперимента
8.  …


## Prerequisites

 Дистрибутив R:

1.  [Windows](http://cran.r-project.org/bin/windows/base/R-2.14.1-win.exe)
2.  [Linux](http://cran.r-project.org/bin/linux)
3.  [MacOS X](http://cran.r-project.org/bin/macosx/)
4.  [Revolution-R](http://info.revolutionanalytics.com/free-academic.html)

Редакторы и оболочки:

1.  [R-Studio (Windows, Linux, MacOS X)](http://rstudio.org/download/)
2.  [Tinn-R (Windows)](http://www.sciviews.org/Tinn-R/)
3.  [RKWard (Linux)](http://rkward.sourceforge.net/)


## Рекомендуемая литература

 

### Книги


1.  **Peter Dalgaard**. *Introductory Statistics with R*. Springer, 2002.
2.  **John Maindonald and John Braun**. *Data Analysis and Graphics Using R*. Cambridge University Press, Cambridge, 2003.
3.  **John Verzani**. *Using R for Introductory Statistics*. Chapman & Hall/CRC, Boca Raton, FL, 2005.
4.  **Paul Murrell**. *R Graphics*. Chapman & Hall/CRC, Boca Raton, FL, 2005.
5.  **Ермаков С.М.** *Статистическое моделирование, часть II* [PDF](../../assets/study/books/mmm_part2.pdf)
6.  **Голяндина Н.Э.** *Метод «Гусеница»-SSA: анализ временных рядов*: Учеб. пособие. СПб: Изд-во СПбГУ, 2004. 76 с.[PDF](http://www.gistatgroup.com/gus/ssa_an.pdf)
7.  **Шипунов А.Б., Балдин Е.М., Волкова П.А., Коробейников А.И., Назарова С.А., Петров С.В., Суфиянов В.Г.** Наглядная статистика. Используем R! – М.: ДМК Пресс, 2012. – 298 с.


### Статьи


1.  **John Maindonald**. *Using R for Data Analysis and Graphics - Introduction, Examples and Commentary*. [PDF](http://cran.r-project.org/doc/contrib/usingR.pdf)
2.  **John Verzani**. *Simple R*. [PDF](http://cran.r-project.org/doc/contrib/Verzani-SimpleR.pdf)
3.  **Petra Kuhnert and Bill Venables**. *An Introduction to R: Software for Statistical Modelling & Computing*. [ZIP](http://cran.r-project.org/doc/contrib/Kuhnert+Venables-R_Course_Notes.zip)
4.  **David Rossiter**. *Introduction to the R Project for Statistical Computing for Use at the ITC*. [PDF](http://cran.r-project.org/doc/contrib/Rossiter-RIntro-ITC.pdf)
5.  **Е.М. Балдин, А.И. Коробейников, А.Б. Шипунов** *Анализ данных с R* [www](http://www.inp.nsk.su/~baldin/DataAnalysis/)
6.  **А.И. Коробейников** *Оценки максимального правдоподобия в условиях цензурирования на базе EM-алгоритма* [PDF](../../assets/study/spring2008/em.pdf)
7.  **Patrick Burns** *The R Inferno* [PDF](http://www.burns-stat.com/pages/Tutor/R_inferno.pdf)
8.  **Patrick Burns** *S Poetry* [PDF](http://www.burns-stat.com/pages/Spoetry/Spoetry.pdf)


## Задачи


Условные обозначения:

1.  Решетка - задание выдано, плюс - зачтено, звездочка - штраф, минус - хм, незачет. Кроме того, пишется дата и время.

|  | 0 | [1](../../assets/study/spring2012/compstat/task1.pdf) | [2](../../assets/study/spring2012/compstat/task2.pdf) | [3](../../assets/study/spring2012/compstat/task3.pdf) | 4 | 5 | 6 | 7 | [8](../../assets/study/spring2011/compstat/simulation.pdf) | [9](../../assets/study/spring2012/compstat/ssa.pdf) | Penalty |
|:--:|----|----|----|:--:|:--:|----|:--:|----|:--:|:---|----|
| Ломтев Максим | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \# | 8 | 6 | 

30%

 |
| Плотников Павел | \+ | \+ | \+ | \+ | \+ | \+ | [toothgrowth.txt](../../assets/study/spring2012/compstat/toothgrowth.txt) | \# | 9 | 11 | 

40%

 |
| Раевская Ксения | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \# | 11 | 12 | 

30%

 |
| Романов Егор | \+ | \+ | \+ | \+ | [echocardiogram.zip](../../assets/study/spring2012/compstat/echocardiogram.zip) | \+ | \+ | \# | 12 | 13 | 

40%

 |
| Скурат Евгения | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 13 | \+ | 

10%

 |
| Советкин Евгений | \+ | \+ | \+ | 1.5, [faithful.txt](../../assets/study/spring2012/compstat/faithful.txt) | \+ | \+ | \+ | \+ | \+ | \+ | 

10%

 |
| Уфлянд Анна | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 15 | \+ | 

10%

 |
| Федоренко Кристина | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 14 | \+ | 

10%

 |
| Матушкина Ольга | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \# | \+ | \+ | 

10%

 |
| Чернышев Виталий | \+ | 13 | 12 | 1, [2dn2.txt](../../assets/study/spring2012/compstat/2dn2.txt) | [postoperative.zip](../../assets/study/spring2012/compstat/postoperative.zip) | \# | [twins.txt](../../assets/study/spring2012/compstat/twins.txt) | \# | 10 | 17 | 

90%

 |

|  | 0 | [1](../../assets/study/spring2012/compstat/task1.pdf) | [2](../../assets/study/spring2012/compstat/task2.pdf) | [3](../../assets/study/spring2012/compstat/task3.pdf) | 4 | 5 | 6 | 7 | [8](../../assets/study/spring2011/compstat/simulation.pdf) | [9](../../assets/study/spring2012/compstat/ssa.pdf) | Penalty |
|:--:|----|----|----|:--:|:--:|----|:--:|----|----|---:|----|
| Афанасьев Михаил | \+ | \+ | \+ | 1, [vdata.txt](../../assets/study/spring2012/compstat/vdata.txt) | [hillvalley.zip](../../assets/study/spring2012/compstat/hillvalley.zip) | \# | [insectsprays.txt](../../assets/study/spring2012/compstat/insectsprays.txt) | \# | 7 | 6 | 

70%

 |
| Богдан Владимир | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \# | 

10%

 |
| Влох Дмитрий | \+ | \+ | \+ | \+ | [germany.zip](../../assets/study/spring2012/compstat/germany.zip) | \# | [uswages.txt](../../assets/study/spring2012/compstat/uswages.txt) | \# | 6 | 8 | 

60%

 |
| Горлова Марина | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

0%

 |
| Степаненко Илья | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 10 | 

10%

 |
| Вьюшкова Евгения | \+ | \+ | \+ | \+ | \+ | \# | \+ | \+ | 3 | 4 | 

30%

 |
| Пеунова Таисия | \+ | \+ | \+ | \+ | \+ | \# | [twins.txt](../../assets/study/spring2012/compstat/twins.txt) | \+ | 2 | \+ | 

30%

 |
| Степанян Адраник | \+ | \+ | 6 | 2, [vdata.txt](../../assets/study/spring2012/compstat/vdata.txt) | [wine.zip](../../assets/study/spring2012/compstat/wine.zip) | \# | [twins.txt](../../assets/study/spring2012/compstat/twins.txt) | \# | 7 | 17 | 

80%

 |

** Внимание:** Если напротив Вашей фамилии отсутствует назначенное задание, то для его получения Вам следует отправить запрос по почте.