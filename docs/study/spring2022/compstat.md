---
title: "422 гр., все. Спецкурс «Выч. методы и пакеты в статистическом исследовании»"
---

 **Место и время проведения:** вторник, 3 пара, ауд 2406; 4 пара, ауд 2406  
**Преподаватель:** Коробейников Антон Иванович  
**Преподаватель:** Звонарев Никита Константинович  


---

## Программа курса


### Базовый R


      - Базовые операции: понятие "workspace", присваивание, просмотр списка переменных, удаление переменных из workspace'а. Функции c() и seq(). Использование встроенной справки.
      - Объекты R. Общие свойства (mode, length). Основные типы объектов: vector, matrix, data frame, list, expression. Конверсия объектов друг в друга.
      - Основные операции (арифметика, логические операции). Проверка равенства (==, identical, all.equal). Индексирование "векторных" переменных (включая именованные индексы).
      - Вызов функций. Правила передачи аргументов. Аргументы по умолчанию. Ellipsis (...) operator. Область видимости переменных.
      - Чтение и запись данных из файла. Функции scan, read.table, write.table и пр.
      - Основные встроенные "скалярные" функции: sum, prod, max, min, which.max, which.min, range, length
      - Основные встроенные "векторные" функции: round, rev, sort, rank, scale, pmin, pmax, cum{sum, prod, min, max}, diff, match, which
      - Операции с матрицами: cbind, rbind, t, diag, solve, qr, eigen, svd
      - Функции над блоками данных: lapply, sapply, replicate
      - Графические устройства (функции dev.*). Разбиение устройства на блоки. Понятие о графических параметрах
      - Высокоуровневые графические функции: plot, curve, pairs, density
      - Низкоуровневые графические функции: points, line, axis, legend
      - Распределения. Функции распределения, плотности. Моделирование. Функции “d”, “p”, “q”, “r”. Функция sample
      - Отладка. Функции debug, browser, traceback
      - Векторизация. Эффективная работа с памятью
      - Нахождение (локальных) экстремумов функций


### Задачи


1.  Вычисление интеграла методом Монте-Карло (до 15.03 включительно)
2.  Оценки максимального правдоподобия (до 22.03 включительно)
3.  Моделирование. Адаптивный метод отбора (до 29.03 включительно)
4.  EM-алгоритм. Построение ОМП для смеси нормально распределенных случайных величин (до 11.04 включительно)
5.  Моделирование. Markov Chain Monte-Carlo. Метод Метрополиса-Хастингса (до 26.04 включительно)


## (Возможные) будущие задачи


1.  Support Vector Machines
2.  Бутстреп
3.  Вычисление стационарного распределения марковской цепи
4.  Метод Гусеница-SSA
5.  Проверка статистических гипотез
6.  Кластерный анализ
7.  Нейронные сети
8.  Деревья классификации и регрессии. Методы улучшения классификаторов. Bagging. Boosting. Алгоритм AdaBoost
9.  Логистическая и нелинейная регрессия
10. Планирование эксперимента
11. Hidden Markov Models
12. …


## Prerequisites

 Дистрибутив R:

1.  [Windows](http://cran.r-project.org/bin/windows/base/R-4.0.4-win.exe)
2.  [Linux](http://cran.r-project.org/bin/linux)
3.  [MacOS X](http://cran.r-project.org/bin/macosx/)

Редакторы и оболочки:

1.  [R-Studio (Windows, Linux, MacOS X)](http://rstudio.org/download/)


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


Условные обозначения: Решетка - задание выдано, плюс - зачтено, звездочка - штраф, минус - хм, незачет.

|                                | [MC](../../assets/study/spring2022/compstat/mc.pdf) | [MLE](../../assets/study/spring2022/compstat/mle.pdf) | [Modelling](../../assets/study/spring2022/compstat/modelling.pdf) | [EM](../../assets/study/spring2022/compstat/em.pdf) | [MCMC](../../assets/study/spring2022/compstat/mcmc.pdf) |
|--------------------------------|----------|:--------:|:---------|:--------:|:--------:|
| Пономаренко Артем Владимирович | \+       |    -    | ?        |    \+    |    \+    |
| Сенов Михаил Андреевич         | \+       |    \+    | -       |    \+    |    \+    |
| Глушков Игорь Андреевич        | -       |    ?     | -       |          |          |
| Попов Сергей Александрович     | \+       |    \+    | -       |    \+    |    \+    |
| Айнабеков Захар Андреевич      | \+       |    -    | -       |    \+    |    \+    |
| Ким Эрик Евгеньевич            | \+       |    \+    | \+       |    \+    |    \+    |
| Веселова Влада Валерьевна      | \+       |    \+    | \+       |    \+    |    \+    |
| Логинов Андрей Сергеевич       | \+       |    \+    | -       |    \+    |    \+    |
| Дядичкин Михаил Павлович       | -       |    -    | -       |          |          |
| Положиев Роман Игоревич        | \+       |    -    | -       |    \+    |    1     |
| Крашенинников Егор Иванович    | \+       |    \+    | -       |    \+    |    \+    |
| Григорьев Дмитрий Артемович    | \+       |    \+    | \+       |    \+    |    \+    |
| Васильцов Арсений              | \+       |    \+    | -       |          |          |

** Внимание:** Если напротив Вашей фамилии отсутствует назначенное задание, то для его получения Вам следует отправить запрос по почте.