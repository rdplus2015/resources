

# ORM - RELATIONSHIP
"""
# Create Superuser
    - python manage.py createsuperuser
# Many to One 
    - class BlogPosts(models.Model):
            author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
            # on_delete = models.CASCADE # SET_DEFAULT, default = 1 # models.PROTECT
    
    >>> from blog.models import BlogPosts as bp
    >>> from django.contrib.auth.models import User as u
    >>> user = u.objects.get(pk=1)
    >>> post = bp.objects.get(pk=1)
    >>> post.author = user
    >>> post.save()
    
# Many to Many
     - class BlogPosts(models.Model):
            author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
            # on_delete = models.CASCADE # SET_DEFAULT, default = 1 # models.PROTECT
            category = models.ManyToManyField(Category) # add category  
            # Category class must be defined before BlogPosts class 
            
    >>> from blog.models import BlogPosts, Category
    >>> bp = BlogPosts.objects.all()
    >>> cat = Category.objects.all()
    >>> bp[0].category.set([cat[0], cat[1]]) 
    >>> bp[0].category.clear() # delete all manytomany relations
    
    #set() methode overwrite older value, use add() for adding
    # we can use variable for do the same operations
    >>> post = BlogPosts.objects.get(pk=1)
    >>> post.category.add(cat[0])
    post.category.remove(cat[0]) # remove one ManyMany relation 

# Reverse operations
    # one to many or Many to Many
    - instance.classnameinmin_set.a()  # can use author filter methods
    >>> cat = Category.objects.get(pk=1)
    >>> cat.blogposts_set.all()
    <QuerySet [<BlogPosts: BlogPosts object (1)>, <BlogPosts: BlogPosts object (2)>]>
"""


# ADMIN DASHBOARD

#Simple
"""
# admin.py
from django.contrib import admin
from blog.models import BlogPost

admin.site.register(BlogPost)

This function allows you to indicate to Django that this model must be present in the administration interface.
"""

#Advaned
"""
To provide a few more options for displaying and editing models, we can create a class that inherits 
from admin.ModelAdmin and use the admin.register decorator

from django.contrib import admin
from blog.models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass
"""

# Admin class managemeent
"""
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display (), list_editable(), list_display_links = (),  search_fields = (), list_filter = (), autocompletfiels()
    empty_value_display = "Unknown"
    list_per_page = 1
    # filter_horizontal 
"""

# custom model
"""
    class Meta: # use it in model 
        verbose_name = 'Article'
    
    def get_absolute_url(self):
        return reverse("blog-post", kwargs={"slug": self.slug}) 
        
    @property
    def word_count(self): # call that property in your admin file in list_display 
        return len(self.content.split()) 
"""


# VIEW BASED ON CLASS

# View

# TemplateView

# Simple way
"""
#view.py
class HomePageView(TemplateView):
    template_name = 'home.html'

#urls.py
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    ]
"""


# return one template and send dynamic data (medium level)
# the advantage is that you have just one methode to write for change context data
"""
#view.py
class BasePageView(TemplateView):
    template_name = None
    title = None # title can contain data from database and be define here 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class HomePageView(BasePageView):
    template_name = 'home.html'
    title = 'Home' # remove if content is from database 

#urls.py 
urlpatterns = [
    path('example/<str:title>/', HomePageView.as_view(), name='example'),
    path('example/', HomePageView.as_view(title='xxx'), name='example'),
]
"""

