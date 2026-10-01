---
title: "Кружок «Интеллектуальный анализ данных» (1, 2, 3... курс)"
---

**Место и время проведения:** среда, пятая пара (17:10-18:45), ауд. 4399 [группа vk](https://vk.com/sm_idata)  
**Преподаватель:** Шлемов Александр Юрьевич  
**Преподаватель:** Коробейников Антон Иванович  
—-

## Темы

1.  Распознавание 0 и 1. [Сами MNIST](http://yann.lecun.com/exdb/mnist/) и [материалы к занятию](https://drive.google.com/file/d/0B5lhltGu1FQaclo2Q25zelh1ZlU/view?usp=sharing). Исходно MNIST выложены в довольно странном формате, но я его уже почитал и пересохранил данные в формате RDA (внутренний формат R). Файл лежит в архиве

Задание:  
* Установить R, запустить пример. Может потребоваться установка дополнительных пакетов (latticeExtra), установите его с помощью \`install.packages(“latticeExtra”)\`

- Придумать 3 собственных признака, потенциально отличающих 0 от 1. Реализовать их (добавить в код) и проверить, как хорошо они разделяют данные
- (*) Попробовать каким-то образом совместить несколько признаков и улучшить результат

## Язык R

### Дистрибутивы

1.  [R](https://cran.r-project.org/bin/windows/base/)
2.  [R Studio](https://www.rstudio.com/products/rstudio/)

### Литература

#### Основная

1.  [Шипунов А.Б., Балдин Е.М., Волкова П.А., Коробейников А.И., Назарова С.А., Петров С.В., Суфиянов В.Г. "Наглядная статистика. Используем R!"](http://herba.msu.ru/shipunov/school/books/rbook.pdf) — Отличное введение в статистику и анализ данных с примерами на R
2.  [Hadley Wickham: "Advanced R"](http://adv-r.had.co.nz/) — Достаточно краткое, но исчерпывающее руководство от очень известного R-гуру, автора множества пакетов

#### Дополнительная

1.  [Joseph Adler: "R in a nutshell"](http://web.udl.es/Biomath/Bioestadistica/R/Manuals/r_in_a_nutshell.pdf) — Большая книга по языку R, среднего уровня для среднего читателя. Я больше рекомендую Hadley.
2.  [Patrick Burns: "The R Inferno"](http://www.burns-stat.com/documents/books/the-r-inferno/) — “Ад R”, потенциальные ошибки при программировании на R и способы их избежать. Рекомендуется к чтению после некоторого опыта в R
3.  [Patrick Burns: "The S Poetry"](http://www.burns-stat.com/pages/Spoetry/Spoetry.pdf) — Книга от автора “The R Inferno”, еще про S. Немного устарела, но неплохо написана
4.  [Sarkar, Deepayan: "Lattice. Multivariate Data Visualization with R"](http://www.springer.com/978-0-387-75968-5) — Исчерпывающий обзор графической системы “lattice” с примерами использования. Я в своих примерах использую именно lattice для рисования графиков
5.  [latticeExtra](http://latticeextra.r-forge.r-project.org/) — Пакет, расширяющий возможности стандартного lattice, я его много использую и крайне рекомендую
6.  [lattice](http://lattice.r-forge.r-project.org/) — Сайт графической системы lattice
7.  [ggplot2](http://ggplot2.org/) — Сайт графической системы ggplot2, альтернатива lattice
8.  [Winston Chang: "R Graphics Cookbook"](http://amzn.com/1449316956?tag=ggplot2-20) — Введение в ggplot и рецепты

#### Еще ресурсы

1.  **Peter Dalgaard**. *Introductory Statistics with R*. Springer, 2002.
2.  **John Maindonald and John Braun**. *Data Analysis and Graphics Using R*. Cambridge University Press, Cambridge, 2003.
3.  **John Verzani**. *Using R for Introductory Statistics*. Chapman & Hall/CRC, Boca Raton, FL, 2005.
4.  **Paul Murrell**. *R Graphics*. Chapman & Hall/CRC, Boca Raton, FL, 2005.
5.  **John Maindonald**. *Using R for Data Analysis and Graphics - Introduction, Examples and Commentary*. [PDF](http://cran.r-project.org/doc/contrib/usingR.pdf)
6.  **John Verzani**. *Simple R*. [PDF](http://cran.r-project.org/doc/contrib/Verzani-SimpleR.pdf)
7.  **Petra Kuhnert and Bill Venables**. *An Introduction to R: Software for Statistical Modelling & Computing*. [ZIP](http://cran.r-project.org/doc/contrib/Kuhnert+Venables-R_Course_Notes.zip)
8.  **David Rossiter**. *Introduction to the R Project for Statistical Computing for Use at the ITC*. [PDF](http://cran.r-project.org/doc/contrib/Rossiter-RIntro-ITC.pdf)
9.  **Е.М. Балдин, А.И. Коробейников, А.Б. Шипунов** *Анализ данных с R* [www](http://www.inp.nsk.su/~baldin/DataAnalysis/)
