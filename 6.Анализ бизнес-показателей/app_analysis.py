#!/usr/bin/env python
# coding: utf-8

# # Анализ бизнес-показателей развлекательного приложения Procrastinate Pro+
# 

# Вы - маркетинговый аналитик развлекательного приложения Procrastinate Pro+. Несколько прошлых месяцев ваш бизнес постоянно нес убытки - в привлечение пользователей была вложена куча денег, а толку никакого. Вам нужно разобраться в причинах этой ситуации.
# 
# У вас в распоряжении есть лог сервера с данными о посещениях приложения новыми пользователями, зарегистрировавшимися в период с 2019-05-01 по 2019-10-27, выгрузка их покупок за этот период, а также статистика рекламных расходов. Вам предстоит изучить, как люди пользуются продуктом, когда они начинают покупать, сколько денег приносит каждый клиент, когда он окупается и какие факторы отрицательно влияют на привлечение пользователей.

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Загрузка-данных-и-подготовка-их-к-анализу" data-toc-modified-id="Загрузка-данных-и-подготовка-их-к-анализу-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Загрузка данных и подготовка их к анализу</a></span><ul class="toc-item"><li><span><a href="#Описание-данных" data-toc-modified-id="Описание-данных-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Описание данных</a></span></li><li><span><a href="#Загрузка-файлов" data-toc-modified-id="Загрузка-файлов-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Загрузка файлов</a></span><ul class="toc-item"><li><span><a href="#Вывод" data-toc-modified-id="Вывод-1.2.1"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Вывод</a></span></li></ul></li><li><span><a href="#Предобработка-данных" data-toc-modified-id="Предобработка-данных-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Предобработка данных</a></span></li></ul></li><li><span><a href="#Задаём-функции-для-расчета-и-анализа-LTV,-ROI,-удержания-и-конверсии" data-toc-modified-id="Задаём-функции-для-расчета-и-анализа-LTV,-ROI,-удержания-и-конверсии-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Задаём функции для расчета и анализа LTV, ROI, удержания и конверсии</a></span><ul class="toc-item"><li><span><a href="#Функция-для-создания-пользовательских-профилей" data-toc-modified-id="Функция-для-создания-пользовательских-профилей-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Функция для создания пользовательских профилей</a></span></li><li><span><a href="#Функция-для-расчёта-удержания" data-toc-modified-id="Функция-для-расчёта-удержания-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Функция для расчёта удержания</a></span></li><li><span><a href="#Функция-для-расчёта-конверсии" data-toc-modified-id="Функция-для-расчёта-конверсии-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Функция для расчёта конверсии</a></span></li><li><span><a href="#Функция-для-расчёта-LTV-и-ROI" data-toc-modified-id="Функция-для-расчёта-LTV-и-ROI-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Функция для расчёта LTV и ROI</a></span></li><li><span><a href="#Функция-для-сглаживания-фрейма" data-toc-modified-id="Функция-для-сглаживания-фрейма-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Функция для сглаживания фрейма</a></span></li><li><span><a href="#Функция-для-визуализации-удержания" data-toc-modified-id="Функция-для-визуализации-удержания-2.6"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Функция для визуализации удержания</a></span></li><li><span><a href="#Функция-для-визуализации-конверсии" data-toc-modified-id="Функция-для-визуализации-конверсии-2.7"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>Функция для визуализации конверсии</a></span></li><li><span><a href="#Функция-для-визуализации-LTV-и-ROI" data-toc-modified-id="Функция-для-визуализации-LTV-и-ROI-2.8"><span class="toc-item-num">2.8&nbsp;&nbsp;</span>Функция для визуализации LTV и ROI</a></span></li></ul></li><li><span><a href="#Провём-исследовательский-анализ-данных" data-toc-modified-id="Провём-исследовательский-анализ-данных-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Провём исследовательский анализ данных</a></span><ul class="toc-item"><li><span><a href="#Создадим-пользовательские-профили.-Определим-минимальную-и-максимальную-даты-привлечения-пользователей." data-toc-modified-id="Создадим-пользовательские-профили.-Определим-минимальную-и-максимальную-даты-привлечения-пользователей.-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Создадим пользовательские профили. Определим минимальную и максимальную даты привлечения пользователей.</a></span></li><li><span><a href="#Выясним,-из-каких-стран-пользователи-приходят-в-приложение-и-на-какую-страну-приходится-больше-всего-платящих-пользователей.-Постром-таблицу,-отражающую-количество-пользователей-и-долю-платящих-из-каждой-страны." data-toc-modified-id="Выясним,-из-каких-стран-пользователи-приходят-в-приложение-и-на-какую-страну-приходится-больше-всего-платящих-пользователей.-Постром-таблицу,-отражающую-количество-пользователей-и-долю-платящих-из-каждой-страны.-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Выясним, из каких стран пользователи приходят в приложение и на какую страну приходится больше всего платящих пользователей. Постром таблицу, отражающую количество пользователей и долю платящих из каждой страны.</a></span><ul class="toc-item"><li><span><a href="#Выясним,-из-каких-стран-пользователи-приходят-в-приложение" data-toc-modified-id="Выясним,-из-каких-стран-пользователи-приходят-в-приложение-3.2.1"><span class="toc-item-num">3.2.1&nbsp;&nbsp;</span>Выясним, из каких стран пользователи приходят в приложение</a></span></li><li><span><a href="#Выясним,-на-какую-страну-приходится-больше-всего-платящих-пользователей." data-toc-modified-id="Выясним,-на-какую-страну-приходится-больше-всего-платящих-пользователей.-3.2.2"><span class="toc-item-num">3.2.2&nbsp;&nbsp;</span>Выясним, на какую страну приходится больше всего платящих пользователей.</a></span></li><li><span><a href="#Выясним,-какими-устройствами-пользуются-клиенты-." data-toc-modified-id="Выясним,-какими-устройствами-пользуются-клиенты-.-3.2.3"><span class="toc-item-num">3.2.3&nbsp;&nbsp;</span>Выясним, какими устройствами пользуются клиенты .</a></span></li><li><span><a href="#Посмотрим-,какие-устройства-предпочитают-платящие-пользователи." data-toc-modified-id="Посмотрим-,какие-устройства-предпочитают-платящие-пользователи.-3.2.4"><span class="toc-item-num">3.2.4&nbsp;&nbsp;</span>Посмотрим ,какие устройства предпочитают платящие пользователи.</a></span></li><li><span><a href="#Определим-каналы,-из-которых-пришло-больше-всего-пользователей" data-toc-modified-id="Определим-каналы,-из-которых-пришло-больше-всего-пользователей-3.2.5"><span class="toc-item-num">3.2.5&nbsp;&nbsp;</span>Определим каналы, из которых пришло больше всего пользователей</a></span></li><li><span><a href="#Выясним,-из-каких-каналов-пришло-больше-всего-платящих-пользователей" data-toc-modified-id="Выясним,-из-каких-каналов-пришло-больше-всего-платящих-пользователей-3.2.6"><span class="toc-item-num">3.2.6&nbsp;&nbsp;</span>Выясним, из каких каналов пришло больше всего платящих пользователей</a></span></li></ul></li></ul></li><li><span><a href="#Маркетинг" data-toc-modified-id="Маркетинг-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Маркетинг</a></span><ul class="toc-item"><li><span><a href="#Посчитаем-общую-сумму-расходов-на-маркетинг.-Выясним,-как-траты-распределены-по-источникам.-Визуализируем-изменения-метрик-во-времени." data-toc-modified-id="Посчитаем-общую-сумму-расходов-на-маркетинг.-Выясним,-как-траты-распределены-по-источникам.-Визуализируем-изменения-метрик-во-времени.-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Посчитаем общую сумму расходов на маркетинг. Выясним, как траты распределены по источникам. Визуализируем изменения метрик во времени.</a></span><ul class="toc-item"><li><span><a href="#Посчитаем-общую-сумму-расходов-на-маркетинг." data-toc-modified-id="Посчитаем-общую-сумму-расходов-на-маркетинг.-4.1.1"><span class="toc-item-num">4.1.1&nbsp;&nbsp;</span>Посчитаем общую сумму расходов на маркетинг.</a></span></li><li><span><a href="#Посмотрим-общую-сумму-расходов-на-меркетинг-по-каналам-привлечения." data-toc-modified-id="Посмотрим-общую-сумму-расходов-на-меркетинг-по-каналам-привлечения.-4.1.2"><span class="toc-item-num">4.1.2&nbsp;&nbsp;</span>Посмотрим общую сумму расходов на меркетинг по каналам привлечения.</a></span></li><li><span><a href="#Визуализируем-изменения-метрик-во-времени" data-toc-modified-id="Визуализируем-изменения-метрик-во-времени-4.1.3"><span class="toc-item-num">4.1.3&nbsp;&nbsp;</span>Визуализируем изменения метрик во времени</a></span></li><li><span><a href="#Вывод" data-toc-modified-id="Вывод-4.1.4"><span class="toc-item-num">4.1.4&nbsp;&nbsp;</span>Вывод</a></span></li></ul></li><li><span><a href="#Узнаем,-сколько-в-среднем-стоило-привлечение-одного-пользователя-из-каждого-источника.-Рассчитаем-средний-CAC-на-одного-пользователя-для-всего-проекта-и-для-каждого-источника-трафика." data-toc-modified-id="Узнаем,-сколько-в-среднем-стоило-привлечение-одного-пользователя-из-каждого-источника.-Рассчитаем-средний-CAC-на-одного-пользователя-для-всего-проекта-и-для-каждого-источника-трафика.-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Узнаем, сколько в среднем стоило привлечение одного пользователя из каждого источника. Рассчитаем средний CAC на одного пользователя для всего проекта и для каждого источника трафика.</a></span><ul class="toc-item"><li><span><a href="#Рассчитаем-средний-CAC-на-одного-пользователя-для-всего-проекта." data-toc-modified-id="Рассчитаем-средний-CAC-на-одного-пользователя-для-всего-проекта.-4.2.1"><span class="toc-item-num">4.2.1&nbsp;&nbsp;</span>Рассчитаем средний CAC на одного пользователя для всего проекта.</a></span></li><li><span><a href="#Рассчитаем-средний-CAC--для-каждого-источника-трафика." data-toc-modified-id="Рассчитаем-средний-CAC--для-каждого-источника-трафика.-4.2.2"><span class="toc-item-num">4.2.2&nbsp;&nbsp;</span>Рассчитаем средний CAC  для каждого источника трафика.</a></span></li><li><span><a href="#Вывод" data-toc-modified-id="Вывод-4.2.3"><span class="toc-item-num">4.2.3&nbsp;&nbsp;</span>Вывод</a></span></li></ul></li></ul></li><li><span><a href="#Оценить-окупаемость-рекламы-для-привлечения-пользователей" data-toc-modified-id="Оценить-окупаемость-рекламы-для-привлечения-пользователей-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Оценить окупаемость рекламы для привлечения пользователей</a></span><ul class="toc-item"><li><span><a href="#Проанализируем-общую-окупаемость-рекламы.-Постром-графики-LTV-и-ROI,-а-также-графики-динамики-LTV,-CAC-и-ROI." data-toc-modified-id="Проанализируем-общую-окупаемость-рекламы.-Постром-графики-LTV-и-ROI,-а-также-графики-динамики-LTV,-CAC-и-ROI.-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Проанализируем общую окупаемость рекламы. Постром графики LTV и ROI, а также графики динамики LTV, CAC и ROI.</a></span></li><li><span><a href="#Проанализируем-окупаемость-рекламы-с-разбивкой-по-рекламным-каналам.-Построим-графики-LTV-и-ROI,-а-также-графики-динамики-LTV,-CAC-и-ROI." data-toc-modified-id="Проанализируем-окупаемость-рекламы-с-разбивкой-по-рекламным-каналам.-Построим-графики-LTV-и-ROI,-а-также-графики-динамики-LTV,-CAC-и-ROI.-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Проанализируем окупаемость рекламы с разбивкой по рекламным каналам. Построим графики LTV и ROI, а также графики динамики LTV, CAC и ROI.</a></span></li><li><span><a href="#Проанализируйте-окупаемость-рекламы-с-разбивкой-по-странам.-Постройте-графики-LTV-и-ROI,-а-также-графики-динамики-LTV,-CAC-и-ROI." data-toc-modified-id="Проанализируйте-окупаемость-рекламы-с-разбивкой-по-странам.-Постройте-графики-LTV-и-ROI,-а-также-графики-динамики-LTV,-CAC-и-ROI.-5.3"><span class="toc-item-num">5.3&nbsp;&nbsp;</span>Проанализируйте окупаемость рекламы с разбивкой по странам. Постройте графики LTV и ROI, а также графики динамики LTV, CAC и ROI.</a></span></li><li><span><a href="#Построим-и-изучим-графики-конверсии-и-удержания-с-разбивкой-по-устройствам,-странам,-рекламным-каналам." data-toc-modified-id="Построим-и-изучим-графики-конверсии-и-удержания-с-разбивкой-по-устройствам,-странам,-рекламным-каналам.-5.4"><span class="toc-item-num">5.4&nbsp;&nbsp;</span>Построим и изучим графики конверсии и удержания с разбивкой по устройствам, странам, рекламным каналам.</a></span><ul class="toc-item"><li><span><a href="#Конверсия-с-разбивкой-по-странам" data-toc-modified-id="Конверсия-с-разбивкой-по-странам-5.4.1"><span class="toc-item-num">5.4.1&nbsp;&nbsp;</span>Конверсия с разбивкой по странам</a></span></li><li><span><a href="#Удержание-с-разбивкой-по-странам" data-toc-modified-id="Удержание-с-разбивкой-по-странам-5.4.2"><span class="toc-item-num">5.4.2&nbsp;&nbsp;</span>Удержание с разбивкой по странам</a></span></li><li><span><a href="#Конверсия-с-разбивкой-по-устройствам" data-toc-modified-id="Конверсия-с-разбивкой-по-устройствам-5.4.3"><span class="toc-item-num">5.4.3&nbsp;&nbsp;</span>Конверсия с разбивкой по устройствам</a></span></li><li><span><a href="#Удержание-с-разбивкой-по-устройствам" data-toc-modified-id="Удержание-с-разбивкой-по-устройствам-5.4.4"><span class="toc-item-num">5.4.4&nbsp;&nbsp;</span>Удержание с разбивкой по устройствам</a></span></li><li><span><a href="#Конверсия-с-разбивкой-по-каналам" data-toc-modified-id="Конверсия-с-разбивкой-по-каналам-5.4.5"><span class="toc-item-num">5.4.5&nbsp;&nbsp;</span>Конверсия с разбивкой по каналам</a></span></li><li><span><a href="#Удержание-с-разбивкой-по-каналам" data-toc-modified-id="Удержание-с-разбивкой-по-каналам-5.4.6"><span class="toc-item-num">5.4.6&nbsp;&nbsp;</span>Удержание с разбивкой по каналам</a></span></li><li><span><a href="#Общий-вывод" data-toc-modified-id="Общий-вывод-5.4.7"><span class="toc-item-num">5.4.7&nbsp;&nbsp;</span>Общий вывод</a></span></li></ul></li></ul></li><li><span><a href="#Выводы" data-toc-modified-id="Выводы-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Выводы</a></span></li><li><span><a href="#Чек-лист-готовности-проекта" data-toc-modified-id="Чек-лист-готовности-проекта-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Чек-лист готовности проекта</a></span></li></ul></div>

