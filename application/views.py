import datetime
import io
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import FileResponse
from reportlab.pdfgen import canvas

from application.functions import create_context
from application.decorators import allowed_users
from application.models import Offer, Truck, Request, Contract

TYPE_FREIGHT = ['furniture', 'animals', 'food', 'cars', 'medication', 'electronics', 'machinery']
FUEL_TYPE = ['benzine', 'diesel']
TRUCK_TYPE = ['truck', 'van', 'trailer', 'refrigerated truck']


# Create your views here.
# @login_required(login_url='login')
# def home(request):
#     gis = GIS()
#     map = gis.map("Palm Springs, CA")
#     return render(request, 'application/home.html', {'map': map})


@login_required(login_url='login')
def home(request):
    user = request.user
    user_groups = [group.name for group in user.groups.all()]
    context = {'user_groups': user_groups}
    return render(request, 'application/main_layout_application.html', context)


@login_required(login_url='login')
def account(request):
    user = request.user
    user_groups = [group.name for group in user.groups.all()]
    context = {'user_groups': user_groups}
    return render(request, 'application/account.html', context)


@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def administrator(request):
    return redirect('admin')


@allowed_users(allowed_roles=['transportator'])
@login_required(login_url='login')
def offer_view(request):
    user = request.user
    user_groups = [group.name for group in user.groups.all()]
    offer = Offer()
    trucks = Truck.objects.all().filter(ownerId=request.user)
    sender = request.user.username.__str__()
    freight_type = TYPE_FREIGHT
    price_per_km = 0

    if request.method == "POST":
        offer.senderID = request.user
        offer.truckID = Truck.objects.all().get(id=request.POST.get("truckID"))
        offer.freight_type = request.POST.get("f_t")
        offer.price_per_km = request.POST.get('price_per_km')
        offer.price_per_km_emptyTruck = request.POST.get('price_per_km_emptyTruck')
        offer.departure_date = request.POST.get('departure_date')
        offer.arrival_date = request.POST.get('arrival_date')
        offer.source = request.POST.get('source')
        offer.destination = request.POST.get('destination')
        offer.phone = request.POST.get('phone')
        offer.email = request.POST.get('email')
        offer.other_details = request.POST.get('other_details')
        offer.save()

    context = {'user_groups': user_groups,
               'trucks': trucks,
               'sender': sender,
               'f_t': freight_type,
               'price_per_km': price_per_km}
    return render(request, "application/create_offer.html", context)


@login_required(login_url='login')
def trucks(request):
    user = request.user
    user_groups = [group.name for group in user.groups.all()]

    curr_trucks = Truck.objects.all().filter(ownerId=request.user)
    new_truck = Truck()

    if request.method == "POST":
        new_truck.ownerId = request.user
        new_truck.brand = request.POST.get('brand')
        new_truck.registration_plate = request.POST.get('reg_plt')
        new_truck.fuel = request.POST.get('fuel')
        new_truck.type = request.POST.get('type')
        new_truck.max_load = request.POST.get('max_load')
        new_truck.save()

    context = {'user_groups': user_groups, 'trucks': curr_trucks, 'fuel_t': FUEL_TYPE, 'truck_t': TRUCK_TYPE}
    return render(request, "application/trucks.html", context=context)


@allowed_users(allowed_roles=['client'])
@login_required(login_url='login')
def create_request(request):
    user = request.user
    user_groups = [group.name for group in user.groups.all()]
    transport_request = Request()
    client = request.user.username.__str__()
    freight_types = TYPE_FREIGHT
    registration_date = datetime.date.today()
    max_price = 0
    source = ''
    destination = ''
    arrival_date = None
    weight = 0

    if request.method == 'POST':
        transport_request.clientID = request.user
        transport_request.source = request.POST.get('source')
        transport_request.destination = request.POST.get('destination')
        transport_request.departure_date = request.POST.get('departure_date')
        transport_request.arrival_date = request.POST.get('arrival_date')
        transport_request.freight_type = request.POST.get('freight_types')
        transport_request.max_price = request.POST.get('max_price')
        transport_request.weight = request.POST.get('weight')
        transport_request.phone = request.POST.get('phone')
        transport_request.email = request.POST.get('email')
        transport_request.other_details = request.POST.get('other_details')
        transport_request.save()

    context = {'user_groups': user_groups, 'client': client, 'freight_types': freight_types,
               'registration_date': registration_date, 'max_price': max_price, 'source': source,
               'destination': destination, 'arrival_date': arrival_date, 'weight': weight}

    return render(request, "application/create_request.html", context)


@allowed_users(allowed_roles=['client'])
@login_required(login_url='login')
def offers(request):
    context = create_context(request)
    users = User.objects.all()
    offers = Offer.objects.all()
    trucks = Truck.objects.all()
    context['users'] = users
    context['offers'] = offers
    context['trucks'] = trucks
    return render(request, "application/offers.html", context)


