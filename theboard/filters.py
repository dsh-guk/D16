from django.forms import DateInput, SelectDateWidget
from django_filters import FilterSet, DateFromToRangeFilter    # импортируем filterset 
from django_filters.widgets import RangeWidget

from .models import Post
 

# создаём фильтр
class PostFilter(FilterSet):
    post_date = DateFromToRangeFilter(label='Dates From To Range', widget=RangeWidget(attrs={'type': 'date'}))
    
    class Meta:
        model = Post
        # поля, которые мы будем фильтровать (т. е. отбирать по каким-то критериям, имена берутся из моделей)
        fields = {            
            'title': ['icontains'],  # по названию публикации            
            'category': ['exact'],  # по категории
        }