# **Цель:** Выявить причины убытков от вложений в рекламу для компании, выпускающей развлекательное приложение Procrastinate Pro+ .
# 
# **Выборка:** Есть данные о пользователях, привлечённых с 1 мая по 27 октября 2019 года:
# -  лог сервера с данными об их посещениях,
# -  выгрузка их покупок за этот период,
# -  рекламные расходы.

# ## Загрузка данных и подготовка их к анализу
# Загрузить данные о визитах, заказах и расходах в переменные. Оптимизировать данные для анализа.  
# Путь к файлам:
# 
#  -   /datasets/visits_info_short.csv. 
#  -   /datasets/orders_info_short.csv. 
#  -   /datasets/costs_info_short.csv.

# ###  Описание данных

# Путь к файлам:
# 
# /datasets/visits_info_short.csv.
# /datasets/orders_info_short.csv.
# /datasets/costs_info_short.csv.

# **Таблица visits_log_short** (лог сервера с информацией о посещениях сайта):  
# 
# `User Id` — уникальный идентификатор пользователя  
# `Device` — категория устройства пользователя  
# `Session start` — дата и время начала сессии  
# `Session End` — дата и время окончания сессии  
# `Channel` — идентификатор рекламного источника, из которого пришел пользователь  
# `Region` - страна пользователя    
# 
# **Таблица orders_log_short** (информация о заказах):  
# 
# `User Id` — уникальный id пользователя, который сделал заказ  
# `Event Dt` — дата и время покупки  
# `Revenue` — выручка    
# 
# **Таблица costs_short** (информация о затратах на маркетинг):    
# 
# `Channel` — идентификатор рекламного источника  
# `Dt` — дата  
# `Costs` — затраты на этот рекламный источник в этот день    

