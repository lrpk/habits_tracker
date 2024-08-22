from django.shortcuts import render, redirect
from .models import Habits
from django.utils import timezone

def habits_view(request):
    habits = Habits.objects.all()

    if request.method == "POST":
        for habit in habits:
            checkbox_value = request.POST.get(f"habit_{habit.id}")  # Отримуємо значення чекбокса для конкретної звички
            if checkbox_value:
                # Перевіряємо, чи це сьогоднішня відмітка
                if not habit.is_checked_today or habit.last_checked != timezone.now().date():
                    habit.strike_count += 1
                    habit.last_checked = timezone.now().date()
                    habit.is_checked_today = True
                    habit.save()
        return redirect('habits_view')  # Перенаправлення на ту ж сторінку для запобігання повторного сабміту

    # Скидаємо відмітку на початку нового дня
    for habit in habits:
        if habit.last_checked != timezone.now().date():
            habit.is_checked_today = False
            habit.save()

    return render(request, 'my_site/habits_template.html', {'habits': habits})
