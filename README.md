
<img src="ekbana.png" alt="drawing" style="width:200px; float:right"/>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<h1 style="text-align:center">Python Report</h1>
<h2 style="text-align:center">A complete guide to python</h2>

<h3 style="text-align:center">(In this report I have covered the overall concept of python and python framework)</h3>
<br><br><br>
<br>

<h3 style="text-align:center">Presented by:</h3>
<h3 style="text-align:center">Tankman Sodari</h3>
<h3 style="text-align:center">(Python Trainee)</h3>
<br><br>
<br><br>


# Introduction to Git and Github
A git is the version control system. Version control means tracking the change in the system. We can save the initial version of our code into the git, and when we update the code, we again save our code into the git. It helps to track down the bug as well as go back to the previous version of the code.

GitHub is a place where git repositories are hosted.GitHub serves as a location for uploading copies of a Git repository.stored. There are two types of repository
1. Local repository
    - This is the Working Directory
2. Remote Repository
    - This is the repository that we created manually on Github
<br>
<br>

**How to Add a File to a Git?**

- **git ini**t -this command creates the local repo
- **git status** - this command tracks down the changes
- **git add.**  -stages new files and modifications, without deletions
- **git add .A**  -stages all changes
- **git commit -m "my commit"** 
  
Now after committing, push the staging file to a remote repo that was created manually.
  - **git remote add origin "remote repo link"**
  
The connection was established between the local and remote repo. 

After this, push the remote repo in the default branch
  - **git push origin master**

If we change the file from the remote repo then we must pull the file to the local repo to save the changes
  - **git pull origin master**
<br>
<br><br>

**Branching and Merging**

Git branching allows developers to diverge from the production version of code to fix a bug or add a feature. Developers create branches to work with a copy of the code without modifying the existing version. i.e different people can create a different branch and write different code for testing and so on without modification of the main code.
Git merging combines sequences of commits into one unified history of commits

***how to work with the branch*?**
- **git branch** <br>
    (list all the branches, the Master branch is the default working branch)
- **git branch python-day-1** <br>
(Creates a new branch,python-day-1 is the branch name, also called feature branch )
- **git checkout python-day-1** <br>
(Switch to the tanka branch, now python-day-1 is the working branch)
- **git add .**<br>
(If you have added a  new file  or have changed some code)
- **git commit -m "my commit"**
- **git push origin python-day-1**

**Note:** these changes are only for the feature branch and won't apply in the master branch until the merging process won't happen.

***how to work with the Merging?***

Now merge the Feature Branch into the Master Branch.<br>
**Note:** If you want to merge the Feature Branch into Master Branch first switch the branch into Master Branch
- **git checkout master** <br>
Now you can merge the branch
- **git merge python-day-1**
- **git push origin master**
<br>
<br>

***Conflict in Merging***

Git can handle most merges on its own with automatic merging features. A conflict arises when two separate branches have made edits to the same line in a file, or when a file has been deleted in one branch but edited in the other. Conflicts will most likely happen when working in a team environment.

![conflit image](pull-push.jpg)

Let’s assume there are two developers: Developer A and Developer B. Both of them pull the same code file from the remote repository and try to make various changes to that file. After making the changes, Developer A pushes the file back to the remote repository from his local repository. Now, when Developer B tries to push that file after making the changes from his end, he is unable to do so, as the file has already been changed in the remote repository.
To prevent such conflicts, developers work in separate isolated branches. The Git merge command combines separate branches and resolves any conflicting edits.

***How to Resolve Merge Conflicts in Git?***

There are a few steps that could reduce the steps needed to resolve merge conflicts in Git.

1. The easiest way to resolve a conflicted file is to open it and make any necessary changes
2. After editing the file, we can use the git add a command to stage the new merged content
3. The final step is to create a new commit with the help of the git commit command
4. Git will create a new merge commit to finalize the merge

Let us now look into the Git commands that may play a significant role in resolving conflicts.

***Git Commands to Resolve Conflicts***

The git log --merge command helps to produce the list of commits that are causing the conflict
  - **git log --merge**

The git diff command helps to identify the differences between the state's repositories or files
 - **git diff** 

The git checkout command is used to undo the changes made to the file, or for changing branches
 - **git checkout** 

The git reset --mixed command is used to undo changes to the working directory and staging area
 - **git reset --mixed** 

The git merge --abort command helps in exiting the merge process and returning back to the state before the merging began
 - **git merge --abort**

The git reset command is used at the time of merge conflict to reset the conflicted files to their original state
 - **git reset**

<hr>
<br><br>
<br><br>


# Introduction to Basic Python  

Python is a high-level, general-purpose programming language. Python is a simple and easy-to-understand language that feels like reading simple English. The pseudo-code of python is easy to learn by beginners.

**Features**

- Easy to understand
- Free and open source
- Portable and high-level language

**<u>Modules, comments, and pip</u>**

Modules are those codes written by others and we just import them. There are build-in and external modules.

Comments can be used to explain Python code. Comments can be used to make the code more readable. there are two types of comment 

- Single-line:  #single line comment
- Multiline:    ''' multi-line comment'''

PIP is the package manager for python and uses to install modules and packages.
For e.g pip install django

**<u>Varialbles and datatypes</u>**

**Variable** is the container to store a value. eg. name="ram". keywords are the reserved word in python such as def, class, etc. Each variable may have a different type of data.

    name="ram"
    print(type(name))

Output
    
    <class 'str'>
<br>

**<u>String</u>**

Python String is an immutable sequence of Unicode characters. In Python, str class handles string objects, and strings are of type str. To define a string literal, you can use single quotes, double quotes, or triple quotes.

    str1 = 'hello world!' #single quotes
    str2 = "hello world!" #double quotes
    str3 = """hello world!""" #triple quoted with   double quotes
    str4 = '''hello world!''' #triple quoted with   single quotes

*String slicing:*

String slicing helps to get some character in the string.

    str = "hello world!"
    print(str[0])

Output:

    h
<br>

    str = "hello world!"
    print(str[0:4])

Output:

    hell

The string has different methods and all string methods return new values. They do not change the original string. Some methods are capitalize(),count(),endswith(),islower(),find() and so on

**<u> List and Tuple</u>**

Lists are used to store multiple items in a single variable with different types.

    list=['apple',12,"ball"]

String has different methods such as pop(),sort(),reverse(),append(),insert().remove() and many more.
Tuples are the same as lists but tuple is immutable i.e, they won’t change once it is created. Tuples have some methods such as count() and index().

**<u>Dictionary and Set</u>**

Dictionary is used to store key-value pairs. A dictionary is a collection that is ordered*, changeable, and does not allow duplicates.

    dict={
        'name':'tanka',
        'age':23
    }

Dictionary methods are item(),keys(),update({‘key’:’value’}),get(‘key’) and so on
A Set is a collection of unordered items. Each element in the set must be unique, and immutable, and the sets remove the duplicate elements.

    set={1,2,3,4,'tankman',6}

Set methods are len(),remove(),pop(),clear() and so on.

**<u>Conditional Statement</u>**

*if, else and elif*

    if (condition1):
        //code
    elif (condition2):
        //code
    else:
        //code

**<u>Loops</u>**

while,
do while,
for

    for i in range(8):
        print(i)

<u>Functions</u>

    def functionname():
        //code
    functionname()
<br>

**Object-Oriented Programming**

**<u>Class and Object:</u>**

The class is a blueprint for creating objects. For eg, a class is an empty form/template and when we add something to that form then it becomes the object of that form. An object is an instantiation of the class.

    class form:
    def func(self):
        print(f"my name is {self.name}")
        print(f"my age is {self.age}")
    obj=form()
    obj.name="tankman"
    obj.age=23
    obj.func()

Output

    my name is tankman
    my age is 23

**<u>Constructor</u>**

Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. In Python the __init__() method is called the constructor and is always called when an object is created.

    class Ekbana:
        # default constructor
        def __init__(self):
            self.name = "Ekbana"
        # a method for printing data members
        def func(self):
            print(self.name)
    obj = Ekbana()
    obj.func()

Output

    Ekbana
<hr>
<br>


    class Add:
        a = 0
        b = 0
        def __init__(self, num1, num2):
            self.num1 = num1
            self.num2 = num2
        def calculate(self):
            self.answer = self.num1 + self.num2
            print(f"the sum is: {self.answer}")
    obj = Add(2, 3)
    obj.calculate()

Output

    the sum is: 5
<hr>
<br><br>

**<u>Inheritance</u>**

Inheritance allows us to define a class that inherits all the methods and properties from another class.

**Parent class** is the class being inherited from, also called the base class.

**Child class** is the class that inherits from another class, also called the derived class.

    class Employee:
        company="ekbana"
        def detail(self):
            print(f"this is {self.company} company")  
    class Program(Employee):
        lang="python"
        def showdetail(self):
            print(f"this is {self.lang} langauge and learning in {self.company}")
    e=Employee()
    e.detail()
    p=Program()
    p.showdetail()

Output

    this is ekbana company
    this is python langauge and learning in ekbana
<hr>

    class Company:
        def __init__(self,name,age):
            self.name=name
            self.age=age  
        def power(self):
            print(f"this is {self.name} company and is {self.age} year old")
    class Employee(Company):
    
        def sal(self,ename,salary):
            print(f'the name is {ename} and salary is {salary} and from {self.name} company')
    comp=Company('ekbana',12)
    comp.power()
    emp=Employee("Ekbana",10)
    emp.sal("tankman",300000)

