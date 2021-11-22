Время выполнения filter.py: 

![Время выполнения filter.py](https://github.com/angst-storm/IDE/filter-profile.png) 

Время выполнения old_filter.py: 

![Время выполнения old_filter.py](https://github.com/angst-storm/IDE/old_filter-profile.png) 

Согласно этим результатам, filter.py выполнялся дольше old_filter.py. Это можно объяснить тем, что 98.2% времени выполнения filter.py было затрачено на ввод данных. 


Время выполнения filter_with_filename.py:

![Время выполнения filter_with_filename.py](https://github.com/angst-storm/IDE/filter_with_filename-profile.png) 

Благодаря исключению input, время выполнения filter_with_filename.py сократилось значительно относительно filter.py. Также filter_with_filename.py эффективней old_filter.py благодаря оптимизациям (в первую очередь, матричным преобразованиям). 