@allowed_users(allowed_roles=['transportator'])
@login_required(login_url='login')
def requests(request):
    context = create_context(request)
    users = User.objects.all()
    requests = Request.objects.all()
    context['users'] = users
    context['requests'] = requests
    return render(request, "application/requests.html", context)


@allowed_users(allowed_roles=['client'])
def generate_contract_for_offer(request, pk):
    buffer = io.BytesIO()
    offer = Offer.objects.get(id=pk)
    p = canvas.Canvas(buffer)
    contract = Contract()
    if request.method == 'POST':
        contract.transporterID = offer.senderID
        contract.senderID = request.user
        contract.truckID = offer.truckID
        contract.source = offer.source
        contract.destination = offer.destination
        contract.date = datetime.date.today()
        contract.freight_type = offer.freight_type
        contract.km = 10000
        contract.final_price = offer.price_per_km * contract.km
        offer.delete()
        contract.save()

    p.drawString(50, 750, 'Contract' + '    ' + 'No: ' + str(contract.id))
    p.drawString(50, 710, 'The current contract is made between the component parts, ' +
                 'the client: ' + request.user.last_name + ' ' + request.user.first_name)
    p.drawString(40, 690, ' and the transporter: ' + offer.senderID.last_name + ' ' + offer.senderID.first_name + '.')
    p.drawString(50, 660, 'The transporter is obliged to take the goods from the source location: ' + contract.source)
    p.drawString(40, 640, 'and deliver them to the destination location: ' + contract.destination + '.')
    p.drawString(50, 610, 'The transporter will take over the goods of the type ' + contract.freight_type +
                 ', will use the truck with the')
    p.drawString(40, 590, '  following information: ' + 'truck id ' + str(contract.truckID.id) + ', '
                 + 'registration plate ' + contract.truckID.registration_plate + ', brand '
                 + contract.truckID.brand + ', type ' + contract.truckID.type + ', ')
    p.drawString(40, 570, 'fuel ' + contract.truckID.fuel + ', maximum load ' + str(contract.truckID.max_load) + '.')
    p.drawString(50, 540, 'The price agreed by the two parts is going to be paid by the client and is '
                 + str(contract.final_price) + ' lei.')
    p.drawString(50, 480, 'The date of the contract is ' + str(contract.date) + '.')
    p.drawImage(
        'C:\\Users\\40729\\Desktop\\Automatica si Calculatoare\\TransportPlatform\\application\\static\\application'
        '\\css\\images\\signature.png', 40, 300, 220, 150)
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='contract.pdf')


@allowed_users(allowed_roles=['transportator'])
def generate_contract_for_request(request, pk):
    buffer = io.BytesIO()
    req = Request.objects.get(id=pk)
    p = canvas.Canvas(buffer)
    contract = Contract()
    trucks = Truck.objects.filter(ownerId=request.user)
    for truck in trucks:
        if req.weight <= truck.max_load:
            t = truck

    print(t.id)
    if request.method == 'POST':
        contract.transporterID = request.user
        contract.senderID = req.clientID
        contract.truckID = t
        contract.source = req.source
        contract.destination = req.destination
        contract.date = datetime.date.today()
        contract.freight_type = req.freight_type
        contract.final_price = req.max_price
        contract.km = 1000
        req.delete()
        contract.save()

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(50, 750, 'Contract' + '    ' + 'No: ' + str(contract.id))
    p.drawString(50, 710, 'The current contract is made between the component parts, ' +
                 'the client: ' + req.clientID.last_name + ' ' + req.clientID.first_name)
    p.drawString(40, 690, ' and the transporter: ' + request.user.last_name + ' ' + request.user.first_name + '.')
    p.drawString(50, 660, 'The transporter is obliged to take the goods from the source location: ' + contract.source)
    p.drawString(40, 640, 'and deliver them to the destination location: ' + contract.destination + '.')
    p.drawString(50, 610, 'The transporter will take over the goods of the type ' + contract.freight_type +
                 ', will use the truck with the')
    p.drawString(40, 590, '  following information: ' + 'truck id ' + str(contract.truckID.id) + ', '
                 + 'registration plate ' + contract.truckID.registration_plate + ', brand '
                 + t.brand + ', type ' + contract.truckID.type + ', ')
    p.drawString(40, 570, 'fuel ' + contract.truckID.fuel + ', maximum load ' + str(contract.truckID.max_load) + '.')
    p.drawString(50, 540, 'The price agreed by the two parts is going to be paid by the client and is '
                 + str(contract.final_price) + ' lei.')
    p.drawString(50, 480, 'The date of the contract is ' + str(contract.date) + '.')
    p.drawImage(
        'C:\\Users\\40729\\Desktop\\Automatica si Calculatoare\\TransportPlatform\\application\\static\\application'
        '\\css\\images\\signature.png', 40, 300, 220, 150)
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='contract.pdf')


@login_required(login_url='login')
def contracts(request):
    context = create_context(request)
    contracts = Contract.objects.all()
    user = request.user
    context['contracts'] = contracts
    context['user'] = user
    return render(request, 'application/contracts.html', context=context)
