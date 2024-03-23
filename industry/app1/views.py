from django.shortcuts import render,  redirect
from django.views import View
from .forms import DeliveryChallanForm, DeliveryChallanToolsForm, DeliveryChallanToolsFormSet, ServiceOrderForm, ServiceToolsForm, TransportMovementOrderForm,TransportOrderForm, TransportToolsForm
from .models import ServiceOrder, ServiceTools, TransportOrder, ShedDetails, TransportTools, Vendor, VendorHandles
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse




# class TransportMovementOrderClass(View):
#     def get(self, request):
#         form = TransportMovementOrderForm()
#         return render(request, 'app1/transportform.html', {'form': form})

#     def post(self, request):
#         form = TransportMovementOrderForm(request.POST)
#         if form.is_valid():
#             movement_date = form.cleaned_data['movement_date']
#             source_shed = form.cleaned_data['source_shed']
#             destination_shed = form.cleaned_data['destination_shed']
#             tool_count = form.cleaned_data['tool_count']
#             # Create a new transport order object
#             transport_order = TransportOrder.objects.create(
#                 movement_date=movement_date,
#                 source_shed=source_shed,
#                 destination_shed=destination_shed,
#                 tool_count=tool_count
#             )
#             # You can add further processing or redirection logic here
#         return render(request, 'app1/transportform.html', {'form': form})
    

# class TransportToolsClass(CreateView):
#     model = TransportTools
#     form_class = TransportToolsForm
#     template_name = 'app1/transport_tools_form.html'
#     success_url = reverse_lazy('app1:transport_tools_form')  # Replace 'app1' with your app name

#     def get_success_url(self):
#         return self.request.path

# class ServiceOrderClass(View):
#     def get(self, request):
#         form = ServiceOrderForm()
#         return render(request, 'app1/service_order_form.html', {'form': form})

#     def post(self, request):
#         form = ServiceOrderForm(request.POST)
#         if form.is_valid():
#             date = form.cleaned_data['date']
#             amount = form.cleaned_data['amount']
#             description = form.cleaned_data['description']
#             tool_count = form.cleaned_data['tool_count']
#             # Create a new service order object
#             service_order = ServiceOrder.objects.create(
#                 date=date,
#                 amount=amount,
#                 description=description,
#                 tool_count=tool_count
#             )
#             # You can add further processing or redirection logic here
#         return render(request, 'app1/service_order_form.html', {'form': form})


# class ServiceToolsClass(CreateView):
#     model = ServiceTools
#     form_class = ServiceToolsForm
#     template_name = 'app1/service_tools_form.html'
#     success_url = reverse_lazy('app1:service_tools_form')  # Replace 'app1' with your app name

#     def get_success_url(self):
#         return self.request.path
def home(request):
    return render(request, 'app1/home.html')


# class TransportOrderView(View):
#     def get(self, request):
#         order_form = TransportOrderForm()
#         tool_forms = [TransportToolsForm(prefix=str(x)) for x in range(3)]  # Adjust the range as needed
#         return render(request, 'app1/transport_order_form.html', {'order_form': order_form, 'tool_forms': tool_forms})

#     def post(self, request):
#         order_form = TransportOrderForm(request.POST)
#         tool_forms = [TransportToolsForm(request.POST, prefix=str(x)) for x in range(3)]  # Adjust the range as needed

#         if order_form.is_valid() and all(form.is_valid() for form in tool_forms):
#             transport_order = order_form.save()
#             for form in tool_forms:
#                 if form.cleaned_data.get('tool'):
#                     tool = form.cleaned_data['tool']
#                     TransportTools.objects.create(transport=transport_order, tool=tool)
#             return redirect('home')  # Replace 'success_url' with your desired success URL

#         return render(request, 'app1/transport_order_form.html', {'order_form': order_form, 'tool_forms': tool_forms})


# class TransportOrderView(View):
#     def get(self, request):
#         order_form = TransportOrderForm()
#         tool_forms = [TransportToolsForm(prefix=str(x)) for x in range(3)]  # Adjust the range as needed
#         data = {
#             'order_form': order_form.data,
#             'tool_forms': [form.data for form in tool_forms]
#         }
#         return JsonResponse(data)

#     def post(self, request):
#         order_form = TransportOrderForm(request.POST)
#         tool_forms = [TransportToolsForm(request.POST, prefix=str(x)) for x in range(3)]  # Adjust the range as needed

#         if order_form.is_valid() and all(form.is_valid() for form in tool_forms):
#             transport_order = order_form.save()
#             for form in tool_forms:
#                 if form.cleaned_data.get('tool'):
#                     tool = form.cleaned_data['tool']
#                     TransportTools.objects.create(transport=transport_order, tool=tool)
#             return JsonResponse({'success': True})  # Return success response as JSON

#         errors = {
#             'order_form_errors': order_form.errors,
#             'tool_form_errors': [form.errors for form in tool_forms]
#         }
#         return JsonResponse(errors, status=400)  # Return errors as JSON with status code 400

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TransportOrder
from .serializers import TransportOrderSerializer, TransportToolsSerializer

class TransportOrderView(APIView):
    def get(self, request):
        orders = TransportOrder.objects.all()
        serializer = TransportOrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        order_serializer = TransportOrderSerializer(data=request.data)
        if order_serializer.is_valid():
            transport_order = order_serializer.save()
            tools_serializer = TransportToolsSerializer(data=request.data.get('tools'), many=True)
            if tools_serializer.is_valid():
                tools_serializer.save(transport=transport_order)
                return Response({'success': True})
            else:
                transport_order.delete()  # Rollback if tools data is invalid
                return Response(tools_serializer.errors, status=400)
        else:
            return Response(order_serializer.errors, status=400)