# Advanced # dynamic template and one Url
"""
templates/
└── base_templates/
    ├── base.html
    └── partials/
        ├── header.html
        └── footer.html
└── pages/
    ├── page1.html
    └── page2.html

# views.py
from django.views.generic import TemplateView
from .models import Page

class DynamicTemplateView(TemplateView):
    base_template_path = 'base_templates/base.html'
    pages_template_path = 'pages/'

    def get_template_names(self):
        page_name = self.kwargs.get('page_name')
        template_name = f"{self.pages_template_path}{page_name}.html"
        return [template_name, self.base_template_path]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_name = self.kwargs.get('page_name')
        page = Page.objects.get(title=page_name)  # Supposons que le titre correspond au nom de la page
        context['page'] = page
        return context
        
Simplicity in URL management: Having a single URL simplifies the configuration in urls.py, reducing the complexity of
managing URLs in your application.

Flexibility of data model: Using a slug in the URL allows your application to be flexible by enabling easy addition, 
modification, and deletion of pages in the database without needing to modify URLs in your application code.

Code reusability: By using a single view to handle all dynamic pages, you can reuse the same code to render different 
pages, reducing code duplication and simplifying maintenance of your application.

Performance: Ensure that the template lookup based on the slug is efficient to avoid performance issues, especially 
if you have a large number of dynamic pages in your application.
"""

# Create View
# Update View
# Delete View


CRUB
# Listview // lister les elements

# from django.views.generic import ListView // recuperer tous les données du models


























# POSTGRESQL

