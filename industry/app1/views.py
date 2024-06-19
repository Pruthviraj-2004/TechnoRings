import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .forms import AnotherServiceOrderForm, AnotherServiceToolForm, CalibrationReportForm, DeliveryChallanForm, DeliveryChallanToolsFormSet, InstrumentFamilyGroupForm, InstrumentForm, InstrumentGroupMasterForm, ShedDetailsForm, ShedLoginForm, ShedToolsForm, TransportOrderForm, TransportToolsForm, VendorForm, VendorHandlesForm
from .models import InstrumentFamilyGroup, InstrumentGroupMaster, CalibrationReport, DeliveryChallan, DeliveryChallanTools, InstrumentModel,  ServiceOrder, ServiceTools, ServiceType, ShedTools, TransportOrder, ShedDetails, TransportTools, Vendor, VendorHandles, VendorType
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CalibrationReportSerializer, DeliveryChallanSerializer, DeliveryChallanToolsSerializer, InstrumentFamilyGroupSerializer, InstrumentGroupMasterSerializer, InstrumentModelSerializer, ServiceOrderSerializer, ServiceToolsSerializer, ServiceTypeSerializer, ShedDetailsSerializer, ShedToolsSerializer, TransportOrderSerializer, TransportToolsSerializer, VendorHandlesSerializer, VendorSerializer, VendorTypeSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.parsers import MultiPartParser, FormParser
from django.utils.dateparse import parse_datetime
from datetime import timedelta
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

class VendorTypeView(APIView):
    def get(self, request):
        vendor_types = VendorType.objects.all()
        serializer = VendorTypeSerializer(vendor_types, many=True)
        return Response({'vendor_types': serializer.data})

class InstrumentToolsView(APIView):
    def get(self, request):
        instruments = InstrumentModel.objects.all()
        serializer = InstrumentModelSerializer(instruments, many=True)
        return Response({'instrument_models': serializer.data})

class InstrumentServiceToolsView(APIView):
    def get(self, request):
        instruments = InstrumentModel.objects.filter(service_status=True)
        serializer = InstrumentModelSerializer(instruments, many=True)        
        return Response({'instrument_models': serializer.data})

class InstrumentFamilyGroupView(APIView):
    def get(self, request):
        instruments = InstrumentFamilyGroup.objects.all()
        serializer = InstrumentFamilyGroupSerializer(instruments, many=True)
        return Response({'instrument_family_groups': serializer.data})

class InstrumentGroupMasterView(APIView):
    def get(self, request):
        instruments = InstrumentGroupMaster.objects.all()
        serializer = InstrumentGroupMasterSerializer(instruments, many=True)
        return Response({'instrument_group_masters': serializer.data})

class VendorView(APIView):
    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response({'vendors': serializer.data})
    
class VendorHandlesView(APIView):
    def get(self, request):
        vendor_handles = VendorHandles.objects.all()
        serializer = VendorHandlesSerializer(vendor_handles, many=True)
        return Response({'vendor_handles': serializer.data})

class ShedDetailsView(APIView):
    def get(self, request):
        shed_details = ShedDetails.objects.all()
        serializer = ShedDetailsSerializer(shed_details, many=True)
        return Response({'shed_details': serializer.data})

class ShedToolsView(APIView):
    def get(self, request):
        shed_tools = ShedTools.objects.all()
        serializer = ShedToolsSerializer(shed_tools, many=True)
        return Response({'shed_tools': serializer.data})

class AllTransportOrderView(APIView):
    def get(self, request):
        transport_orders = TransportOrder.objects.all()
        serializer = TransportOrderSerializer(transport_orders, many=True)
        return Response({'transport_orders': serializer.data})
    
class RecentTransportOrderView(APIView):
    def get(self, request):
        recent_transport_orders = TransportOrder.objects.order_by('-movement_date')[:10]
        serializer = TransportOrderSerializer(recent_transport_orders, many=True)
        return Response({'transport_orders': serializer.data})

class AllServiceOrderView(APIView):
    def get(self, request):
        service_orders = ServiceOrder.objects.all()
        serializer = ServiceOrderSerializer(service_orders, many=True)
        return Response({'service_orders': serializer.data})
    
class RecentServiceOrderView(APIView):
    def get(self, request):
        recent_service_orders = ServiceOrder.objects.order_by('-date')[:10]
        serializer = ServiceOrderSerializer(recent_service_orders, many=True)
        return Response({'service_orders': serializer.data})
    
class AllDeliveryChallanView(APIView):
    def get(self, request):
        delivery_challan = DeliveryChallan.objects.all()
        serializer = DeliveryChallanSerializer(delivery_challan, many=True)
        return Response({'delivery_challan': serializer.data})
    
class RecentDeliveryChallanView(APIView):
    def get(self, request):
        recent_delivery_challan = DeliveryChallan.objects.order_by('-received_date')[:10]
        serializer = DeliveryChallanSerializer(recent_delivery_challan, many=True)
        return Response({'delivery_challan': serializer.data})

class CalibrationReportView(APIView):
    def get(self, request):
        calibration_reports = CalibrationReport.objects.all()
        serializer = CalibrationReportSerializer(calibration_reports, many=True)
        return Response({'calibration_reports': serializer.data})

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
  
class TransportOrderViews(APIView):
    def get(self, request, movement_id):
        transport_order = get_object_or_404(TransportOrder, pk=movement_id)
        transport_order_serializer = TransportOrderSerializer(transport_order)
        transport_tools = TransportTools.objects.filter(transport=transport_order)
        transport_tools_serializer = TransportToolsSerializer(transport_tools, many=True)
        return Response({'transport_order': transport_order_serializer.data, 'transport_tools': transport_tools_serializer.data})

class ServiceOrderViews(APIView):
    def get(self, request, service_id):
        service_order = get_object_or_404(ServiceOrder, pk=service_id)
        service_order_serializer = ServiceOrderSerializer(service_order)
        service_tools = ServiceTools.objects.filter(service=service_order)
        service_tools_serializer = ServiceToolsSerializer(service_tools, many=True)
        return Response({'service_order': service_order_serializer.data, 'service_tools': service_tools_serializer.data})        

class DeliveryChallanViews(APIView):
    def get(self, request, deliverychallan_id):
        delivery_challan = get_object_or_404(DeliveryChallan, pk=deliverychallan_id)
        delivery_challan_serializer = DeliveryChallanSerializer(delivery_challan)
        delivery_challan_tools = DeliveryChallanTools.objects.filter(deliverychallan=delivery_challan)
        delivery_challan_tools_serializer = DeliveryChallanToolsSerializer(delivery_challan_tools, many=True)
        return Response({'delivery_challan': delivery_challan_serializer.data, 'delivery_challan_tools': delivery_challan_tools_serializer.data})
    
class ServiceTypeView(APIView):
    def get(self, request):
        service_types = ServiceType.objects.all()
        serializer = ServiceTypeSerializer(service_types, many=True)
        return Response(serializer.data)

