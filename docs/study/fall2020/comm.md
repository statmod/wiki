---
title: "422 гр., все. Спецкурс «Современные средства и методы научной коммуникации в области статистического моделирования»"
---

**Место и время проведения:** вторник, третья пара (13:40-15:15), ауд. 3381  
**Преподаватель:** Коробейников Антон Иванович  
—-

## Программа курса

1.  Базовый R
    1.  Введение. Краткий обзор. Базовые операции: понятие “workspace”, присваивание, просмотр списка переменных, удаление переменных из workspace’а. Функции c() и seq(). Использование встроенной справки.
    2.  Объекты R. Общие свойства (mode, length). Основные типы объектов: vector, matrix, data frame, list, expression. Конверсия объектов друг в друга.
    3.  Основные операции (арифметика, логические операции). Проверка равенства (==, identical, all.equal). Индексирование “векторных” переменных (включая именованные индексы).
    4.  Вызов функций. Правила передачи аргументов. Аргументы по умолчанию. Ellipsis (…) operator. Область видимости переменных.
    5.  Чтение и запись данных из файла. Функции scan, read.table, write.table и пр.
    6.  Основные встроенные “скалярные” функции: sum, prod, max, min, which.max, which.min, range, length
    7.  Основные встроенные “векторные” функции: round, rev, sort, rank, scale, pmin, pmax, cum{sum, prod, min, max}, diff, match, which
    8.  Операции с матрицами: cbind, rbind, t, diag, solve, qr, eigen, svd
    9.  Функции над блоками данных: lapply, sapply, replicate
    10. Графические устройства (функции dev.*). Разбиение устройства на блоки. Понятие о графических параметрах
    11. Высокоуровневые графические функции: plot, curve, pairs, density
    12. Низкоуровневые графические функции: points, line, axis, legend
    13. Распределения. Функции распределения, плотности. Моделирование. Функции “d”, “p”, “q”, “r”. Функция sample
    14. Отладка. Функции debug, browser, traceback
    15. Векторизация. Эффективная работа с памятью
    16. Нахождение (локальных) экстремумов функций
2.  Чуть больше R
    1.  Преобразование данных. Пакеты tidyr и plyr. [tidyr.pdf](../../assets/study/fall2016/intror/tidyr.pdf)
    2.  Пакет lattice. Введение. [intro.R](../../assets/study/fall2009/intror/intro.r.txt)
    3.  Пакет lattice. Изображение одномерных данных. [univariate.R](../../assets/study/fall2009/intror/univariate.r.txt)
    4.  Пакет lattice. Изображение двумерных данных: скаттерплоты, матрицы скаттерплотов, parallel plot’ы. Стили линий и т.п.[xyplot.R](../../assets/study/fall2009/intror/xyplot.r.txt), [splom.R](../../assets/study/fall2009/intror/splom.r.txt), [parallel.R](../../assets/study/fall2009/intror/parallel.r.txt)
    5.  Пакет lattice. Функции типа identify(). [lattice.identify.R](../../assets/study/fall2009/intror/lattice.identify.r.txt)
    6.  Системы рисования. Пакет ggplot [ggplot.zip](../../assets/study/fall2016/intror/ggplot.zip).

## Зачет

Для получения зачета необходимо представить:

1.  Отчет о НИР
2.  Подготовить краткое сообщение о НИР + слайды
3.  Сдать все домашние задания

## Доклады

#### 01.12

1.  Олег Чемокос

#### 08.12

1.  Владимир Попов
2.  Егор Шаповал

#### Когда-нибудь

1.  Игорь Глушков
2.  Игорь Тихонов
3.  Иван Сурушкин
4.  Илья Шешуков
5.  Анна Белкова
6.  Злата Конищева
7.  Полина Лобанова

## Успехи

Условные обозначения: + - задание зачтено; \# - решение задания получено; ! - решение задания получено, проверено, требует исправлений, - - решение задания не получено, * - штраф