Output

    this is ekbana company and is 12 year old
    the name is tankman and salary is 300000 and from Ekbana company

**<u>Encapsulation</u>**

Encapsulation in Python describes the concept of bundling data and methods within a single unit.

    class Employee:
        def __init__(self,name):
            self.__name=name
            # indicate the name is protected
        def get(self):
            print(f"my name is {self.__name}")
    class Ram(Employee):
        def getprivate(self):
            print(f"my name is {self.__name}")
    obj=Employee("tankman")
    print(obj._Employee__name)
    obj1=Ram("ram")
    obj1.getprivate()
    # this above code throw the error
    # so how to solve this, well once we decleared the property private is only access inside the class

**<u>Abstraction</u>**

Abstraction in python is defined as a process of handling complexity by hiding unnecessary information from the user. This is one of the core concepts of object-oriented programming (OOP) languages.

    from abc import ABC, abstractmethod
    class Car(ABC):
        def __init__(self,name):
            self.name = name
        def description(self):
            print("This the description function of class car.")
        @abstractmethod
        def price(self,x):
            print(f"The {self.name}'s price is {x} lakhs.")
            print("hello")
    class new(Car):
        def price(self,x):
            print(f"The {self.name}'s price is {x} lakhs.")
    obj = new("Honda City")
    obj.description()
    obj.price(25)

Output

    TypeError: Can't instantiate abstract class Abstract with abstract method get

**<u>Polymorphism</u>**

Polymorphism in python defines methods in the child class that have the same name as the methods in the parent class.

    class Ram:
    def about(self):
        print("This the  ram.")
    class Hari:
    def about(self):
        print("This the  hari.")
    obj1 = Ram()
    obj2 = Hari()
    for car in (obj1,obj2):
    car.about()

Output

    This the  ram.
    This the  hari.

**<u>Static Method</u>**

The methods, which are bound to a class rather than its object. Used when some processing is related to the class but doesn't need the class or its instance to perform it.

    class Static_Method:
        @staticmethod
        def get(n,r):
            name=n
            roll=r
            print(f"my name is {name} and roll is {roll}")
    obj=Static_Method()
    Static_Method.get("tankman",15)

Output

    my name is tankman and roll is 15

**<u>Class Method</u>**

A class method is a method that is bound to a class rather than its object. It doesn't require the creation of a class instance, much like the static method. The difference between a static method and a class method is: Static method knows nothing about the class and just deals with the parameters.

    class Class_Method:
        fp="yes"        #class variable
        @classmethod     #decorator
        def myfunc(cls,r):   #class method
            cls.r=r
            print(f"holiday ? :{cls.fp} and is very {cls.r} ")
    obj=Class_Method()
    Class_Method.myfunc("strict")  #calling class method

Output

    holiday ? :yes and is very strict

**<u>Lambda Expression</u>**

A lambda expression is a breakdown of a function into one line, used when you want to use a function only one time and it returns a value.

    x=lambda a,b: a*b
    res=x(5,3)
    print(res)

Output

    15

**<u>Datetime</u>**

The date contains the year, month, day, hour, minute, second, and microsecond. The DateTime module has many methods to return information about the date object.

    import datetime
    x=datetime.datetime.now()
    print(x.year)
    print(x.strftime("%A"))

Output

    2022
    Saturday

<hr><br>
<br>
<br>

# Introduction to Django Rest Framework

**<u>Application Programming Interface(API)</u>**

An API is a software intermediary that allows two or more applications to talk to each other. For e.g waiter.

![APi](api.png)

**How does API Work?**

![APi work](api%20work.png)

**REST**

REST is the guideline to develop web API


**REST API/RESTFul API**

The API which is developed using REST

**CRUD Operations**

![](crud.png)

**Django Rest Framework**

DRF is a powerful and flexible toolkit for building web Api.

*Why DRF?*

- It has web browsable API used to test our API during development
- Authentication policies including packages for OAuth1 and OAuth2
- Serializer supports ORM and non ORM data

**Serializer**

In DRF, serializers are responsible for converting complex data such as queryset and model instances to native python datatype called serialization.

**Querset** - Overall database data

**Instance** - particular obj of database

**Native python datatype** - dictionary

Then the data can easily be rendered into JSON, XML format which is understandable for the frontend.

It has 2 methods:
- Dumps: convert python obj to JSON string
- Loads: used to parse JSON string

![](serializer.png)

**Deserializer**

The process of converting JSON data into query sets or complex data types is called deserialization. The above figure explains the both serialization and deserialization process.

**Validation in DRF**

1. Field level validation

	This validation is used for single field

        def validate_roll(self,value): #field level validation
            if value>=100:
                raise serializers.ValidationError("Roll Must be under 100")
            return value
2. Object level validation

    This validation is used for multiple fields

        def validate(self, data):#object leve validation
        naam=data.get('name')
        rol=data.get('roll')
        ct=data.get('city')
        if naam.lower()=='aakash' and ct.lower()!='pataal':
            raise serializers.ValidationError(" city must be paatal")
        return data

3. Validator

    This is used for custom validation on field

        def mustvowel(value):
        for i in value:
            if(i!='a' or i!='e' or i!='i' or i!='o' or i!='u' or i!='A' or i!='E' or i!='I' or i!='O' or i!='U'):
                raise serializers.ValidationError("Name must contain vowel letter")
            return value

**Model Serializer**

It include simple default implementation of create() and update() method
It inherits the overall mode class properties in the serailizer which reduce the burden on writing code.

    class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
 
**API_VIEW**

The APIView is the most basic type of view we can use to build our API. It enables us to describe the logic which makes our API endpoint. An APIView allows us to define functions that match the standard HTTP methods: GET, POST, PUT, PATCH, DELETE.

    @api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
    class StudentAPI(APIView):
    def get(self):
        pass
    def post(self, request):
        pass
    def put(self, request):
        pass        
    def patch(self, request):
       pass  
     def delete(self,id):
        pass

**Authentication and Permissions**

Currently, in the above API, we haven't applied any restrictions, so anyone with the URL can access the data and can able to alter the data. Hence Authentication and Permission are needed.
Authentication

In DRF we have the following types of Authentications:

1. **Basic Authentication**
    - Basic authentication is needed only for testing purposes while deployment.
    - It requires a simple Username and Password for an authentication
    - request.user will be a Django user instance

            #In setting.py
            REST_FRAMEWORK={
                'DEFAULT_AUTHENTICATION_CLASSES':['rest_framework.authentication.
            BasicAuthentication'],
            }
            #in views.py
            authentication_classes = [BasicAuthentication]

2. **Session Authentication**

    - It uses Django default session backend for authentication
    - request.user will be Django user 
    - instance request.auth will be None

            #In setting.py
            REST_FRAMEWORK={
                'DEFAULT_AUTHENTICATION_CLASSES':['rest_framework.authentication.
            SessionAuthentication],
            }
            #in views.py
            authentication_classes = [SessionAuthentication]

3)**Token Authentication**
   - The token authentication schema uses a simple token-based HTTP authentication schema.
   - Token authentication is appropriate for client-server setups,such as native desktop and mobile clients
   - Make sure to run py manage.py makemigrations changing in the setting because it provides Django database migrations
   - request.user will be Django user instance
   - request.auth will be rest_framework.authtoken.model.token instance

*How to generate token?*

- Using admin application
- Using django command prompt
- By exposing an API endpoint
- By using signals

*How to use token Authentication*

    #Get Request
    http http://127.0.0.1:8000/api/
    
    #Post Request with auth
    http http://127.0.0.1:8000/api/ 'Authorization: Token 1234567890tghbsdfyesff'
    
    #Post Request or submitting form
    http -f POST http://127.0.0.1:8000/api/ name=Tankman address=tikapur 'Authorrization: Token 1234567890tghbsdfyesff'
    
    #Put Request
    http PUT http://127.0.0.1:8000/api/1/ Authorization: Token 1234567890tghbsdfyesff'
    
    #Delete Request
    http DELETE http://127.0.0.1:8000/api/1/ Authorization: Token 1234567890tghbsdfyesff'

**Permissions**

Permissions are used to grant or deny access for different classes of users to different parts of the API. Permission checks are always run at the very start of the view before any other code is allowed to proceed. Permission checks will typically use the authentication information in the request.user and request.auth properties to determine if the incoming request should be permitted.

There are the following methods in the permissions

- AllowAny
- IsAuthenticated
- IsAdminUser
- IsAuthenticatedOrReadOnly
- DjangoModelPermissions
- DjangoModelPermissionsOrAnonReadOnly
  
        #In setting.py
        REST_FRAMEWORK={   'DEFAULT_PERMISSION_CLASSES':['rest_framework.permissions.AllowAny],
        }
        #in views.py
        permission_classes = [IsAuthenticated]

**JSON Web Token & Simple JWT Authentication**

- It is a third-party package used for token-based authentication
- It is better than other authentication methods because it doesn't store the token in the database. Hence it doesn’t take time to check the given token to the database and if matches then perform the operations, which results in increasing the performance.
- Simple JWT provides a JSON web token authentication backend for the Django REST framework.
- pip install djangorestframework_simplejwt
- To use JWT, we need to configure in the setting.py

        REST_FRAMEWORK = {
            'DEFAULT_AUTHENTICATION_CLASSES': (
                'rest_framework_simplejwt.authentication.JWTAuthentication',
            ),
            'DEFAULT_PERMISSION_CLASSES':(
                'rest_framework.permissions.IsAuthenticated'),
        }

- The urls.py will be

        urlpatterns = [
        path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
        path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),
        path('verifytoken/',TokenVerifyView.as_view(),name='token_verify'),   
        ]

