---
title: "Спецкурс «Выч. методы и пакеты в статистическом исследовании» (4 курс)"
---

**Место и время проведения:** 3 пара, ауд 2446; 4-5 пары, ауд 4526   

**Преподаватель:** Коробейников Антон Иванович   

**Преподаватель:** Шлемов Александр Юрьевич   

----

## Программа курса
### Темы состоявшихся занятий
  - Введение. Краткий обзор. Базовые операции: понятие "workspace", присваивание, просмотр списка переменных, удаление переменных из workspace'а. Функции c() и seq(). Использование встроенной справки. * (09.02.2011) *
  - Объекты R. Общие свойства (mode, length). Основные типы объектов: vector, matrix, data frame, list, expression. Конверсия объектов друг в друга. * (09.02.2011) *
  - Основные операции (арифметика, логические операции). Проверка равенства (==, identical, all.equal). Индексирование "векторных" переменных (включая именованные индексы). * (09.02.2011) *
  - Вызов функций. Правила передачи аргументов. Аргументы по умолчанию. Ellipsis (...) operator. * (16.02.2011) *
  - Чтение и запись данных из файла. Функции scan, read.table, write.table и пр. * (16.02.2011) *
  - Основные встроенные "скалярные" функции: sum, prod, max, min, which.max, which.min, range, length * (16.02.2011) *
  - Основные встроенные "векторные" функции: round, rev, sort, rank, scale, pmin, pmax, cum{sum, prod, min, max}, diff, match, which * (16.02.2011, частично) *
  - Операции с матрицами: cbind, rbind, t, diag, solve, qr, eigen, svd. * (16.02.2011) *
  - Функции над блоками данных: lapply, sapply, replicate. * (02.03.2011) *
  - Графические устройства (функции dev.*). Разбиение устройства на блоки. Понятие о графических параметрах. * (02.03.2011) *
  - Высокоуровневые графические функции: plot, curve, pairs, density. * (02.03.2011) *
  - Низкоуровневые графические функции: points, line, axis, legend. * (02.03.2011) *
  - Распределения. Функции распределения, плотности. Моделирование. Функции “d”, “p”, “q”, “r”. Функция sample. * (02.03.2011) *
  - Отладка. Функции debug, browser, traceback. * (09.03.2011) *
  - Векторизация. Эффективная работа с памятью.  * (09.03.2011) *
  - Нахождение (локальных) экстремумов функций.  * (09.03.2011) *

### Темы будущих занятий
### Задачи
  - Вычисление стационарного распределения марковской цепи.  * (Problem 0, 09.03.2011) *
  - Моделирование. Адаптивный метод отбора.  * (Problem 1, 09.03.2011) *
  - Вычисление интеграла методом Монте-Карло. * (Problem 2, 23.03.2011) *
  - Оценки максимального правдоподобия.  * (Problem 3, 23.03.2011) *
  - EM-алгоритм. Построение ОМП для смеси нормально распределенных случайных величин.  * (Problem 4, 30.03.2011) *
  - Support Vector Machines. * (Problem 5, 06.04.2011) *
  - Линейная регрессия. * (Problem 6, 13.04.2011) *
  - Кластерный анализ. * (Problem 7, 20.04.2011) *
  - Нейронные сети. * (Problem 8, 27.04.2011) *
  - Метод Гусеница-SSA. * (Problem 9, 04.05.2011) *
  - Деревья классификации и регрессии. Методы улучшения классификаторов. Bagging. Boosting. Алгоритм AdaBoost. * (Problem 10, 11.05.2011) *


### (Возможные) будущие задачи
  - Моделирование. Markov Chain Monte-Carlo. Метод Метрополиса-Хастингса. Метод Гиббса.
  - Логистическая и нелинейная регрессия
  - Планирование эксперимента
  - ...