# ### Загрузка файлов  
# 
# Загружаем необходимые библиотеки для исследования

# In[1]:


import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from matplotlib import pyplot as plt


# Загружаем файлы
# 

# In[2]:


sessions, orders,costs = (
    pd.read_csv('/datasets/visits_info_short.csv'),  # лог сервера с информацией о посещениях сайта
    pd.read_csv('/datasets/orders_info_short.csv'),  # информация о заказах
    pd.read_csv('/datasets/costs_info_short.csv'),  # информация о затратах на маркетинг
)


# In[3]:


display(sessions.head(5),orders.head(5)) # лог сервера с информацией о посещениях сайта и информация о заказах
costs.head(5) # информация о затратах на маркетинг|


# Посмотрим общую информацию о данных в таблицах

# In[4]:


sessions.info() # лог сервера с информацией о посещениях сайта


# In[5]:


orders.info() # информация о заказах


# In[6]:


costs.info() # информация о затратах на маркетинг


#  #### Вывод

# Во всех таблицах в столбцах отсутствую пропуски. Типы данных в столбцах  `object`, `float64`, `int64`.  
# Названия столбцов необходимо превести к нижнему регистру и изменить стиль заголовков. Столбцы, содержащие дату и время преобразовать тип данных на datetime.

# ### Предобработка данных

# Создаём функцию для получения информации о дубликатах:

# In[7]:


def first_look (df):
    
    
  '''Функция получения первичной информации о датафрейме'''
# для творчества и примера - оставлены только основные строки кода
  for element in df.columns:
    count = +1
  if count == 0:

    print('Дубликатов в таблице ',df.duplicated().sum())
  else:
    print('Дубликатов в таблице ', 'НЕТ')


# In[8]:


first_look(sessions)


# In[9]:


first_look(orders)


# In[10]:


first_look(costs)


# * Дубликатов нет.
# * Необходимо изменить типы данных.
# * Нужно привести названия столбцов к нижнему регистру.

# В таблицах во всех столбцах, где информация о дате и времени- тип столбцов `object`

# In[11]:


# преобразуем данные о времени для дальнейших расчётов
sessions['Session Start'] = pd.to_datetime(sessions['Session Start'])
sessions['Session End']=pd.to_datetime(sessions['Session End'])
orders['Event Dt'] = pd.to_datetime(orders['Event Dt'])
costs['dt']=pd.to_datetime(costs['dt']).dt.date


# Переименуем названия столбцов

# In[12]:


sessions = sessions.rename(columns = {'User Id': 'user_id', 'Session Start': 'session_start', 'Session End':'session_end'})


# Приведём названия столбцов к нижнему регистру

# In[13]:


sessions.columns = sessions.columns.str.lower()
orders.columns = orders.columns.str.lower()
costs.columns = costs.columns.str.lower()


# ## Задаём функции для расчета и анализа LTV, ROI, удержания и конверсии
# 

# Соберём функции для создания профилей, расчёта удержания, конверсии, LTV и ROI : get_profiles(), get_retention(), get_conversion() и get_ltv().

# ### Функция для создания пользовательских профилей

# In[14]:


