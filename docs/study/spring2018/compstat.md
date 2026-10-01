---
title: "422 гр., все. Спецкурс «Выч. методы и пакеты в статистическом исследовании» (4 курс)"
---

 **Место и время проведения:** вторник, 3 пара, ауд 2414; 4 пара, ауд 2414  
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


1.  Вычисление интеграла методом Монте-Карло (до 13.03 включительно)
2.  Оценки максимального правдоподобия (до 20.03 включительно)
3.  Моделирование. Адаптивный метод отбора (до 27.03 включительно)
4.  EM-алгоритм. Построение ОМП для смеси нормально распределенных случайных величин (до 03.04 включительно)
5.  [Support Vector Machines](../../assets/study/spring2018/compstat/svm.pdf) (до 10.04 включительно)


### (Возможные) будущие задачи


1.  Бутстреп
2.  Вычисление стационарного распределения марковской цепи
3.  Метод Гусеница-SSA
4.  Проверка статистических гипотез
5.  Кластерный анализ
6.  Нейронные сети
7.  Деревья классификации и регрессии. Методы улучшения классификаторов. Bagging. Boosting. Алгоритм AdaBoost
8.  Моделирование. Markov Chain Monte-Carlo. Метод Метрополиса-Хастингса. Метод Гиббса.
9.  Логистическая и нелинейная регрессия
10. Планирование эксперимента
11. Hidden Markov Models
12. …


## Prerequisites

 Дистрибутив R:

1.  [Windows](http://cran.r-project.org/bin/windows/base/R-3.4.3-win.exe)
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

** Внимание:** Если напротив Вашей фамилии отсутствует назначенное задание, то для его получения Вам следует отправить запрос по почте.

|                     | [Integral](../../assets/study/spring2018/compstat/integral.pdf) | [MLE](../../assets/study/spring2018/compstat/mle.pdf) | [Modelling](../../assets/study/spring2018/compstat/modelling.pdf) | [EM](../../assets/study/spring2018/compstat/em.pdf) | SVM | Итого |
|:-------------------:|:---------|:--------:|:--------:|:--------:|:---:|------:|
| Романова Елизавета  | \+       |    \+    |    \+    |    \+    | -  |   4/5 |
|     Лунев Иван      | \+       |    \+    |    \+    |    \+    | \+  |   5/5 |
| Рукавишникова Анна  | \+       |    \+    |    \+    |    \+    | -  |   4/5 |
|     Кароль Петр     | -       |    \+    |    \+    |    -    | \+  |   3/5 |
|  Страшко Владислав  | \+       |    \+    |    -    |    \+    | \+  |   4/5 |
|   Зенкова Наталья   | \+       |    \+    |    -    |    \+    | \+  |   4/5 |
|   Мийоски Антоний   | -       |    -    |    -    |    -    | -  |   0/5 |
|   Торбеева Ольга    | -       |    \+    |    \+    |    \+    | \+  |   4/5 |
| Ставинова Елизавета | \+       |    \+    |    \+    |    \+    | \+  |   5/5 |
|   Федоров Никита    | -       |    -    |    \+    |    \+    | \+  |   3/5 |

|                       | [Integral](../../assets/study/spring2018/compstat/integral.pdf) | [MLE](../../assets/study/spring2018/compstat/mle.pdf) | [Modelling](../../assets/study/spring2018/compstat/modelling.pdf) | [EM](../../assets/study/spring2018/compstat/em.pdf) | SVM | Итого |
|:---------------------:|:--------:|:--------:|:--------:|:--------:|:---:|------:|
|     Быков Кирилл      |    \+    |    \+    |    \+    |    \+    | \+  |   5/5 |
|     Мейер Никита      |    \+    |    \+    |    \+    |    \+    | \+  |   5/5 |
|   Понизова Вероника   |    \+    |    \+    |    -    |    \+    | \+  |   4/5 |
| Третьякова Александра |    \+    |    \+    |    \+    |    \+    | \+  |   5/5 |
|    Ольга Крютченко    |    -    |    \+    |    -    |    \+    | \+  |   3/5 |
|     Зуйкова Алиса     |    \+    |    \+    |    \+    |    \+    | \+  |   5/5 |
|   Федорченко Сергей   |    \+    |    -    |    -    |    -    | -  |   1/5 |
|     Родигин Юрий      |    \+    |    \+    |    -    |    \+    | -  |   3/5 |
|  Волканова Маргарита  |    \+    |    \+    |    \+    |    \+    | -  |   4/5 |
| Бакшинская Екатерина  |    \+    |    \+    |    \+    |    \+    | \+  |   5/5 |