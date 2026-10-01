---
title: "522 гр., по выбору. Спецкурс «Интеллектуальный анализ данных» (5 курс)"
---

 **Место и время проведения:** каждая вторая суббота, 10:00 – ~13:00, online  
**Преподаватель:** Абильдаев Темирлан, t.abildaev23@gmail.com  


---

## Программа курса


1.  14.02. [Causal Inference. Structural Causal Models (SCM), граф SCM. Проблема идентифицируемости, d-разделение, свойства марковости и достоверности. Методы построения SCM. Do-исчисление и контрфактуалы.](../../assets/study/spring2025/islr/01-causal-inference.pdf)
2.  28.02. [Регрессия и УМО. Экспоненциальное семейство распределений, обобщённая линейная регрессия. Выбор регрессоров. Оценка качества модели.](../../assets/study/spring2025/islr/02-regression.pdf)
3.  14.03. Классификация:
    - [Байесовский классификатор. GDA, QDA, LDA, логистическая регрессия.](../../assets/study/spring2025/islr/03-classification-parametric.pdf)
    - [Дерево решений: 
построение, обрезка. Ансамбль деревьев.](../../assets/study/spring2025/islr/03-classification-trees.pdf)
    - [Метод опорных векторов.](../../assets/study/spring2025/islr/03-classification-svm.pdf)
4.  28.03. [Кластеризация. Классификация алгоритмов, основные алгоритмы. Оценка качества алгоритма.](../../assets/study/spring2025/islr/04-clustering.pdf)
5.  XX.XX. Глубокое обучение. Shallow neural networks, deep neural networks. Многослойный перцептрон. Оптимизация: backpropagation, SGD, Adam. Основы PyTorch.
6.  XX.XX. Глубокое обучение. Основные архитектуры. Обучение нейросети с использованием PyTorch.
7.  XX.XX. [Natural Language Processing. Трансформерная архитектура, механизм внимания (self-attention). Большие языковые модели (LLM). Современный pipeline, токенизация.](../../assets/study/spring2025/islr/07-nlp.pdf)
8.  XX.XX. [Обучение с подкреплением. Марковские процессы принятия решений (MDP). Награда, value function, state-action value function. Уравнения Беллмана. Value-based и policy-based алгоритмы.](../../assets/study/spring2025/islr/08-reinforcement-learning.pdf)[Глубокое обучение с подкреплением.](../../assets/study/spring2025/islr/08-deep-reinforcement-learning.pdf)


## Рекомендуемая литература


1.  [L. Wasserman, All of Statistics](../../assets/study/spring2025/islr/wasserman_all_of_statistics.pdf)
2.  [G. James, D. Witten, T. Hastie, R. Tibshirani, An Introduction to Statistical Learning](../../assets/study/spring2025/islr/james_et_al_islr.pdf)
3.  [J. Peters, D. Janzing, B. Scholkopf, Elements of Causal Inference](../../assets/study/spring2025/islr/peters_et_al_elements_of_causal_inference.pdf)
4.  [S. J. D. Prince, Understanding Deep Learning](../../assets/study/spring2025/islr/prince_understanding_deep_learning.pdf)
5.  [R. S. Sutton, A. G. Barto, Reinforcement Learning: An Introduction](../../assets/study/spring2025/islr/sutton_barto_reinforcement_learning.pdf)
6.  [Страница курса S. J. D. Prince, здесь можно посмотреть ppt-слайды лекций по основам DL](https://udlbook.github.io/udlbook)
7.  [Курсы от команды Huggingface](https://huggingface.co/learn)
8.  [Введение в PyTorch от команды самого PyTorch](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)


## Вопросы к зачёту


1.  Определение причинно-следственной связи в Causal inference. Structural Causal Model (SCM). Граф, соответствующий SCM. Проблема идентифицируемости. Три фундаментальных вида связи и соответствующие им зависимости (независимости): chains, confounding, mediating.
2.  Общая постановка задачи регрессии. Экспоненциальное семейство распределений, обобщённая линейная регрессия. Примеры: линейная, логистическая и лог-линейная регрессии.
3.  Задача классификации. Байесовский классификатор. GDA, QDA, LDA, логистическая регрессия.
4.  Задача кластеризации. Некорректность, классификация алгоритмов. Два примеры алгоритмов классификации (любых). Оценка качества алгоритмов: когда известны настоящие кластеры и когда неизвестны.
5.  Глубокие нейронные сети. Основные архитектуры глубоких нейронных сетей: многослойный перцептрон, свёрточная сеть, трансформер. Как обучают нейронные сети: backpropagation – forward pass, backward pass.