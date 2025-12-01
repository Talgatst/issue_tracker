from django.urls import path
from webapp.views import IssueListView, IssueDetailView, IssueCreateView, IssueUpdateView, IssueDeleteView

urlpatterns = [
    path('', IssueListView.as_view(), name='issue_list'),
    path('issue/<int:pk>/', IssueDetailView.as_view(), name='issue_detail'),
    path('issue/create/', IssueCreateView.as_view(), name='issue_create'),
    path('issue/<int:pk>/edit/', IssueUpdateView.as_view(), name='issue_update'),
    path('issue/<int:pk>/delete/', IssueDeleteView.as_view(), name='issue_delete'),
]