# функция для создания пользовательских профилей
def get_profiles(sessions, orders, ad_costs):
    # Шаг 1. Передадим в функцию расчета профиля данные о рекламных затратах (фрейм ad_costs)
    
    # сортируем сессии по id пользователя и дате для того,чтобы работал first
    # находим первые значения для параметров пользователя - будем считать их основными 
    profiles = (sessions.sort_values(by = ['user_id', 'session_start'])           
                        .groupby('user_id').agg({'session_start' : 'first',       
                                                 'channel': 'first',
                                                 'device': 'first',
                                                 'region': 'first'})                                 
                        .rename(columns = {'session_start' : 'first_ts'})  
                        .reset_index()  # вернем все данные из индекса в колонки                                           
               )
    # определим дату первого посещеня 
    # и начало месяца первого посещения - они понадобятся нам при когортном анализе
    profiles['dt'] = profiles['first_ts'].dt.date                                 
    profiles['month'] = profiles['first_ts'].astype('datetime64[M]')     
    
    # добавляем признак платящих пользователей
    profiles['payer'] = profiles['user_id'].isin(orders['user_id'].unique())   
            
    # Шаг 2. К данным о рекламных затратах добавим количества привлеченных пользователей
    new_users = profiles.groupby(['dt', 'channel']).agg({'user_id': 'nunique'}).rename(columns = {'user_id': 'unique_users'}).reset_index()
    ad_costs = ad_costs.merge(new_users, on = ['dt', 'channel'], how = 'left')
    
    # Шаг 3. Найдем среднюю стоимость привлечения пользователя
    ad_costs['acquisition_cost'] = ad_costs['costs'] / ad_costs['unique_users']
    
    # Шаг 4. Присоединим данные к профилям пользователей информацию о средней стоимости привлечения в день привлечения пользователя из нужного источника
    profiles = profiles.merge(ad_costs[['dt', 'channel', 'acquisition_cost']], on = ['dt', 'channel'], how = 'left')
    profiles['acquisition_cost'] = profiles['acquisition_cost'].fillna(0) # органические пользователи будут стоить 0
    
    return profiles


# ### Функция для расчёта удержания

# In[15]:


# функция для расчёта удержания

def get_retention(
    profiles,
    sessions,
    observation_date,
    horizon_days,
    dimensions=[],
    ignore_horizon=False,
):

    # добавляем столбец payer в передаваемый dimensions список
    dimensions = ['payer'] + dimensions

    # исключаем пользователей, не «доживших» до горизонта анализа
    last_suitable_acquisition_date = observation_date
    if not ignore_horizon:
        last_suitable_acquisition_date = observation_date - timedelta(
            days=horizon_days - 1
        )
    result_raw = profiles.query('dt <= @last_suitable_acquisition_date')

    # собираем «сырые» данные для расчёта удержания
    result_raw = result_raw.merge(
        sessions[['user_id', 'session_start']], on='user_id', how='left'
    )
    result_raw['lifetime'] = (
        result_raw['session_start'] - result_raw['first_ts']
    ).dt.days

    # функция для группировки таблицы по желаемым признакам
    def group_by_dimensions(df, dims, horizon_days):
        result = df.pivot_table(
            index=dims, columns='lifetime', values='user_id', aggfunc='nunique'
        )
        cohort_sizes = (
            df.groupby(dims)
            .agg({'user_id': 'nunique'})
            .rename(columns={'user_id': 'cohort_size'})
        )
        result = cohort_sizes.merge(result, on=dims, how='left').fillna(0)
        result = result.div(result['cohort_size'], axis=0)
        result = result[['cohort_size'] + list(range(horizon_days))]
        result['cohort_size'] = cohort_sizes
        return result

    # получаем таблицу удержания
    result_grouped = group_by_dimensions(result_raw, dimensions, horizon_days)

    # получаем таблицу динамики удержания
    result_in_time = group_by_dimensions(
        result_raw, dimensions + ['dt'], horizon_days
    )

    # возвращаем обе таблицы и сырые данные
    return result_raw, result_grouped, result_in_time


# ### Функция для расчёта конверсии

# In[16]:



# функция для расчёта конверсии

def get_conversion(
    profiles,
    purchases,
    observation_date,
    horizon_days,
    dimensions=[],
    ignore_horizon=False,
):

    # исключаем пользователей, не «доживших» до горизонта анализа
    last_suitable_acquisition_date = observation_date
    if not ignore_horizon:
        last_suitable_acquisition_date = observation_date - timedelta(
            days=horizon_days - 1
        )
    result_raw = profiles.query('dt <= @last_suitable_acquisition_date')

    # определяем дату и время первой покупки для каждого пользователя
    first_purchases = (
        purchases.sort_values(by=['user_id', 'event_dt'])
        .groupby('user_id')
        .agg({'event_dt': 'first'})
        .reset_index()
    )

    # добавляем данные о покупках в профили
    result_raw = result_raw.merge(
        first_purchases[['user_id', 'event_dt']], on='user_id', how='left'
    )

    # рассчитываем лайфтайм для каждой покупки
    result_raw['lifetime'] = (
        result_raw['event_dt'] - result_raw['first_ts']
    ).dt.days

    # группируем по cohort, если в dimensions ничего нет
    if len(dimensions) == 0:
        result_raw['cohort'] = 'All users' 
        dimensions = dimensions + ['cohort']

    # функция для группировки таблицы по желаемым признакам
    def group_by_dimensions(df, dims, horizon_days):
        result = df.pivot_table(
            index=dims, columns='lifetime', values='user_id', aggfunc='nunique'
        )
        result = result.fillna(0).cumsum(axis = 1)
        cohort_sizes = (
            df.groupby(dims)
            .agg({'user_id': 'nunique'})
            .rename(columns={'user_id': 'cohort_size'})
        )
        result = cohort_sizes.merge(result, on=dims, how='left').fillna(0)
        # делим каждую «ячейку» в строке на размер когорты
        # и получаем conversion rate
        result = result.div(result['cohort_size'], axis=0)
        result = result[['cohort_size'] + list(range(horizon_days))]
        result['cohort_size'] = cohort_sizes
        return result

    # получаем таблицу конверсии
    result_grouped = group_by_dimensions(result_raw, dimensions, horizon_days)

    # для таблицы динамики конверсии убираем 'cohort' из dimensions
    if 'cohort' in dimensions: 
        dimensions = []

    # получаем таблицу динамики конверсии
    result_in_time = group_by_dimensions(
        result_raw, dimensions + ['dt'], horizon_days
    )

    # возвращаем обе таблицы и сырые данные
    return result_raw, result_grouped, result_in_time


# ### Функция для расчёта LTV и ROI

# In[17]:


# функция для расчёта LTV и ROI