from .forms import AnotherServiceOrderForm, AnotherServiceToolForm
from .models import ServiceOrder, ServiceTools

class ServiceOrderView(View):
    def get(self, request):
        order_form = AnotherServiceOrderForm()
        tool_forms = [AnotherServiceToolForm(prefix=str(x)) for x in range(3)]  # Adjust the range as needed

        return render(request, 'app1/service_order_form1.html', {'order_form': order_form, 'tool_forms': tool_forms})

    def post(self, request):
        order_form = AnotherServiceOrderForm(request.POST)
        tool_forms = [AnotherServiceToolForm(request.POST, prefix=str(x)) for x in range(3)]

        if order_form.is_valid() and all(form.is_valid() for form in tool_forms):
            service_order = order_form.save()
            vendor_id = request.POST.get('vendor')  # Get the vendor ID from the form

            for form in tool_forms:
                if form.cleaned_data.get('tool'):
                    tool = form.cleaned_data['tool']
                    ServiceTools.objects.create(service=service_order, tool=tool, vendor_id=vendor_id)  # Pass vendor_id to create ServiceTools

            return redirect('generate_bill')  # Redirect to GenerateBillView

        # Handle invalid forms
        return render(request, 'app1/service_order_form1.html', {'order_form': order_form, 'tool_forms': tool_forms})

# class ServiceOrderView(View):
#     def get(self, request):
#         order_form = AnotherServiceOrderForm()
#         tool_forms = [AnotherServiceToolForm(prefix=str(x)) for x in range(3)]  # Adjust the range as needed

#         data = {
#             'order_form': order_form.data,
#             'tool_forms': [form.data for form in tool_forms]
#         }

#         return JsonResponse(data)

#     def post(self, request):
#         order_form = AnotherServiceOrderForm(request.POST)
#         tool_forms = [AnotherServiceToolForm(request.POST, prefix=str(x)) for x in range(3)]

#         if order_form.is_valid() and all(form.is_valid() for form in tool_forms):
#             service_order = order_form.save()
#             vendor_id = request.POST.get('vendor')

#             for form in tool_forms:
#                 if form.cleaned_data.get('tool'):
#                     tool = form.cleaned_data['tool']
#                     ServiceTools.objects.create(service=service_order, tool=tool, vendor_id=vendor_id)

#             return JsonResponse({'success': True})

#         errors = {
#             'order_form_errors': order_form.errors,
#             'tool_form_errors': [form.errors for form in tool_forms]
#         }
#         return JsonResponse(errors, status=400)

class GenerateBillView(View):
    def get(self, request):
        service_tools = ServiceTools.objects.all()
        bill_items = []
        total_amount = 0
        for service_tool in service_tools:
            tool = service_tool.tool
            vendor = service_tool.vendor
            vendor_handles = VendorHandles.objects.filter(tool=tool, vendor=vendor)
            for vendor_handle in vendor_handles:
                cost = vendor_handle.cost
                amount = 1 * cost  # Assuming each tool has a count of 1
                total_amount += amount
                bill_items.append({'tool': tool, 'cost': cost, 'amount': amount})
        return render(request, 'app1/generate_bill.html', {'bill_items': bill_items, 'total_amount': total_amount})

# class GenerateBillView(View):
#     def get(self, request):
#         service_tools = ServiceTools.objects.all()
#         bill_items = []
#         total_amount = 0
#         for service_tool in service_tools:
#             tool = service_tool.tool
#             vendor = service_tool.vendor
#             vendor_handles = VendorHandles.objects.filter(tool=tool, vendor=vendor)
#             for vendor_handle in vendor_handles:
#                 cost = vendor_handle.cost
#                 amount = 1 * cost  # Assuming each tool has a count of 1
#                 total_amount += amount
#                 bill_items.append({'tool': tool.name, 'cost': cost, 'amount': amount})  # Assuming tool has a 'name' attribute
#         data = {
#             'bill_items': bill_items,
#             'total_amount': total_amount
#         }
#         return JsonResponse(data)

class CreateDeliveryChallanView(View):
    def get(self, request):
        delivery_challan_form = DeliveryChallanForm()
        delivery_challan_tools_formset = DeliveryChallanToolsFormSet()
        return render(request, 'app1/delivery_challan.html', {'delivery_challan_form': delivery_challan_form, 'delivery_challan_tools_formset': delivery_challan_tools_formset})

    def post(self, request):
        delivery_challan_form = DeliveryChallanForm(request.POST)
        delivery_challan_tools_formset = DeliveryChallanToolsForm(request.POST)
        if delivery_challan_form.is_valid() and delivery_challan_tools_formset.is_valid():
            delivery_challan = delivery_challan_form.save()
            for form in delivery_challan_tools_formset:
                delivery_challan_tool = form.save(commit=False)
                delivery_challan_tool.deliverychallan = delivery_challan
                delivery_challan_tool.save()
            return redirect('home')  # Redirect to success URL
        return render(request, 'app1/delivery_challan.html', {'delivery_challan_form': delivery_challan_form, 'delivery_challan_tools_formset': delivery_challan_tools_formset})
    