## Prerequisites
Дистрибутив R:
  - [Windows](http://cran.r-project.org/bin/windows/base/R-2.12.1-win.exe)
  - [Linux](http://cran.r-project.org/bin/linux)
  - [MacOS X](http://cran.r-project.org/bin/macosx/)
  - [Revolution-R](http://info.revolutionanalytics.com/free-academic.html)
Редакторы и оболочки:
  - [Tinn-R (Windows)](http://www.sciviews.org/Tinn-R/)
  - [SciViews-K (Windows, Linux, MacOS X)](http://www.sciviews.org/SciViews-K/index.html)
  - [RKWard (Linux)](http://rkward.sourceforge.net/)

## Рекомендуемая литература
### Книги
  - **Peter Dalgaard**. *Introductory Statistics with R*. Springer, 2002.
  - **John Maindonald and John Braun**. *Data Analysis and Graphics Using R*. Cambridge University Press, Cambridge, 2003.
  - **John Verzani**. *Using R for Introductory Statistics*. Chapman & Hall/CRC, Boca Raton, FL, 2005.
  - **Paul Murrell**. *R Graphics*. Chapman & Hall/CRC, Boca Raton, FL, 2005. 
  - **Ермаков С.М.** *Статистическое моделирование, часть II* [PDF](../../assets/study/books/mmm_part2.pdf)
  - **Голяндина Н.Э.** *Метод «Гусеница»-SSA: анализ временных рядов*: Учеб. пособие. СПб: Изд-во СПбГУ, 2004. 76 с.[PDF](http://www.gistatgroup.com/gus/ssa_an.pdf)


### Статьи
  - **John Maindonald**. *Using R for Data Analysis and Graphics - Introduction, Examples and Commentary*. [PDF](http://cran.r-project.org/doc/contrib/usingR.pdf)
  - **John Verzani**. *Simple R*.  [PDF](http://cran.r-project.org/doc/contrib/Verzani-SimpleR.pdf)
  - **Petra Kuhnert and Bill Venables**. *An Introduction to R: Software for Statistical Modelling & Computing*. [ZIP](http://cran.r-project.org/doc/contrib/Kuhnert+Venables-R_Course_Notes.zip) 
  - **David Rossiter**. *Introduction to the R Project for Statistical Computing for Use at the ITC*. [PDF](http://cran.r-project.org/doc/contrib/Rossiter-RIntro-ITC.pdf)
  - **Е.М. Балдин, А.И. Коробейников, А.Б. Шипунов** *Анализ данных с R* [www](http://www.inp.nsk.su/~baldin/DataAnalysis/)
  - **А.И. Коробейников** *Оценки максимального правдоподобия в условиях цензурирования на базе EM-алгоритма* [PDF](../../assets/study/spring2008/em.pdf)
  - **Patrick Burns** *The R Inferno* [PDF](http://www.burns-stat.com/pages/Tutor/R_inferno.pdf)
  - **Patrick Burns** *S Poetry* [PDF](http://www.burns-stat.com/pages/Spoetry/Spoetry.pdf)


## Задачи
Условные обозначения:
  - Решетка - задание запрошено и выдано, плюс - зачтено, звездочка - штраф, минус - хм, незачет 
Кроме того, пишется дата и время.

|  | 0 | [1](../../assets/study/spring2011/compstat/simulation.pdf) | [2](../../assets/study/spring2011/compstat/integral.pdf) | [3](../../assets/study/spring2011/compstat/mle.pdf) | [4](../../assets/study/spring2011/compstat/mclust.pdf) | 5 | [6](../../assets/study/spring2011/compstat/regression.pdf) | [7](../../assets/study/spring2011/compstat/clust.pdf) | 8 | [9](../../assets/study/spring2011/compstat/ssa.pdf) | 10* | Penalty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Бояров Андрей | + | 8 | 2 | 15 | + | + |  | + | + | + | + | 30% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Галиаскарова Наталья | + | 9 | + | 16 | + | + |  | + | + | 4 |  | 40% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Горбунова Ирина | + | + | + | + | + | + | + | + | + | 15 | + | 0% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Притыковская Наталья | + | + | + | + | + | + | + | + | + | + | + | -10% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Сенов Александр | + | 15 | + | + | + | + | + | + | + | + | + | 0% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Сукманская Ксения | + | 14 | + | 20 | + | + | + | + | + | 5 | + | 20% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Векличева Марья | + | + | + | + | + | + | + | + | + | + | + | -10% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Портянко Иван | + | + | + | + | + | + | + | + | + | + | + | -10% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |


|  | 0 | [1](../../assets/study/spring2011/compstat/simulation.pdf) | [2](../../assets/study/spring2011/compstat/integral.pdf) | [3](../../assets/study/spring2011/compstat/mle.pdf) | [4](../../assets/study/spring2011/compstat/mclust.pdf) | 5 | [6](../../assets/study/spring2011/compstat/regression.pdf) | [7](../../assets/study/spring2011/compstat/clust.pdf) | 8 | [9](../../assets/study/spring2011/compstat/ssa.pdf) | 10* | Penalty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Губанов Сергей | + | + | + | + | + | + | + | + |  | 11 |  | 20% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Жукова Екатерина | + | + | + | + | + | + | + | + | + | + | + | -10% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Сыров Денис | + | + | + | + | + | + | + | + | + | + |  | 0% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Бойченко Алексей | + | + | + | + | + | + |  | 11 |  | 12 |  | 

40%

 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Чернышев Виталий | + | + | + | + | + | [glaucomam.zip](../../assets/study/spring2010/compstat/svm/glaucomam.zip) |  | 3 |  | 13 |  | 

50%

 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Яковлева Юлия | + | + | + | + | + | + |  | + |  | + |  | 20% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Золкин Никита | + | 6 | + | 2 | 1, [2dn.txt](../../assets/study/spring2010/compstat/2dn.txt) | + | + | + | + | + | + | 20% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Гольдвирт Серафима | + | + | 17 | + | + | + |  | + |  | + |  | 30% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Булович Надежда | + | + | + | + | + | + |  | + |  | 1 |  | 30% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |


** Внимание:** Если напротив Вашей фамилии отсутствует назначенное задание, то для его получения Вам следует отправить запрос по почте.


## Разное
Список рассылки: [http://groups.google.com/a/statmod.ru/group/r-spring-2011](http://groups.google.com/a/statmod.ru/group/r-spring-2011)