def home(request):
    return render(request, 'app1/home.html')

# Just creates new Tools and in shed
# class TransportOrderView(View):
#     def get(self, request):
#         order_form = TransportOrderForm()
#         tool_forms = [TransportToolsForm(prefix=str(x)) for x in range(3)]
#         return render(request, 'app1/transport_order_form.html', {'order_form': order_form, 'tool_forms': tool_forms})

#     def post(self, request):
#         order_form = TransportOrderForm(request.POST)
#         tool_forms = [TransportToolsForm(request.POST, prefix=str(x)) for x in range(3)]

#         if order_form.is_valid() and all(form.is_valid() for form in tool_forms):
#             transport_order = order_form.save()
#             for form in tool_forms:
#                 if form.cleaned_data.get('tool'):
#                     tool = form.cleaned_data['tool']
#                     TransportTools.objects.create(transport=transport_order, tool=tool)
#             return redirect('home')

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
                tool_movement_remarks = tool_data.get('tool_movement_remarks', 'good')
                tool = get_object_or_404(InstrumentModel, pk=tool_id)
                TransportTools.objects.create(transport=transport_order, tool=tool, tool_movement_remarks=tool_movement_remarks)

            return JsonResponse({'success': True}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @method_decorator(csrf_exempt, name='dispatch')
# class TransportAcknowledgmentView(View):
#     def get(self, request, order_id):
#         transport_order = get_object_or_404(TransportOrder, pk=order_id)
#         return render(request, 'app1/transport_acknowledge.html', {'transport_order': transport_order})

#     def post(self, request, order_id):
#         transport_order = get_object_or_404(TransportOrder, pk=order_id)
#         transport_order.acknowledgment = True
#         transport_order.save()

#         # Get the selected tools for this transport order
#         selected_tools = TransportTools.objects.filter(transport=transport_order)

#         # Update ShedTools from source shed to destination shed for selected tools only
#         source_shed = transport_order.source_shed
#         destination_shed = transport_order.destination_shed
#         transported_tools = ShedTools.objects.filter(shed=source_shed, using_tool__in=selected_tools.values_list('tool', flat=True))

#         try:
#             with transaction.atomic():
#                 selected_tools.update(acknowledgment=True)
#                 transported_tools.update(shed=destination_shed)
#                 return JsonResponse({'success': True, 'message': 'Transport acknowledgment successful.'})
#         except Exception as e:
#             return JsonResponse({'success': False, 'error': str(e)})

@method_decorator(csrf_exempt, name='dispatch')
class TransportAcknowledgmentView(View):
    def get(self, request, order_id):
        transport_order = get_object_or_404(TransportOrder, pk=order_id)
        return render(request, 'app1/transport_acknowledge.html', {'transport_order': transport_order})

    def post(self, request, order_id):
        transport_order = get_object_or_404(TransportOrder, pk=order_id)
        transport_order.acknowledgment = True

        try:
            with transaction.atomic():
                # Update acknowledgment status for the transport order
                transport_order.save()

                # Get the selected tools for this transport order
                selected_tools = TransportTools.objects.filter(transport=transport_order)

                # Update ShedTools from source shed to destination shed for selected tools only
                source_shed = transport_order.source_shed
                destination_shed = transport_order.destination_shed
                transported_tools = ShedTools.objects.filter(shed=source_shed, using_tool__in=selected_tools.values_list('tool', flat=True))
                transported_tools.update(shed=destination_shed)

                selected_tools.update(acknowledgment=True)

                # Update current_shed field of InstrumentModel for acknowledged tools
                acknowledged_instruments = selected_tools.values_list('tool', flat=True)
                InstrumentModel.objects.filter(instrument_no__in=acknowledged_instruments).update(current_shed=destination_shed)

                return JsonResponse({'success': True, 'message': 'Transport acknowledgment successful.'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

# @method_decorator(csrf_exempt, name='dispatch')
# class TransportAcknowledgmentToolsView(View):
#     def get(self, request, order_id):
#         transport_order = get_object_or_404(TransportOrder, pk=order_id)
#         return render(request, 'app1/transport_acknowledge_tools.html', {'transport_order': transport_order})

#     def post(self, request, order_id):
#         transport_order = get_object_or_404(TransportOrder, pk=order_id)

#         # Get the tools to be acknowledged from the request
#         tool_ids = request.POST.getlist('tool_ids')

#         # Filter out any empty values from tool_ids
#         tool_ids = [tool_id for tool_id in tool_ids if tool_id]

#         try:
#             with transaction.atomic():
#                 # Get the tools for this transport order
#                 selected_tools = TransportTools.objects.filter(transport=transport_order, tool_id__in=tool_ids)

#                 # Update the selected tools acknowledgment to True
#                 selected_tools.update(acknowledgment=True)

#                 # Update ShedTools from source shed to destination shed for selected tools
#                 source_shed = transport_order.source_shed
#                 destination_shed = transport_order.destination_shed
#                 transported_tools = ShedTools.objects.filter(shed=source_shed, using_tool__in=selected_tools.values_list('tool', flat=True))
#                 transported_tools.update(shed=destination_shed)

#                 # Check if all tools for the transport order are acknowledged
#                 all_tools_acknowledged = not TransportTools.objects.filter(transport=transport_order, acknowledgment=False).exists()
#                 transport_order.acknowledgment = all_tools_acknowledged
#                 transport_order.save()

#                 return JsonResponse({'success': True, 'message': 'Selected tools acknowledgment updated successfully.'})
#         except Exception as e:
#             return JsonResponse({'success': False, 'error': str(e)})

# @method_decorator(csrf_exempt, name='dispatch')
# class TransportAcknowledgmentToolsView(View):
#     def get(self, request, order_id):
#         transport_order = get_object_or_404(TransportOrder, pk=order_id)
#         return render(request, 'app1/transport_acknowledge_tools.html', {'transport_order': transport_order})

#     def post(self, request, order_id):
#         transport_order = get_object_or_404(TransportOrder, pk=order_id)

#         try:
#             # Parse JSON data from request.body
#             data = json.loads(request.body.decode('utf-8'))
#             tool_ids = data.get('tool_ids', [])

#             # Filter out any empty values from tool_ids
#             tool_ids = [tool_id for tool_id in tool_ids if tool_id]

#             with transaction.atomic():
#                 # Get the tools for this transport order
#                 selected_tools = TransportTools.objects.filter(transport=transport_order, tool_id__in=tool_ids)

#                 # Update the selected tools acknowledgment to True
#                 selected_tools.update(acknowledgment=True)

#                 # Update ShedTools from source shed to destination shed for selected tools
#                 source_shed = transport_order.source_shed
#                 destination_shed = transport_order.destination_shed
#                 transported_tools = ShedTools.objects.filter(shed=source_shed, using_tool__in=selected_tools.values_list('tool', flat=True))
#                 transported_tools.update(shed=destination_shed)

#                 # Check if all tools for the transport order are acknowledged
#                 all_tools_acknowledged = not TransportTools.objects.filter(transport=transport_order, acknowledgment=False).exists()
#                 transport_order.acknowledgment = all_tools_acknowledged
#                 transport_order.save()

#                 return JsonResponse({'success': True, 'message': 'Selected tools acknowledgment updated successfully.'})
#         except json.JSONDecodeError:
#             return JsonResponse({'success': False, 'error': 'Invalid JSON data.'})
#         except Exception as e:
#             return JsonResponse({'success': False, 'error': str(e)})

@method_decorator(csrf_exempt, name='dispatch')
class TransportAcknowledgmentToolsView(View):
    def get(self, request, order_id):
        transport_order = get_object_or_404(TransportOrder, pk=order_id)
        return render(request, 'app1/transport_acknowledge_tools.html', {'transport_order': transport_order})

    def post(self, request, order_id):
        transport_order = get_object_or_404(TransportOrder, pk=order_id)

        try:
            data = json.loads(request.body.decode('utf-8'))
            tool_ids = data.get('tool_ids', [])

            tool_ids = [tool_id for tool_id in tool_ids if tool_id]

            with transaction.atomic():
                selected_tools = TransportTools.objects.filter(transport=transport_order, tool_id__in=tool_ids)

                selected_tools.update(acknowledgment=True)

                source_shed = transport_order.source_shed
                destination_shed = transport_order.destination_shed
                transported_tools = ShedTools.objects.filter(shed=source_shed, using_tool__in=selected_tools.values_list('tool', flat=True))
                transported_tools.update(shed=destination_shed)

                acknowledged_instruments = selected_tools.values_list('tool', flat=True)
                InstrumentModel.objects.filter(instrument_no__in=acknowledged_instruments).update(current_shed=destination_shed)

                all_tools_acknowledged = not TransportTools.objects.filter(transport=transport_order, acknowledgment=False).exists()
                transport_order.acknowledgment = all_tools_acknowledged
                transport_order.save()

                return JsonResponse({'success': True, 'message': 'Selected tools acknowledgment updated successfully.'})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON data.'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

def update_service_status():
    instrument_models = InstrumentModel.objects.all()

    for instrument in instrument_models:
        latest_calibration_report = CalibrationReport.objects.filter(calibration_tool=instrument).order_by('calibration_date').first()

        if latest_calibration_report and latest_calibration_report.notification_date == timezone.now().date():
            instrument.service_status = True
            instrument.save()
            
            print(f"Instrument tool '{instrument.instrument_name}' has been updated.")

import schedule
import time
from django.utils import timezone
import threading

def start_scheduler():
    schedule.every().minutes.do(update_service_status)
    schedule.every().hour.do(update_service_status)
    schedule.every().day.at("00:15").do(update_service_status)

    while True:
        schedule.run_pending()
        if all(not job.should_run for job in schedule.jobs):
            break
        time.sleep(1)

scheduler_thread = threading.Thread(target=start_scheduler)
scheduler_thread.start()

# just creates new service orders
# @method_decorator(csrf_exempt, name='dispatch')
# class ServiceOrderView(View):
#     def get(self, request):
#         order_form = AnotherServiceOrderForm()
#         tool_forms = [AnotherServiceToolForm(prefix=str(x)) for x in range(3)]

#         return render(request, 'app1/service_order_form1.html', {'order_form': order_form, 'tool_forms': tool_forms})

#     def post(self, request):
#         order_form = AnotherServiceOrderForm(request.POST)
#         tool_forms = [AnotherServiceToolForm(request.POST, prefix=str(x)) for x in range(3)]

#         if order_form.is_valid() and all(form.is_valid() for form in tool_forms):
#             service_order = order_form.save()
#             vendor_id = request.POST.get('vendor')

#             total_amount = 0

#             for form in tool_forms:
#                 if form.cleaned_data.get('tool'):
#                     tool = form.cleaned_data['tool']
#                     service_tool = ServiceTools.objects.create(service=service_order, tool=tool, vendor_id=vendor_id)

#                     # Calculate the cost if the service type is 'calibration'
#                     service_type = service_tool.service_type.service_type
#                     if service_type.lower() == 'calibration':
#                         vendor_handles = VendorHandles.objects.filter(tool=tool, vendor_id=vendor_id)
#                         for vendor_handle in vendor_handles:
#                             total_amount += vendor_handle.cost

#             # Update the service order amount with the calculated total amount
#             service_order.amount = total_amount
#             service_order.save()

#             # Redirect to GenerateBillView with the created service order ID
#             return redirect('generate_bill', service_order_id=service_order.service_id)

#         # Handle invalid forms
#         return render(request, 'app1/service_order_form1.html', {'order_form': order_form, 'tool_forms': tool_forms})
               
# def update_service_status(request):
#     # Get all instrument models
#     instrument_models = InstrumentModel.objects.all()

#     # Iterate over each instrument model
#     for instrument in instrument_models:
#         # Get the latest calibration report for the instrument
#         latest_calibration_report = CalibrationReport.objects.filter(calibration_tool=instrument).order_by('calibration_date').first()

#         # Check if a calibration report exists and if the notification date matches the current date
#         if latest_calibration_report and latest_calibration_report.notification_date == timezone.now().date():
#             # Update the service status of the instrument
#             instrument.service_status = True
#             instrument.save()

#     return JsonResponse({'success': True, 'message': 'Service status updated successfully'})

@method_decorator(csrf_exempt, name='dispatch')
class ServiceOrderView(APIView):
    def get(self, request):
        service_orders = ServiceOrder.objects.all()
        service_order_serializer = ServiceOrderSerializer(service_orders, many=True)

        service_tools = ServiceTools.objects.all()
        service_tools_serializer = ServiceToolsSerializer(service_tools, many=True)

        vendors = Vendor.objects.all()
        vendor_serializer = VendorSerializer(vendors, many=True)

        instrument_models = InstrumentModel.objects.all()
        instrument_serializer = InstrumentModelSerializer(instrument_models, many=True)

        response_data = {
            'service_orders': service_order_serializer.data,
            'service_tools': service_tools_serializer.data,
            'vendors': vendor_serializer.data,
            'instrument_tools': instrument_serializer.data,
        }

        return Response(response_data)

    def post(self, request):
        order_serializer = ServiceOrderSerializer(data=request.data)
        
        if order_serializer.is_valid():
            service_order = order_serializer.save()

            tools_data = request.data.get('tools', [])
            total_amount = 0

            for tool_data in tools_data:
                tool_id = tool_data.get('tool')
                vendor_id = tool_data.get('vendor')
                service_type_id = tool_data.get('service_type')
                tool = get_object_or_404(InstrumentModel, pk=tool_id)
                vendor = get_object_or_404(Vendor, pk=vendor_id)
                service_type = get_object_or_404(ServiceType, pk=service_type_id)
                service_remarks = tool_data.get('service_remarks', 'good')

                service_tool = ServiceTools.objects.create(service=service_order,tool=tool,vendor=vendor,service_type=service_type,service_remarks=service_remarks)

                if service_tool.service_type.service_type.lower() == 'calibration':
                    vendor_handles = VendorHandles.objects.filter(tool=tool, vendor=vendor)
                    for vendor_handle in vendor_handles:
                        total_amount += vendor_handle.cost

            service_order.amount = total_amount
            service_order.save()

            return Response({'success': True, 'serviceorder_id': service_order.service_id, 'total_amount': total_amount}, status=status.HTTP_201_CREATED)
        else:
            return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GenerateBillView(View):
    def get(self, request, service_order_id):
        service_tools = ServiceTools.objects.filter(service_id=service_order_id)
        bill_items = []
        total_amount = 0

        for service_tool in service_tools:
            tool = service_tool.tool
            service_type = service_tool.service_type.service_type

            if service_type.lower() == 'calibration':
                vendor = service_tool.vendor
                vendor_handles = VendorHandles.objects.filter(tool=tool, vendor=vendor)

                for vendor_handle in vendor_handles:
                    cost = vendor_handle.cost
                    amount = 1 * cost
                    total_amount += amount
                    bill_items.append({'tool': tool.instrument_name,'service_type': service_type,'cost': cost,'amount': amount})
            else:
                bill_items.append({'tool': tool.instrument_name,'service_type': service_type,'cost': 0,'amount': 0})

        try:
            service_order = ServiceOrder.objects.get(service_id=service_order_id)
            service_order.amount = total_amount
            service_order.save()
        except ServiceOrder.DoesNotExist:
            return JsonResponse({'error': f'Service Order with ID {service_order_id} does not exist'}, status=404)

        data = {'bill_items': bill_items,'total_amount': total_amount}
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class StoreDeliveryChallan(APIView):
    parser_classes = (MultiPartParser, FormParser)
    
    def post(self, request):
        data = request.data

        # Retrieve the service order to get the vendor
        service_id = data.get('service')
        if not service_id:
            return JsonResponse({'success': False, 'errors': 'Service ID is required'}, status=400)

        try:
            service_order = ServiceOrder.objects.get(pk=service_id)
        except ServiceOrder.DoesNotExist:
            return JsonResponse({'success': False, 'errors': 'Invalid Service ID'}, status=400)

        vendor = service_order.vendor

        # Add the vendor to the data
        data = data.copy()  # Make a mutable copy of the data
        data['vendor'] = vendor.vendor_id

        # Create DeliveryChallan instance
        delivery_challan_form = DeliveryChallanForm(data)
        if delivery_challan_form.is_valid():
            delivery_challan = delivery_challan_form.save()

            # Process each tool's data
            tool_data_list = []
            index = 0
            while True:
                tool_data = {
                    'calibration_tool': data.get(f'toolData[{index}][calibration_tool]'),
                    'calibration_date': data.get(f'toolData[{index}][calibration_date]'),
                    'calibration_report_no': data.get(f'toolData[{index}][calibration_report_no]'),
                    'calibration_agency': data.get(f'toolData[{index}][calibration_agency]'),
                    'result': data.get(f'toolData[{index}][result]'),
                    'action': data.get(f'toolData[{index}][action]'),
                    'remark': data.get(f'toolData[{index}][remark]'),
                    'calibration_report_file': request.FILES.get(f'toolData[{index}][calibration_report_file]'),
                    'calibration_report_file2': request.FILES.get(f'toolData[{index}][calibration_report_file2]')
                }
                if not tool_data['calibration_tool']:
                    break
                tool_data_list.append(tool_data)
                index += 1

            # Collect errors for each tool's calibration report form
            errors = []
            for tool_info in tool_data_list:
                calibration_report_form = CalibrationReportForm(tool_info, files={'calibration_report_file': tool_info['calibration_report_file']})
                if calibration_report_form.is_valid():
                    calibration_report = calibration_report_form.save(commit=False)
                    calibration_report.calibration_tool_id = tool_info['calibration_tool']
                    
                    # Handle first file
                    if tool_info['calibration_report_file']:
                        calibration_report.calibration_report_file.save(tool_info['calibration_report_file'].name, tool_info['calibration_report_file'])

                    # Handle second file
                    if tool_info['calibration_report_file2']:
                        calibration_report.calibration_report_file2.save(tool_info['calibration_report_file2'].name, tool_info['calibration_report_file2'])

                    # Calculate next calibration date and notification date
                    calibration_frequency = calibration_report.calibration_tool.calibration_frequency
                    calibration_date = calibration_report.calibration_date
                    next_calibration_date = calibration_date + timedelta(days=calibration_frequency)
                    calibration_report.next_calibration_date = next_calibration_date

                    try:
                        # Filter by tool and vendor
                        vendor_handle = VendorHandles.objects.filter(tool=calibration_report.calibration_tool, vendor=vendor).first()
                        if not vendor_handle:
                            raise VendorHandles.DoesNotExist

                        turnaround_time = vendor_handle.turnaround_time
                        notification_date = next_calibration_date - timedelta(days=turnaround_time)
                        calibration_report.notification_date = notification_date
                    except VendorHandles.DoesNotExist:
                        errors.append({
                            'tool': tool_info['calibration_tool'],
                            'errors': 'Vendor handle not found for the selected tool.'
                        })
                        continue

                    calibration_report.save()

                    # Create DeliveryChallanTools instance
                    delivery_challan_tool = DeliveryChallanTools(
                        deliverychallan=delivery_challan,
                        tool_id=tool_info['calibration_tool'],
                        calibration_report=calibration_report
                    )
                    delivery_challan_tool.save()
                else:
                    errors.append({
                        'tool': tool_info['calibration_tool'],
                        'errors': calibration_report_form.errors
                    })

            if errors:
                return JsonResponse({'success': False, 'errors': errors}, status=400)
            else:
                # Update service_pending to False
                service_order.service_pending = False
                service_order.save()
                return JsonResponse({'success': True, 'message': 'Data saved successfully'})
        else:
            return JsonResponse({'success': False, 'errors': delivery_challan_form.errors}, status=400)

# class InstrumentTransportHistoryView(View):
#     def get(self, request, instrument_id):
#         instrument = InstrumentModel.objects.get(pk=instrument_id)
#         transport_history = TransportTools.objects.filter(tool=instrument)
    
#         return render(request, 'app1/instrument_transport_history.html', {'instrument': instrument, 'transport_history': transport_history})
    
class InstrumentTransportHistoryView(APIView):
    def get(self, request, instrument_id):
        instrument = InstrumentModel.objects.get(pk=instrument_id)
        transport_history = TransportTools.objects.filter(tool=instrument)
        serialized_transport_history = TransportToolsSerializer(transport_history, many=True).data
        
        movement_ids = [item['transport'] for item in serialized_transport_history]
        
        transport_orders = TransportOrder.objects.filter(movement_id__in=movement_ids)
        serialized_transport_orders = TransportOrderSerializer(transport_orders, many=True).data
        
        return Response({
            'instrument': InstrumentModelSerializer(instrument).data,
            'transport_history': serialized_transport_history,
            'transport_orders': serialized_transport_orders
        })
    
# class InstrumentServiceHistoryView(View):
#     def get(self, request, instrument_id):
#         instrument = InstrumentModel.objects.get(pk=instrument_id)
#         service_history = ServiceTools.objects.filter(tool=instrument)
    
#         return render(request, 'app1/instrument_service_history.html', {'instrument': instrument, 'service_history': service_history})

class InstrumentServiceHistoryView(APIView):
    def get(self, request, instrument_id):
        instrument = InstrumentModel.objects.get(pk=instrument_id)
        service_history = ServiceTools.objects.filter(tool=instrument).select_related('service')
        
        serialized_service_history = []
        for service_tool in service_history:
            service_order_data = {
                'service_id': service_tool.service.service_id,
                'date': service_tool.service.date,
                'amount': service_tool.service.amount,
                'description': service_tool.service.description,
                'tool_count': service_tool.service.tool_count,
                'vendor': service_tool.service.vendor.name
            }
            serialized_service_history.append(service_order_data)
        
        return Response({'instrument': InstrumentModelSerializer(instrument).data, 'service_history': serialized_service_history})    

class InstrumentCalibrationHistoryView(APIView):
    def get(self, request, instrument_id):
        instrument = get_object_or_404(InstrumentModel, pk=instrument_id)
        
        calibration_history = CalibrationReport.objects.filter(calibration_tool=instrument)
        
        serialized_calibration_history = CalibrationReportSerializer(calibration_history, many=True).data
        
        return Response({'instrument': InstrumentModelSerializer(instrument).data,'calibration_history': serialized_calibration_history})

@method_decorator(csrf_exempt, name='dispatch')
class AddInstrumentModelView1(View):
    def get(self, request):
        instrument_model_form = InstrumentForm()
        return render(request, 'app1/instrument_model_form.html', {'instrument_model_form': instrument_model_form})

    # def post(self, request):
    #     instrument_model_form = InstrumentForm(request.POST)
    #     if instrument_model_form.is_valid():
    #         instrument_model_form.save()
    #         return redirect('home')
    #     return render(request, 'app1/instrument_model_form.html', {'instrument_model_form': instrument_model_form})
    
    def post(self, request):
        body_data = json.loads(request.body)

        instrument_name = body_data.get('instrument_name')
        manufacturer_name = body_data.get('manufacturer_name')
        year_of_purchase = body_data.get('year_of_purchase')
        gst = body_data.get('gst')
        description = body_data.get('description')
        instrument_range = body_data.get('instrument_range')
        least_count = body_data.get('least_count')
        type_of_tool_id = body_data.get('type_of_tool_id')
        calibration_frequency = body_data.get('calibration_frequency')

        instrument_data = {
            'instrument_name': instrument_name,
            'manufacturer_name': manufacturer_name,
            'year_of_purchase': year_of_purchase,
            'gst': gst,
            'description': description,
            'instrument_range': instrument_range,
            'least_count': least_count,
            'type_of_tool': type_of_tool_id,
            'calibration_frequency': calibration_frequency
        }

        form = InstrumentForm(instrument_data)

        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})
        
@method_decorator(csrf_exempt, name='dispatch')
class AddInstrumentGroupMasterView(View):
    def get(self, request):
        instrument_group_master_form = InstrumentGroupMasterForm()
        return render(request, 'app1/instrument_group_master_form.html', {'instrument_group_master_form': instrument_group_master_form})

    # def post(self, request):
    #     instrument_group_master_form = InstrumentGroupMasterForm(request.POST)
    #     if instrument_group_master_form.is_valid():
    #         instrument_group_master_form.save()
    #         return redirect('home')
    #     return render(request, 'app1/instrument_group_master_form.html', {'instrument_group_master_form': instrument_group_master_form})

    def post(self, request):
        body_data = json.loads(request.body)

        tool_group_name = body_data.get('toolGroupName')
        tool_group_code = body_data.get('toolGroupCode')

        instrument_group_master_data = {'tool_group_name': tool_group_name,'tool_group_code': tool_group_code,}

        form = InstrumentGroupMasterForm(instrument_group_master_data)

        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})

