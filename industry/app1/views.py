from django.http import JsonResponse
from django.shortcuts import render,  redirect
from django.views import View
from .forms import CalibrationReportForm, DeliveryChallanForm, DeliveryChallanToolsForm, DeliveryChallanToolsFormSet, ServiceOrderForm, ServiceToolsForm, TransportMovementOrderForm,TransportOrderForm, TransportToolsForm
from .models import CalibrationReport, DeliveryChallan, DeliveryChallanTools, InstrumentModel,  ServiceOrder, ServiceTools, ShedTools, TransportOrder, ShedDetails, TransportTools, Vendor, VendorHandles
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
    
class CalibrationReportView(APIView):
    def get(self, request):
        calibration_report = CalibrationReport.objects.all()
        calibration_report_serializer = CalibrationReportSerializer(calibration_report, many=True)

        response_data = {
            'calibration_report' : calibration_report_serializer.data,
        }

        return Response(response_data)

def home(request):
    return render(request, 'app1/home.html')

#Just creates new Tools and in shed
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

# class TransportOrderView(APIView):
#     def get(self, request):
#         orders_details = TransportOrder.objects.all()
#         orders_serializer = TransportOrderSerializer(orders_details, many=True)
        
#         instrument_models = InstrumentModel.objects.all()
#         instrument_serializer = InstrumentModelSerializer(instrument_models, many=True)

#         shed_details = ShedDetails.objects.all()
#         shed_serializer = ShedDetailsSerializer(shed_details, many=True)

#         shed_tools_details = ShedTools.objects.all()
#         shed_tools_serializer = ShedToolsSerializer(shed_tools_details, many=True)

#         response_data = {
#             'transport_orders': orders_serializer.data,
#             'instrument_models': instrument_serializer.data,
#             'shed_details' : shed_serializer.data,
#             'shed_tools_details' : shed_tools_serializer.data,
#         }

#         return Response(response_data)

#     def post(self, request):
#         # Deserialize the received data
#         serializer = TransportOrderSerializer(data=request.data)
#         if serializer.is_valid():
#             # Extract relevant data from the request
#             movement_date = serializer.validated_data['movement_date']
#             source_shed_id = serializer.validated_data['source_shed']
#             destination_shed_id = serializer.validated_data['destination_shed']
#             tool_count = serializer.validated_data['tool_count']
#             acknowledgment = serializer.validated_data.get('acknowledgment', False)
#             tools_data = request.data.get('tools', [])

#             # Retrieve source and destination shed objects
#             # source_shed = get_object_or_404(ShedDetails, pk=source_shed_id)
#             # destination_shed = get_object_or_404(ShedDetails, pk=destination_shed_id)

#             # Create the transport order
#             transport_order = TransportOrder.objects.create(
#                 movement_date=movement_date,
#                 source_shed=source_shed_id,
#                 destination_shed=destination_shed_id,
#                 tool_count=tool_count,
#                 acknowledgment=acknowledgment
#             )

#             # Create tools associated with the transport order
#             for tool_data in tools_data:
#                 tool_id = tool_data.get('tool')
#                 tool = get_object_or_404(InstrumentModel, pk=tool_id)
#                 TransportTools.objects.create(transport=transport_order, tool=tool)

#             return JsonResponse({'success': True}, status=status.HTTP_201_CREATED)
#         else:
#             return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Updates the tools in the shed
# class TransportOrderView(View):
#     def get(self, request):
#         order_form = TransportOrderForm()
#         tool_forms = [TransportToolsForm(prefix=str(x)) for x in range(3)]  # Adjust the range as needed
#         return render(request, 'app1/transport_order_form.html', {'order_form': order_form, 'tool_forms': tool_forms})

#     def post(self, request):
#         order_form = TransportOrderForm(request.POST)
#         tool_forms = [TransportToolsForm(request.POST, prefix=str(x)) for x in range(3)]  # Adjust the range as needed

#         if order_form.is_valid() and all(form.is_valid() for form in tool_forms):
#             with transaction.atomic():  # Use transaction to ensure data consistency
#                 transport_order = order_form.save()
#                 for form in tool_forms:
#                     if form.cleaned_data.get('tool'):
#                         tool = form.cleaned_data['tool']
#                         transport_tool = TransportTools.objects.create(transport=transport_order, tool=tool)
#                         # Update ShedTools from source shed to destination shed
#                         source_shed = transport_order.source_shed
#                         destination_shed = transport_order.destination_shed
#                         ShedTools.objects.filter(shed=source_shed, using_tool=tool).update(shed=destination_shed)
#                 return redirect('home')  # Replace 'success_url' with your desired success URL

#         return render(request, 'app1/transport_order_form.html', {'order_form': order_form, 'tool_forms': tool_forms})

