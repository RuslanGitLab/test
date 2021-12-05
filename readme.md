# Данный проект содержит код обсуждаемый в блоге: https://www.youtube.com/channel/UCsiciSevtM1q0VrOs7ics0g
# Ссылка на репозиторий: https://gitlab.soaqa.ru/Soaqa/youtube_project
# Версия Python == 3.9.0
## Вы можете использовать представленный в данном проекте код как вам заблагорассудится. 
## При желании вы можете запросить доступ к проекту и делать merge requests, ставя в поле Assignee пользователя @SoaQa/ Bogdan Soloviev

# Комментарии к видео, запуск и настройка
## GenericForeignKey - запуск проекта и тестов
* Склонируйте проект `git clone https://gitlab.soaqa.ru/Soaqa/youtube_project` и переключитесь на ветку `generic_foreign_key`
* Создайте python virtual environment `python3.9 -m venv venv`, активируйте его и установите зависимости из `requirements.txt`
* Выполните миграции `python manage.py migrate` 
* запустите тесты командой `python manage.py test core`