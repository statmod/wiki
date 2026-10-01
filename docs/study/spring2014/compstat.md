---
title: "Спецкурс «Выч. методы и пакеты в статистическом исследовании» (4 курс)"
---

 **Место и время проведения:** вторник, 3 пара, ауд TBA; 4-5 пары, ауд TBA  
**Преподаватель:** Коробейников Антон Иванович  
**Преподаватель:** Шлемов Александр Юрьевич  


---

## Программа курса


### Темы состоявшихся занятий


1.  Введение. Краткий обзор. Базовые операции: понятие “workspace”, присваивание, просмотр списка переменных, удаление переменных из workspace’а. Функции c() и seq(). Использование встроенной справки. // (11.02.2014) //
2.  Объекты R. Общие свойства (mode, length). Основные типы объектов: vector, matrix, data frame, list, expression. Конверсия объектов друг в друга. // (11.02.2014) //
3.  Основные операции (арифметика, логические операции). Проверка равенства (==, identical, all.equal). Индексирование “векторных” переменных (включая именованные индексы). // (11.02.2014) //
4.  Вызов функций. Правила передачи аргументов. Аргументы по умолчанию. Ellipsis (…) operator. Область видимости переменных. // (11.02.2014) //
5.  Чтение и запись данных из файла. Функции scan, read.table, write.table и пр. // (18.02.2014) //
6.  Основные встроенные “скалярные” функции: sum, prod, max, min, which.max, which.min, range, length // (18.02.2014) //
7.  Основные встроенные “векторные” функции: round, rev, sort, rank, scale, pmin, pmax, cum{sum, prod, min, max}, diff, match, which // (18.02.2014) //
8.  Операции с матрицами: cbind, rbind, t, diag, solve, qr, eigen, svd // (18.02.2014) //
9.  Функции над блоками данных: lapply, sapply, replicate // (18.02.2014) //
10. Графические устройства (функции dev.*). Разбиение устройства на блоки. Понятие о графических параметрах // (25.02.2014) //
11. Высокоуровневые графические функции: plot, curve, pairs, density // (25.02.2014) //
12. Низкоуровневые графические функции: points, line, axis, legend // (25.02.2014) //
13. Распределения. Функции распределения, плотности. Моделирование. Функции “d”, “p”, “q”, “r”. Функция sample // (25.02.2014) //
14. Отладка. Функции debug, browser, traceback // (25.02.2014) //
15. Векторизация. Эффективная работа с памятью // (25.02.2014) //
16. Нахождение (локальных) экстремумов функций // (25.02.2014) //


### Темы будущих занятий


### Задачи


1.  Вычисление стационарного распределения марковской цепи (Task 0)
2.  Вычисление интеграла методом Монте-Карло (Task 1)
3.  Моделирование. Адаптивный метод отбора (Task 2)
4.  Оценки максимального правдоподобия (Task 3)
5.  EM-алгоритм. Построение ОМП для смеси нормально распределенных случайных величин (Task 4)
6.  Support Vector Machines (Task 5)
7.  Метод Гусеница-SSA (Task 6)
8.  Бутстреп (Task 7)
9.  Линейные модели I (Task 8)
10. Линейные модели II (Task 9)


### (Возможные) будущие задачи


1.  Проверка статистических гипотез
2.  Кластерный анализ
3.  Нейронные сети
4.  Деревья классификации и регрессии. Методы улучшения классификаторов. Bagging. Boosting. Алгоритм AdaBoost
5.  Моделирование. Markov Chain Monte-Carlo. Метод Метрополиса-Хастингса. Метод Гиббса.
6.  Логистическая и нелинейная регрессия
7.  Планирование эксперимента
8.  Hidden Markov Models
9.  …


## Prerequisites

 Дистрибутив R:

1.  [Windows](http://cran.r-project.org/bin/windows/base/R-3.0.2-win.exe)
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

1.  Решетка - задание выдано, плюс - зачтено, звездочка - штраф, минус - хм, незачет. Кроме того, пишется дата и время. Если вы отправляете задание по почте, то ) — означает, что Ваше решение в целом понравилось проверяющему, ? — означает, что прислано что-то разумное, но переписку следовало бы продолжить.