class TransportOrderView(View):
    def get(self, request):
        order_form = TransportOrderForm()
        tool_forms = [TransportToolsForm(prefix=str(x)) for x in range(3)]  # Adjust the range as needed
        return render(request, 'app1/transport_order_form.html', {'order_form': order_form, 'tool_forms': tool_forms})
    
    def post(self, request):
        order_form = TransportOrderForm(request.POST)
        tool_forms = [TransportToolsForm(request.POST, prefix=str(x)) for x in range(3)]  # Adjust the range as needed

        if order_form.is_valid() and all(form.is_valid() for form in tool_forms):
            with transaction.atomic():  # Use transaction to ensure data consistency
                transport_order = order_form.save()
                tool_data = []
                for form in tool_forms:
                    if form.cleaned_data.get('tool'):
                        tool = form.cleaned_data['tool']
                        transport_tool = TransportTools.objects.create(transport=transport_order, tool=tool)
                        # Update ShedTools from source shed to destination shed
                        source_shed = transport_order.source_shed
                        destination_shed = transport_order.destination_shed
                        ShedTools.objects.filter(shed=source_shed, using_tool=tool).update(shed=destination_shed)
                        tool_data.append({
                            'tool_id': tool.pk,
                            'tool_name': tool.instrument_name,
                            'transport_tool_id': transport_tool.pk,
                            'transport_order_id': transport_order.pk,
                            'source_shed': source_shed.name,
                            'destination_shed': destination_shed.name
                        })
                return JsonResponse({'success': True, 'tool_data': tool_data})
        
        errors = {
            'order_errors': order_form.errors,
            'tool_errors': [form.errors for form in tool_forms]
        }
        return JsonResponse({'success': False, 'errors': errors})

# just creates new service orders
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

    # def post(self, request):
    #     # Serialize the incoming data
    #     order_serializer = ServiceOrderSerializer(data=request.data)
        
    #     # Check if the incoming data is valid
    #     if order_serializer.is_valid():
    #         # Save the service order
    #         service_order = order_serializer.save()

    #         # Retrieve and validate the list of tools
    #         tools_data = request.data.get('tools', [])
    #         for tool_data in tools_data:
    #             # Retrieve the tool and vendor objects
    #             tool_id = tool_data.get('tool')
    #             vendor_id = tool_data.get('vendor')
    #             tool = get_object_or_404(InstrumentModel, pk=tool_id)
    #             vendor = get_object_or_404(Vendor, pk=vendor_id)

    #             # Create the ServiceTools instance with proper vendor
    #             ServiceTools.objects.create(service=service_order, tool=tool, vendor=vendor)

    #         # Return success response
    #         return Response({'success': True}, status=status.HTTP_201_CREATED)
    #     else:
    #         # Return error response if service order data is not valid
    #         return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class GenerateBillView(View):
#     def get(self, request, service_order_id):
#         service_order = get_object_or_404(ServiceOrder, pk=service_order_id)

#         service_tools = ServiceTools.objects.filter(service=service_order)
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
        service_tools = ServiceTools.objects.filter(service_id=service_order_id)
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
                bill_items.append({'tool': tool.instrument_name, 'cost': cost, 'amount': amount})

        data = {
            'bill_items': bill_items,
            'total_amount': total_amount
        }
        return JsonResponse(data)

class DeliveryChallanView(View):
    def get(self, request):
        # Retrieve shed, vendor, and service details
        sheds = ShedDetails.objects.all()
        vendors = Vendor.objects.all()
        services = ServiceOrder.objects.all()
        instruments = InstrumentModel.objects.all()

        # Create form instances
        delivery_challan_form = DeliveryChallanForm()
        delivery_challan_tools_formset = DeliveryChallanToolsFormSet()
        calibration_report_form = CalibrationReportForm()

        # Pass form instances and context variables to the template
        return render(request, 'app1/delivery_challan.html', {
            'delivery_challan_form': delivery_challan_form,
            'delivery_challan_tools_formset': delivery_challan_tools_formset,
            'calibration_report_form': calibration_report_form,
            'sheds': sheds,
            'vendors': vendors,
            'services': services,
            'instruments': instruments,
        })

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

# class DeliveryChallanView(View):
#     def post(self, request):
#         # Extract data from the request
#         received_date = request.POST.get('receivedDate')
#         vendor_name = request.POST.get('vendor')
#         shed_id = request.POST.get('shed')
#         service_id = request.POST.get('service')
#         tools_data = request.POST.getlist('tools')

#         # Store delivery challan details
#         vendor = Vendor.objects.get(name=vendor_name)
#         shed = ShedDetails.objects.get(pk=shed_id)
#         service = ServiceOrder.objects.get(pk=service_id)
#         delivery_challan = DeliveryChallan.objects.create(received_date=received_date, vendor=vendor, shed=shed, service=service)