*How to get tokens using the command line?*

    #First get token
    http POST http://127.0.0.1:8000/api/gettoken/ username=”xyz” password=”xyz
    #verify the token
    http POST http://127.0.0.1:8000/api/verifytoken/ token=”1213124123asasda”
    #refresh token
    http POST http://127.0.0.1:8000/api/refreshtoken/ refresh=”1213124123asasda”
 


*Note: In Postman we can easily generate and test the token
*

    #views.py
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

*How to use the Token?*

    http http://127.0.0.1:8000/api/
    #It requires authentication credential
    
    #Get Request
    http http://127.0.0.1:8000/api/ ‘Authoriation:Bearer 12323425qwqeasdas
    
    #Post Request 
    http -f POST http://127.0.0.1:8000/api/ name=Tankman address=tikapur 'Authorrization: Bearer 1234567890tghbsdfyesff'
    
    #Update Request
    http PUT http://127.0.0.1:8000/api/1/ ‘Authoriation:Bearer 12323425qwqeasdas’
    
    #Delete Request
    http DELETE http://127.0.0.1:8000/api/1/ ‘Authoriation:Bearer 12323425qwqeasdas’

<hr>
<br><br><br>

# Introduction to Django 

Django is one of the popular python frameworks. It is used for web applications (both frontend and backend). It easily handles JSON response and database connector. It follows MVT architecture.

![MVT](mvt.png)

This diagram explains the overall concept of MVT architecture.

**Models**

The models indicate the table in the database. Each field represents the column and we must register the model and migrate it.

    py manage.py makemigrations
    Py manage.py migrate

**Static**

The static files are those files that anyone can easily access. for eg images, text, and so on. Static files are always under the static folder. For a dynamic URL, we must load the static first.

    {% load static %}

**Templates**

Templates are the .html file, which is also called frontend files. We can easily inherit the templates as well as include the template in the current template.

    {% extends 'core/main.html' %}
    {% include 'core/status.html' %}

**ORM**

Object Relational Mapping is the method of playing with the database data. It helps to create, update, delete, read and perform overall CRUD operations.

    data = Customer.objects.all()
    orderdelivered = Order.objects.filter(status='Delivered').count()

**User Registration**

As you may have seen, Django comes with a built-in user registration form. We just need to configure it to our needs (i.e. collect an email address upon registration).
forms.py

    class RegisterForm(UserCreationForm):
        class Meta:
            model = User
            fields = ['__all__']

Django comes with a pre-built register form called UserCreationForm that connects to the pre-built model User. However, the UserCreationForm only requires a username and password (password1 is the initial password and password2 is the password confirmation). 

**User Login**

we want the user to have the ability to login freely. So we need a login template, URL, and views function.
forms.py

    class LoginForm(AuthenticationForm):
        username = UsernameField(widget=forms.TextInput(
            attrs={'class': 'form-control', 'autofocus': True}))
        password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
            render_value=True, attrs={'class': 'form-control', 'autocomplete': 'current-password'}))

AuthenticationForm is the pre-built Django form logging in a user. To write your login function, add an if/else statement that uses the Django function to authenticate(). This function is used to verify user credentials (username and password) and return the correct User object stored in the backend. If the backend authenticates the credentials, the function will run Django login() to log in to the authenticated user. Else if the user is not authenticated, it returns a message to the user stating they entered an invalid username or password.
views.py

    if fm.is_valid():
                fname = fm.cleaned_data['username']
                ps = fm.cleaned_data['password']
                user = authenticate(username=fname, password=ps)
                if user is not None:
                    login(request, user)
                    return redirect('/')

**User Model**

The default User model in Django uses a username to uniquely identify a user during authentication. If we want to use an email address, we'll need to create a custom User model by either subclassing AbstractUser or AbstractBaseUser

**Extending the User model using AbstractUser**

Django’s built-in authentication system is great. For the most part, we can use it out-of-the-box, saving a lot of development and testing effort. It fits most of the use cases and is very safe. But sometimes we need to do some fine adjustments to fit our Web application. Commonly we want to store a few more data related to our User. If your Web application has a social appeal, you might want to store a short bio, the location of the user, and other things like that.

The Custom User model is a new User model that inherits from AbstractUser. It requires special care and updating some references through the settings.py. Ideally, it should be done at the beginning of the project, since it will dramatically impact the database schema. Extra care while implementing it.

***When should we use a Custom User Model Extending AbstractUser?***

We should use it when you are perfectly happy with how Django handles the authentication process and you wouldn’t change anything on it. Yet, you want to add some extra information directly to the User model, without having to create an extra class.

1. First we need to create a custom User model  from AbstractUser

        from django.contrib.auth.models import AbstractUser
        from .manager import UserManager
    
        class User(AbstractUser):
        username=None
        email=models.EmailField(_('Email address'),unique=True)
        bio=models.TextField(max_length=200,null=True,blank=True)
        last_logout_time=models.DateTimeField(null=True,blank=True)
    
        objects = UserManager()
        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = []
    
        def __str__(self):
            return self.email

2. Add Auth_user in setting.py

        AUTH_USER_MODEL ='myapp.User'

3. create a ModelManager to manage the Custom User in manage.py. 

    The default user manager has some default methods like create_user and create_superuser and we can also override our default methods.

        from django.contrib.auth.base_user import BaseUserManager
        class UserManager(BaseUserManager):
        use_in_migrations = True
        def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
 
        def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
 
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

**Extending the User model using AbstractBaseUser**

It is an entirely new User model that inherits from AbstractBaseUser. It requires special care and updating some references through the settings.py. Ideally, it should be done at the beginning of the project, since it will dramatically impact the database schema. Extra care while implementing it. 

***When should we use a Custom User Model Extending AbstractBaseUser?***

You should use a Custom User Model when your application has specific requirements in relation to the authentication process. For example, in some cases, it makes more sense to use an email address as your identification token instead of a username.

1. First we need to create a custom User model from AbstracBaseUser with default permission
   
        from django.contrib.auth.models import      AbstractBaseUser, PermissionsMixin
        class User(AbstractBaseUser, PermissionsMixin):
        email = models.EmailField(_("Email Address"), max_length=254, unique=True)
        user_name = models.CharField(max_length=50, unique=True)
        first_name = models.CharField(max_length=50)
        start_date = models.DateTimeField(default=timezone.now)
        about = models.TextField(_('About'), max_length=200, blank=True, null=True)
        is_staff = models.BooleanField(default=False)
        is_active = models.BooleanField(default=False)
    
        objects = CustomUser()
        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['user_name','first_name']
    
        def __str__(self):
            return self.user_name

2. Add Auth_user in setting.py

        AUTH_USER_MODEL ='myapp.User'

3.  create a ModelManager to manage the User in manage.py.

        from django.contrib.auth.base_user import BaseUserManager
 
        class CustomUser(BaseUserManager):
        use_in_migrations=True
    
        def create_user(self,email,user_name,first_name,password,**extra_fields):
            if not email:
                raise ValueError('The must provide email address')
            email = self.normalize_email(email)
            user = self.model(email=email,user_name=user_name,first_name=first_name, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user
    
        def create_superuser(self,email,user_name,first_name,password,**extra_fields):
            extra_fields.setdefault('is_superuser', True)
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_active', True)
    
            if extra_fields.get('is_superuser') is not True:
                raise ValueError('Superuser must have is_superuser=True.')
            if extra_fields.get('is_staff') is not True:
                raise ValueError('Superuser must have is_staff=True.')
            if extra_fields.get('is_active') is not True:
                raise ValueError('Superuser must have is_sactive=True.')
    
            return self.create_user(email,user_name,first_name,password,**extra_fields)
<br><br>
<hr>

**.ENV FILES**

Applications are made to be deployed. At some point during development, we will need to think about the environment in which our application will run and whether it contains sensitive info or not. The process of setting or changing an environment variable is time-consuming and over time the number of environment variables we have to manage grows out of control. Eventually naming conflicts becomes an issue and every new variable requires a lengthy prefix to distinguish itself from similar variables. Using a .env file will enable us to use environment variables for local development without polluting the global environment namespace. It will also keep our environment variable names and values isolated to the same project that utilizes them. A .env file is a text file containing key-value pairs of all the environment variables required by your application. This file is included with our project locally but not saved to source control so that you aren't putting potentially sensitive information at risk.

In short ,Env files are those file that contain sensitive info.

1. create an .env file

        # environment variables defined inside a .env file
        SECRET_KEY=django-insecure-p7)07b=p0o+3-!br$$#_3an4ws+nm+#l(4teq^bzrmwoq@67=7
        DEBUG=True
2. Install pip install python-dotenv
3. go to the file where sensitive info is stored and add these code

        import os
        from dotenv import load_dotenv
        from pathlib import Path
        load_dotenv()
        # SECURITY WARNING: keep the secret key used in production secret!
        SECRET_KEY = os.getenv('SECRET_KEY')
        
        # SECURITY WARNING: don't run with debug turned on in production!
        DEBUG = os.getenv('DEBUG')

4. create .gitignore file and add .env file inside of it

        # Environments
        .env

