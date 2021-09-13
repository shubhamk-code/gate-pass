from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, response, FileResponse
from .models import *
from .forms import VisitorForm, ContractorForm
from .filters import *
import csv
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


def home(request):
    return render(request, 'gatePassApp/master.html')

def banned(request):
    visitors = Visitor.objects.all()
    myfilter = VisitorFilter(request.GET, queryset=visitors)
    visitors = myfilter.qs
    context = {'visitors': visitors, 'myfilter': myfilter}
    return render(request, 'gatePassApp/banned.html', context)


def cancelled(request):
    visitors = Visitor.objects.all()
    myfilter = VisitorFilter(request.GET, queryset=visitors)
    visitors = myfilter.qs
    context = {'visitors': visitors, 'myfilter': myfilter}
    return render(request, 'gatePassApp/cancelled.html', context)

def profile(request, visitor_id):
    user = Visitor.objects.get(pk=visitor_id)
    context = {'user': user}
    return render(request, 'gatePassApp/userProfile.html', context)


def visitor(request):
    visitors = Visitor.objects.all()
    myfilter = VisitorFilter(request.GET, queryset=visitors)
    visitors = myfilter.qs
    context = {'visitors': visitors, 'myfilter': myfilter}
    return render(request, 'gatePassApp/visitor.html', context)


def visitorAppoints(request):
    visitors = Visitor.objects.all()
    myfilter = VisitorFilter(request.GET, queryset=visitors)
    visitors = myfilter.qs
    context = {'visitors': visitors, 'myfilter': myfilter}
    return render(request, 'gatePassApp/visitorAppoints.html', context)


def employeeAppoints(request):
    visitors = Visitor.objects.all()
    for visitor in visitors:
        if visitor.staff == "None":
            visitor.staff = None
    myfilter = VisitorFilter(request.GET, queryset=visitors)
    visitors = myfilter.qs
    context = {'visitors': visitors, 'myfilter': myfilter}
    return render(request, 'gatePassApp/employeeAppoints.html', context)


def contractor(request):
    contractors = Contractor.objects.all()
    myfilter = ContractorFilter(request.GET, queryset=contractors)
    contractors = myfilter.qs
    context = {'contractors': contractors, 'myfilter': myfilter}
    return render(request, 'gatePassApp/contractor.html', context)


def search_visitors(request):
    if request.method == 'GET':
        searched = request.POST['searched']
        visitors = Visitor.objects.filter(name__contains=searched)
        context = {'searched': searched, 'visitors': visitors}
        return render(request, 'gatePassApp/visitor.html', context)
    return render(request, 'gatePassApp/visitor.html')


def search_contractors(request):
    if request.method == 'GET':
        searched = request.POST['searched']
        contractors = Contractor.objects.filter(name__contains=searched)
        context = {'searched': searched, 'contractors': contractors}
        return render(request, 'gatePassApp/contractor.html', context)
    return render(request, 'gatePassApp/contractor.html')


def addVisitor(request):
    form = VisitorForm()
    print(form.data, request.POST)
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            # if visitor is not None:
            #     if visitor.ban == 'Unbanned':
            #         return redirect('visitor')
            #     else:
            #         return redirect('visitor')
            form.save()
            return redirect('visitor')
    context = {'form': form}
    return render(request, 'gatePassApp/visitor-form.html', context)


def addContractor(request):
    form = ContractorForm()
    print(form.data, request.POST)
    if request.method == 'POST':
        form = ContractorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contractor')
    context = {'form': form}
    return render(request, 'gatePassApp/contractor-form.html', context)


def updateVisitor(request, pk):
    visitor = Visitor.objects.get(id=pk)
    form = VisitorForm(instance=visitor)
    if request.method == 'POST':
        form = VisitorForm(request.POST, instance=visitor)
        # if visitor is not None:
        #     if visitor.ban == 'Unbanned':
        #         return redirect('visitor')
        #     else:
        #         return redirect('visitor')
        if form.is_valid():
            form.save()
            return redirect('visitor')
    context = {'form': form}
    return render(request, 'gatePassApp/visitor-form.html', context)


