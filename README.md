# Tigers_Segmentation
Проект сегментации амурских тигров.

## Цель проекта 
Обучить модель сегментации на открытом датасете фотографий амурских тигров с использованием архитектуры U-Net

## Описание проекта
Модель сегментации позволит идентифицировать тигров по их уникальным полоскам, что в дальнейшем может быть использовано для подсчета популяции амурских тигров

## Задачи
1) Подготовка данных (Обучение модели YOLOv8 для детекции тигров и создания кропов)
2) Разметка данных (Label Studio с использованием SAM)
3) Обучение модели U-Net
4) Валидация и тестирование данных (метрики для оценки: IoU и F1-Score)

## Участники проекта
- Гребнев Никита
- Романова Виктория
- Соловьев Антон
- Сидоркин Георгий
- Копотев Никита 
- Чудинова Алёна
- Ахаимов Данила

## Использование модели на платформе Google Colab
1) выполнить установку необходимых библиотек в requirements.txt
```python
!pip install segmentation-models-pytorch
!pip install pytorch-lightning==1.5.4
!pip install torchtext==0.6.0
!pip install aspose-zip
```
2) Выполнить импорт размеченного датасета
3) Выполнить импорт необходимых библиотек
```python
import os
import torch
import matplotlib.pyplot as plt
import pytorch_lightning as pl
import segmentation_models_pytorch as smp
import numpy as np

from pprint import pprint
from torch.utils.data import DataLoader
from PIL import Image
```
4) Использовать код 