That’s it, now we have successfully hidden our sensitive information. If u push our code to GitHub that no can able to see our .env file where all the sensitive info is stored

<br>
<hr>

# Structured Query Language

SQL is a standard language for storing, manipulating and retrieving data in databases. It uses RDBMS structure so there is a relationship between tables. It can process single records as well as a set of records at a time.

**Installation**

**Step 1:** To install it, update the package index on your server if you’ve not done so recently:

    sudo apt update

**Step 2:** Then install the mysql-server package:

    Sudo apt install mysql-server

**Step 3:** Ensure that the server is running using the systemctl start command:

    sudo systemctl start mysql.service

These commands will install and start MySQL, but will not prompt you to set a password or make any other configuration changes. Because this leaves your installation of MySQL insecure, we will address this next.

**Step 4:** Configuring MySQL

    sudo mysql_secure_installation

This will take you through a series of prompts where you can make some changes to your MySQL installation’s security options. The first prompt will ask whether you’d like to set up the Validate Password Plugin.

**Step 5**: Creating a Dedicated MySQL User and Granting Privileges

    sudo mysql

**Note:** If you installed MySQL with another tutorial and enabled password authentication for root, you will need to use a different command to access the MySQL shell. The following will run your MySQL client with regular user privileges, and you will only gain administrator privileges within the database by authenticating:

    sudo mysql -u root -p

Now let's do some useful work in sql . First we need to create a database and add some tables in it.

NOTE: In sql you can write in any case

- CREATE Database
   
        mysql> create database second_database;

- USE Database
   
        mysql> use second_database;

- CREATE TABLE

        mysql> create table second_table ( id int(2), name varchar(50)address text(50), dob date);
        mysql> desc second_table;
        +---------+-------------+------+-----+---------+-------+
        | Field   | Type    	| Null 	| Key 	| Default 	| Extra |
        +---------+-------------+------+-----+---------+-------+
        | id  	| int     		| YES  | 	| NULL	|   	|
        | name	| varchar(50)   | YES  | 	| NULL	|   	|
        | address | tinytext	| YES  | 	| NULL	|   	|
        | dob 	| date    	| YES  | 	| NULL	|   	|
        +---------+-------------+------+-----+---------+-------+
        5 rows in set (0.00 sec)

- SHOW DATABASES/TABLES
  
        mysql> show tables;

**DataTypes**

1. INT(1) or INTEGER(1)
2. DEC(4,2) or DECIMAL(4,2)
3. CHAR or CHARACTER
4. VARCHAR(40)
5. TEXT
6. DATE
7. DATETIME
8. TIMESTAMP

- INSERT INTO

        mysql> insert into second_table
        -> (
        -> id,name,age,address,dob)
        -> values(
        -> 1,'tanka',23,'tikapur',
        -> '1999-01-27');
        Query OK, 1 row affected (0.00 sec)

    Output

        mysql> select * from second_table;
        +------+-------+------+---------+------------+
        | id   | name  | age  | address | dob        |
        +------+-------+------+---------+------------+
        |    1 | tanka |   23 | tikapur | 1999-01-27 |
        +------+-------+------+---------+------------+
        1 row in set (0.00 sec)

- INSERT INTO- without specifying  column name 

        mysql> insert into second_table
        -> values(
        -> 1,'tanka',23,'tikapur',
        -> '1999-01-27');
        Query OK, 1 row affected (0.00 sec)

    Output

        mysql> select * from second_table;
        +------+-------+------+---------+------------+
        | id   | name  | age  | address | dob        |
        +------+-------+------+---------+------------+
        |    1 | tanka |   23 | tikapur | 1999-01-27 |
        +------+-------+------+---------+------------+
        1 row in set (0.00 sec)

- INSERT INTO - with changing order of column 

        mysql> insert into table_name
        -> (
        ->col2,col1,col3)
        -> values(
        ->val2,val2,val3);
        Query OK, 1 row affected (0.00 sec)

- INSERT INTO  Data Only  specified column

	We can skip the column whose data is unknown so that we get null value for that column.

        INSERT INTO - Multiple records as One
        mysql> insert into second_table
        -> values
        -> (3,'kalu',22,'kailali','2001-01-23'),
        -> (4,'david',24,'ktm','2301-01-23'),
        -> (5,'dipesh',21,'achham','2002-04-23'),
        -> (6,'neeru',25,'tkp','1996-04-23');
        Query OK, 4 rows affected (0.01 sec)
        Records: 4  Duplicates: 0  Warnings: 0

    Output

        mysql> select * from second_table;
        +------+--------+------+---------+------------+
        | id   | name   | age  | address | dob        |
        +------+--------+------+---------+------------+
        |    3 | kalu   |   22 | kailali | 2001-01-23 |
        |    4 | david  |   24 | ktm     | 2301-01-23 |
        |    5 | dipesh |   21 | achham  | 2002-04-23 |
        |    6 | neeru  |   25 | tkp     | 1996-04-23 |
        +------+--------+------+---------+------------+
        6 rows in set (0.00 sec)

- SELECT 

	The select statement is used to select data from a database and retrieve the info.
Select all column from table

        mysql> select * from table_name

    Select particular column from table

        mysql> select * from second_table
        -> where
        -> name='tanka';
    Output 

        +------+-------+------+---------+------------+
        | id   | name  | age  | address | dob        |
        +------+-------+------+---------+------------+
        |    1 | tanka |   23 | tikapur | 1999-01-27 |
        +------+-------+------+---------+------------+
        1 row in set (0.00 sec)


- SELECT with LIMIT
  
        mysql> select id from second_table
        -> limit 3;

    Output

        +------+--------+------+---------+------------+
        | id   | name   | age  | address | dob        |
        +------+--------+------+---------+------------+
        |    1 | kalu   |   22 | kailali | 2001-01-23 |
        |    2 | david  |   24 | ktm     | 2301-01-23 |
        |    3 | dipesh |   21 | achham  | 2002-04-23 |
        +------+--------+------+---------+------------+

- WHERE clause and Operator 

    In WHERE clause we have =,>,<,!=,BETWEEN,IN,LIKE,IS NOT NULL,IS NULL operators.

        mysql> select * from second_table where age>20;
        +------+---------+------+---------+------------+
        | id   | name    | age  | address | dob        |
        +------+---------+------+---------+------------+
        |    1 | tanka   |   23 | tikapur | 1999-01-27 |
        |    2 | sujana  |   22 | solu    | 2001-01-23 |
        |    3 | kalu    |   22 | kailali | 2001-01-23 |
        |    4 | david   |   24 | ktm     | 2301-01-23 |
        |    5 | dipesh  |   21 | achham  | 2002-04-23 |
        |    6 | neeru   |   25 | tkp     | 1996-04-23 |
        |    7 | seeru   |   26 | btkpur  | 2003-04-23 |
        |    8 | tankman |   26 | tikapur | 2005-04-23 |
        +------+---------+------+---------+------------+
        8 rows in set (0.00 sec)
<br>

        mysql> select * from second_table where age BETWEEN 10 and 20;
        +------+---------+------+---------+------------+
        | id   | name    | age  | address | dob        |
        +------+---------+------+---------+------------+
        |    9 | nirmala |   19 | solu    | 2010-04-23 |
        +------+---------+------+---------+------------+
        1 row in set (0.00 sec)
<br>

        mysql> select * from second_table where id IN (2,3);
        +------+--------+------+---------+------------+
        | id   | name   | age  | address | dob        |
        +------+--------+------+---------+------------+
        |    2 | sujana |   22 | solu    | 2001-01-23 |
        |    3 | kalu   |   22 | kailali | 2001-01-23 |
        +------+--------+------+---------+------------+
        2 rows in set (0.00 sec)

<br>

        mysql> select * from second_table where age  not between 10 and 20;
        +------+---------+------+---------+------------+
        | id   | name    | age  | address | dob        |
        +------+---------+------+---------+------------+
        |    1 | tanka   |   23 | tikapur | 1999-01-27 |
        |    2 | sujana  |   22 | solu    | 2001-01-23 |
        |    3 | kalu    |   22 | kailali | 2001-01-23 |
        |    4 | david   |   24 | ktm     | 2301-01-23 |
        |    5 | dipesh  |   21 | achham  | 2002-04-23 |
        |    6 | neeru   |   25 | tkp     | 1996-04-23 |
        |    7 | seeru   |   26 | btkpur  | 2003-04-23 |
        |    8 | tankman |   26 | tikapur | 2005-04-23 |
        +------+---------+------+---------+------------+
        8 rows in set (0.00 sec)

<br>

        mysql> select * from second_table where id IN (2,3) and name like 'k%';
        +------+------+------+---------+------------+
        | id   | name | age  | address | dob        |
        +------+------+------+---------+------------+
        |    3 | kalu |   22 | kailali | 2001-01-23 |
        +------+------+------+---------+------------+
        1 row in set (0.00 sec)

<br>

        mysql> select * from second_table where id IN (2,3) and name not  like 'k%';
        +------+--------+------+---------+------------+
        | id   | name   | age  | address | dob        |
        +------+--------+------+---------+------------+
        |    2 | sujana |   22 | solu    | 2001-01-23 |
        +------+--------+------+---------+------------+
        1 row in set (0.00 sec)

