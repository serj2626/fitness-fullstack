import django_filters

from .models import CoachReview


class CoachReviewFilter(django_filters.FilterSet):
    # 🔥 Кастомный параметр sort с понятными значениями
    sort = django_filters.ChoiceFilter(
        choices=[
            ("newest", "Сначала новые"),
            ("oldest", "Сначала старые"),
            ("rating_high", "Высокий рейтинг"),
            ("rating_low", "Низкий рейтинг"),
        ],
        method="filter_sort",
    )

    class Meta:
        model = CoachReview
        fields = ["coach", "rating"]

    def filter_sort(self, queryset, name, value):
        if value == "newest":
            return queryset.order_by("-created_at")
        elif value == "oldest":
            return queryset.order_by("created_at")
        elif value == "rating_high":
            return queryset.order_by("-rating", "-created_at")
        elif value == "rating_low":
            return queryset.order_by("rating", "created_at")
        return queryset
