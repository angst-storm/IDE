Время выполнения filter.py: 

![Время выполнения filter.py](https://github.com/angst-storm/IDE/blob/master/filter-profile.png) 

Время выполнения old_filter.py: 

![Время выполнения old_filter.py](https://github.com/angst-storm/IDE/blob/master/old_filter-profile.png) 

Согласно этим результатам, filter.py выполнялся дольше old_filter.py. Это можно объяснить тем, что 98.2% времени выполнения filter.py было затрачено на ввод данных. 

---

Время выполнения filter_with_filename.py:

![Время выполнения filter_with_filename.py](https://github.com/angst-storm/IDE/blob/master/filter_with_filename-profile.png) 

Благодаря исключению input, время выполнения filter_with_filename.py сократилось значительно относительно filter.py. Также filter_with_filename.py эффективней old_filter.py благодаря оптимизациям (в первую очередь, матричным преобразованиям). 

---

Изображения:

Исходное:

![Исходное изображение](https://github.com/angst-storm/IDE/blob/master/test_img.png) 

Результат работы old_filter.py:

![Результат работы old_filter.py](https://github.com/angst-storm/IDE/blob/master/old_result.png) 

Результат работы filter.py:

![Результат работы old_filter.py](https://github.com/angst-storm/IDE/blob/master/result.png)

---

Исполнение тестов для median_gray():

![Исполнение тестов для median_gray()](https://github.com/angst-storm/IDE/blob/master/doctest-median_gray.png) 

Все тесты пройдены. Написание тестов на gray_pixelation() слишком тяжело, так как возвращаемое значение - изображение.

---

Результат инспектирования:

![Результат инспектирования](https://github.com/angst-storm/IDE/blob/master/inspect.png) 

Замечаний к коду нет, помимо дублирования кода в filter.py и filter_with_filename.py (обусловлено прошлыми заданиями).

---

Работа с отладчиком.

Тип изображения (JPEG, выделено):

![Тип изображения](https://github.com/angst-storm/IDE/blob/master/image-format.png) 

Высота изображения (933, выделено):

![Высота изображения](https://github.com/angst-storm/IDE/blob/master/image-height.png) 

Ширина изображения (934, выделено):

![Ширина изображения](https://github.com/angst-storm/IDE/blob/master/image-width.png) 

Размер блока (10):

![Размер блока](https://github.com/angst-storm/IDE/blob/master/block-size.png) 

Число градаций серого (5):

![Число градаций серого](https://github.com/angst-storm/IDE/blob/master/gradations-count.png) 