- ORDER BY Ascending/Descending

    - ASC - sort in ascending order
    - DESC - sort in descending order

            mysql> select * from second_table
            -> order by name ASC;
            +------+---------+------+---------+------------+
            | id   | name    | age  | address | dob        |
            +------+---------+------+---------+------------+
            |    4 | david   |   24 | ktm     | 2301-01-23 |
            |    5 | dipesh  |   21 | achham  | 2002-04-23 |
            |    3 | kalu    |   22 | kailali | 2001-01-23 |
            |    6 | neeru   |   25 | tkp     | 1996-04-23 |
            |    9 | nirmala |   19 | solu    | 2010-04-23 |
            |    7 | seeru   |   26 | btkpur  | 2003-04-23 |
            |    1 | tanka   |   23 | tikapur | 1999-01-27 |
            |    8 | tankman |   26 | tikapur | 2005-04-23 |
            |    2 | sujana  |   22 | solu    | 2001-01-23 |
            +------+---------+------+---------+------------+
            9 rows in set (0.00 sec)


- NOT NULL, UNIQUE KEY, PRIMARY KEY

    Each table has many unique keys which define each column uniquely. But one table have only one primary key which  cannot be null and must  be unique.

        mysql> create table third_table
        ( id int (2) not null primary key,
        name varchar(50), age int(60),
        address text(60),
        roll int(5) unique key );
        Query OK, 0 rows affected, 3 warnings (0.04 sec)

    Output

        mysql> desc third_table;
        +---------+-------------+------+-----+---------+-------+
        | Field   | Type        | Null | Key | Default | Extra |
        +---------+-------------+------+-----+---------+-------+
        | id      | int         | NO   | PRI | NULL    |       |
        | name    | varchar(50) | YES  |     | NULL    |       |
        | age     | int         | YES  |     | NULL    |       |
        | address | tinytext    | YES  |     | NULL    |       |
        | roll    | int         | YES  | UNI | NULL    |       |
        +---------+-------------+------+-----+---------+-------+
        5 rows in set (0.00 sec)

- AUTO INCREMENT
  
    Used to generate a unique number, when a new record is inserted into a table. One table has only one auto increment and it ignores the null value.

**Step 1:** Create table 

        mysql> create table fourth__table
        ( id int (2) not null primary key auto_increment,
        name varchar(50),
        age int(60),
        address text(60),
        roll int(5)
        );

Output 

    mysql> desc fourth__table;
    +---------+-------------+------+-----+---------+----------------+
    | Field   | Type        | Null | Key | Default | Extra          |
    +---------+-------------+------+-----+---------+----------------+
    | id      | int         | NO   | PRI | NULL    | auto_increment |
    | name    | varchar(50) | YES  |     | NULL    |                |
    | age     | int         | YES  |     | NULL    |                |
    | address | tinytext    | YES  |     | NULL    |                |
    | roll    | int         | YES  |     | NULL    |                |
    +---------+-------------+------+-----+---------+----------------+
    5 rows in set (0.00 sec)

**Step 2:** Insert value

    mysql> insert into fourth__table(name,age,address,roll)
    values
    ( 'tanka',23,'tikapur',23),
    ('david',20,'kaillai',20),
    ('sujana',17,'solu',12);
    Query OK, 3 rows affected (0.01 sec)
    Records: 3  Duplicates: 0  Warnings: 0

Output

    mysql> select * from fourth__table;
    +----+--------+------+---------+------+
    | id | name   | age  | address | roll |
    +----+--------+------+---------+------+
    |  1 | tanka  |   23 | tikapur |   23 |
    |  2 | david  |   20 | kaillai |   20 |
    |  3 | sujana |   17 | solu    |   12 |
    +----+--------+------+---------+------+
    3 rows in set (0.00 sec)

- AUTO INCREMENT with particular number

        mysql> create table fifth_table
        -> (
        -> id int primary key auto_increment,
        -> name varchar(50),
        -> age int(2));
        Query OK, 0 rows affected, 1 warning (0.03 sec)
    <br>

        mysql> alter table fifth_table auto_increment = 10;
        Query OK, 0 rows affected (0.02 sec)
        Records: 0  Duplicates: 0  Warnings: 0
    <br>

        mysql> insert into fifth_table(name,age) values ('tankaman',12);
        Query OK, 1 row affected (0.01 sec)

Output

    mysql> select * from fifth_table;
    +----+----------+------+
    | id | name     | age  |
    +----+----------+------+
    | 10 | tankaman |   12 |
    +----+----------+------+
    1 row in set (0.00 sec)


- Aliases

Aliases are used to temporarily  rename a table name or a column name. AS is optional. Here are an example.

    mysql> select col_name from table_name AS alias_name
    mysql> select col_name AS alias_name from table_name
    mysql> select col_name alias_name from table_name
    mysql> select col_name AS "alias name" from table_name

- SELECT DISTINCT
  
The select distinct statement is used to return only distinct (different) values. Inside a table,a column contains many duplicate values and sometimes you want a list of different values then select distinct is used.

    mysql> select distinct name from fourth__table;
    +----------+
    | name     |
    +----------+
    | tanka    |
    | david    |
    | tankaman |
    +----------+
    4 rows in set (0.00 sec)

- ALTER TABLE 
  
This command is used to add , change, modify and drop existing structure of the table.

  1. ADD COLUMN

    mysql> alter table fifth_table
    -> add column new_col text(50);
    Query OK, 0 rows affected (0.03 sec)
    Records: 0  Duplicates: 0  Warnings: 0

Output

    mysql> select * from fifth_table;
    +----+----------+------+---------+
    | id | name     | age  | new_col |
    +----+----------+------+---------+
    | 10 | tankaman |   12 | NULL    |
    +----+----------+------+---------+
    1 row in set (0.00 sec)

2. CHANGE COLUMN

Change column  is used to change column names and data types of existing     columns without constraints.

    mysql> alter table fifth_table change column new_col rollno int(5);
    Query OK, 0 rows affected, 1 warning (0.02 sec)
    Records: 0  Duplicates: 0  Warnings: 1

Output

    mysql> select * from fifth_table;
    +----+----------+------+---------+
    | id | name     | age  | rollno |
    +----+----------+------+---------+
    | 10 | tankaman |   12 | NULL    |
    +----+----------+------+---------+
    1 row in set (0.00 sec)

3. MODIFY COLUMN

Used to modify size of data type of an existing column

    mysql> alter table fifth_table
    -> modify column age int(1);
    Query OK, 0 rows affected, 1 warning (0.02 sec)
    Records: 0  Duplicates: 0  Warnings: 1


4. DROP COLUMN
   
Used to delete column

    mysql> alter table fifth_table drop column new_col;
    Query OK, 0 rows affected (0.07 sec)
    Records: 0  Duplicates: 0  Warnings: 0
    mysql> select * from fifth_table;
    +----------+----+----------+------+--------+
    | new_colm | id | name     | age  | rollno |
    +----------+----+----------+------+--------+
    | NULL     | 10 | tankaman |   12 |   NULL |
    +----------+----+----------+------+--------+
    1 row in set (0.00 sec)

- UPDATE
 
The update statement is used to update existing records in a table

    mysql> select * from fifth_table;
    +----+----------+------+--------+
    | id | name     | age  | rollno |
    +----+----------+------+--------+
    | 10 | tankaman |   12 |   NULL |
    +----+----------+------+--------+
    1 row in set (0.00 sec)

    mysql> update fifth_table
    -> set rollno=12
    -> where id=10;
    Query OK, 1 row affected (0.01 sec)
    Rows matched: 1  Changed: 1  Warnings: 0

Output

    mysql> select * from fifth_table;
    +----+----------+------+--------+
    | id | name     | age  | rollno |
    +----+----------+------+--------+
    | 10 | tankaman |   12 |     12 |
    +----+----------+------+--------+
    1 row in set (0.00 sec)


- DELETE 
  
Used to delete specific column

    mysql> delete from second_table
    -> where  id=2;
    Query OK, 1 row affected (0.01 sec)

Output

    mysql> select * from second_table;
    +------+---------+------+---------+------------+
    | id   | name    | age  | address | dob        |
    +------+---------+------+---------+------------+
    |    1 | tanka   |   23 | tikapur | 1999-01-27 |
    |    3 | kalu    |   22 | kailali | 2001-01-23 |
    |    4 | david   |   24 | ktm     | 2301-01-23 |
    |    5 | dipesh  |   21 | achham  | 2002-04-23 |
    |    6 | neeru   |   25 | tkp     | 1996-04-23 |
    |    7 | seeru   |   26 | btkpur  | 2003-04-23 |
    |    8 | tankman |   26 | tikapur | 2005-04-23 |
    |    9 | nirmala |   19 | solu    | 2010-04-23 |
    +------+---------+------+---------+------------+
    8 rows in set (0.00 sec)


- MIN/MAX
- 
The min() returns the smallest value of the selected column and max() returns the largest value from the selected column.

    mysql> select * from new;
    +------+---------+------+---------+------------+
    | id   | name    | age  | address | dob        |
    +------+---------+------+---------+------------+
    |    3 | kalu    |   22 | kailali | 2001-01-23 |
    |    4 | david   |   24 | ktm     | 2301-01-23 |
    |    5 | dipesh  |   21 | achham  | 2002-04-23 |
    |    6 | neeru   |   25 | tkp     | 1996-04-23 |
    |    7 | seeru   |   26 | btkpur  | 2003-04-23 |
    |    8 | tankman |   26 | tikapur | 2005-04-23 |
    |    9 | nirmala |   19 | solu    | 2010-04-23 |
    +------+---------+------+---------+------------+
    7 rows in set (0.00 sec)

