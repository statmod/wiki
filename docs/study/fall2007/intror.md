---
title: "Спецкурс «Введение в обработку данных» (3 курс)"
---

**Место и время проведения:** четверг, вторая пара (11:15-12:50), ауд. 2444-II (дальняя).  
**Преподаватель:** Голяндина Нина Эдуардовна [^1]  
**Преподаватель:** Коробейников Антон Иванович [^2]  
—-

## Введение

FIXME

## Программа курса

//Курс в некотором смысле «экспериментальный»: программа может (и будет) менятся во время семестра //

### Темы состоявшихся занятий

1.  Введение. Краткий обзор. Базовые операции: понятие “workspace”, присваивание, просмотр списка переменных, удаление переменных из workspace’а. Функции c() и seq(). Использование встроенной справки. *(27.09.2007)*
2.  Объекты R. Общие свойства (mode, length). Основные типы объектов: vector, factor, matrix, data frame, list, ts (time series), expression. Конверсия объектов друг в друга. *(27.09.2007, 04.10.2007)*
3.  Вызов функций. Правила передачи аргументов. Аргументы по умолчанию. Ellipsis (…) operator. *(04.10.2007)*
4.  Основные операции (арифметика, логические операции). Проверка равенства (==, identical, all.equal). Индексирование “векторных” переменных (включая именованные индексы). //(04.10.2007, 11.10.2007) //
5.  Чтение данных из файла и с клавиатуры: функции read.table, scan. Запись данных в файл: функции write, write.table. //(11.10.2007, 18.10.2007) //
6.  Основные встроенные “скалярные” функции: sum, prod, max, min, which.max, which.min, range, length //(18.10.2007) //
7.  Основные встроенные “векторные” функции: round, rev, sort, rank, scale, pmin, pmax, cum{sum, prod, min, max}, diff, match, which //(18.10.2007) //
8.  Группировка, категоризующие переменные, функции над блоками данных: rowsum, aggregate, subset, lapply, sapply //(25.10.2007) //
9.  Операции с матрицами: cbind, rbind, t, diag, solve, qr, eigen, svd. //(25.10.2007) //
10. Графические устройства (функции dev.*). Разбиение устройства на блоки: split.screen, screen, erase.screen, close.screen, layout, show.layout. //(25.10.2007) //
11. Высокоуровневые графические функции: plot, curve, boxplot, coplot, matplot, pairs, hist. *(01.11.2007)*
12. Распределения. Функции распределения, плотности. Моделирование. Функции “d”, “p”, “q”, “r”. *(08.11.2007)*
13. Метод наименьших квадратов. Линейная регрессия. *(08.11.2007, 15.11.2007)*

### Темы будущих занятий

1.  Низкоуровневые графические функции: points, lines, text, mtext, segments, arrows, axes, legend, title. Графические параметры.
2.  Пакеты grid и lattice.
3.  Циклы и векторизация. Написание скриптов R [^3].
4.  …

## Prerequisites

Дистрибутив R:

1.  [Windows](http://cran.r-project.org/bin/windows/base/R-2.6.0-win32.exe)
2.  [Linux](http://cran.r-project.org/bin/linux)
3.  [MacOS X](http://cran.r-project.org/bin/macosx/)

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

## Задачи

Условные обозначения:

1.  Цифра в клетке - порядковый номер “подхода”. Наличие цифры означает, что решение было получено, **проверено**, и результат отослан обратно.
2.  Плюс - зачет, звездочка - штраф, минус - хм, незачет ;-)

Кроме того, пишется дата и время.

|             |       Task1        | Task2 | Task3 | Task4 (on-line) | Зачет |
|-------------|:------------------:|:-----:|:-----:|----------------:|------:|
| Бонько Е.   |         \+         |  \+   |  \+   |              \+ |     ✔ |
| Попов С.    |         \+         |  \+   |  \+   |              \+ |     ✔ |
| Тимофеев А. |         \+         |  \+   |  \+   |              \+ |     ✔ |
| Тимофеев И. |         \+         |  \+   |  \+   |              \+ |     ✔ |
| Фандеев Д.  |         \+         |  \+   |  -   |              - |     ✘ |
| Юдичев П.   | 2* (31.10, 21:02) |  -*  |  -   |              - |     ✘ |

## Разное


<table border=0 style="background-color: #fff; padding: 5px;" cellspacing=0>
  <tr><td>
  <img src="http://groups.google.com/groups/img/3nb/groups_bar.gif"
         height=26 width=132 alt="Google Groups">
  </td></tr>
  <tr><td style="padding-left: 5px">
  <b>Subscribe to StatMod R Course. Fall 2007.</b>
  </td></tr>
  <form action="http://groups.google.com/group/statmod-r-course-fall-2007/boxsubscribe">
  <tr><td style="padding-left: 5px;">
  Email: <input type=text name=email>
  <input type=submit name="sub" value="Subscribe">
  </td></tr>
</form>
<tr><td align=right>
  <a href="http://groups.google.com/group/statmod-r-course-fall-2007">Visit this group</a>
</td></tr>
</table>

 — *[Anton Korobeynikov](mailto:asl@math.spbu.ru) 2007/11/08 23:17*

[^1]: в сентябре

[^2]: октябрь-декабрь

[^3]: при наличии времени