@method_decorator(csrf_exempt, name='dispatch')
class AddInstrumentFamilyView(View):
    def get(self, request):
        instrument_family_form = InstrumentFamilyGroupForm()
        return render(request, 'app1/instrument_family_form.html', {'instrument_family_form': instrument_family_form})

    # def post(self, request):
    #     instrument_family_form = InstrumentFamilyGroupForm(request.POST)
    #     if instrument_family_form.is_valid():
    #         instrument_family_form.save()
    #         return redirect('home')
    #     return render(request, 'app1/instrument_family_form.html', {'instrument_family_form': instrument_family_form})
    
    def post(self, request):
        body_data = json.loads(request.body)

        instrument_family_name = body_data.get('instrument_family_name')
        instrument_group_master_id = body_data.get('instrument_group_master')

        try:
            instrument_group_master = InstrumentGroupMaster.objects.get(pk=instrument_group_master_id)
        except InstrumentGroupMaster.DoesNotExist:
            return JsonResponse({'success': False, 'errors': 'Instrument Group Master does not exist'}, status=400)

        instrument_family_data = {'instrument_family_name': instrument_family_name,'instrument_group_master': instrument_group_master.tool_group_id}

        form = InstrumentFamilyGroupForm(data=instrument_family_data)

        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})
        
