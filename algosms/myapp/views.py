from django.shortcuts import render,redirect , HttpResponse
from .forms import ClientLogin
from .models import Account
from .forms import *
from django.contrib.auth import authenticate,login,logout
from datetime import datetime
from .models import ClientDetail , ClientSignal 
from django.utils import timezone
import datetime
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def logoutUser(request):
    logout(request)
    return redirect('index')

def client_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['password']
        user = authenticate(username=u,password=p)
        if user:
            login(request,user)
            error = "no"
        else:
            error = "yes"    
    return render(request,'client_login.html', locals())
     


# def client_login(request):
#     if request.method == 'POST':
#         Acc = Account()
#         user_id = request.POST.get('user_id')
#         password = request.POST.get('password')
#         user = authenticate(username = user_id , password = password )
#         if user is not None:
#             if Account.objects.filter(user_id=user_id, is_client=True).exists():
#                 login(request,user)
#                 return redirect('client_dashboard',emp_id=user_id)
#             else:
#                 messages.info(request, 'Invalid, user not An Client.')
#                 form = ClientLogin()
#                 return render(request,'client_login.html',context={'form':form})
#         else:
#             messages.info(request, 'Invalid Credentials.')
#             form = ClientLogin()
#             return render(request,'client_login.html',context={'form':form})
#     form = ClientLogin()
#     return render(request,'client_login.html',context={'form':form})



def register11(request):
    if request.method == 'POST':
        user = Account()
        if request.POST.get('password1') == request.POST.get('password2'):
            user.user_id = request.POST.get('user_id')
            user.set_password(request.POST.get('password1'))
            user.is_client=True
            user.is_client=False
            user.date_joined=datetime.datetime.now()
            user.save()
            add = ClientDetail()

            add.client = user
            add.SYMBOL = request.POST.get('SYMBOL')
            add.TYPE = request.POST.get('TYPE')
            add.QUANTITY = request.POST.get('QUANTITY')
            add.ENTRY_PRICE = request.POST.get('ENTRY_PRICE')
            add.EXIT_PRICE = request.POST.get('EXIT_PRICE')
            add.created_at = request.POST.get('created_at')
            # add.QUANTITY = MDepartment.objects.get(department_id=request.POST.get('department'))
            # add.company = MCompany.objects.get(company_id=request.POST.get('company'))
            # add.grade = MGrade.objects.get(grade_id=request.POST.get('grade'))
            add.save()
            return redirect('admin_dashboard')
     #   form = RegisterEmployeeForm()
     #   formSub = employeeInfoForm()
    return render(request,'register.html', )#context={'form':form,'formSub':formSub})

def admin_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    # if Account.objects.filter(user_id= request.user.user_id, is_client=True):
    #     client = Client.objects.all()
    #     LeaveRequests = TLeave.objects.filter(is_approved=0)
    #     return render(request,'admin_dashboard.html', context={'allEmp':allEmp, 'LeaveR':LeaveRequests})
    # else:
    #     messages.info(request, 'You Are Not Authorized To Access That Page')
        # return redirect('index')
    return render(request,'admin_dashboard.html')   



def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"  
        except:
            error = "yes"          
    return render(request,'admin_login.html', locals()) 

# def admin_login(request):
#     if request.method == 'POST':
#         Acc = Account()
#         user_id = request.POST.get('user_id')
#         password = request.POST.get('password')
#         user = authenticate(username = user_id , password = password )
#         if user is not None:
#             if Account.objects.filter(user_id=user_id, is_client=True).exists():
#                 login(request,user)
#                 return redirect('admin_dashboard')
#             else:
#                 messages.info(request, 'Invalid, user not An Admin.')
#                 form = ClientLogin()
#                 return render(request,'admin_login.html',context={'form':form})
#         else:
#             messages.info(request, 'Invalid Credentials.')
#             form = ClientLogin()
#             return render(request,'admin_login.html',context={'form':form})
#     form = ClientLogin()
#     return render(request,'admin_login.html',context={'form':form})

