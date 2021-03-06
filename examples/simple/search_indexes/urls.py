from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    AddressDocumentViewSet,
    AuthorDocumentViewSet,
    BookCompoundSearchBackendDocumentViewSet,
    BookDefaultFilterLookupDocumentViewSet,
    BookDocumentViewSet,
    BookFunctionalSuggesterDocumentViewSet,
    BookMoreLikeThisDocumentViewSet,
    BookMultiMatchSearchFilterBackendDocumentViewSet,
    BookMultiMatchOptionsPhasePrefixSearchFilterBackendDocumentViewSet,
    BookOrderingByScoreCompoundSearchBackendDocumentViewSet,
    BookOrderingByScoreDocumentViewSet,
    BookSimpleQueryStringSearchFilterBackendDocumentViewSet,
    BookSimpleQueryStringBoostSearchFilterBackendDocumentViewSet,
    CityCompoundSearchBackendDocumentViewSet,
    CityDocumentViewSet,
    PublisherDocumentViewSet,
)

__all__ = ('urlpatterns',)

router = DefaultRouter()

# **********************************************************
# *********************** Addresses ************************
# **********************************************************
addresses = router.register(
    r'addresses',
    AddressDocumentViewSet,
    base_name='addressdocument'
)

# **********************************************************
# ************************* Authors ************************
# **********************************************************
authors = router.register(
    r'authors',
    AuthorDocumentViewSet,
    base_name='authordocument'
)

# **********************************************************
# ************************** Books *************************
# **********************************************************
books = router.register(
    r'books',
    BookDocumentViewSet,
    base_name='bookdocument'
)

books_ordered_by_score = router.register(
    r'books-ordered-by-score',
    BookOrderingByScoreDocumentViewSet,
    base_name='bookdocument_ordered_by_score'
)

books_functional_suggester = router.register(
    r'books-functional-suggester',
    BookFunctionalSuggesterDocumentViewSet,
    base_name='bookdocument_functional_suggester'
)

books_more_like_this = router.register(
    r'books-more-like-this',
    BookMoreLikeThisDocumentViewSet,
    base_name='bookdocument_more_like_this'
)

books_default_filter_lookup = router.register(
    r'books-default-filter-lookup',
    BookDefaultFilterLookupDocumentViewSet,
    base_name='bookdocument_default_filter_lookup'
)

books_compound_search_backend = router.register(
    r'books-compound-search-backend',
    BookCompoundSearchBackendDocumentViewSet,
    base_name='bookdocument_compound_search_backend'
)

books_compound_search_backend_ordered_by_score = router.register(
    r'books-compound-search-backend-ordered-by-score',
    BookOrderingByScoreCompoundSearchBackendDocumentViewSet,
    base_name='bookdocument_compound_search_backend_ordered_by_score'
)

books_multi_match_backend = router.register(
    r'books-multi-match-search-backend',
    BookMultiMatchSearchFilterBackendDocumentViewSet,
    base_name='bookdocument_multi_match_search_backend'
)

books_multi_match_phrase_prefix_backend_ordered_by_score = router.register(
    r'books-multi-match-phrase-prefix-search-backend',
    BookMultiMatchOptionsPhasePrefixSearchFilterBackendDocumentViewSet,
    base_name='bookdocument_multi_match_phrase_prefix_search_backend'
)

books_simple_query_string_backend = router.register(
    r'books-simple-query-string-search-backend',
    BookSimpleQueryStringSearchFilterBackendDocumentViewSet,
    base_name='bookdocument_simple_query_string_search_backend'
)

books_simple_query_string_boost_backend = router.register(
    r'books-simple-query-string-boost-search-backend',
    BookSimpleQueryStringBoostSearchFilterBackendDocumentViewSet,
    base_name='bookdocument_simple_query_string_boost_search_backend'
)

# **********************************************************
# ************************* Cities *************************
# **********************************************************

cities = router.register(
    r'cities',
    CityDocumentViewSet,
    base_name='citydocument'
)

cities_compound_search_backend = router.register(
    r'cities-compound-search-backend',
    CityCompoundSearchBackendDocumentViewSet,
    base_name='citydocument_compound_search_backend'
)

# **********************************************************
# *********************** Publishers ***********************
# **********************************************************

publishers = router.register(
    r'publishers',
    PublisherDocumentViewSet,
    base_name='publisherdocument'
)

# **********************************************************
# ********************** URL patterns **********************
# **********************************************************

urlpatterns = [
    url(r'^', include(router.urls)),
]
