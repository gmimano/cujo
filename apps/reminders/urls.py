from django.conf.urls.defaults import patterns, url

from reminders.forms import ReminderForm_days

urlpatterns = patterns('reminders.views',
    url(r'^list/$', 'reminder_list', (), 'reminder_list'),
    url(r'^list/all/$', 'reminder_list', ({'view_all': True}), 'reminder_list_all'),
    url(r'^list/expired/now/$', 'expired_remider_list', (), 'expired_remider_list'),
    url(r'^list/expired/now/all/$', 'expired_remider_list', ({'view_all': True}), 'expired_remider_list_all'),
    url(r'^list/expired/future/$', 'future_expired_remider_list', (), 'future_expired_remider_list'),
    url(r'^list/expired/future/all/$', 'future_expired_remider_list', ({'view_all': True}), 'future_expired_remider_list_all'),
    url(r'^add/date/$', 'reminder_add', (), 'reminder_add'),
    url(r'^add/days/$', 'reminder_add', ({'form_class': ReminderForm_days}), 'reminder_add_days'),
    url(r'^(?P<reminder_id>\d+)/edit/date/$', 'reminder_edit', (), 'reminder_edit'),
    url(r'^(?P<reminder_id>\d+)/edit/days/$', 'reminder_edit', ({'form_class': ReminderForm_days}), 'reminder_edit_days'),
    url(r'^(?P<reminder_id>\d+)/$', 'reminder_view', (), 'reminder_view'),
    url(r'^(?P<reminder_id>\d+)/delete/$', 'reminder_delete', (), 'reminder_delete'),
    url(r'^multiple/delete/$', 'reminder_multiple_delete', (), 'reminder_multiple_delete'),
    url(r'^(?P<reminder_id>\d+)/participant/add/$', 'participant_add', (), 'participant_add'),
    url(r'^(?P<reminder_id>\d+)/participant/list/$', 'participant_list', (), 'participant_list'),
    url(r'^participant/(?P<participant_id>\d+)/remove/$', 'participant_remove', (), 'participant_remove'),
)
