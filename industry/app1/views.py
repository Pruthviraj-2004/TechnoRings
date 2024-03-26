from django.http import JsonResponse
from django.shortcuts import render,  redirect
from django.views import View
from .forms import CalibrationReportForm, DeliveryChallanForm, DeliveryChallanToolsForm, DeliveryChallanToolsFormSet, ServiceOrderForm, ServiceToolsForm, TransportMovementOrderForm,TransportOrderForm, TransportToolsForm
from .models import CalibrationReport, InstrumentModel,  ServiceOrder, ServiceTools, ShedTools, TransportOrder, ShedDetails, TransportTools, Vendor, VendorHandles
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TransportOrder
from .serializers import CalibrationReportSerializer, InstrumentModelSerializer, ServiceOrderSerializer, ServiceToolsSerializer, ShedDetailsSerializer, ShedToolsSerializer, TransportOrderSerializer, TransportToolsSerializer, VendorHandlesSerializer, VendorSerializer

from .forms import AnotherServiceOrderForm, AnotherServiceToolForm
from .models import ServiceOrder, ServiceTools

from django.db import transaction
from django.shortcuts import get_object_or_404

class VendorView(APIView):
    def get(self, request):
        vendor = Vendor.objects.all()
        vendor_serializer = VendorSerializer(vendor, many=True)

        response_data = {
            'vendor' : vendor_serializer.data,
        }

        return Response(response_data)
    
class InstrumentToolsView(APIView):
    def get(self, request):
        instruments = InstrumentModel.objects.all()
        instrument_serializer = InstrumentModelSerializer(instruments, many=True)

        response_data = {
            'instrument_models': instrument_serializer.data,
        }

        return Response(response_data)
    
class ShedDetailsView(APIView):
    def get(self, request):
        shed_details = ShedDetails.objects.all()
        shed_serializer = ShedDetailsSerializer(shed_details, many=True)

        response_data = {
            'shed_details' : shed_serializer.data,
        }

        return Response(response_data)

class ShedToolsView(APIView):
    def get(self, request):
        shed_tools_details = ShedTools.objects.all()
        shed_tools_serializer = ShedToolsSerializer(shed_tools_details, many=True)

        response_data = {
            'shed_tools_details' : shed_tools_serializer.data,
        }

        return Response(response_data)

class VendorHandlesView(APIView):
    def get(self, request):
        vendor_handles = VendorHandles.objects.all()
        vendor_handles_serializer = VendorHandlesSerializer(vendor_handles, many=True)

        response_data = {
            'vendor_handles' : vendor_handles_serializer.data,
        }

        return Response(response_data)
    
class CalibrationReportView(APIView):
    def get(self, request):
        calibration_report = CalibrationReport.objects.all()
        calibration_report_serializer = CalibrationReportSerializer(calibration_report, many=True)

        response_data = {
            'calibration_report' : calibration_report_serializer.data,
        }

        return Response(response_data)
        
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