def get_ltv(
    profiles,
    purchases,
    observation_date,
    horizon_days,
    dimensions=[],
    ignore_horizon=False,
):

    # исключаем пользователей, не «доживших» до горизонта анализа
    last_suitable_acquisition_date = observation_date
    if not ignore_horizon:
        last_suitable_acquisition_date = observation_date - timedelta(
            days=horizon_days - 1
        )
    result_raw = profiles.query('dt <= @last_suitable_acquisition_date')
    # добавляем данные о покупках в профили
    result_raw = result_raw.merge(
        purchases[['user_id', 'event_dt', 'revenue']], on='user_id', how='left'
    )
    # рассчитываем лайфтайм пользователя для каждой покупки
    result_raw['lifetime'] = (
        result_raw['event_dt'] - result_raw['first_ts']
    ).dt.days
    # группируем по cohort, если в dimensions ничего нет
    if len(dimensions) == 0:
        result_raw['cohort'] = 'All users'
        dimensions = dimensions + ['cohort']

    # функция группировки по желаемым признакам
    def group_by_dimensions(df, dims, horizon_days):
        # строим «треугольную» таблицу выручки
        result = df.pivot_table(
            index=dims, columns='lifetime', values='revenue', aggfunc='sum'
        )
        # находим сумму выручки с накоплением
        result = result.fillna(0).cumsum(axis=1)
        # вычисляем размеры когорт
        cohort_sizes = (
            df.groupby(dims)
            .agg({'user_id': 'nunique'})
            .rename(columns={'user_id': 'cohort_size'})
        )
        # объединяем размеры когорт и таблицу выручки
        result = cohort_sizes.merge(result, on=dims, how='left').fillna(0)
        # считаем LTV: делим каждую «ячейку» в строке на размер когорты
        result = result.div(result['cohort_size'], axis=0)
        # исключаем все лайфтаймы, превышающие горизонт анализа
        result = result[['cohort_size'] + list(range(horizon_days))]
        # восстанавливаем размеры когорт
        result['cohort_size'] = cohort_sizes

        # собираем датафрейм с данными пользователей и значениями CAC, 
        # добавляя параметры из dimensions
        cac = df[['user_id', 'acquisition_cost'] + dims].drop_duplicates()

        # считаем средний CAC по параметрам из dimensions
        cac = (
            cac.groupby(dims)
            .agg({'acquisition_cost': 'mean'})
            .rename(columns={'acquisition_cost': 'cac'})
        )

        # считаем ROI: делим LTV на CAC
        roi = result.div(cac['cac'], axis=0)

        # удаляем строки с бесконечным ROI
        roi = roi[~roi['cohort_size'].isin([np.inf])]

        # восстанавливаем размеры когорт в таблице ROI
        roi['cohort_size'] = cohort_sizes

        # добавляем CAC в таблицу ROI
        roi['cac'] = cac['cac']

        # в финальной таблице оставляем размеры когорт, CAC
        # и ROI в лайфтаймы, не превышающие горизонт анализа
        roi = roi[['cohort_size', 'cac'] + list(range(horizon_days))]

        # возвращаем таблицы LTV и ROI
        return result, roi

    # получаем таблицы LTV и ROI
    result_grouped, roi_grouped = group_by_dimensions(
        result_raw, dimensions, horizon_days
    )

    # для таблиц динамики убираем 'cohort' из dimensions
    if 'cohort' in dimensions:
        dimensions = []

    # получаем таблицы динамики LTV и ROI
    result_in_time, roi_in_time = group_by_dimensions(
        result_raw, dimensions + ['dt'], horizon_days
    )

    return (
        result_raw,  # сырые данные
        result_grouped,  # таблица LTV
        result_in_time,  # таблица динамики LTV
        roi_grouped,  # таблица ROI
        roi_in_time,  # таблица динамики ROI
    )


# А также функции для визуализации этих метрик — filter_data(), plot_retention(), plot_conversion() и plot_ltv_roi().

# ### Функция для сглаживания фрейма

# In[18]:


# функция для сглаживания фрейма

def filter_data(df, window):
    # для каждого столбца применяем скользящее среднее
    for column in df.columns.values:
        df[column] = df[column].rolling(window).mean() 
    return df


# ### Функция для визуализации удержания

# In[19]:


# функция для визуализации удержания

def plot_retention(retention, retention_history, horizon, window=7):

    # задаём размер сетки для графиков
    plt.figure(figsize=(15, 10))

    # исключаем размеры когорт и удержание первого дня
    retention = retention.drop(columns=['cohort_size', 0])
    # в таблице динамики оставляем только нужный лайфтайм
    retention_history = retention_history.drop(columns=['cohort_size'])[
        [horizon - 1]
    ]

    # если в индексах таблицы удержания только payer,
    # добавляем второй признак — cohort
    if retention.index.nlevels == 1:
        retention['cohort'] = 'All users'
        retention = retention.reset_index().set_index(['cohort', 'payer'])

    # в таблице графиков — два столбца и две строки, четыре ячейки
    # в первой строим кривые удержания платящих пользователей
    ax1 = plt.subplot(2, 2, 1)
    retention.query('payer == True').droplevel('payer').T.plot(
        grid=True, ax=ax1
    )
    plt.legend()
    plt.xlabel('Лайфтайм')
    plt.title('Удержание платящих пользователей')

    # во второй ячейке строим кривые удержания неплатящих
    # вертикальная ось — от графика из первой ячейки
    ax2 = plt.subplot(2, 2, 2, sharey=ax1)
    retention.query('payer == False').droplevel('payer').T.plot(
        grid=True, ax=ax2
    )
    plt.legend()
    plt.xlabel('Лайфтайм')
    plt.title('Удержание неплатящих пользователей')

    # в третьей ячейке — динамика удержания платящих
    ax3 = plt.subplot(2, 2, 3)
    # получаем названия столбцов для сводной таблицы
    columns = [
        name
        for name in retention_history.index.names
        if name not in ['dt', 'payer']
    ]
    # фильтруем данные и строим график
    filtered_data = retention_history.query('payer == True').pivot_table(
        index='dt', columns=columns, values=horizon - 1, aggfunc='mean'
    )
    filter_data(filtered_data, window).plot(grid=True, ax=ax3)
    plt.xlabel('Дата привлечения')
    plt.title(
        'Динамика удержания платящих пользователей на {}-й день'.format(
            horizon
        )
    )

    # в чётвертой ячейке — динамика удержания неплатящих
    ax4 = plt.subplot(2, 2, 4, sharey=ax3)
    # фильтруем данные и строим график
    filtered_data = retention_history.query('payer == False').pivot_table(
        index='dt', columns=columns, values=horizon - 1, aggfunc='mean'
    )
    filter_data(filtered_data, window).plot(grid=True, ax=ax4)
    plt.xlabel('Дата привлечения')
    plt.title(
        'Динамика удержания неплатящих пользователей на {}-й день'.format(
            horizon
        )
    )
    
    plt.tight_layout()
    plt.show()


# ### Функция для визуализации конверсии

# In[20]:


# функция для визуализации конверсии

def plot_conversion(conversion, conversion_history, horizon, window=7):

    # задаём размер сетки для графиков
    plt.figure(figsize=(15, 5))

    # исключаем размеры когорт
    conversion = conversion.drop(columns=['cohort_size'])
    # в таблице динамики оставляем только нужный лайфтайм
    conversion_history = conversion_history.drop(columns=['cohort_size'])[
        [horizon - 1]
    ]

    # первый график — кривые конверсии
    ax1 = plt.subplot(1, 2, 1)
    conversion.T.plot(grid=True, ax=ax1)
    plt.legend()
    plt.xlabel('Лайфтайм')
    plt.title('Конверсия пользователей')

    # второй график — динамика конверсии
    ax2 = plt.subplot(1, 2, 2, sharey=ax1)
    columns = [
        # столбцами сводной таблицы станут все столбцы индекса, кроме даты
        name for name in conversion_history.index.names if name not in ['dt']
    ]
    filtered_data = conversion_history.pivot_table(
        index='dt', columns=columns, values=horizon - 1, aggfunc='mean'
    )
    filter_data(filtered_data, window).plot(grid=True, ax=ax2)
    plt.xlabel('Дата привлечения')
    plt.title('Динамика конверсии пользователей на {}-й день'.format(horizon))

    plt.tight_layout()
    plt.show()