Output

    mysql> select min(age) from new;
    +----------+
    | min(age) |
    +----------+
    |       19 |
    +----------+
    1 row in set (0.00 sec)

- GROUP BY
  
The group by statement group, that have the same values into the summary rows ,like 
“Find the number of customers in each row”. The  group by statement is often used with max(),min(),avg(),sum()  to group the results by one or more columns.

    mysql> select name,min(age) from new group by name;
    +---------+----------+
    | name    | min(age) |
    +---------+----------+
    | kalu    |       22 |
    | david   |       24 |
    | dipesh  |       21 |
    | neeru   |       25 |
    | seeru   |       26 |
    | tankman |       26 |
    | nirmala |       19 |
    +---------+----------+
    7 rows in set (0.00 sec)

- HAVING
  
The having clause is added because where keyword cannot be used with aggregate function

    mysql> select name,max(age) from new group by name having max(age) > 30;
    +------+----------+
    | name | max(age) |
    +------+----------+
    | kalu |       39 |
    +------+----------+
    1 row in set (0.00 sec)

- JOINS
  
The joins clause is used to combine rows from two or more tables, based on a related column between them. Simply, the join makes a relationship from 2 or more tables.

1. Cross join
   
The cross join keyword returns all the records from both table
![cross join](crossjoin.png)

Here we have two tables

    mysql> select * from employee;
    +-------+-------+---------+
    | empid | name  | city    |
    +-------+-------+---------+
    |     1 | tanka | tikapur |
    |     2 | david | achham  |
    |     3 | neeru | ktm     |
    +-------+-------+---------+
    3 rows in set (0.01 sec)
 
    mysql> select * from department;
    +-----+---------+
    | did | depname |
    +-----+---------+
    | 101 | IT      |
    | 102 | HR      |
    | 103 | ADMIN   |
    +-----+---------+
    3 rows in set (0.00 sec)


Output

    mysql> select * from employee cross join department;
    +-------+-------+---------+-----+---------+
    | empid | name  | city    | did | depname |
    +-------+-------+---------+-----+---------+
    |     3 | neeru | ktm     | 101 | IT      |
    |     2 | david | achham  | 101 | IT      |
    |     1 | tanka | tikapur | 101 | IT      |
    |     3 | neeru | ktm     | 102 | HR      |
    |     2 | david | achham  | 102 | HR      |
    |     1 | tanka | tikapur | 102 | HR      |
    |     3 | neeru | ktm     | 103 | ADMIN   |
    |     2 | david | achham  | 103 | ADMIN   |
    |     1 | tanka | tikapur | 103 | ADMIN   |
    +-------+-------+---------+-----+---------+
    9 rows in set (0.00 sec)
    
    mysql> select name,depname from employee cross join department;
    +-------+---------+
    | name  | depname |
    +-------+---------+
    | neeru | IT      |
    | david | IT      |
    | tanka | IT      |
    | neeru | HR      |
    | david | HR      |
    | tanka | HR      |
    | neeru | ADMIN   |
    | david | ADMIN   |
    | tanka | ADMIN   |
    +-------+---------+
    9 rows in set (0.00 sec)


2. Inner join
   
The inner join selects records that have matching value in both table

![inner join](innerjoin.gif)

Here we have two tables

    mysql> select * from emp;
    +-------+-------+---------+
    | empid | name  | city    |
    +-------+-------+---------+
    |     1 | tanka | tikapur |
    |     2 | david | achham  |
    |     3 | neeru | ktm     |
    +-------+-------+---------+
    3 rows in set (0.01 sec)
    
    mysql> select * from dep;
    +-----+---------+-------+
    | did | depname | empid |
    +-----+---------+-------+
    | 101 | IT      |     3 |
    | 102 | HR      |     1 |
    | 103 | ADMIN   |     2 |
    +-----+---------+-------+
    3 rows in set (0.00 sec)


Output 

    mysql> select emp.name,dep.depname from emp inner join dep on emp.empid=dep.empid;
    +-------+---------+
    | name  | depname |
    +-------+---------+
    | tanka | HR      |
    | david | ADMIN   |
    | neeru | IT      |
    +-------+---------+
    3 rows in set (0.00 sec)
 
3. left join

The left  keyword returns all records from the left table and matching records from the right table.

![left join](leftjoin.gif)

The left join in the table that comes before the join is the left table and the table that comes after the join is the right table.

So we have 2 tables

    mysql> select * from emp;
    +-------+--------+---------+
    | empid | name   | city    |
    +-------+--------+---------+
    |     1 | tanka  | tikapur |
    |     2 | david  | achham  |
    |     3 | neeru  | ktm     |
    |     7 | dipesh | kailali |
    +-------+--------+---------+
    4 rows in set (0.00 sec)
    
    mysql> select * from dep;
    +-----+---------+-------+
    | did | depname | empid |
    +-----+---------+-------+
    | 101 | IT      |     3 |
    | 102 | HR      |     1 |
    | 103 | ADMIN   |     2 |
    +-----+---------+-------+
    3 rows in set (0.00 sec)

Output 

    mysql> select name,depname from emp left join dep on emp.empid=dep.empid;
    +--------+---------+
    | name   | depname |
    +--------+---------+
    | tanka  | HR      |
    | david  | ADMIN   |
    | neeru  | IT      |
    | dipesh | NULL    |
    +--------+---------+
    4 rows in set (0.00 sec)

4. right join
   
The right join keyword returns all records from the right table (table2), and the matching records (if any) from the left table (table1).

![right join](rightjoin.gif)



So we have 2 tables

    mysql> select * from emp;
    +-------+--------+---------+
    | empid | name   | city    |
    +-------+--------+---------+
    |     1 | tanka  | tikapur |
    |     2 | david  | achham  |
    |     3 | neeru  | ktm     |
    |     7 | dipesh | kailali |
    +-------+--------+---------+
    4 rows in set (0.00 sec)
    
    mysql> select * from dep;
    +-----+---------+-------+
    | did | depname | empid |
    +-----+---------+-------+
    | 101 | IT      |     3 |
    | 102 | HR      |     1 |
    | 103 | ADMIN   |     2 |
    +-----+---------+-------+
    3 rows in set (0.00 sec)

Output 

    mysql> select name,depname from dep left join emp on emp.empid=dep.empid;
    +-------+---------+
    | name  | depname |
    +-------+---------+
    | neeru | IT      |           
<br>
<hr>
<br>

# HTML

HTML is the standard markup language for creating Web pages.

**What is HTML?**

- HTML stands for Hyper Text Markup Language
- HTML is the standard markup language for creating Web pages
- HTML describes the structure of a Web page
- HTML consists of a series of elements
- HTML elements tell the browser how to display the content
- HTML elements label pieces of content such as "this is a heading", "this is a paragraph", "this is a link", etc.

       <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>my title</title>
        </head>
        <body>
        <h1>My First Heading</h1>
        <p>My first paragraph.</p>
        </body>
        </html>

- The !DOCTYPE html declaration defines that this document is an HTML5 document
- The html element is the root element of an HTML page
- The head element contains meta information about the HTML page
- The title element specifies a title for the HTML page (which is shown in the browser's title bar or in the page's tab)
- The body element defines the document's body, and is a container for all the visible contents, such as headings, paragraphs, images, hyperlinks, tables, lists, etc.
- The h1 element defines a large heading

**Html Tables**

HTML tables allow web developers to arrange data into rows and columns.

    <table>
    <tr>
    <th>Company</th>
    <th>Contact</th>
    <th>Country</th>
    </tr>
    <tr>
    <td>ekbana</td>
    <td>98797978</td>
    <td>nepal</td>
    </tr>
    <tr>
    <td>ekbana solution</td>
    <td>345345345</td>
    <td>lalitpur</td>
    </tr>
    </table>

**HTML Links - Hyperlinks**

HTML links are hyperlinks. You can click on a link and jump to another document. When you move the mouse over a link, the mouse arrow will turn into a little hand. 

    <a href="url">link text</a>
    <button onclick="document.location='default.asp'">HTML Tutorial</button>


**HTML Layout Elements and Techniques**

HTML has several semantic elements that define the different parts of a web page:

    <header> - Defines a header for a document or a section
    <nav> - Defines a set of navigation links
    <section> - Defines a section in a document
    <article> - Defines an independent, self-contained content
    <aside> - Defines content aside from the content (like a sidebar)
    <footer> - Defines a footer for a document or a section
    <details> - Defines additional details that the user can open and close on demand
    <summary> - Defines a heading for the <details> element



**HTML Forms**

An HTML form is used to collect user input. The user input is most often sent to a server for processing. 


The form Element

    <form action="" method="get">
    <label for="first">Name:</label>
    <input type="text" value="" name="first">
    <br>
    <label for="last">Last:</label>
    <input type="text" value="" name="last">
    <br>
    <label for="email">Email:</label>
    <input type="email" value="" name="email">
    <br>
    <input type="submit" value="Submit">
    </form>

The input Element

The HTML input element is the most used form element.  An input element can be displayed in many ways, depending on the type attribute.  Here are some examples:


Text Fields

    <form>
    <label for="fname">First name:</label><br>
    <input type="text" id="fname" name="fname"><br>
    <label for="lname">Last name:</label><br>
    <input type="text" id="lname" name="lname">
    </form>