** Внимание:** Если напротив Вашей фамилии отсутствует назначенное задание, то для его получения Вам следует отправить запрос по почте.

|  | Task 0 | [Task 1](../../assets/study/spring2014/compstat/task1.pdf) | [Task 2](../../assets/study/spring2014/compstat/task2.pdf) | [Task 3](../../assets/study/spring2014/compstat/task3.pdf) | [Task 4](../../assets/study/spring2014/compstat/task4.pdf) | Task 5 | [Task 6](../../assets/study/spring2014/compstat/ssa.pdf) | Task 7 | Task 8 | Task 9 | Penalty |
|:--:|----|----|----|----|:--:|:--:|----|----|----|:--:|----|
| Андреев | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

0%

 |
| Звонарев | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

0%

 |
| Кипрушкин | \+ | \+ | 12 | 18 | \+ | \+ | \+ | \# | \+ | [uwgs.txt](../../assets/study/spring2014/compstat/uswages.txt) | 

40%

 |
| Куликов | \+ | \+ | \+ | \+ | [2, banknote.txt](../../assets/study/spring2014/compstat/banknote.txt) | [hillvalley.zip](../../assets/study/spring2013/compstat/hillvalley.zip) | 5 | \# | \# | [inss.txt](../../assets/study/spring2013/compstat/insectsprays.txt) | 

60%

 |
| Тарасов | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

0%

 |
| Федяева | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

0%

 |
| Багина | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

0%

 |
| Бородина | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

0%

 |
| Буракова | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \# | \# | [pul.txt](../../assets/study/spring2013/compstat/pulp.txt) | 

30%

 |
| Волосенко | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

0%

 |
| Погосян | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

0%

 |
| Воеводская | \+ | \+ | \+ | 5 | [2, wreath2.txt](../../assets/study/spring2014/compstat/wreath.txt) | [ionosphere.zip](../../assets/study/spring2013/compstat/ionosphere.zip) | 8 | \# | \# | [uw.txt](../../assets/study/spring2014/compstat/uswages.txt) | 

70%

 |

|  | Task 0 | [Task 1](../../assets/study/spring2014/compstat/task1.pdf) | [Task 2](../../assets/study/spring2014/compstat/task2.pdf) | [Task 3](../../assets/study/spring2014/compstat/task3.pdf) | [Task 4](../../assets/study/spring2014/compstat/task4.pdf) | Task 5 | [Task 6](../../assets/study/spring2014/compstat/ssa.pdf) | Task 7 | Task 8 | Task 9 | Penalty |
|:--:|----|----|----|----|:--:|:--:|---:|:--:|----|:--:|:--:|
| Яковлева | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

0%

 |
| Калашникова | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

0%

 |
| Смирнова | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

0%

 |
| Абдрахманов | \+ | \+ | \+ | \+ | \+ | [ozone1.zip](../../assets/study/spring2013/compstat/ozone1.zip) | \+ | \+ | \+ | \+ | 

10%

 |
| Шувалов | \+ | \+ | \+ | 6 | \+ | [ozone2.zip](../../assets/study/spring2013/compstat/ozone2.zip) | 13 | \# | \# | [plp.txt](../../assets/study/spring2013/compstat/pulp.txt) | 

60%

 |
| Грицай | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

0%

 |
| Просвирнина | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

0%

 |
| Севастьянова | \+ | \+ | \+ | \+ | [2, tn2.txt](../../assets/study/spring2014/compstat/tn.txt) | [spect.zip](../../assets/study/spring2013/compstat/spect.zip) | 7 | \# | \# | [ins.txt](../../assets/study/spring2013/compstat/insectsprays.txt) | 

60%

 |
| Тихомиров | \+ | \+ | \+ | 3 | \+ | \+ | \+ | \# | \# | [pg.txt](../../assets/study/spring2013/compstat/plantgrowth.txt) | 

40%

 |
| Сорокин | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

0%

 |
| Артишевская | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | 

0%

 |