# ### Функция для визуализации LTV и ROI

# In[21]:


# функция для визуализации LTV и ROI

def plot_ltv_roi(ltv, ltv_history, roi, roi_history, horizon, window=7):

    # задаём сетку отрисовки графиков
    plt.figure(figsize=(20, 10))

    # из таблицы ltv исключаем размеры когорт
    ltv = ltv.drop(columns=['cohort_size'])
    # в таблице динамики ltv оставляем только нужный лайфтайм
    ltv_history = ltv_history.drop(columns=['cohort_size'])[[horizon - 1]]

    # стоимость привлечения запишем в отдельный фрейм
    cac_history = roi_history[['cac']]

    # из таблицы roi исключаем размеры когорт и cac
    roi = roi.drop(columns=['cohort_size', 'cac'])
    # в таблице динамики roi оставляем только нужный лайфтайм
    roi_history = roi_history.drop(columns=['cohort_size', 'cac'])[
        [horizon - 1]
    ]

    # первый график — кривые ltv
    ax1 = plt.subplot(2, 3, 1)
    ltv.T.plot(grid=True, ax=ax1)
    plt.legend()
    plt.xlabel('Лайфтайм')
    plt.title('LTV')

    # второй график — динамика ltv
    ax2 = plt.subplot(2, 3, 2, sharey=ax1)
    # столбцами сводной таблицы станут все столбцы индекса, кроме даты
    columns = [name for name in ltv_history.index.names if name not in ['dt']]
    filtered_data = ltv_history.pivot_table(
        index='dt', columns=columns, values=horizon - 1, aggfunc='mean'
    )
    filter_data(filtered_data, window).plot(grid=True, ax=ax2)
    plt.xlabel('Дата привлечения')
    plt.title('Динамика LTV пользователей на {}-й день'.format(horizon))

    # третий график — динамика cac
    ax3 = plt.subplot(2, 3, 3, sharey=ax1)
    # столбцами сводной таблицы станут все столбцы индекса, кроме даты
    columns = [name for name in cac_history.index.names if name not in ['dt']]
    filtered_data = cac_history.pivot_table(
        index='dt', columns=columns, values='cac', aggfunc='mean'
    )
    filter_data(filtered_data, window).plot(grid=True, ax=ax3)
    plt.xlabel('Дата привлечения')
    plt.title('Динамика стоимости привлечения пользователей')

    # четвёртый график — кривые roi
    ax4 = plt.subplot(2, 3, 4)
    roi.T.plot(grid=True, ax=ax4)
    plt.axhline(y=1, color='red', linestyle='--', label='Уровень окупаемости')
    plt.legend()
    plt.xlabel('Лайфтайм')
    plt.title('ROI')

    # пятый график — динамика roi
    ax5 = plt.subplot(2, 3, 5, sharey=ax4)
    # столбцами сводной таблицы станут все столбцы индекса, кроме даты
    columns = [name for name in roi_history.index.names if name not in ['dt']]
    filtered_data = roi_history.pivot_table(
        index='dt', columns=columns, values=horizon - 1, aggfunc='mean'
    )
    filter_data(filtered_data, window).plot(grid=True, ax=ax5)
    plt.axhline(y=1, color='red', linestyle='--', label='Уровень окупаемости')
    plt.xlabel('Дата привлечения')
    plt.title('Динамика ROI пользователей на {}-й день'.format(horizon))

    plt.tight_layout()
    plt.show()


# Теперь можно приступать к анализу.

# ## Провём исследовательский анализ данных
# 

# ### Создадим пользовательские профили. Определим минимальную и максимальную даты привлечения пользователей.

# Для этого вызовем функцию get_profiles(), передав ей данные о посещениях, покупках и тратах на рекламу.

# In[22]:


# получаем профили пользователей
profiles = get_profiles(sessions, orders, costs)
print(profiles.head(5))


# **Определим минимальную и максимальную дату привлечения пользователей.**

# In[23]:


min_analysis_date = sessions['session_start'].min()
observation_date =  sessions['session_start'].max()# ваш код здесь

print('Минимальная дата привлечения пользователей : ', min_analysis_date) 
print('Максимальная дата привлечения пользователей : ', observation_date)


# Просто потренеруемся

# In[24]:


analysis_horizon = 14 
max_analysis_date = observation_date - timedelta(days=analysis_horizon - 1)
print(max_analysis_date)


# **Установим момент и горизонт анализа данных.**  
# Предположим, что на календаре 1 ноября 2019 года, и зададим двух недельный горизонт анализа.

# In[25]:


observation_date = datetime(2019, 11, 1).date()  # момент анализа
horizon_days = 14  # горизонт анализа


# ### Выясним, из каких стран пользователи приходят в приложение и на какую страну приходится больше всего платящих пользователей. Постром таблицу, отражающую количество пользователей и долю платящих из каждой страны.

# #### Выясним, из каких стран пользователи приходят в приложение

# In[26]:


print(
    profiles.groupby('region').agg({'user_id': 'nunique'}).sort_values(by='user_id', ascending=False)
    
)


# **Вывод**  
# Больше всего пользователей приходят в приложение из USA

# #### Выясним, на какую страну приходится больше всего платящих пользователей. 

# In[27]:


print(profiles.groupby('region').agg({'payer': 'mean'}).sort_values(by='payer', ascending=False))


# **Вывод**  
# Больше всего платящих пользователей приходится на USA

# #### Выясним, какими устройствами пользуются клиенты .

# In[28]:


print(
    profiles.groupby('device').agg({'user_id': 'nunique'}).sort_values(by='user_id', ascending=False))


# **Вывод**  
# Клиенты приложения больше всего пользуются устройством iPhone

# #### Посмотрим ,какие устройства предпочитают платящие пользователи.

# In[29]:


print(profiles.groupby('device').agg({'payer': 'mean'}).sort_values(by='payer', ascending=False))


# **Вывод**  
# Пользователи больше всего предпочитают  Mac и iPhone

# #### Определим каналы, из которых пришло больше всего пользователей

# In[30]:


print(
    profiles.groupby('channel').agg({'user_id': 'nunique'}).sort_values(by='user_id', ascending=False))


# **Вывод**  
# Из органического канала больше всего приходят пользователи

# #### Выясним, из каких каналов пришло больше всего платящих пользователей

# In[31]:


print(profiles.groupby('channel').agg({'payer': 'mean'}).sort_values(by='payer', ascending=False))


# **Вывод**  
# Больше всего платящих пользователей пришли из  FaceBoom,  AdNonSense, lambdaMediaAds