# =====================================================================================
def registration(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['fname']
        ln = request.POST['lname']
        mo = request.POST['mobile']
        em = request.POST['email']
        fromd = request.POST['fromdate']
        tod = request.POST['todate']
        pwd = request.POST['pwd']
        try:
            user = User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            ClientDetail.objects.create(user = user,mobile=mo,fromdate=fromd,todate=tod,)
            error = "no"
        except:
            error = "yes" 
    return render(request,'register.html',locals())    




# class ForexTrade:
#     def __init__(self):
#         self.open_positions = {}

#     def buy(self, user, symbol, quantity, entry_price):
#         if symbol in self.open_positions:
#             raise Exception(f"You already have an open position for {symbol}.")
#         self.open_positions[symbol] = {'quantity': quantity, 'entry_price': entry_price}
#         ClientSignal.objects.create(user=user, SYMBOL=symbol, TYPE='BUY_ENTRY', QUANTITY=quantity, ENTRY_PRICE=entry_price, created_at=timezone.now())

#     def close(self, user, symbol, exit_price):
#         if symbol not in self.open_positions:
#             raise Exception(f"You do not have an open position for {symbol} to close.")
#         entry_price = self.open_positions[symbol]['entry_price']
#         quantity = self.open_positions[symbol]['quantity']
#         prloss = (exit_price - entry_price) * quantity
#         total_pl = prloss * datetime.datetime.today().day
#         ClientSignal.objects.create(user=user, SYMBOL=symbol, TYPE='BUY_EXIT', QUANTITY=quantity, ENTRY_PRICE=entry_price, EXIT_PRICE=exit_price, PRLOSS=prloss, TotalPL=total_pl, created_at=timezone.now())
#         del self.open_positions[symbol]


# Function to handle admin messages
# Function to handle admin messages
import random
import string

def generate_unique_id():
    characters = string.ascii_letters + string.digits
    unique_id = ''.join(random.choice(characters) for _ in range(10))
    return unique_id
#ids = None

def admin_message(request):
    error = ""
    user = request.user
    current_date = timezone.now().date()
    d = request.session.get('message_id')
    if request.method == "POST":
        if request.user.is_authenticated:
            client_signals = ClientSignal.objects.filter( message_id = d , ids = 'No')
            
            user = request.user
            sy = request.POST['symbol']
            ty = request.POST['type']
         
            qty_str = request.POST['quantity']
         
            if ty == 'BUY_EXIT' or ty == 'SELL_EXIT':
                    for client_signal in client_signals:
                        if qty_str.strip():  # Check if quantity string is not empty or only whitespace
                            qty = int(qty_str)
                        elif ty == 'BUY_EXIT':
                            qty = client_signal.QUANTITY     
                            enp = client_signal.ENTRY_PRICE
                            exp = int(request.POST['exit_price'])

                        elif ty == 'SELL_EXIT':
                            qty = client_signal.QUANTITY     
                            enp = client_signal.ENTRY_PRICE
                            exp = int(request.POST['exit_price'])    

                        else:
                            qty = 0 # Set qty to a default value or handle it according to your logic
                            enp = int(request.POST['entry_price'])
                            exp =  None
                    
                    
                    
                        if ty == 'BUY_EXIT':
                        
                            prloss = (float(exp) - float(enp)) * qty
                            t = ClientSignal.objects.filter( TYPE = 'BUY_EXIT' , created_at__date=current_date )
                            total = 0
                            for p in t:
                                total += p.cumulative_pl
                            total_pl = int(total) + int(prloss) 

                        elif ty == 'SELL_EXIT':
                            prloss = (float(exp) - float(enp)) * qty
                            t = ClientSignal.objects.filter( TYPE = 'SELL_EXIT' , created_at__date=current_date )
                            total = 0
                            for p in t:
                                total += p.cumulative_pl
                            
                        
                            total_pl = int(total) + int(prloss)
                            
                    
                            
                        creat = ClientSignal.objects.create(user=user, SYMBOL=sy, TYPE=ty, QUANTITY=qty, 
                                                    ENTRY_PRICE=enp, EXIT_PRICE=exp, profit_loss=prloss, 
                                                    cumulative_pl=total_pl, created_at=timezone.now(),
                                                    message_id = client_signal.message_id ,client_id  = client_signal.client_id )
                

            else:
                    qty = 0 # Set qty to a default value or handle it according to your logic
                    enp = int(request.POST['entry_price'])
                    exp =  None
                    prloss = None
                    total_pl = None                                    
                    if ty == 'BUY_ENTRY' or ty == 'SELL_ENTRY':
                        
                        creat = ClientSignal.objects.create(user=user, SYMBOL=sy, TYPE=ty, QUANTITY=qty, 
                                                ENTRY_PRICE=enp, EXIT_PRICE=None, profit_loss=prloss, 
                                                cumulative_pl=total_pl, created_at=timezone.now())
                        i = generate_unique_id()
                        creat.message_id = creat.id
                        creat.ids = i
                        creat.save()      
                        request.session['message_id'] = creat.id
                    #    request.session['ids'] = i
                        global my_global_variable
                        my_global_variable = i
                       
                        error = "no"
         
    return render(request, 'admin_messages.html', )

 
def admin_signals(request):
    buy_entry_signals = ClientSignal.objects.filter(TYPE='BUY_ENTRY')
    buy_exit_signals = ClientSignal.objects.filter(TYPE='BUY_EXIT')
    return render(request, 'admin_signals.html', {'buy_entry_signals': buy_entry_signals, 'buy_exit_signals': buy_exit_signals})

def admin_thistory(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    clientsignal = ClientSignal.objects.all()
    return render(request,'admin_thistory.html',locals())

def admin_tstatus(request):
    return render(request,'admin_tstatus.html')

def admin_client(request):
    return render(request,'admin_client.html')

def admin_help_center(request):
    return render(request,'admin_help_center.html')


# def client_signals(request):
#     if not request.user.is_authenticated:
#         return redirect('client_login')
#     error = ""
#     user = request.user
#     clientcignal = ClientSignal.objects.get(user=user)
#     if request.method == "POST":
#         SYMBOL = request.POST['SYMBOL'] 
#         TYPE = request.POST['TYPE']
#         QUANTITY = request.POST['QUANTITY']
#         ENTRY_PRICE = request.POST['ENTRY_PRICE']
#         EXIT_PRICE = request.POST['EXIT_PRICE']
#         profit_loss = request.POST['profit_loss']
#         cumulative_pl = request.POST['cumulative_pl']
#         created_at = request.POST['created_at']
        
#         clientcignal.user.SYMBOL = SYMBOL
#         clientcignal.user.TYPE = TYPE
#         clientcignal.user.QUANTITY = QUANTITY
#         clientcignal.user.ENTRY_PRICE = ENTRY_PRICE
#         clientcignal.user.EXIT_PRICE = EXIT_PRICE
#         clientcignal.user.profit_loss = profit_loss
#         clientcignal.user.cumulative_pl = cumulative_pl
#         clientcignal.user.created_at = created_at
#         try:
#             clientcignal.save()
#             clientcignal.user.save()
#             error = ""
#         except:
#             error = ""
#     return render(request,'client_signals.html',locals())
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import ClientSignal

def client_signals(request):
    # if not request.user.is_authenticated:
    #     return redirect('client_login')
    today = timezone.now().date()
    signals = ClientSignal.objects.filter(created_at__date=today)
    return render(request, 'client_signals.html', {'clientsignal': signals})  



from datetime import datetime
def client_trade_HISTORY(request):
    # Assuming you want to filter by today's date
    today = datetime.now().date()

    # Filter ClientSignal objects for today
    clientsignal = ClientSignal.objects.filter(created_at__date=today)

    # Pass the filtered data to the template
    return render(request, 'client_thistory.html', {'clientsignal': clientsignal})

def client_tstatus(request):
    return render(request,'client_tstatus.html')

def change_password(request):
    if not request.user.is_authenticated:
        return redirect('client_login')
    error = ""
    user = request.user
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"
            else:
                error = "not"    
        except:
            error = "yes"
    return render(request,'client_change_password.html',locals())            


def admin_change_password(request):
    if not request.user.is_authenticated:
        return redirect('client_login')
    error = ""
    user = request.user
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"
            else:
                error = "not"    
        except:
            error = "yes"
    return render(request,'admin_change_password.html',locals()) 

# def client_dashboard(request):
#     return render(request,'client_dashboard.html')
def client_dashboard(request):
    # Redirect to login page if user is not authenticated
    if not request.user.is_authenticated:
        return redirect('client_login')
    
    # Initialize error message
    error = ""
    
    # Get the current user
    user = request.user
    
    # Get the current date
    current_date = timezone.now().date()
    
    # Filter records for the current day
    client_signals = ClientSignal.objects.filter(user=user, created_at__date=current_date).order_by('-id')

    # Check if client_signals exist for the current day
    if client_signals.exists():
        # Select the first object if multiple are found
        client_signal = client_signals.first()
        print('ttttttttttttttttt')
        print('if')
    else:
        # If no object is found, create a new one
        client_signal = ClientSignal.objects.create(user=user, created_at=current_date)
        print('else')
    # Handle POST request
    if request.method == "POST":
        try:
            # Update client_signal with form data
            
            QUANTITY = request.POST.get('QUANTITY', '')
            if QUANTITY:
                client_signal.QUANTITY = int(QUANTITY)
            else:
                client_signal.QUANTITY = None  # If no value is provided
            
            
            # Ensure that QUANTITY, ENTRY_PRICE, EXIT_PRICE, profit_loss, and cumulative_pl are decimal numbers
            # You can use DecimalField validation to ensure these fields accept only decimal values
            
            client_signal.save()
            
            # Reset error message
            error = ""
            return HttpResponse('add qty')
        except Exception as e:
            # Capture and print any exceptions
            error = str(e)
            print(error)
    
    # Render the template with client_signal and error message
    return render(request, 'client_dashboard.html', {'client_signal': client_signal, 'error': error})

def multibank(request):
    return render(request,'multibank.html')


def dashboard_view(request):
    # Logic for rendering the dashboard view
    return render(request, 'dashboard.html', {'switch_on': False})