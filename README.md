
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
<br><br><br>

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


        