<br>
<br>
<hr>

# CSS

CSS is the language we use to style a Web page

**What is CSS?**

- CSS stands for Cascading Style Sheets
- CSS describes how HTML elements are to be displayed on screen, paper, or in other media
- CSS saves a lot of work. It can control the layout of multiple web pages all at once
External stylesheets are stored in CSS files

**CSS Selectors**

A CSS selector selects the HTML element(s) you want to style.

- The CSS element Selector
- The CSS class Selector
- The CSS id Selector
- The CSS Universal Selector

        body{
        font-family: 'Sansita',sans-serif;
        }
        *{
        padding-top: 5%;
        }
        .emailform{
        margin-bottom: 10px;
        }
        #sub{
        background-color: green;
        }

<br>
<br>
<hr>

# JavaScript

Js is an engine of a web application. JavaScript helps to program the behavior of web pages

**Overview**

- Core Javascript
- Document Object Model
- Accessing Document Element
- Event Handling
- Event Type
- Window
- Form Handling
- Form validation

**Core Javascript**

Variables

There are 3 Ways to Declare a JavaScript Variable
- Using var
- Using let
- Using const
  
        <script>
            var name="tanka"
            const salary="200000"  
        { 
            let overview=document.write(name , salary)
        }
        </script>

The value of a variable always varies, and the const is always constant  and has a block scope which means its value is the same within a scope.

**Operators**

    Operator    Description
    +           Addition
    -           Subtraction
    *           Multiplication
    **          Exponentiation (ES2016)
    /           Division
    %           Modulus (Division Remainder)
    ++          Increment
    --          Decrement
    ==          equal to
    ===         equal value and equal type
    !=          not equal
    !==         not equal value or not equal type
    >           greater than
    <           less than
    >=          greater than or equal to
    <=          less than or equal to
    ?           Ternary operator
    &           and
    |           or
    !           not

<br>

    <script>
        var a=2
        var b=4
        var c=document.write(a+b)
        var c=document.write(a-b)
        var c=document.write(a/b)
        var c=document.write(a%b)
        var c=document.write(a^b)
    </script>

**Prompt**

This operator is used to prompt the alert box on the window.

    <script>
        var a=prompt("Enter your name:")
        document.write(a)
    </script>


**Function**

A JavaScript function is a block of code designed to perform a particular task. A JavaScript function is executed when "something" invokes it (calls it).

    <script>
        var a=2
        var b=4
        var c= sum(a,b)
        function sum(a,b) {
            return a*b
        }
        document.write(c)
    </script>


**String**

JavaScript strings are for storing and manipulating text.

    <p id="len"></p>
    <p id="ind"></p>
    <p id="slice"></p>
    <p id="search"></p>
    <p id="match"></p>
    <p id="include"></p>

    <script>
        var name="tankaman sodari"
        var favourite="game of throne, showoff"
    
    document.getElementById('len').innerHTML=favourite.length
    document.getElementById('ind').innerHTML=favourite[0]
    document.getElementById('slice').innerHTML=favourite.slice(1,5)
        document.getElementById('slice').innerHTML=favourite.replace('throne','tanka')
    document.getElementById('search').innerHTML=favourite.search('of')
    document.getElementById('match').innerHTML=favourite.match(/of/g)
        document.getElementById('include').innerHTML=favourite.includes("game")
    </script>


**String Templates**

Template Literals use back-ticks (``) rather than the quotes ("") to define a string. Template literals provide an easy way to interpolate variables and expressions into strings. The method is called string interpolation.

    <script>
        let firstName = "tanka";
        let lastName = "sodari";
        let text = `Welcome ${firstName}, ${lastName}!`;
        let total = `total: ${firstName}, ${lastName}!`;
        document.getElementById("demo").innerHTML = text;
    </script>

**Array**

An array is a special variable, which can hold more than one value

    <p id="demo"></p>
    <script>
        var text=[]
        var arr=["apple",'ball','cat','dog']
        arr.push("Lemon");  // Adds a new element (Lemon) to arr
        arr.pop()  // removes the last element from an array:
        arr.shift() //method removes the first array element
        arr.unshift() //adds a new element to an array (at the beginning),
        arr.sort()     //sort in ascending
        arr.reverse 	//sort in descending
        for(let i=0;i<arr.length;i++){
            text=text+arr[i]
        }
        document.getElementById('demo').innerHTML= text
    </script>


**Array Iteration**

Array iteration methods operate on every array item.
forEach()  method
The forEach() method calls a function (a callback function) once for each array element.

    note=[‘apple ,’ball’,’cat’,’dog’]  
    note.forEach((element, index) => {
        html += `<div class="col-md-3 notecard mb-5">
        <div class="card" style="width: 18rem;">
            <div class="card-body ">
                <h5 class="card-title">Note ${index + 1}</h5>
                <hr>
                <p class="card-text">${element}
                </p>
                <a href="#" class="btn btn-danger">Delete Notes</a>
            </div>
        </div>
    </div>`
    });

When we have to iterate whole elements then we use Array.from method

    let searchnote = document.getElementsByClassName('notecard')
    Array.from(searchnote).forEach((element) => {
        let text=element.getElementsByTagName('p')[0].innerText
        if(text.includes(input_value)){
            element.style.display="block"
        }
        else{
            element.style.display="none"
    
        }
    })


**Classes and Object**

JavaScript Classes are templates for JavaScript Objects. Use the keyword class to create a class. Always add a method named constructor():

    class Book{
    constructor(name, author, type) {
        this.name = name;
        this.author = author;
        this.type = type;
    }
    }
    let book = new Book(“tanka”, “david”, “programmer”)


**Document Object Model**

The Dom is an API for HTML and XML documents. According to DOm,every html tag is a object and nested tag are children

![Dom](Screenshot%20(122).png)

**Accessing Document Element**

Often, with JavaScript, you want to manipulate HTML elements.
To do so, you have to find the elements first. There are several ways to do this:

![selector](Screenshot%20(126).png)

1. getElementsById

Get the element with the specified ID

    let tableBody=document.getElementById('tableBody') 

Length property

    let tableBody=document.getElementById('tableBody').length;
    // or
    let tableBody=document.getElementById('tableBody')
    len=tableBody.length;
 