class TransportOrderView(APIView):
    def get(self, request):
        orders_details = TransportOrder.objects.all()
        orders_serializer = TransportOrderSerializer(orders_details, many=True)
        
        instrument_models = InstrumentModel.objects.all()
        instrument_serializer = InstrumentModelSerializer(instrument_models, many=True)

        shed_details = ShedDetails.objects.all()
        shed_serializer = ShedDetailsSerializer(shed_details, many=True)

        shed_tools_details = ShedTools.objects.all()
        shed_tools_serializer = ShedToolsSerializer(shed_tools_details, many=True)

        response_data = {
            'transport_orders': orders_serializer.data,
            'instrument_models': instrument_serializer.data,
            'shed_details' : shed_serializer.data,
            'shed_tools_details' : shed_tools_serializer.data,
        }

        return Response(response_data)

    # def post(self, request):
    # # Deserialize the received data
    #     serializer = TransportOrderSerializer(data=request.data)
    #     if serializer.is_valid():
    #         # Extract relevant data from the request
    #         movement_date = serializer.validated_data['movement_date']
    #         source_shed = serializer.validated_data['source_shed']
    #         destination_shed = serializer.validated_data['destination_shed']
    #         tool_count = serializer.validated_data['tool_count']
    #         acknowledgment = serializer.validated_data.get('acknowledgment', False)

    #         # Create the transport order
    #         transport_order = TransportOrder.objects.create(
    #             movement_date=movement_date,
    #             source_shed=source_shed,
    #             destination_shed=destination_shed,
    #             tool_count=tool_count,
    #             acknowledgment=acknowledgment
    #         )

    #         return JsonResponse({'success': True}, status=201)
    #     else:
    #         return JsonResponse(serializer.errors, status=400)

    def post(self, request):
        # Deserialize the received data
        serializer = TransportOrderSerializer(data=request.data)
        if serializer.is_valid():
            # Extract relevant data from the request
            movement_date = serializer.validated_data['movement_date']
            source_shed_id = serializer.validated_data['source_shed']
            destination_shed_id = serializer.validated_data['destination_shed']
            tool_count = serializer.validated_data['tool_count']
            acknowledgment = serializer.validated_data.get('acknowledgment', False)
            tools_data = request.data.get('tools', [])

            # Retrieve source and destination shed objects
            # source_shed = get_object_or_404(ShedDetails, pk=source_shed_id)
            # destination_shed = get_object_or_404(ShedDetails, pk=destination_shed_id)

            # Create the transport order
            transport_order = TransportOrder.objects.create(
                movement_date=movement_date,
                source_shed=source_shed_id,
                destination_shed=destination_shed_id,
                tool_count=tool_count,
                acknowledgment=acknowledgment
            )

            # Create tools associated with the transport order
            for tool_data in tools_data:
                tool_id = tool_data.get('tool')
                tool = get_object_or_404(InstrumentModel, pk=tool_id)
                TransportTools.objects.create(transport=transport_order, tool=tool)

            return JsonResponse({'success': True}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ServiceOrderView(View):
#     def get(self, request):
#         order_form = AnotherServiceOrderForm()
#         tool_forms = [AnotherServiceToolForm(prefix=str(x)) for x in range(3)]  # Adjust the range as needed

#         return render(request, 'app1/service_order_form1.html', {'order_form': order_form, 'tool_forms': tool_forms})

#     def post(self, request):
#         order_form = AnotherServiceOrderForm(request.POST)
#         tool_forms = [AnotherServiceToolForm(request.POST, prefix=str(x)) for x in range(3)]

#         if order_form.is_valid() and all(form.is_valid() for form in tool_forms):
#             service_order = order_form.save()
#             vendor_id = request.POST.get('vendor')  # Get the vendor ID from the form

#             for form in tool_forms:
#                 if form.cleaned_data.get('tool'):
#                     tool = form.cleaned_data['tool']
#                     ServiceTools.objects.create(service=service_order, tool=tool, vendor_id=vendor_id)  # Pass vendor_id to create ServiceTools

#             return redirect('generate_bill')  # Redirect to GenerateBillView

#         # Handle invalid forms
#         return render(request, 'app1/service_order_form1.html', {'order_form': order_form, 'tool_forms': tool_forms})

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

            # Redirect to GenerateBillView with the created service order ID
            return redirect('generate_bill', service_order_id=service_order.service_id)

        # Handle invalid forms
        return render(request, 'app1/service_order_form1.html', {'order_form': order_form, 'tool_forms': tool_forms})

# class ServiceOrderView(APIView):
#     def get(self, request):
#         service_orders = ServiceOrder.objects.all()
#         service_order_serializer = ServiceOrderSerializer(service_orders, many=True)

#         service_tools = ServiceTools.objects.all()
#         service_tools_serializer = ServiceToolsSerializer(service_tools, many=True)

#         vendors = Vendor.objects.all()
#         vendor_serializer = VendorSerializer(vendors, many=True)

#         instrument_models = InstrumentModel.objects.all()
#         instrument_serializer = InstrumentModelSerializer(instrument_models, many=True)

#         response_data = {
#             'service_orders': service_order_serializer.data,
#             'service_tools': service_tools_serializer.data,
#             'vendors': vendor_serializer.data,
#             'instrument_tools' : instrument_serializer.data,
#         }

#         return Response(response_data)

#     # def post(self, request):
#     #     # Serialize the incoming data
#     #     order_serializer = ServiceOrderSerializer(data=request.data)
        
#     #     # Check if the incoming data is valid
#     #     if order_serializer.is_valid():
#     #         # Save the service order
#     #         service_order = order_serializer.save()

#     #         # Retrieve and validate the list of tools
#     #         tools_data = request.data.get('tools', [])
#     #         tools_serializer = ServiceToolsSerializer(data=tools_data, many=True)
            
#     #         if tools_serializer.is_valid():
#     #             # Save the tools associated with the service order
#     #             for tool_data in tools_data:
#     #                 tool_id = tool_data.get('tool')
#     #                 tool = get_object_or_404(InstrumentModel, pk=tool_id)
#     #                 ServiceTools.objects.create(service=service_order, tool=tool)

#     #             # Return success response
#     #             return Response({'success': True}, status=status.HTTP_201_CREATED)
#     #         else:
#     #             # If tool data is not valid, delete the service order
#     #             service_order.delete()
#     #             return Response(tools_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     #     else:
#     #         # Return error response if service order data is not valid
#     #         return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def post(self, request):
#         # Serialize the incoming data
#         order_serializer = ServiceOrderSerializer(data=request.data)
        
#         # Check if the incoming data is valid
#         if order_serializer.is_valid():
#             # Save the service order
#             service_order = order_serializer.save()

#             # Retrieve and validate the list of tools
#             tools_data = request.data.get('tools', [])
#             for tool_data in tools_data:
#                 # Retrieve the tool and vendor objects
#                 tool_id = tool_data.get('tool')
#                 vendor_id = tool_data.get('vendor')
#                 tool = get_object_or_404(InstrumentModel, pk=tool_id)
#                 vendor = get_object_or_404(Vendor, pk=vendor_id)

#                 # Create the ServiceTools instance with proper vendor
#                 ServiceTools.objects.create(service=service_order, tool=tool, vendor=vendor)

#             # Return success response
#             return Response({'success': True}, status=status.HTTP_201_CREATED)
#         else:
#             # Return error response if service order data is not valid
#             return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
#                 bill_items.append({'tool': tool, 'cost': cost, 'amount': amount})
#         return render(request, 'app1/generate_bill.html', {'bill_items': bill_items, 'total_amount': total_amount})
    
class GenerateBillView(View):
    def get(self, request, service_order_id):
        # Retrieve the service order
        service_order = get_object_or_404(ServiceOrder, pk=service_order_id)
        
        # Now you can generate the bill for the given service order and render the template
        # with the bill items and total amount
        service_tools = ServiceTools.objects.filter(service=service_order)
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
    
class DeliveryChallanView(View):
    def get(self, request):
        delivery_challan_form = DeliveryChallanForm()
        delivery_challan_tools_formset = DeliveryChallanToolsFormSet()
        calibration_report_form = CalibrationReportForm()  # Include CalibrationReportForm
        return render(request, 'app1/delivery_challan.html', {'delivery_challan_form': delivery_challan_form, 'delivery_challan_tools_formset': delivery_challan_tools_formset, 'calibration_report_form': calibration_report_form})

    def post(self, request):
        delivery_challan_form = DeliveryChallanForm(request.POST)
        delivery_challan_tools_formset = DeliveryChallanToolsFormSet(request.POST)
        calibration_report_form = CalibrationReportForm(request.POST)

        if calibration_report_form.is_valid():
            # Store calibration report details
            calibration_report = calibration_report_form.save(commit=False)
            
            # Set the calibration_tool_id programmatically
            calibration_report.calibration_tool_id = 1  # Replace <some_tool_id> with the actual ID
            
            calibration_report.save()
            
            if delivery_challan_form.is_valid() and delivery_challan_tools_formset.is_valid():
                # Store delivery challan details
                delivery_challan = delivery_challan_form.save()
                
                for form in delivery_challan_tools_formset:
                    if form.is_valid():
                        tool_instance = form.save(commit=False)
                        tool_instance.deliverychallan = delivery_challan
                        tool_instance.save()
                        # Associate the calibration report with the delivery challan tool
                        tool_instance.calibration_report = calibration_report
                        tool_instance.save() 
                        
                return redirect('home')

        return render(request, 'app1/delivery_challan.html', {'delivery_challan_form': delivery_challan_form, 'delivery_challan_tools_formset': delivery_challan_tools_formset, 'calibration_report_form': calibration_report_form})

class InstrumentTransportHistoryView(View):
    def get(self, request, instrument_id):
        instrument = InstrumentModel.objects.get(pk=instrument_id)
        transport_history = TransportTools.objects.filter(tool=instrument)
    
        return render(request, 'app1/instrument_transport_history.html', {'instrument': instrument, 'transport_history': transport_history})

class InstrumentServiceHistoryView(View):
    def get(self, request, instrument_id):
        instrument = InstrumentModel.objects.get(pk=instrument_id)
        service_history = ServiceTools.objects.filter(tool=instrument)
    
        return render(request, 'app1/instrument_service_history.html', {'instrument': instrument, 'service_history': service_history})
