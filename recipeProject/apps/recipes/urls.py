from django.urls import path
from . import views #pylint: disable = E0402

urlpatterns = [
    path('home', views.home), # GET only
    path('yours', views.yours), # GET only
    path('new', views.new), # GET only
    path('create', views.create), # POST only
    path('<int:n>', views.show), # if GET then show page, if DELETE then delete entry, if POST then update data
    path('<int:n>/edit', views.edit), # if GET then show edit page
    path('<int:n>/delete', views.confirmDelete), # GET only
    path('<int:n>/delete/yes', views.delete), # delete on confirmation
    path('<int:n>/ajax', views.showAjax), # fetch location of single recipe
    path('books/new', views.newBook), # GET only
    path('books/create', views.createBook), # POST only
    path('books/<int:n>', views.showBook), # if GET then show page, if DELETE then delete entry, if POST then update data
    path('books/<int:n>/edit', views.editBook), # if GET then show edit page
    path('books/<int:n>/delete', views.confirmDeleteBook), # GET only
    path('books/<int:n>/delete/yes', views.deleteBook), # delete on confirmation
    path('mapsearch', views.mapSearch), # GET only
    path('mapsearch/ajax', views.mapSearchAjax), # AJAX nonsense
    path('search', views.search), # if GET then show search page, if POST then do search stuff
    path('search/results', views.searchResults), # GET only
    # path('ingsearch', views.ingSearch), # if GET then show search page, if POST then do search stuff
    path('logout', views.logout_view),
]