# **Выводы**  
# 
#  1. Больше всего пользователй приходят в приложение Procrastinate Pro+ из USA  
#  2. Больше всего платящих пользователей также приходится на USA
#  3. Больше всего клиентов приложения Procrastinate Pro+ пользуются iPhone  
#  4. Платящие пользователи приложения предпочитают Mac, iPhone и Android.  
#     Их доля доставляет 6,4% 6,2% и 5,9% соответственно.  
#     Доля пользователей приложения предпочитающих персональный компьютер не сильно отличается и составляет 5%.  
#  5. Больше всего пользователей пришло из каналов Оrganic, FaceBoom, TipTop или 56439, 29144 и 19561 уникальных пользователей соответственно.
#  6. Больше всего платящих пользователей из каналов  приходится на FaceBoom (12,2%), AdNonSense(11,3%), lambdaMediaAds(10,5%), TipTop (9,6%) и RocketSuperAds(7,9%). 
#  7. Следует отметить, не смотря на то, что больше всего пользователей приложения пришло из органического канала, доля платящих самая минимальная 2,1%.
#  

# ## Маркетинг
# 

# ### Посчитаем общую сумму расходов на маркетинг. Выясним, как траты распределены по источникам. Визуализируем изменения метрик во времени.

# #### Посчитаем общую сумму расходов на маркетинг. 

# In[32]:


print('Общая сумма расходов на маркетинг : ',round(costs['costs'].sum()))


# #### Посмотрим общую сумму расходов на меркетинг по каналам привлечения.

# In[33]:


print(
    costs.groupby('channel').agg({'costs': 'sum'}).sort_values(by='costs', ascending=False))


# #### Визуализируем изменения метрик во времени

# In[34]:


cost_dynamics = costs.pivot_table(
    index='dt',
    columns='channel',
    values='costs', 
    aggfunc='sum'
    ).plot(figsize=(18, 15), grid=True)
plt.ylabel('Затраты на маркетинг, $')
plt.xlabel('Дата привлечения')
plt.title('Динамика расходов на маркетинг по каналам привлечения')
plt.show()


# #### Вывод  
# 
# - Общая сумма расходов на маркетинг за весь период составила 105497 долларов. 
# - Больше всего расходов на маркетинг потратила компания на привлечение пользователей на каналах TipTop и FaceBoom,  
#   или 54751 долларов  и 32445 долларов соответственно.  
# - Динамика показывает, что компания ежемесячно увеличивает расходы на маркетинг по каналам TipTop и FaceBoom.
# 

# ### Узнаем, сколько в среднем стоило привлечение одного пользователя из каждого источника. Рассчитаем средний CAC на одного пользователя для всего проекта и для каждого источника трафика. 

# #### Рассчитаем средний CAC на одного пользователя для всего проекта. 

# In[35]:


print(
   profiles['acquisition_cost'].mean())


# #### Рассчитаем средний CAC  для каждого источника трафика.

# In[36]:


print(
    profiles.groupby('channel').agg({'acquisition_cost': 'mean'}).sort_values(by='acquisition_cost', ascending=False))


# Убираем органический канал из дальнейшего анализа - за них мы ничего не платим.

# In[37]:


profiles=profiles[profiles['channel'] != 'organic'] #  убираем органический канал


# Снова рассчитаем средний CAC - посмотрим, нет ли органик канала

# In[38]:


print(
    profiles.groupby('channel').agg({'acquisition_cost': 'mean'}).sort_values(by='acquisition_cost', ascending=False))


# #### Вывод  
# 
# 1. Средний САС на одного пользователя для всего проекта составил 70 центов.  
# 2. Самым затратным каналом стал TipTop с 2,8 долларами  на 1 пользователя.
# 3. Компания не вкладывается в рекламу на органическом канале.

# ## Оценить окупаемость рекламы для привлечения пользователей
# 

# ### Проанализируем общую окупаемость рекламы. Постром графики LTV и ROI, а также графики динамики LTV, CAC и ROI.

# **Считаем LTV и ROI**

# Для начала оценим общую ситуацию — посмотрим на окупаемость рекламы. Рассчитаем и визуализируем LTV и ROI, вызвав функции get_ltv() и plot_ltv_roi()

# In[39]:


# считаем LTV и ROI
ltv_raw, ltv_grouped, ltv_history, roi_grouped, roi_history = get_ltv(
    profiles, orders, observation_date, horizon_days
)

# строим графики
plot_ltv_roi(ltv_grouped, ltv_history, roi_grouped, roi_history, horizon_days)


# **По графикам можно сделать такие выводы:**  
# 
# 1. Рекламе не хватило 20% чтобы окупиться. ROI в конце 14-го дня — чуть выше 60%.
# 2. CAC стартовал с 75 центов и увеличивался до 1,3 долларов. Значит,компания ежемесячно увеличивала траты на маркетинг.
# 3. LTV достаточно стабилен.
# 4. Попробуем углублённо проанализировать  текущую ситуацию, пройдём по всем доступным характеристикам пользователей — стране, источнику и устройству первого посещения.

# ### Проанализируем окупаемость рекламы с разбивкой по рекламным каналам. Построим графики LTV и ROI, а также графики динамики LTV, CAC и ROI.

# **Проверим источники привлечения (channel).**

# In[40]:


# смотрим окупаемость с разбивкой по источникам привлечения

dimensions = ['channel']

ltv_raw, ltv_grouped, ltv_history, roi_grouped, roi_history = get_ltv(
    profiles, orders, observation_date, horizon_days, dimensions=dimensions
)

plot_ltv_roi(
    ltv_grouped, ltv_history, roi_grouped, roi_history, horizon_days, window=14
)


# **По графикам можно сделать такие выводы:**  
# 
# 1. Окупились все каналы, кроме TipTop, FaceBoom и AdNonSense.
# 2. В течение всего периода САС был стабилен по всем каналам, кроме TipTop. Компания по каналу TipTop значительно наращивала расходы по маркетингу в течение всего периода проекта.

# ### Проанализируйте окупаемость рекламы с разбивкой по странам. Постройте графики LTV и ROI, а также графики динамики LTV, CAC и ROI.

# **Перейдём к разбивке по странам: передадим параметру dimensions столбец region.**

# In[41]:


# смотрим окупаемость с разбивкой по странам

dimensions = ['region']

ltv_raw, ltv_grouped, ltv_history, roi_grouped, roi_history = get_ltv(
    profiles, orders, observation_date, horizon_days, dimensions=dimensions
)

plot_ltv_roi(
    ltv_grouped, ltv_history, roi_grouped, roi_history, horizon_days, window=14
)


# **По графикам можно сделать такие выводы:** 
# 
# 1. Реклама окупилась по всем странам, кроме USA.  
# 2. Компания наращивала расходы на маркетинг по USA. Стоимость привлечения для других стран стабильна.
# 3. LTV  подвержен сезонности, но стабилен.
# 4. Лучше всего окупается Великобритания, а также Германия и Франция.

# ### Построим и изучим графики конверсии и удержания с разбивкой по устройствам, странам, рекламным каналам.

# Посчитаем и визуализируем конверсию, вызвав функции get_conversion() и plot_conversion().

# #### Конверсия с разбивкой по странам

# In[42]:


# смотрим конверсию с разбивкой по странам


conversion_raw, conversion_grouped, conversion_history = get_conversion(
    profiles, orders, observation_date, horizon_days, dimensions=dimensions
)

