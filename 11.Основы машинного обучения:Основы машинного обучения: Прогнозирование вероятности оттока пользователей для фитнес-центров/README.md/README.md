## Проект:Прогнозирование вероятности оттока пользователей для фитнес-центров
**Анализ и разработка стратегии по удержанию клиентов сети фитнес-центров «Культурист-датасаентист»**  
[ipynb](https://github.com/moseevaevgeniya/-yandex_praktikum/blob/643c9cfa7d020e877ba129b317465b177346b103/11.%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B%20%D0%BC%D0%B0%D1%88%D0%B8%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D1%8F:%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B%20%D0%BC%D0%B0%D1%88%D0%B8%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D1%8F:%20%D0%9F%D1%80%D0%BE%D0%B3%D0%BD%D0%BE%D0%B7%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%B2%D0%B5%D1%80%D0%BE%D1%8F%D1%82%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D0%BE%D1%82%D1%82%D0%BE%D0%BA%D0%B0%20%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D0%B5%D0%B9%20%D0%B4%D0%BB%D1%8F%20%D1%84%D0%B8%D1%82%D0%BD%D0%B5%D1%81-%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%BE%D0%B2/README.md/ML_fitness.ipynb) [html](https://github.com/moseevaevgeniya/-yandex_praktikum/blob/a8c06b78305912ddbfa53443acdff26d6e1eb604/11.%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B%20%D0%BC%D0%B0%D1%88%D0%B8%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D1%8F:%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B%20%D0%BC%D0%B0%D1%88%D0%B8%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D1%8F:%20%D0%9F%D1%80%D0%BE%D0%B3%D0%BD%D0%BE%D0%B7%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%B2%D0%B5%D1%80%D0%BE%D1%8F%D1%82%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D0%BE%D1%82%D1%82%D0%BE%D0%BA%D0%B0%20%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D0%B5%D0%B9%20%D0%B4%D0%BB%D1%8F%20%D1%84%D0%B8%D1%82%D0%BD%D0%B5%D1%81-%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%BE%D0%B2/README.md/ML_fitness.html)
### Описание проекта
Сеть фитнес-центров «Культурист-датасаентист» разрабатывает стратегию взаимодействия с клиентами на основе аналитических данных. Распространённая проблема фитнес-клубов и других сервисов — отток клиентов. Как понять, что клиент больше не с вами?  
**Цели проекта:**
1. Cрогнозировать вероятность оттока (на уровне следующего месяца) для каждого клиента;  
2. Сформировать типичные портреты клиентов: выделить несколько наиболее ярких групп и охарактеризовать их основные свойства;  
3. Проанализировать основные признаки, наиболее сильно влияющие на отток;  
4. Сформулировать основные выводы и разработать рекомендации по повышению качества работы с клиентами.  
### Навыки и инструменты  
- Библиотеки: python, pandas, pandas_profiling, scipy, numpy, matplotlib, seaborn, sklearn;  
- Машинное обучение;  
- Классификация;  
- Кластеризация.  
### Выводы
1. В ходе проведения работы были исследованы данные клиентов фитнес-центра:   
- Описан гипотетический портрет клиента (распределение по полу примерно одинаково,большинство клиентов (85%) живет или работает рядом с фитнес-клубом,около 30% клиентов пришли по программе "Приведи друга", средняя длительность абонементов клиентов - 4.6 месяцев, около 40% клиентов посещают групповые занятия, средний возраст клиентов 29 лет, средние дополнительные расходы на клиента - 146, средний срок до окончания договора - 4.3 месяцев,доля оттока - 27% и пр.;  
2. Для прогнозирования оттока в будущем были обучены две модели бинарной классификации: логистическая регрессиия `LogisticRegression` и случайный лес `RandomForestClassifier`. Доля правильных прогнозов и полнота чуть выше в модели логистической регрессии.  
- Была проведена кластеризация данных при помощи дендрограммы и модели `KMean`. Дендрограмма показала, что минимальное количество кластеров для нашего набора данных - 4. Далее была проведена кластеризация быстрым методом - `KMean`, разбиение проводилось на 5 кластеров. Исходя из этих данных были конкретизированы портреты клиентов.
3. Рекомендации:
- Выгоднее продавать больше долгосрочных абонементов - на них отток ниже;    
- Больше пользы будет от кластеризации при общении с сотрудниками фитнесс-центра - их менеджерами, которые общаются с клиентами, а так же с маркетологами.  
4. Основная ценность проделанной работы - это возможность предсказывать вероятность оттока в последующий месяц клиентов, благодаря чему менеджеры клуба могут фокусироваться на клиентах, которых клуб может потерять.  
