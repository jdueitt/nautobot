from django.urls import path

from extras import views
from extras.models import ConfigContext, GitRepository, Status, Tag


app_name = 'extras'
urlpatterns = [

    # Tags
    path('tags/', views.TagListView.as_view(), name='tag_list'),
    path('tags/add/', views.TagEditView.as_view(), name='tag_add'),
    path('tags/import/', views.TagBulkImportView.as_view(), name='tag_import'),
    path('tags/edit/', views.TagBulkEditView.as_view(), name='tag_bulk_edit'),
    path('tags/delete/', views.TagBulkDeleteView.as_view(), name='tag_bulk_delete'),
    path('tags/<str:slug>/edit/', views.TagEditView.as_view(), name='tag_edit'),
    path('tags/<str:slug>/delete/', views.TagDeleteView.as_view(), name='tag_delete'),
    path('tags/<str:slug>/changelog/', views.ObjectChangeLogView.as_view(), name='tag_changelog', kwargs={'model': Tag}),

    # Config contexts
    path('config-contexts/', views.ConfigContextListView.as_view(), name='configcontext_list'),
    path('config-contexts/add/', views.ConfigContextEditView.as_view(), name='configcontext_add'),
    path('config-contexts/edit/', views.ConfigContextBulkEditView.as_view(), name='configcontext_bulk_edit'),
    path('config-contexts/delete/', views.ConfigContextBulkDeleteView.as_view(), name='configcontext_bulk_delete'),
    path('config-contexts/<int:pk>/', views.ConfigContextView.as_view(), name='configcontext'),
    path('config-contexts/<int:pk>/edit/', views.ConfigContextEditView.as_view(), name='configcontext_edit'),
    path('config-contexts/<int:pk>/delete/', views.ConfigContextDeleteView.as_view(), name='configcontext_delete'),
    path('config-contexts/<int:pk>/changelog/', views.ObjectChangeLogView.as_view(), name='configcontext_changelog', kwargs={'model': ConfigContext}),

    # Git repositories
    path('git-repositories/', views.GitRepositoryListView.as_view(), name='gitrepository_list'),
    path('git-repositories/add/', views.GitRepositoryEditView.as_view(), name='gitrepository_add'),
    path('git-repositories/delete/', views.GitRepositoryBulkDeleteView.as_view(), name='gitrepository_bulk_delete'),
    path('git-repositories/edit/', views.GitRepositoryBulkEditView.as_view(), name='gitrepository_bulk_edit'),
    path('git-repositories/import/', views.GitRepositoryBulkImportView.as_view(), name='gitrepository_import'),
    path('git-repositories/<str:slug>/', views.GitRepositoryView.as_view(), name='gitrepository'),
    path('git-repositories/<str:slug>/edit/', views.GitRepositoryEditView.as_view(), name='gitrepository_edit'),
    path('git-repositories/<str:slug>/delete/', views.GitRepositoryDeleteView.as_view(), name='gitrepository_delete'),
    path('git-repositories/<str:slug>/changelog/', views.ObjectChangeLogView.as_view(), name='gitrepository_changelog', kwargs={'model': GitRepository}),
    path('git-repositories/<str:slug>/result/', views.GitRepositoryResultView.as_view(), name='gitrepository_result'),
    path('git-repositories/<str:slug>/sync/', views.GitRepositorySyncView.as_view(), name='gitrepository_sync'),

    # Image attachments
    path('image-attachments/<int:pk>/edit/', views.ImageAttachmentEditView.as_view(), name='imageattachment_edit'),
    path('image-attachments/<int:pk>/delete/', views.ImageAttachmentDeleteView.as_view(), name='imageattachment_delete'),

    # Change logging
    path('changelog/', views.ObjectChangeListView.as_view(), name='objectchange_list'),
    path('changelog/<int:pk>/', views.ObjectChangeView.as_view(), name='objectchange'),

    # Custom jobs
    path('custom-jobs/', views.CustomJobListView.as_view(), name='customjob_list'),
    path('custom-jobs/results/<int:pk>/', views.CustomJobResultView.as_view(), name='customjob_jobresult'),
    path('custom-jobs/<path:class_path>/', views.CustomJobView.as_view(), name='customjob'),

    # Generic job results
    path('job-results/', views.JobResultListView.as_view(), name='jobresult_list'),
    path('job-results/<int:pk>/', views.JobResultView.as_view(), name='jobresult'),
    path('job-results/delete/', views.JobResultBulkDeleteView.as_view(), name='jobresult_bulk_delete'),
    path('job-results/<int:pk>/delete/', views.JobResultDeleteView.as_view(), name='jobresult_delete'),

    # Custom statuses
    path('statuses/', views.StatusListView.as_view(), name='status_list'),
    path('statuses/add/', views.StatusEditView.as_view(), name='status_add'),
    path('statuses/edit/', views.StatusBulkEditView.as_view(), name='status_bulk_edit'),
    path('statuses/delete/', views.StatusBulkDeleteView.as_view(), name='status_bulk_delete'),
    path('statuses/import/', views.StatusBulkImportView.as_view(), name='status_import'),
    path('statuses/<int:pk>/', views.StatusView.as_view(), name='status'),
    path('statuses/<int:pk>/edit/', views.StatusEditView.as_view(), name='status_edit'),
    path('statuses/<int:pk>/delete/', views.StatusDeleteView.as_view(), name='status_delete'),
    path('statuses/<int:pk>/changelog/', views.ObjectChangeLogView.as_view(), name='status_changelog', kwargs={'model': Status}),
]