#         # Store calibration details for each tool
#         for tool_data in tools_data:
#             calibration_date = tool_data.get('calibrationDate')
#             calibration_report_number = tool_data.get('calibrationReportNumber')
#             calibration_agency = tool_data.get('calibrationAgency')
#             result = tool_data.get('result')
#             action = tool_data.get('action')
#             next_calibration_date = tool_data.get('nextCalibrationDate')
#             remark = tool_data.get('remark')
#             tool_name = tool_data.get('toolName')

#             # Get or create the instrument model
#             tool, created = InstrumentModel.objects.get_or_create(instrument_name=tool_name)

#             # Create and associate the calibration report
#             calibration_report = CalibrationReport.objects.create(calibration_tool=tool, calibration_date=calibration_date,
#                                                                    calibration_report_no=calibration_report_number,
#                                                                    calibration_agency=calibration_agency, result=result,
#                                                                    action=action, next_calibration_date=next_calibration_date,
#                                                                    remark=remark)

#             # Create and associate the delivery challan tool
#             DeliveryChallanTools.objects.create(deliverychallan=delivery_challan, tool=tool, calibration_report=calibration_report)

#         return JsonResponse({'message': 'Delivery challan created successfully'}, status=201)

# class InstrumentTransportHistoryView(View):
#     def get(self, request, instrument_id):
#         instrument = InstrumentModel.objects.get(pk=instrument_id)
#         transport_history = TransportTools.objects.filter(tool=instrument)
    
#         return render(request, 'app1/instrument_transport_history.html', {'instrument': instrument, 'transport_history': transport_history})

class InstrumentTransportHistoryView(View):
    def get(self, request, instrument_id):
        instrument = InstrumentModel.objects.get(pk=instrument_id)
        transport_history = TransportTools.objects.filter(tool=instrument)
        serialized_data = serializers.serialize('json', transport_history)
        return JsonResponse({'instrument': instrument, 'transport_history': serialized_data}, safe=False)

from django.core import serializers

# class InstrumentServiceHistoryView(View):
#     def get(self, request, instrument_id):
#         instrument = InstrumentModel.objects.get(pk=instrument_id)
#         service_history = ServiceTools.objects.filter(tool=instrument)
    
#         return render(request, 'app1/instrument_service_history.html', {'instrument': instrument, 'service_history': service_history})

class InstrumentServiceHistoryView(View):
    def get(self, request, instrument_id):
        instrument = InstrumentModel.objects.get(pk=instrument_id)
        service_history = ServiceTools.objects.filter(tool=instrument)
        serialized_data = serializers.serialize('json', service_history)
        return JsonResponse({'instrument': instrument, 'service_history': serialized_data}, safe=False)

class ShedDetailView1(View):
    def get(self, request, shed_id):
        shed = get_object_or_404(ShedDetails, pk=shed_id)
        shed_tools = ShedTools.objects.filter(shed=shed)
        return render(request, 'app1/shed_detail.html', {'shed': shed, 'shed_tools': shed_tools})
    
class ShedDetailAPIView(APIView):
    def get(self, request, shed_id):
        shed = get_object_or_404(ShedDetails, pk=shed_id)
        shed_serializer = ShedDetailsSerializer(shed)
        shed_tools = ShedTools.objects.filter(shed=shed)
        shed_tools_serializer = ShedToolsSerializer(shed_tools, many=True)
        return Response({'shed': shed_serializer.data, 'shed_tools': shed_tools_serializer.data})

class VendorDetailsView1(APIView):
    def get(self, request, vendor_id):
        vendor = get_object_or_404(Vendor, pk=vendor_id)
        vendor_serializer = VendorSerializer(vendor)
        vendor_handles = VendorHandles.objects.filter(vendor=vendor)
        vendor_handles_serializer = VendorHandlesSerializer(vendor_handles, many=True)
        return Response({'vendor': vendor_serializer.data, 'vendor_handles': vendor_handles_serializer.data})
    
# class VendorDetailsView1(APIView):
#     def get(self, request, vendor_id):
#         # Retrieve vendor details
#         vendor = get_object_or_404(Vendor, pk=vendor_id)

#         # Retrieve vendor handles (tool handles) associated with the vendor
#         vendor_handles = VendorHandles.objects.filter(vendor=vendor)
#         vendor_handles_serializer = VendorHandlesSerializer(vendor_handles, many=True)

#         # Render the vendor details page with the retrieved data
#         return render(request, 'app1/vendor_details.html', {'vendor': vendor, 'vendor_handles': vendor_handles})
                