2. getElementsByTagName

        let searchnote = document.getElementsByClassNam('notecard')
            let text=searchnote.getElementsByTagName('p’)
        let text=searchnote.getElementsByTagName('*’)	

or

        let searchnote = document.getElementsByClassName('notecard').getElementsByTagName('p’)
 
 
Loop property

    let tableBody=document.getElementById('tableBody')
    len=tableBody.length;
    for(i=0;i<len;i++){
    let all=document.getElementsByTagName('p')[i]
    }
    
3. getElementsByClassName

Get the element with the specified ID

    let searchnote = document.getElementsByClassName('notecard')

4. querySelector

It returns the first match of the passed selector string 

    document.querySelector("p").style.backgroundColor = "red";
    document.querySelector(".id").style.backgroundColor = "red";
    document.querySelector("#class").style.backgroundColor = "red";

5. querySelectorAll

It returns the node list of DOM element that matches the query
	
    <h2 class="example">A heading</h2>
    <p class="example">A paragraph.</p>
    
    <script>
    const nodeList = document.querySelectorAll(".example");
    for (let i = 0; i < nodeList.length; i++) {
    Var result=document.querySelectorAll(“.geek”)[i];
    }
    </script>

**Event Handling**

The actions to which javascript can respond are called events. An event handler is javascript code associated with a particular part of the document and a particular event. A handler is executed if and when the given event occurs at the part of the document to which it is associated.

**addEventListener:**

    let addbook = document.getElementById('addbook')
    addbook.addEventListener(click, function(e) {
    alert(“hello”)
    }

**Advanced Javascript**

**How does JS work?**

In every browser we have a javascript engine, this javascript engine takes the js code line by line and runs each line .
 The Js engine has the parser ,converter (which converts to machine code) and finally runs the code. The parser checks each code line by line,and if everything goes right then it produces a data structure called Abstract Syntax Tree(AST). And then convert into machine code and run at last.

**Execution Context and Execution Stack**

![execution context](Screenshot%20(124).png)

Execution Context is the environment where our code is executed and is evaluated. So when a function is called then a new execution context is created for that function. Each execution context is stored in an execution stack. All the variables and functions that are not inside any function,when called a new execution, are created every time a function is executed.
Global execution context is the default context like window object. All the global variables and functions are attached to the global context when they are called.
The execution stack is also called a ‘calling stack’ with a LIFO structure , which is used to store all the execution context  created during the code execution.

    function A() {
    B();  
    console.log("print A")
    }
    function B() {
    console.log("print B")
    C();  
    }
    function C() {
    console.log("print C")
    }
    A();

The functions are stored in the global execution context by default. Whenever a function is called then the execution context for A is created and for B and so on. The structure is in First IN Last OUT.

![global execution stack](Screenshot%20(125).png)

**Hoisting**

Hoisting is a JS mechanism where variables and function declarations are moved to the top of their scope before the code execution.

Suppose if we write the code like this:

    A(2,3);
    function A(a,b) {
    sum=a+b   
    console.log("print sum",sum)
    }

    Then this code is executed in JS like this
    function A(a,b) {
    sum=a+b   
    console.log("print sum",sum)
    }
    A(2,3);

First  it looks for the function and variables declaration on the code if found then it allocates the memory for it (creation phase)  then moves to the top of their scope before the function is called.
This mechanism is hoisting


**Scope Chain**

Child function can get access to the parent variable but parent function can’t get access to the 
Child function.

    function A() {
    var name="tankman"
    B(); 
    function B() {
        console.log("Name is ",name) 
        }
    }
    A();

Output

    Name is tankman



**Strict Mode**

Strict mode prohibits some syntax likely to be defined in future versions of ECMAScript. It prevents, or throws errors, when relatively “unsafe” actions are taken (such as gaining access to the global object). It disables features that are confusing or poorly thought out.

    "use strict"
    sum=2+3
    console.log(sum)

It throws the error that the sum is not defined.

**This Keyword**

- this keyword refers to the object it belongs to. 
- Alone, this refers to the global object(window). 
- In regular function ,alone, this refers to the global objects. 
- In a method, it refers to the owner object.
- In a function, strict mode, this is undefined
- Arrow function doesn’t have this or argument binding


This is a regular function and this refers to the global objects(window)

    function tankman(){
        var add=2+2
        console.log("the sum is ",add)
        console.log(this)
    
    }
    tankman()


This is a method ,where function is inside the object, so this refers to the tankman object.

    const tankman={
    name:"tanka",
    age:"18",
    sum:function(){
        var add=2+2
        console.log("the sum is ",add)
        console.log(this.name)
    }
    }
    tankman.sum()

Example:

    const tankman={
    name:"tanka",
    age:"18",
    sum:function(){
        var add=2+2
        console.log("the sum is ",add)
        console.log(this.name)
        function func1(){
            var name="kalu"
            console.log(name)
            console.log(this)
        }
        func()
    }
    }
    tankman.sum()

Output:

    the sum is  4
    tanka
    kalu
    Window {window: Window, self: Window, document: document, name: '', location: Location, …}

This gives the window object because the func1 function is the regular function.


**In JavaScript Everything is an object?**

Almost everything in JavaScript is an object. In fact, only six things are not objects. They are  null , undefined , strings, numbers, boolean, and symbols.

Array is also an object. So let's prove it,

    const array=[1,2,3]
    console.log(Array.isArray(array))

Output 

    true


**Function is the first class citizens**

A programming language is said to have first class functions when functions in that language are treated like any other variable.

- In javascript we can assign a function to a variable also as a method.
   
- Pass a function as an argument
  
- Returning function(one function can return other function)
  
Assigning a method in js is super easy as well. Similar to how we can assign a function to a variable, we can assign a function as  a value to a key in an object .

    const variablename=function (){
    console.log("we can assign a function to a variable")
    }
    variablename()

Or 

    const variablename =
    {
    name: "tankaman",
    age: 20,
    func1: function () {
        console.log("we can assign a function to a variable")
    }
    }
    variablename.func1

We can also pass a function as an argument like below

    const func1= ()=>{
    console.log("hello")
    }
    
    const greet=(func1,name)=>{
    console.log(func1()+name)
    }
    greet(func1,"tanka")


In js one function can return to another function

    function a(){
    return function b(){
        console.log("hello i am returning from home")
    }
    }
    a()()


**Callback function**

Any function that is passed as an argument is called a callback function.

    const funA=(friend,funcback)=>{
    console.log(`hello sujana i am talking to ${friend}, i will call you back`)
            funcback()
        }
    const funB=()=>{
            console.log("Hello sujana how are u okay")
        }
    funA("prajwol",funB)
 

Output

    hello sujana i am talking to prajwol, i will call you back
    callbackfunction.html:31 Hello sujana how are u okay


A callback is a function that is to be executed after another function has finished executing.

    const funA=()=>{
            setTimeout(()=>{
                console.log("func A")
                funB()
            },3000)
            
        }
    const funB=()=>{
            console.log("func B")
        }
    funA()

Output

    The output will come after 3 second
    func A
    func B
 
 


**Anonymous Function and Higher order Function**

The function that has no name is called an anonymous function.
The higher order functions are those functions that return an anonymous function inside their function.

    const funcA = (name) => {
            if (name === "tanka") {
                return (age) => {
                    console.log(`hello ${name} your age is ${age}`)
                }
            }
        }
        funcA('tanka')(23)

In the above  example it returns the anonymous function of argument age. While calling the funcA we have to pass the argument or () this operator while no arguments  are passing.

    const funcA=(name)=>{
            if (name==="tanka"){
                return (){
                    console.log(`hello ${name}`)
                }
            }
        }
        funcA('tanka')()



**Immediately Invoked Function Expression(IIFE)**

The IIFE is a javascript function that runs as soon as it is defined. It is a design pattern which is also known as a self executing anonymous function and contains two major parts.

- The first is the anonymous function with lexical scope enclosed within the grouping operator (). This prevents accessing variables within the IIFE idiom as well as polluting the global score.
  
- The second part creates the immediately invoked function expressions () through which the js engine will directly interpret the function. 

        (()=>{
                console.log("hello world")
            })()

The yellow part is Grouping operator(anonymous function) and the red one is IIFE. we can also pass the argument and it run as soon as it defined ,independent to any other method or function and cannot access by other global function

    ((name)=>{
            console.log(`hello ${name}`)
        })("tanka")

**Closure**

The closure is the inner function which has the ability to access its parent variable , parameters and global variable.

       let c=2
       const funcA=(b)=>{
           let a=2
           const funcB=()=>{
               let sum=a+b+c
               console.log(`the answer is ${sum}`)
           }
           funcB()
       }
       funcA(2)


**Call Method**

The call method is a predefined Js method  with call(), an obj can use a method belonging to another object. In simple terms one object property can be accessed by another object so we don't have to write the same property again and again.

    const detail={    
            func1:function(){
                console.log(`hello ${this.name}, your age is  ${this.age}`)
            }
            
        }
        const access={
            name:"tanka",
            age:24,
            address:'tkp', 
        }
        detail.func1.call(access)

Here  let us suppose object access  has some property and value that object details need , so with the help of the call method we can access another object property.

    const detail={    
            func1:function(name,address){
                console.log(`hello ${name}, your age is  ${this.age} and address is ${address}`)
            }         
        }
        const access={
    
            age:24,
            address:'tkp', 
        }
        detail.func1.call(access,"tanka","tkp")


The call method  takes the object name, and all others can be arguments.

**Apply Method**

The Apply Method is the same as the call method , the only difference is that the apply method takes an argument as an array while the call method takes an argument separately.

    const detail={    
            func1:function(name){
                console.log(`hello ${name[0]},from ${name[1]} your age is  ${this.age}`)
            }         
        }
    const access={
            age:24,   
        }
    detail.func1.call(access,['tanka','tikapur'])


**Bind Method**

We can bind an object to a common function ,so that the function gives different results when it's needed. And it takes an obj as a first argument and create a new function

    const obj1={
    name:'tanka',
    age:'23',
    funcA:function(){
        console.log(` hello ${this.name} your age is ${this.age}`)
    }
    }
    const obj2={
    name:'david',
    age:'20',
    }
    const commonfunc=obj1.funcA.bind(obj2)
    commonfunc()

Here the obj2 is binded to the function of obj1. The common function is also a function.


    const obj1={
    name:'tanka',
    age:'23',
    }
    const obj2={
    name:'david',
    age:'20',
    }
    const obj3={
    name:'kalu',
    age:'22',
    }
    
    function funcA(address){
    console.log(` hello ${this.name} your age is ${this.age} and your address is ${address}`)
    }
    
    const commonfunc=funcA.bind(obj1)
    commonfunc('tikapur')


Here we can bind a function to any object that we need.we can pass the argument to that function also. 



**For vs ForEach Method**

The JavaScript for loop is used to iterate through the array or the elements for a specified number of times. If a certain amount of iteration is known, it should be used.
The forEach() method is also used to loop through arrays, but it uses a function differently than the classic “for loop”. It passes a callback function for each element of an array together with the below parameters: 

**Current Value (required)**: The value of the current array element 

**Index (optional):** The index number of the current element 

**Array (optional):** The array object the current element belongs to 

We need a callback function to loop through an array by using the forEach method.

    let arr=[1,2,4,5,6,7]
    arr.forEach((element,index)=>{
    console.log(element,index)
    })



The ‘for’ method is faster in performance than the ‘forEach’ method.


**Event Loop**

In synchronous Js , we have to wait until the current task to complete and then execute the next task. Hence performance is slow. But in asynchronous Js ,with the help of event loop , the current task is executing in the background if it takes time and the next task is executing
Javascript has a runtime model based on an event loop, which is responsible for executing the code, collecting and processing events and executing queued sub tasks. 
The below figure will clearly describe the concept of the event loop.

- Heap

  The heap is the memory location where all the variables and obj declaration are stored.

- Execution stack

    The execution stack is also called a ‘calling stack’ with a LIFO structure , which is used to store all the execution context  created during the code execution.

- WebAPIs

    In the webAPIs, all the ajax , setTimeout function and DOM are stored. Whenever a code has ajax,setTimeout and DOM then they are placed in the WebAPIs.
    Task Queue/ Message Queue
    It has a list of messages to be processed. Each message has an associated function that gets called to handle the message. All the callback functions are in the task queue.


![eventloop](Screenshot%20(127).png)

Event loops checks if any call back is in task queue and call stack is empty then, event loop helps to grab that call back and put it in execution stack(call stack)



