from django.urls import path

from surveysApp import apiviews


app_name = 'surveysApp'
urlpatterns = [
    path('login/', apiviews.login, name='login'),
    # Опросы (surveys)
    path('surveysApp/create/', apiviews.survey_create, name='survey_create'),
    path('surveysApp/update/<int:survey_id>/', apiviews.survey_update, name='survey_update'),
    path('surveysApp/view/', apiviews.survey_view, name='survey_view'),
    path('surveysApp/view/active/', apiviews.active_survey_view, name='active_survey_view'),
    # Вопрос (question)
    path('question/create/', apiviews.question_create, name='question_create'),
    path('question/update/<int:question_id>/', apiviews.question_update, name='question_update'),
    # Выбор (choice)
    path('choice/create/', apiviews.choice_create, name='choice_create'),
    path('choice/update/<int:choice_id>/', apiviews.choice_update, name='choice_update'),
    # Ответ (answer)
    path('answer/create/', apiviews.answer_create, name='answer_create'),
    path('answer/view/<int:user_id>/', apiviews.answer_view, name='answer_view'),
    path('answer/update/<int:answer_id>/', apiviews.answer_update, name='answer_update')

]