@method_decorator(csrf_exempt, name='dispatch')
class AddVendorView(View):
    def get(self, request):
        form = VendorForm()
        return render(request, 'app1/vendor_form.html', {'form': form})

    def post(self, request):
        if request.content_type == 'application/json':
            try:
                body_data = json.loads(request.body)
            except json.JSONDecodeError:
                return JsonResponse({'success': False, 'error': 'Invalid JSON data'}, status=400)

            name = body_data.get('name')
            location = body_data.get('location')
            address = body_data.get('address')
            phone_number = body_data.get('phone_number')
            email = body_data.get('email')
            nabl_number = body_data.get('nabl_number')
            vendor_type = body_data.get('vendor_type')

            vendor_data = {'name': name,'location': location,'address': address,'phone_number': phone_number,'email': email,'nabl_number': nabl_number,'vendor_type': vendor_type}

            form = VendorForm(vendor_data)
        else:
            form = VendorForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class AddVendorHandlesView(View):
    def get(self, request):

        form = VendorHandlesForm()
        return render(request, 'app1/vendor_handles_form.html', {'form': form})

    def post(self, request):
        body_data = json.loads(request.body)

        vendor_id = body_data.get('vendor')
        tool_id = body_data.get('tool')
        turnaround_time = body_data.get('turnaround_time')
        cost = body_data.get('cost')

        vendor_handles_data = {'vendor': vendor_id,'tool': tool_id,'turnaround_time': turnaround_time,'cost': cost}

        form = VendorHandlesForm(vendor_handles_data)

        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})