|                 | Task 1    | Task 2   | Доклад | Слайды | Отчет | Зачет |
|-----------------|-----------|----------|-------:|:------:|:-----:|:------|
| Шаповал Егор    | \+        | [Task 2](dataprog/airquality.md) |     \+ |   \+   |  \+   | \+    |
| Чемокос Олег    | \+        | [Task 2](dataprog/creditcard.md) |     \+ |   \+   |  \+   | \+    |
| Белкова Анна    | \+        | [Task 2](dataprog/chickweight.md) |     \+ |   \+   |  \+   | \+    |
| Тихонов Игорь   | *        |          |        |        |       |       |
| Попов Владимир  | \+        | [Task 2](dataprog/quakes.md) |     \+ |   \+   |  \+   | \+    |
| Конищева Злата  | *[Task 1](../../assets/study/fall2020/dataprog/creditcard.txt) |          |        |        |       |       |
| Лобанова Полина | \+        | [Task 2](dataprog/survey.md) |     \+ |   \+   |  \+   | \+    |
| Шешуков Илья    | \+        | [Task 2](dataprog/theoph.md) |        |   \+   |  \+   |       |
| Глушков Игорь   | *[Task 1](../../assets/study/fall2020/dataprog/mtcars.txt) |          |        |        |       |       |
| Сурушкин Иван   | *        |          |        |        |       |       |

**Внимание**: Если напротив Вашей фамилии отсутствует назначенное задание, то для его получения Вам следует отправить запрос по почте.

## Рекомендуемая литература

### Книги

1.  **Львовский С. М.** *Набор и верстка в пакете LaTeX*, 3-е издание. — М.: МЦHМО, 2003, 448 с. [PDF](http://www.mccme.ru/free-books/llang/newllang.pdf)
2.  **Воронцов К.В.** *LaTeX 2e в примерах*, 55 с. [PDF](http://www.ccas.ru/voron/download/voron05latex.pdf)
3.  **Балдин Е.М.** *LaTeX в России* [PDF](http://www.inp.nsk.su/~baldin/LaTeX/lurs.pdf)
4.  **Оетикер Т., Партль Х., Шлегл Э., Хина И.** *Не очень краткое введение в LaTeX2e, или LaTeX2e за 94 минуты.* Перевод с английского Б. Тоботраса, 1999, 108 с [PDF](http://www.ccas.ru/voron/download/books/tex/oetiker99latex.pdf)
5.  **Колодин М. Ю.** *Русский стиль, или новейшие рекомендации для современных российских электронных типографий.* 1999, 28 с. [PDF](http://www.ccas.ru/voron/download/books/tex/kolodin99rust.pdf)
6.  **Peter Dalgaard**. *Introductory Statistics with R*. Springer, 2002.
7.  **John Maindonald and John Braun**. *Data Analysis and Graphics Using R*. Cambridge University Press, Cambridge, 2003.
8.  **John Verzani**. *Using R for Introductory Statistics*. Chapman & Hall/CRC, Boca Raton, FL, 2005.
9.  **Paul Murrell**. *R Graphics*. Chapman & Hall/CRC, Boca Raton, FL, 2005.
10. **Шипунов А.Б., Балдин Е.М., Волкова П.А., Коробейников А.И., Назарова С.А., Петров С.В., Суфиянов В.Г.** *Наглядная статистика. Используем R!* – М.: ДМК Пресс, 2012. – 298 с. [PDF](http://ashipunov.info/shipunov/school/books/rbook.pdf)
11. **Роберт И. Кабаков** *R в действии. Анализ и визуализация данных в R.* – М.: ДМК Пресс, 2013. – 280 с.

### Статьи

1.  **John Maindonald**. *Using R for Data Analysis and Graphics - Introduction, Examples and Commentary*. [PDF](http://cran.r-project.org/doc/contrib/usingR.pdf)
2.  **John Verzani**. *Simple R*. [PDF](http://cran.r-project.org/doc/contrib/Verzani-SimpleR.pdf)
3.  **Petra Kuhnert and Bill Venables**. *An Introduction to R: Software for Statistical Modelling & Computing*. [ZIP](http://cran.r-project.org/doc/contrib/Kuhnert+Venables-R_Course_Notes.zip)
4.  **David Rossiter**. *Introduction to the R Project for Statistical Computing for Use at the ITC*. [PDF](http://cran.r-project.org/doc/contrib/Rossiter-RIntro-ITC.pdf)
5.  **Е.М. Балдин, А.И. Коробейников, А.Б. Шипунов** *Анализ данных с R* [www](http://www.inp.nsk.su/~baldin/DataAnalysis/)
