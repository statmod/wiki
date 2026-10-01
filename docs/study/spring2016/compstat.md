---
title: "Спецкурс «Выч. методы и пакеты в статистическом исследовании» (4 курс)"
---

**Место и время проведения:** вторник, 3 пара, ауд 2412; 4 пара, ауд 2412  
**Преподаватель:** Коробейников Антон Иванович  
**Преподаватель:** Шлемов Александр Юрьевич  
—-

## Программа курса

### Задачи

1.  Вычисление интеграла методом Монте-Карло
2.  Оценки максимального правдоподобия
3.  EM-алгоритм. Построение ОМП для смеси нормально распределенных случайных величин
4.  Моделирование. Адаптивный метод отбора
5.  [Support Vector Machines](../../assets/study/spring2016/compstat/svm.pdf)

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

1.  [Windows](http://cran.r-project.org/bin/windows/base/R-3.2.3-win.exe)
2.  [Linux](http://cran.r-project.org/bin/linux)
3.  [MacOS X](http://cran.r-project.org/bin/macosx/)

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

1.  Решетка - задание выдано, плюс - зачтено, звездочка - штраф, минус - хм, незачет. Кроме того, пишется дата и время. Если вы отправляете задание по почте, то ) — означает, что Ваше решение в целом понравилось проверяющему, ? — означает, что прислано что-то разумное, но переписку следовало бы продолжить. \# — задание выдано.

** Внимание:** Если напротив Вашей фамилии отсутствует назначенное задание, то для его получения Вам следует отправить запрос по почте.

|              | [Integral](../../assets/study/spring2016/compstat/integral.pdf) | [MLE](../../assets/study/spring2016/compstat/mle.pdf) | [EM](../../assets/study/spring2016/compstat/em.pdf) | [Simulation](../../assets/study/spring2016/compstat/simulation.pdf) |   SVM    | Total   |
|:------------:|----------|----------|----------|----------|:--------:|---------|
|   Грязнов    | \+       | \+       | \+       | \+       |    \+    | 

5

 |
|  Жорникова   | \+       | \+       | \+       | \+       |    \+    | 

5

 |
|   Коврыга    | 24       | \+       | \+       | 11       |    \+    | 

3

 |
|   Куликов    | \+       | 11       | [2](../../assets/study/spring2016/compstat/ring.txt.gz) | \+       |    \+    | 

3

 |
|   Пимахов    | \+       | \+       | \+       | 15       |    \+    | 

4

 |
|   Суворов    | \+       | \+       | \+       | 12       | [hillvalley.zip](../../assets/study/spring2015/compstat/hillvalley.zip) | 

3

 |
|  Тихомиров   | \+       | 16       | \+       | \+       | [vehicle.zip](../../assets/study/spring2015/compstat/vehicle.zip) | 

3

 |
| Черниговская | \+       | \+       | \+       | 13       |    \+    | 

4

 |
|    Явейн     | \+       | \+       | \+       | \+       |    \+    | 

5

 |

|              | [Integral](../../assets/study/spring2016/compstat/integral.pdf) | [MLE](../../assets/study/spring2016/compstat/mle.pdf) | [EM](../../assets/study/spring2016/compstat/em.pdf) | [Simulation](../../assets/study/spring2016/compstat/simulation.pdf) |   SVM    | Total    |
|:------------:|----------|---------:|:--------:|----------|:--------:|----------|
|    Агеев     | \+       |       \+ |    \+    | \+       | [diabetis.zip](../../assets/study/spring2015/compstat/diabetis.zip) | 

4

  |
|   Белоусов   | \+       |       \+ |    \+    | 9        |    \+    | 

4

 |
| Гориславский | \+       |        3 |    \+    | \+       | [germany.zip](../../assets/study/spring2015/compstat/germany.zip) | 

3

 |
|  Григорьева  | \+       |        7 |    \+    | \+       | [glaucomam.zip](../../assets/study/spring2015/compstat/glaucomam.zip) | 

3

 |
| Корчажников  | \+       |        4 |    \+    | \+       | [glaucomamvf.zip](../../assets/study/spring2015/compstat/glaucomamvf.zip) | 

3

 |
|   Круглова   | \+       |        9 |    \+    | \+       | [ionosphere.zip](../../assets/study/spring2015/compstat/ionosphere.zip) | 

3

 |
|  Сальников   | \+       |       \+ |    \+    | \+       | [spect.zip](../../assets/study/spring2015/compstat/spect.zip) | 

4

 |
|  Ширинкина   | \+       |       12 |    \+    | \+       |    \+    | 

4

 |