def updateContractor(request, pk):
    contractor = Contractor.objects.get(id=pk)
    form = ContractorForm(instance=contractor)
    if request.method == 'POST':
        form = ContractorForm(request.POST, instance=contractor)
        if form.is_valid():
            form.save()
            return redirect('contractor')
    context = {'form': form}
    return render(request, 'gatePassApp/contractor-form.html', context)


def deleteVisitor(request, pk):
    visitor = Visitor.objects.get(id=pk)
    if request.method == 'POST':
        visitor.delete()
        return redirect('visitor')
    return render(request, 'gatePassApp/deleteVisitor.html', {'object': visitor})


def deleteContractor(request, pk):
    contractor = Contractor.objects.get(id=pk)
    if request.method == 'POST':
        contractor.delete()
        return redirect('contractor')
    return render(request, 'gatePassApp/deleteContractor.html', {'object': contractor})


# generate text file

def visitor_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=visitors.txt'
    visitors = Visitor.objects.all()
    lines = []
    for visitor in visitors:
        lines.append(
            f'{visitor.name}\n{visitor.email}\n{visitor.age}\n{visitor.gender}\n{visitor.contact}\n{visitor.address}\n{visitor.company}\n{visitor.department}\n{visitor.staff}\n{visitor.items}\n{visitor.others}\n\n')
    response.writelines(lines)
    return response


def contractor_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=contractors.txt'
    contractors = Contractor.objects.all()
    lines = []
    for contractor in contractors:
        lines.append(
            f'{contractor.name}\n{contractor.email}\n{contractor.company}\n{contractor.mediator_name}\n{contractor.contact}\n{contractor.contractual}\n\n')
    response.writelines(lines)
    return response


# csv file format

def visitor_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=visitors.csv'
    writer = csv.writer(response)
    visitors = Visitor.objects.all()
    writer.writerow(['Visitor Name', 'Visitor Email', 'Visitor Age',
                    'Visitor Gender', 'Visitor Contact', 'Visitor Address', 'Visitor Company', 'Visitor Department', 'Visitor meeting', 'Visitor items', 'Visitor others'])
    # lines = []
    for visitor in visitors:
        writer.writerow([visitor.name, visitor.email, visitor.age,
                        visitor.gender, visitor.contact, visitor.address, visitor.company, visitor.department, visitor.staff, visitor.items, visitor.others])
    return response


def contractor_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=contractors.csv'
    writer = csv.writer(response)
    contractors = Contractor.objects.all()
    writer.writerow(['Contractor Name', 'Email', 'Company',
                     'Mediator Name', 'contact', 'Contractual'])
    # lines = []
    for contractor in contractors:
        writer.writerow([contractor.name, contractor.email, contractor.company,
                        contractor.mediator_name, contractor.contact, contractor.contractual])
    return response


# pdf file format

def visitor_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica",  14)
    visitors = Visitor.objects.all()
    lines = []
    for visitor in visitors:
        lines.append(visitor.name)
        lines.append(visitor.email)
        lines.append(visitor.age)
        lines.append(visitor.gender)
        lines.append(visitor.contact)
        lines.append(visitor.address)
        lines.append(visitor.company)
        lines.append(visitor.department.department_name)
        lines.append(visitor.staff.name)
        lines.append(visitor.items)
        lines.append(visitor.others)
        lines.append(
            "------------------------------------------------------------------------------------------------")
    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='visitor.pdf')


def contractor_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica",  14)
    contractors = Contractor.objects.all()
    lines = []
    for contractor in contractors:
        lines.append(contractor.name)
        lines.append(contractor.email)
        lines.append(contractor.company)
        lines.append(contractor.mediator_name)
        lines.append("------------------------------------------------------------------------------------------------")
    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='contractor.pdf')


def all_events(request):
    event_list = Event.objects.all()
    context = {'event_list': event_list}
    return render(request, 'gatePassApp/eventList.html', context)