plot_conversion(conversion_grouped, conversion_history, horizon_days)


# **По графикам можно сделать такие выводы:**  
# 
# Судя по графикам, пользователи USA конвертируются очень хорошо, причём постоянно. Видимо, дело в удержании. Вызовем функции get_retention() и plot_retention(), чтобы рассчитать и отразить на графиках этот показатель.

# #### Удержание с разбивкой по странам

# In[43]:


# смотрим удержание с разбивкой по странам


retention_raw, retention_grouped, retention_history = get_retention(
    profiles, sessions, observation_date, horizon_days, dimensions=dimensions
)

plot_retention(retention_grouped, retention_history, horizon_days)


# **По графикам можно сделать такие выводы:**  
# Действительно, пользователи из USA удерживаются стабильно хуже пользователей из других стран. Для платящих пользователей из USA удержание 14-го дня ниже, чем для других стан примерно на 20%.
# 

# #### Конверсия с разбивкой по устройствам

# In[44]:


# смотрим конверсию с разбивкой по устройствам

dimensions = ['device']
conversion_raw, conversion_grouped, conversion_history = get_conversion(
    profiles, orders, observation_date, horizon_days, dimensions=dimensions
)

plot_conversion(conversion_grouped, conversion_history, horizon_days)


# **По графикам можно сделать такие выводы:**  
# 
# Судя по графикам, пользователи Mac, iPhone и Android почти одинаково конвертируются хорошо, причём постоянно. Видимо, дело в удержании. Вызовем функции get_retention() и plot_retention(), чтобы рассчитать и отразить на графиках этот показатель.

# #### Удержание с разбивкой по устройствам

# In[45]:


# смотрим удержание с разбивкой по устройствам
dimensions = ['device']
retention_raw, retention_grouped, retention_history = get_retention(
    profiles, sessions, observation_date, horizon_days, dimensions=dimensions
)

plot_retention(retention_grouped, retention_history, horizon_days) 


# **По графикам можно сделать такие выводы:**  
# Действительно, пользователи всех устройств стабильно слабо удерживаются. Для платящих пользователей на всех устройствах удержание 14-го дня стабильно низкая. 
# Скорее всего, причина в какой-нибудь технической проблеме.

# #### Конверсия с разбивкой по каналам

# In[46]:


# смотрим конверсию с разбивкой по каналам

dimensions = ['channel']
conversion_raw, conversion_grouped, conversion_history = get_conversion(
    profiles, orders, observation_date, horizon_days, dimensions=dimensions
)

plot_conversion(conversion_grouped, conversion_history, horizon_days)


# **По графикам можно сделать такие выводы:**  
# 
# Лучше всего конвертируются пользователи FaceBoom. Также отметим тех у кого конверсия выше 5% - это: AdNonSense, lambdaMediaAds, TipTop, RocketSuperAds. Это тоже хороший показатель. Видимо дело в удержании

# #### Удержание с разбивкой по каналам

# In[47]:


# смотрим удержание с разбивкой по каналам
dimensions = ['channel']
retention_raw, retention_grouped, retention_history = get_retention(
    profiles, sessions, observation_date, horizon_days, dimensions=dimensions
)

plot_retention(retention_grouped, retention_history, horizon_days) 


# **По графикам можно сделать такие выводы:**   
# 
# Действительно, пользователи из FaceBoom и AdNonSense стабильно плохо удерживаются. Для платящих пользователей из этих каналов удержание 14-го дня ниже, чем на других каналах, примерно на 25%. Это  низкий показатель.
# Скорее всего, причина в какой-нибудь технической проблеме.

# #### Общий вывод   
# 
# 1. Расходы на рекламу приложения за весь период проекта не окупился, не хватило пару процентов.  
# 2. Окупилась реклама на всех каналах, кроме TipTop, FaceBoom и AdNonSense.  
# 3. На TipTop компания ежемесячно значительно увеличивает расходы на привлечение пользователей-видимо в связи с популяризацией приложения на На TipTop.
# 4. Пользователи FaceBoom и  AdNonSense имеют высокую конвертацию , при этом показывают очень низкое удержание платящих пользователей. Видимо причина в какой-нибудь технической проблеме.
# 

# ## Выводы
# 

# <div class="alert alert-block alert-info">
#     
# **Общий вывод**  
#     
# Общие расходы на рекламу за весь период не окупились примерно на 20%.
#     Что повлияло на данный показатель?  
# 1. Реклама не окупилась только по США. Причинами стали:  
#     * наращивание стоимости привлечения пользователей канала TipTop для США.  
#       TipTop - очень дорогой канал, тянущий деньги;
#     * пользователи США удерживаются стабильно плохо, хуже других стран примерно на 20%
# 2. Каналы  FaceBoom и AdNonSense приводят платящих пользователей с низким качеством, они быстро уходят.   
#     
#   Также, думаю стоит обратить внимание на органический канал-он больше всего приводит пользователей в приложение,  
#   но только 2% переходят в разряд платящих.
#     
# 
# 
# </div>

# ## Чек-лист готовности проекта
# 

# - [x]  положите данные о визитах, заказах и рекламных тратах в переменные
# - [x]  подготовлены данные к анализу 
# - [x]  проверены тип данных во всех колонках на соответствие значениям
# - [x]  проверены данные на отсутствие дубликатов
# - [x]  задана функция для создания пользовательских профилей
# - [x]  задана Функция для расчёта удержания
# - [x]  задана функция для расчёта конверсии
# - [x]  задана функция для расчёта LTV и ROI
# - [x]  задана функция для сглаживания фрейма
# - [x]  задана функция для визуализации удержания
# - [x]  задана функция для визуализации конверсии
# - [x]  задана функция для визуализации LTV и ROI
# - [x]  получили профили пользователей
# - [x]  определили минимальную и максимальную дату привлечения пользователей 
# - [x]  выяснили, из каких стран пользователи приходят в приложение   
# - [x]  выяснили, на какую страну приходится больше всего платящих пользователей
# - [x]  выяснили, какими устройствами пользуются клиенты 
# - [x]  установили ,какие устройства предпочитают платящие пользователи.
# - [x]  определили каналы, из которых пришло больше всего пользователей
# - [x]  установили, из каких каналов пришло больше всего платящих пользователей
# - [x]  посчитали общую сумму расходов на маркетинг
# - [x]  установили общую сумму расходов на меркетинг по каналам привлечения
# - [x]  визуализируем изменения метрик во времени
# - [x]  рассчитали средний CAC на одного пользователя для всего проекта
# - [x]  рассчитали средний CAC для каждого источника трафика
# - [x]  посчитали LTV и ROI
# - [x]  рассчитана окупаемость рекламы  с разбивкой по источникам привлечения
# - [x]  рассчитана окупаемость рекламы с разбивкой по странам
# - [x]  расчитана конверсия и удержание с разбивкой по странам 
# - [x]  расчитана конверсия и удержание с разбивкой по устройствам 
# - [x]  расчитана конверсия и удержание с разбивкой по каналам
# - [x]  в каждом разделе даны промежуточные
# - [x]  есть общий вывод