@method_decorator(csrf_exempt, name='dispatch')
class AddShedDetailsView(View):
    def get(self, request):
        form = ShedDetailsForm()
        return render(request, 'app1/shed_details_form.html', {'form': form})

    def post(self, request):
        body_data = json.loads(request.body)

        name = body_data.get('name')
        location = body_data.get('location')
        address = body_data.get('address')
        phone_number = body_data.get('phone_number')
        password1 = body_data.get('password1')

        shed_details_data = {'name': name,'location': location,'address': address,'phone_number': phone_number,'password':password1}

        form = ShedDetailsForm(shed_details_data)

        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})
        
@method_decorator(csrf_exempt, name='dispatch')
class AddShedToolsView(View):
    def get(self, request):
        form = ShedToolsForm()
        return render(request, 'app1/shed_tools_form.html', {'form': form})

    def post(self, request):
        body_data = json.loads(request.body)

        shed_id = body_data.get('shed_id')
        tool_id = body_data.get('tool_id')

        shed_tools_data = {'shed': shed_id,'using_tool': tool_id}

        form = ShedToolsForm(shed_tools_data)

        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})

@method_decorator(csrf_exempt, name='dispatch')
class VendorDeleteView(View):
    def get(self, request, vendor_id):
        vendor = Vendor.objects.get(pk=vendor_id)
        return render(request, 'app1/delete_vendor.html', {'vendor': vendor})

    def post(self, request, vendor_id):
        vendor = get_object_or_404(Vendor, pk=vendor_id)
        try:
            vendor.delete()
            return JsonResponse({'success': True, 'message': 'Vendor deleted successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

@method_decorator(csrf_exempt, name='dispatch')
class ShedDeleteView(View):
    def get(self, request, shed_id):
        shed = get_object_or_404(ShedDetails, pk=shed_id)
        return render(request, 'app1/delete_shed.html', {'shed': shed})

    def post(self, request, shed_id):
        shed = get_object_or_404(ShedDetails, pk=shed_id)
        try:
            shed.delete()
            return JsonResponse({'success': True, 'message': 'Shed deleted successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

@method_decorator(csrf_exempt, name='dispatch')
class TransportOrderDeleteView(View):
    def get(self, request, movement_id):
        transport_order = get_object_or_404(TransportOrder, pk=movement_id)
        return render(request, 'app1/delete_transport_order.html', {'transport_order': transport_order})

    def post(self, request, movement_id):
        transport_order = get_object_or_404(TransportOrder, pk=movement_id)
        try:
            transport_order.delete()
            return JsonResponse({'success': True, 'message': 'Transport order deleted successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

@method_decorator(csrf_exempt, name='dispatch')
class ServiceOrderDeleteView(View):
    def get(self, request, service_id):
        service_order = get_object_or_404(ServiceOrder, pk=service_id)
        return render(request, 'app1/delete_service_order.html', {'service_order': service_order})

    def post(self, request, service_id):
        service_order = get_object_or_404(ServiceOrder, pk=service_id)
        try:
            service_order.delete()
            return JsonResponse({'success': True, 'message': 'Service order deleted successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

@method_decorator(csrf_exempt, name='dispatch')
class DeleteDeliveryChallanView(View):
    def get(self, request, delivery_challan_id):
        delivery_challan = get_object_or_404(DeliveryChallan, pk=delivery_challan_id)
        return render(request, 'app1/delete_delivery_challan.html', {'delivery_challan': delivery_challan})

    def post(self, request, delivery_challan_id):
        delivery_challan = get_object_or_404(DeliveryChallan, pk=delivery_challan_id)
        try:
            delivery_challan.delete()
            return JsonResponse({'success': True, 'message': 'Delivery challan deleted successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

@method_decorator(csrf_exempt, name='dispatch')
class DeleteCalibrationReportView(View):
    def get(self, request, calibration_report_id):
        calibration_report = get_object_or_404(CalibrationReport, pk=calibration_report_id)
        return render(request, 'app1/delete_calibration_report.html', {'calibration_report': calibration_report})

    def post(self, request, calibration_report_id):
        calibration_report = get_object_or_404(CalibrationReport, pk=calibration_report_id)
        try:
            calibration_report.delete()
            return JsonResponse({'success': True, 'message': 'Calibration report deleted successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

@method_decorator(csrf_exempt, name='dispatch')
class DeleteShedToolsView(View):
    def get(self, request, shedtool_id):
        shed_tool = get_object_or_404(ShedTools, pk=shedtool_id)
        return render(request, 'app1/delete_shed_tool.html', {'shed_tool': shed_tool})

    def post(self, request, shedtool_id):
        shed_tool = get_object_or_404(ShedTools, pk=shedtool_id)
        try:
            shed_tool.delete()
            return JsonResponse({'success': True, 'message': 'Shed tool deleted successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

@method_decorator(csrf_exempt, name='dispatch')
class DeleteTransportToolsView(View):
    def get(self, request, transporttool_id):
        transport_tool = get_object_or_404(TransportTools, pk=transporttool_id)
        return render(request, 'app1/delete_transport_tool.html', {'transport_tool': transport_tool})

    def post(self, request, transporttool_id):
        transport_tool = get_object_or_404(TransportTools, pk=transporttool_id)
        try:
            transport_tool.delete()
            return JsonResponse({'success': True, 'message': 'Transport tool deleted successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

@method_decorator(csrf_exempt, name='dispatch')
class DeleteServiceToolsView(View):
    def get(self, request, servicetool_id):
        service_tool = get_object_or_404(ServiceTools, pk=servicetool_id)
        return render(request, 'app1/delete_service_tool.html', {'service_tool': service_tool})

    def post(self, request, servicetool_id):
        service_tool = get_object_or_404(ServiceTools, pk=servicetool_id)
        try:
            service_tool.delete()
            return JsonResponse({'success': True, 'message': 'Service tool deleted successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

@method_decorator(csrf_exempt, name='dispatch')
class DeleteDeliveryChallanToolsView(View):
    def get(self, request, deliverychallantool_id):
        delivery_challan_tool = get_object_or_404(DeliveryChallanTools, pk=deliverychallantool_id)
        return render(request, 'app1/delete_delivery_challan_tool.html', {'delivery_challan_tool': delivery_challan_tool})

    def post(self, request, deliverychallantool_id):
        delivery_challan_tool = get_object_or_404(DeliveryChallanTools, pk=deliverychallantool_id)
        try:
            delivery_challan_tool.delete()
            return JsonResponse({'success': True, 'message': 'Delivery challan tool deleted successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

@method_decorator(csrf_exempt, name='dispatch')
class DeleteVendorHandlesView(View):
    def get(self, request, vendorhandle_id):
        vendor_handle = get_object_or_404(VendorHandles, pk=vendorhandle_id)
        return render(request, 'app1/delete_vendor_handles.html', {'vendor_handle': vendor_handle})

    def post(self, request, vendorhandle_id):
        vendor_handle = get_object_or_404(VendorHandles, pk=vendorhandle_id)
        try:
            vendor_handle.delete()
            return JsonResponse({'success': True, 'message': 'Vendor handle deleted successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

@method_decorator(csrf_exempt, name='dispatch')
class DeleteInstrumentGroupMasterView(View):
    def get(self, request, tool_group_id):
        instrument_group = get_object_or_404(InstrumentGroupMaster, pk=tool_group_id)
        return render(request, 'app1/delete_instrument_group.html', {'instrument_group': instrument_group})

    def post(self, request, tool_group_id):
        instrument_group = get_object_or_404(InstrumentGroupMaster, pk=tool_group_id)
        try:
            instrument_group.delete()
            return JsonResponse({'success': True, 'message': 'Instrument group deleted successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

@method_decorator(csrf_exempt, name='dispatch')
class DeleteInstrumentFamilyGroupView(View):
    def get(self, request, instrument_family_id):
        instrument_family = get_object_or_404(InstrumentFamilyGroup, pk=instrument_family_id)
        return render(request, 'app1/delete_instrument_family_group.html', {'instrument_family': instrument_family})

    def post(self, request, instrument_family_id):
        instrument_family = get_object_or_404(InstrumentFamilyGroup, pk=instrument_family_id)
        try:
            instrument_family.delete()
            return JsonResponse({'success': True, 'message': 'Instrument family group deleted successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

@method_decorator(csrf_exempt, name='dispatch')
class DeleteInstrumentModelView(View):
    def get(self, request, instrument_no):
        instrument_model = get_object_or_404(InstrumentModel, pk=instrument_no)
        return render(request, 'app1/delete_instrument_model.html', {'instrument_model': instrument_model})

    def post(self, request, instrument_no):
        instrument_model = get_object_or_404(InstrumentModel, pk=instrument_no)
        try:
            instrument_model.delete()
            return JsonResponse({'success': True, 'message': 'Instrument model deleted successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

class CountOfObjects(View):
    def get(self, request):
        vendor_count = Vendor.objects.count()
        shed_count = ShedDetails.objects.count()
        instruments_count = InstrumentModel.objects.count()
        transport_order_count = TransportOrder.objects.count()
        service_order_count = ServiceOrder.objects.count()
        deliverychallan_count = DeliveryChallan.objects.count()

        # return render(request, 'app1/count_list.html', {'vendor_count':vendor_count,'shed_count':shed_count,'instruments_count':instruments_count})
        data = {'vendor_count': vendor_count,'shed_count': shed_count,'instruments_count': instruments_count,'transport_order_count': transport_order_count,'service_order_count': service_order_count,'deliverychallan_count': deliverychallan_count}
        
        return JsonResponse(data)

class UpdateInstrumentShedView(View):
    def get(self, request, *args, **kwargs):
        instruments = InstrumentModel.objects.all()
        sheds = ShedDetails.objects.all()

        updated_count = 0

        for instrument in instruments:
            found_shed = None
            for shed in sheds:
                if self.instrument_in_shed(instrument, shed):
                    found_shed = shed
                    break
            
            if found_shed:
                instrument.current_shed = found_shed
                instrument.save()
                updated_count += 1
            else:
                instrument.current_shed = None
                instrument.save()

        return JsonResponse({'message': f'Successfully updated {updated_count} instruments.'})

    def instrument_in_shed(self, instrument, shed):
        try:
            ShedTools.objects.get(shed=shed, using_tool=instrument)
            return True
        except ShedTools.DoesNotExist:
            return False
          
class InstrumentsByGroupView(APIView):
    def get(self, request, tool_group_id):
        tool_group = get_object_or_404(InstrumentGroupMaster, pk=tool_group_id)
        
        instruments = InstrumentModel.objects.filter(type_of_tool=tool_group)      
        serialized_instruments = InstrumentModelSerializer(instruments, many=True).data
        
        return Response({'tool_group': tool_group.tool_group_name,'instruments': serialized_instruments})

# class PendingServiceOrdersByVendorView(APIView):
#     def get(self, request, vendor_id):
#         vendor = get_object_or_404(Vendor, pk=vendor_id)
        
#         pending_service_orders = ServiceOrder.objects.filter(vendor=vendor, service_pending=True)
#         serialized_service_orders = ServiceOrderSerializer(pending_service_orders, many=True).data
        
#         return Response({'vendor': vendor.name,'pending_service_orders': serialized_service_orders})

class PendingServiceOrdersByVendorView(APIView):
    def get(self, request, vendor_id):        
        vendor = get_object_or_404(Vendor, pk=vendor_id, vendor_type=1)#1=vendor type - calibration agency
        
        pending_service_orders = ServiceOrder.objects.filter(vendor=vendor, service_pending=True)
        serialized_service_orders = ServiceOrderSerializer(pending_service_orders, many=True).data
        
        return Response({'vendor': vendor.name, 'pending_service_orders': serialized_service_orders})

@method_decorator(csrf_exempt, name='dispatch')
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'app1/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@method_decorator(csrf_exempt, name='dispatch')
class UpdateShedDetailsView(View):

    def get(self, request, shed_id):
        shed = get_object_or_404(ShedDetails, pk=shed_id)
        shed_data = {'shed_id': shed.shed_id,'name': shed.name,'location': shed.location,'phone_number': shed.phone_number}
        return JsonResponse({'success': True, 'data': shed_data})
        
    def post(self, request, shed_id):
        shed = get_object_or_404(ShedDetails, pk=shed_id)
        body_data = json.loads(request.body)

        name = body_data.get('name')
        location = body_data.get('location')
        phone_number = body_data.get('phone_number')

        updated_fields = {}
        if name is not None:
            updated_fields['name'] = name
        if location is not None:
            updated_fields['location'] = location
        if phone_number is not None:
            updated_fields['phone_number'] = phone_number

        if updated_fields:
            ShedDetails.objects.filter(pk=shed_id).update(**updated_fields)
            return JsonResponse({'success': True, 'message': 'Shed details updated successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'No fields to update'}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class UpdateVendorView(View):

    def get(self, request, vendor_id):
        vendor = get_object_or_404(Vendor, pk=vendor_id)
        vendor_data = {
            'vendor_id': vendor.vendor_id,
            'name': vendor.name,
            'location': vendor.location,
            'address': vendor.address,
            'phone_number': vendor.phone_number,
            'email': vendor.email,
            'nabl_number': vendor.nabl_number,
            'nabl_certificate': vendor.nabl_certificate.url if vendor.nabl_certificate else None,
            'vendor_type': vendor.vendor_type_id
        }
        return JsonResponse({'success': True, 'data': vendor_data})
        
    def post(self, request, vendor_id):
        vendor = get_object_or_404(Vendor, pk=vendor_id)
        body_data = json.loads(request.body)

        name = body_data.get('name')
        location = body_data.get('location')
        address = body_data.get('address')
        phone_number = body_data.get('phone_number')
        email = body_data.get('email')
        nabl_number = body_data.get('nabl_number')
        vendor_type_id = body_data.get('vendor_type')

        updated_fields = {}
        if name is not None:
            updated_fields['name'] = name
        if location is not None:
            updated_fields['location'] = location
        if address is not None:
            updated_fields['address'] = address
        if phone_number is not None:
            updated_fields['phone_number'] = phone_number
        if email is not None:
            updated_fields['email'] = email
        if nabl_number is not None:
            updated_fields['nabl_number'] = nabl_number
        if vendor_type_id is not None:
            updated_fields['vendor_type_id'] = vendor_type_id

        if updated_fields:
            Vendor.objects.filter(pk=vendor_id).update(**updated_fields)
            return JsonResponse({'success': True, 'message': 'Vendor details updated successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'No fields to update'}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class UpdateInstrumentGroupMasterView(View):

    def get(self, request, tool_group_id):
        group = get_object_or_404(InstrumentGroupMaster, pk=tool_group_id)
        group_data = {
            'tool_group_id': group.tool_group_id,
            'tool_group_name': group.tool_group_name,
            'tool_group_code': group.tool_group_code
        }
        return JsonResponse({'success': True, 'data': group_data})
        
    def post(self, request, tool_group_id):
        group = get_object_or_404(InstrumentGroupMaster, pk=tool_group_id)
        body_data = json.loads(request.body)

        tool_group_name = body_data.get('tool_group_name')
        tool_group_code = body_data.get('tool_group_code')

        updated_fields = {}
        if tool_group_name is not None:
            updated_fields['tool_group_name'] = tool_group_name
        if tool_group_code is not None:
            updated_fields['tool_group_code'] = tool_group_code

        if updated_fields:
            InstrumentGroupMaster.objects.filter(pk=tool_group_id).update(**updated_fields)
            return JsonResponse({'success': True, 'message': 'Instrument group details updated successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'No fields to update'}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class UpdateInstrumentFamilyGroupView(View):

    def get(self, request, instrument_family_id):
        family = get_object_or_404(InstrumentFamilyGroup, pk=instrument_family_id)
        family_data = {
            'instrument_family_id': family.instrument_family_id,
            'instrument_family_name': family.instrument_family_name,
            'instrument_group_master': family.instrument_group_master_id
        }
        return JsonResponse({'success': True, 'data': family_data})
        
    def post(self, request, instrument_family_id):
        family = get_object_or_404(InstrumentFamilyGroup, pk=instrument_family_id)
        body_data = json.loads(request.body)

        instrument_family_name = body_data.get('instrument_family_name')
        instrument_group_master_id = body_data.get('instrument_group_master')

        updated_fields = {}
        if instrument_family_name is not None:
            updated_fields['instrument_family_name'] = instrument_family_name
        if instrument_group_master_id is not None:
            updated_fields['instrument_group_master_id'] = instrument_group_master_id

        if updated_fields:
            InstrumentFamilyGroup.objects.filter(pk=instrument_family_id).update(**updated_fields)
            return JsonResponse({'success': True, 'message': 'Instrument family group details updated successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'No fields to update'}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class UpdateInstrumentModelView(View):

    def get(self, request, instrument_no):
        instrument = get_object_or_404(InstrumentModel, pk=instrument_no)
        instrument_data = {
            'instrument_no': instrument.instrument_no,
            'instrument_name': instrument.instrument_name,
            'manufacturer_name': instrument.manufacturer_name,
            'year_of_purchase': instrument.year_of_purchase,
            'gst': instrument.gst,
            'description': instrument.description,
            'instrument_range': instrument.instrument_range,
            'least_count': instrument.least_count,
            'type_of_tool': instrument.type_of_tool_id,
            'calibration_frequency': instrument.calibration_frequency,
            'service_status': instrument.service_status,
            'current_shed': instrument.current_shed_id
        }
        return JsonResponse({'success': True, 'data': instrument_data})
        
    def post(self, request, instrument_no):
        instrument = get_object_or_404(InstrumentModel, pk=instrument_no)
        body_data = json.loads(request.body)

        instrument_name = body_data.get('instrument_name')
        manufacturer_name = body_data.get('manufacturer_name')
        year_of_purchase = body_data.get('year_of_purchase')
        gst = body_data.get('gst')
        description = body_data.get('description')
        instrument_range = body_data.get('instrument_range')
        least_count = body_data.get('least_count')
        type_of_tool_id = body_data.get('type_of_tool')
        calibration_frequency = body_data.get('calibration_frequency')

        updated_fields = {}
        if instrument_name is not None:
            updated_fields['instrument_name'] = instrument_name
        if manufacturer_name is not None:
            updated_fields['manufacturer_name'] = manufacturer_name
        if year_of_purchase is not None:
            updated_fields['year_of_purchase'] = year_of_purchase
        if gst is not None:
            updated_fields['gst'] = gst
        if description is not None:
            updated_fields['description'] = description
        if instrument_range is not None:
            updated_fields['instrument_range'] = instrument_range
        if least_count is not None:
            updated_fields['least_count'] = least_count
        if type_of_tool_id is not None:
            updated_fields['type_of_tool_id'] = type_of_tool_id
        if calibration_frequency is not None:
            updated_fields['calibration_frequency'] = calibration_frequency

        if updated_fields:
            InstrumentModel.objects.filter(pk=instrument_no).update(**updated_fields)
            return JsonResponse({'success': True, 'message': 'Instrument details updated successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'No fields to update'}, status=400)  
        
@method_decorator(csrf_exempt, name='dispatch')
class UpdateVendorHandlesView(View):

    def get(self, request, vendorhandle_id):
        vendor_handle = get_object_or_404(VendorHandles, pk=vendorhandle_id)
        vendor_handle_data = {
            'vendorhandle_id': vendor_handle.vendorhandle_id,
            'vendor': vendor_handle.vendor_id,
            'tool': vendor_handle.tool_id,
            'turnaround_time': vendor_handle.turnaround_time,
            'cost': vendor_handle.cost
        }
        return JsonResponse({'success': True, 'data': vendor_handle_data})
        
    def post(self, request, vendorhandle_id):
        vendor_handle = get_object_or_404(VendorHandles, pk=vendorhandle_id)
        body_data = json.loads(request.body)

        vendor_id = body_data.get('vendor')
        tool_id = body_data.get('tool')
        turnaround_time = body_data.get('turnaround_time')
        cost = body_data.get('cost')

        updated_fields = {}
        if vendor_id is not None:
            vendor = get_object_or_404(Vendor, pk=vendor_id)
            updated_fields['vendor'] = vendor
        if tool_id is not None:
            tool = get_object_or_404(InstrumentModel, pk=tool_id)
            updated_fields['tool'] = tool
        if turnaround_time is not None:
            updated_fields['turnaround_time'] = turnaround_time
        if cost is not None:
            updated_fields['cost'] = cost

        if updated_fields:
            VendorHandles.objects.filter(pk=vendorhandle_id).update(**updated_fields)
            return JsonResponse({'success': True, 'message': 'Vendor handle details updated successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'No fields to update'}, status=400)
        