"""
Ubuntu includes PostgreSQL by default. To install PostgreSQL on Ubuntu, use the apt (or other apt-driving) command:
# apt install postgresql

Start and Stop Postgres Server Using the “systemctl” Command
# sudo systemctl status postgresql 

Start the Postgres Server
Use the below-given “sudo” command with the “start” option to begin the Postgres server:
sudo systemctl start postgresql

Stop the Postgres Server
Type the “systemctl” command followed by the “stop” option to halt the Postgres server:
sudo systemctl stop postgresql

# Connexion
La méthode d'authentification configurée pour le serveur PostgreSQL par default est "peer" pour l'utilisateur "postgres"
(l'utilisateur dE OS qui tente de se connecter doit correspondre au compte utilisateur PostgreSQL du même nom)

passer à l'utilisateur "postgres" sur Linux
- sudo su - postgres

Le lien entre l'utilisateur PostgreSQL "postgres" et le système d'exploitation est que PostgreSQL est intégré 
dans le système d'exploitation sur lequel il est installé. Lorsque PostgreSQL est installé, il crée un 
utilisateur système portant généralement le nom "postgres". Ce compte utilisateur est distinct des comptes utilisateurs 
réguliers sur le système d'exploitation.

Lorsque vous exécutez des commandes en tant qu'utilisateur "postgres", vous agissez essentiellement 
sous l'identité de cet utilisateur système spécifique. PostgreSQL utilise ce compte utilisateur pour exécuter ses 
processus et gérer l'accès aux données stockées dans ses bases de données.
Lorsque vous "basculez" ou "passez" à l'utilisateur "postgres" sur votre système d'exploitation, vous changez 
effectivement votre session pour devenir l'utilisateur "postgres". Cela signifie que les actions que vous effectuez 
après cette bascule sont exécutées en tant qu'utilisateur "postgres", avec les autorisations et les privilèges associés 
à cet utilisateur dans le système d'exploitation et dans PostgreSQL.
Cette bascule est souvent nécessaire lorsque vous devez effectuer des actions spécifiques en tant qu'utilisateur 
PostgreSQL, telles que la gestion des bases de données ou l'exécution de commandes SQL via l'interface de ligne de 
commande psql.

IL EXISTE l'authentification par mot de passe pour l'utilisateur "postgres"

connecter à PostgreSQ
- psql

# \du
# \L
# \c dbname 
\dt
# CREATE USER docuser WITH ENCRYPTED PASSWORD "Pwd1010";
# ALTER ROLE docuser SET client_encoding TO 'utf8';
# ALTER ROLE docuser SET default_transaction_isolation TO 'read committed';
# GRANT ALL PRIVILEGES ON DATABASE mblog TO docuser; 

\l (ou \list) : Affiche la liste de toutes les bases de données disponibles.
\c [nom_base_de_données] : Se connecte à la base de données spécifiée.
\dt (ou \d) : Affiche la liste de toutes les tables dans la base de données actuelle.
\d [nom_table] : Affiche la structure de la table spécifiée.
GRANT : Accorde des privilèges à un utilisateur ou un rôle sur une base de données ou une table. Par exemple : GRANT SELECT, INSERT ON nom_table TO nom_utilisateur;
REVOKE : Révoque des privilèges précédemment accordés à un utilisateur ou un rôle. Par exemple : REVOKE SELECT ON nom_table FROM nom_utilisateur;
\q : Quitte l'interface de ligne de commande PostgreSQL.

SQLite :

Avantages :
Léger : SQLite est autonome et ne nécessite pas de processus serveur séparé.
Facile à configurer et à utiliser, surtout pour le développement.
Bon pour les applications de petite à moyenne taille avec une faible à modérée concurrence.
Inconvénients :
Évolutivité et performance limitées par rapport à PostgreSQL et MySQL.
Ne convient pas aux applications de production à grande échelle avec une forte concurrence.
Support limité pour les fonctionnalités avancées telles que les procédures stockées et la recherche en texte intégral.
PostgreSQL :

Avantages :
Hautement évolutif et fiable, adapté aux applications de production à grande échelle.
Ensemble de fonctionnalités complet, y compris le support pour les fonctionnalités SQL avancées, les types de données JSON et la recherche en texte intégral.
Excellent contrôle de la concurrence et conformité ACID.
Fort soutien de la communauté et développement actif.
Inconvénients :
Nécessite plus de ressources par rapport à SQLite et MySQL.
Légèrement plus complexe à configurer et à gérer.
Peut avoir une courbe d'apprentissage plus raide pour les débutants.
MySQL :

Avantages :
largement utilisé et bien pris en charge, surtout dans le développement web.
Bonnes performances, surtout pour les charges de travail en lecture intensive.
Facile à configurer et à gérer, avec une configuration simple.
Convient aux applications de petite à moyenne taille avec une concurrence modérée.
Inconvénients :
Certaines limitations en termes de fonctionnalités par rapport à PostgreSQL, surtout dans les domaines du contrôle de la concurrence et de l'intégrité des données.
Historiquement, il y a eu des préoccupations concernant la licence et la propriété de MySQL, mais celles-ci ont été atténuées avec l'acquisition par Oracle.

psycopg2, qui est un adaptateur PostgreSQL pour Python. 
installer psycopg2 dans votre environnement virtuel. Voici comment vous pouvez le faire :
pip install psycopg2-binary

Oui, lorsque vous utilisez PostgreSQL avec Django, vous avez besoin d'un adaptateur PostgreSQL pour Python, tel que psycopg2, pour permettre à Django de se connecter et d'interagir avec la base de données PostgreSQL.

Donc, si vous utilisez PostgreSQL comme base de données pour votre projet Django, vous devez installer psycopg2 ou un autre adaptateur PostgreSQL compatible avec Django dans votre environnement virtuel. C'est nécessaire pour que Django puisse fonctionner correctement avec votre base de données PostgreSQL.

psycopg2 est l'adaptateur PostgreSQL recommandé pour Django, car il est bien pris en charge et largement utilisé dans la communauté Django. Vous pouvez l'installer dans votre environnement virtuel à l'aide de la commande pip, comme indiqué précédemment :

php

Voici quelques raisons pour lesquelles la version binaire peut être préférée :

Facilité d'installation : La version binaire est précompilée et prête à l'emploi, ce qui signifie qu'elle peut être installée rapidement et facilement avec une simple commande pip install psycopg2-binary.

Évite les problèmes de compilation : La compilation de code source peut parfois être sujette à des problèmes liés aux dépendances système, aux versions de compilateurs, etc. En utilisant la version binaire, vous évitez ces problèmes potentiels.

Portable : La version binaire est généralement portable entre les différentes plateformes et architectures, ce qui signifie que vous pouvez l'utiliser sur différentes configurations système sans avoir à vous soucier de la compatibilité du code source ou des bibliothèques.

Performances : Dans de nombreux cas, il n'y a pas de différence significative de performance entre la version binaire et la version compilée à partir du code source, donc en utilisant la version binaire, vous n'avez pas à sacrifier les performances.

pgAdmin - phpmyadmin - tableplus
https://www.psycopg.org/docs/install.html

