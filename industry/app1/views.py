import json
from django.forms import inlineformset_factory
from django.http import HttpResponse, HttpResponseServerError, JsonResponse
from django.shortcuts import render,  redirect
from django.views import View
from .forms import CalibrationReportForm, DeliveryChallanForm, DeliveryChallanToolsForm, DeliveryChallanToolsFormSet, InstrumentFamilyGroupForm, InstrumentFamilyGroupForm1, InstrumentForm, InstrumentGroupMasterForm, InstrumentGroupMasterForm1, InstrumentModelForm1, ServiceOrderForm, ServiceToolsForm, ShedDetailsForm, ShedToolsForm, TransportMovementOrderForm,TransportOrderForm, TransportToolsForm, VendorForm, VendorHandlesForm
from .models import InstrumentFamilyGroup, InstrumentGroupMaster, TransportOrder, CalibrationReport, DeliveryChallan, DeliveryChallanTools, InstrumentModel,  ServiceOrder, ServiceTools, ShedTools, TransportOrder, ShedDetails, TransportTools, Vendor, VendorHandles
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import CalibrationReportSerializer, InstrumentFamilyGroupSerializer, InstrumentGroupMasterSerializer, InstrumentModelSerializer, ServiceOrderSerializer, ServiceToolsSerializer, ShedDetailsSerializer, ShedToolsSerializer, TransportOrderSerializer, TransportToolsSerializer, VendorHandlesSerializer, VendorSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import AnotherServiceOrderForm, AnotherServiceToolForm
from .models import ServiceOrder, ServiceTools
from django.core import serializers
from django.db import transaction
from django.shortcuts import get_object_or_404
from datetime import timedelta
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction

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
    
class InstrumentFamilyGroupView(APIView):
    def get(self, request):
        instruments = InstrumentFamilyGroup.objects.all()
        instrument_serializer = InstrumentFamilyGroupSerializer(instruments, many=True)

        response_data = {
            'instrument_models': instrument_serializer.data,
        }

        return Response(response_data)
    
class InstrumentGroupMasterView(APIView):
    def get(self, request):
        instruments = InstrumentGroupMaster.objects.all()
        instrument_serializer = InstrumentGroupMasterSerializer(instruments, many=True)

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
# @method_decorator(csrf_exempt, name='dispatch')
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

@method_decorator(csrf_exempt, name='dispatch')
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
# @method_decorator(csrf_exempt, name='dispatch')
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

#             # Redirect to GenerateBillView with the created service order ID
#             return redirect('generate_bill', service_order_id=service_order.service_id)

#         # Handle invalid forms
#         return render(request, 'app1/service_order_form1.html', {'order_form': order_form, 'tool_forms': tool_forms})

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
            'instrument_tools' : instrument_serializer.data,
        }

        return Response(response_data)

    def post(self, request):
        order_serializer = ServiceOrderSerializer(data=request.data)
        
        if order_serializer.is_valid():
            service_order = order_serializer.save()

            tools_data = request.data.get('tools', [])
            for tool_data in tools_data:
                tool_id = tool_data.get('tool')
                vendor_id = tool_data.get('vendor')
                tool = get_object_or_404(InstrumentModel, pk=tool_id)
                vendor = get_object_or_404(Vendor, pk=vendor_id)

                ServiceTools.objects.create(service=service_order, tool=tool, vendor=vendor)

            # Return success response with service order ID
            return Response({'success': True, 'service_order_id': service_order.id}, status=status.HTTP_201_CREATED)
        else:
            # Return error response if service order data is not valid
            return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        
        # Extracting movement_ids from serialized transport history
        movement_ids = [item['transport'] for item in serialized_transport_history]
        
        # Filtering TransportOrder instances based on extracted movement_ids
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
                'vendor': service_tool.service.vendor.name  # Assuming you have a 'name' field in Vendor model
            }
            serialized_service_history.append(service_order_data)
        
        return Response({'instrument': InstrumentModelSerializer(instrument).data, 'service_history': serialized_service_history})
    
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
    
# @method_decorator(csrf_exempt, name='dispatch')
# class DeliveryChallanView(View):
#     def get(self, request):
#         # Retrieve shed, vendor, and service details
#         sheds = ShedDetails.objects.all()
#         vendors = Vendor.objects.all()
#         services = ServiceOrder.objects.all()
#         instruments = InstrumentModel.objects.all()

#         # Create form instances
#         delivery_challan_form = DeliveryChallanForm()
#         delivery_challan_tools_formset = DeliveryChallanToolsFormSet()
#         calibration_report_form = CalibrationReportForm()

#         # Pass form instances and context variables to the template
#         return render(request, 'app1/delivery_challan.html', {
#             'delivery_challan_form': delivery_challan_form,
#             'delivery_challan_tools_formset': delivery_challan_tools_formset,
#             'calibration_report_form': calibration_report_form,
#             'sheds': sheds,
#             'vendors': vendors,
#             'services': services,
#             'instruments': instruments,
#         })
    
    # def post(self, request):
    #     delivery_challan_form = DeliveryChallanForm(request.POST)
    #     DeliveryChallanToolsFormSet = inlineformset_factory(DeliveryChallan, DeliveryChallanTools, form=DeliveryChallanToolsForm, extra=1)
    #     delivery_challan_tools_formset = DeliveryChallanToolsFormSet(request.POST)
    #     calibration_report_form = CalibrationReportForm(request.POST)

    #     if calibration_report_form.is_valid() and delivery_challan_form.is_valid() and delivery_challan_tools_formset.is_valid():
    #         calibration_report = calibration_report_form.save(commit=False)
    #         selected_tool = delivery_challan_tools_formset.cleaned_data[0]['tool']
    #         calibration_frequency = selected_tool.calibration_frequency
    #         calibration_report.calibration_tool = selected_tool
                    
    #         calibration_date = calibration_report.calibration_date
    #         next_calibration_date = calibration_date + timedelta(days=calibration_frequency * 365)
    #         calibration_report.next_calibration_date = next_calibration_date
            
    #         try:
    #             vendor_handle = VendorHandles.objects.filter(tool=selected_tool).first()
    #             if not vendor_handle:
    #                 raise ObjectDoesNotExist("Vendor handle not found for the selected tool.")
    #         except ObjectDoesNotExist:
    #             return HttpResponse('Vendor handle not found for the selected tool.', status=400)
            
    #         turnaround_time = vendor_handle.turnaround_time
    #         notification_date = next_calibration_date - timedelta(days=turnaround_time)
    #         calibration_report.notification_date = notification_date
            
    #         calibration_report.save()
            
    #         delivery_challan = delivery_challan_form.save()

    #         for form in delivery_challan_tools_formset:
    #             if form.is_valid():
    #                 tool_instance = form.save(commit=False)
    #                 tool_instance.deliverychallan = delivery_challan
    #                 tool_instance.calibration_report = calibration_report
    #                 tool_instance.save() 
                            
    #         return redirect('home')
        
    #     return render(request, 'app1/delivery_challan.html', {'delivery_challan_form': delivery_challan_form, 'delivery_challan_tools_formset': delivery_challan_tools_formset, 'calibration_report_form': calibration_report_form})

@method_decorator(csrf_exempt, name='dispatch')
class DeliveryChallanView(View):
    def get(self, request):
        # Retrieve shed, vendor, and service details
        sheds = ShedDetails.objects.all()
        vendors = Vendor.objects.all()
        services = ServiceOrder.objects.all()
        instruments = InstrumentModel.objects.all()

        # Create form instances
        delivery_challan_form = DeliveryChallanForm()
        DeliveryChallanToolsFormSet = inlineformset_factory(DeliveryChallan, DeliveryChallanTools, form=DeliveryChallanToolsForm, extra=1)
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
        # Parse the JSON payload sent from the frontend
        data = json.loads(request.body)

        # Extract data for each form from the payload
        delivery_challan_form_data = data.get('delivery_challan_form')
        delivery_challan_tools_formset_data = data.get('delivery_challan_tools_formset')
        calibration_report_form_data = data.get('calibration_report_form')

        # Create form instances using the extracted data
        delivery_challan_form = DeliveryChallanForm(delivery_challan_form_data)
        delivery_challan_tools_formset = DeliveryChallanToolsFormSet(delivery_challan_tools_formset_data)
        calibration_report_form = CalibrationReportForm(calibration_report_form_data)

        # Perform form validation
        if calibration_report_form.is_valid() and delivery_challan_form.is_valid() and delivery_challan_tools_formset.is_valid():
            calibration_report = calibration_report_form.save(commit=False)
            selected_tool = delivery_challan_tools_formset.cleaned_data[0]['tool']
            calibration_frequency = selected_tool.calibration_frequency
            calibration_report.calibration_tool = selected_tool

            calibration_date = calibration_report.calibration_date
            next_calibration_date = calibration_date + timedelta(days=calibration_frequency * 365)
            calibration_report.next_calibration_date = next_calibration_date

            try:
                vendor_handle = VendorHandles.objects.filter(tool=selected_tool).first()
                if not vendor_handle:
                    raise ObjectDoesNotExist("Vendor handle not found for the selected tool.")
            except ObjectDoesNotExist:
                return JsonResponse({'error': 'Vendor handle not found for the selected tool.'}, status=400)

            turnaround_time = vendor_handle.turnaround_time
            notification_date = next_calibration_date - timedelta(days=turnaround_time)
            calibration_report.notification_date = notification_date

            calibration_report.save()

            delivery_challan = delivery_challan_form.save()

            for form_data in delivery_challan_tools_formset_data:
                form = DeliveryChallanToolsForm(form_data)
                if form.is_valid():
                    tool_instance = form.save(commit=False)
                    tool_instance.deliverychallan = delivery_challan
                    tool_instance.calibration_report = calibration_report
                    tool_instance.save()

            return JsonResponse({'success': True})  # Return a success response
        else:
            errors = {
                'delivery_challan_errors': delivery_challan_form.errors,
                'delivery_challan_tools_errors': delivery_challan_tools_formset.errors,
                'calibration_report_errors': calibration_report_form.errors
            }
            return JsonResponse({'success': False, 'errors': errors}, status=400)             

@method_decorator(csrf_exempt, name='dispatch')
class AddInstrumentView(View):
    def get(self, request):
        instrument_family_group_form = InstrumentFamilyGroupForm1()
        instrument_group_master_form = InstrumentGroupMasterForm1()
        instrument_model_form = InstrumentModelForm1()
        return render(request, 'app1/instrument_form.html', {
            'instrument_family_group_form': instrument_family_group_form,
            'instrument_group_master_form': instrument_group_master_form,
            'instrument_model_form': instrument_model_form
        })

    def post(self, request):
        instrument_family_group_form = InstrumentFamilyGroupForm1(request.POST)
        instrument_group_master_form = InstrumentGroupMasterForm1(request.POST)
        instrument_model_form = InstrumentModelForm1(request.POST)
        print(request.POST)
        if instrument_family_group_form.is_valid() and instrument_group_master_form.is_valid() and instrument_model_form.is_valid():
            # Save Instrument Group Master
            instrument_group_master = instrument_group_master_form.save()

            # Save Instrument Family Group
            instrument_family_group = instrument_family_group_form.save(commit=False)
            instrument_family_group.instrument_group_master = instrument_group_master
            instrument_family_group.save()

            # Save Instrument Model
            instrument_model = instrument_model_form.save(commit=False)
            instrument_model.type_of_tool = instrument_group_master
            instrument_model.save()

            return redirect('home')

        return render(request, 'app1/instrument_form.html', {
            'instrument_family_group_form': instrument_family_group_form,
            'instrument_group_master_form': instrument_group_master_form,
            'instrument_model_form': instrument_model_form
        })  
    
    
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
        # Parse JSON data from the request body
        body_data = json.loads(request.body)

        # Extract instrument model details from the parsed data
        instrument_name = body_data.get('instrument_name')
        manufacturer_name = body_data.get('manufacturer_name')
        year_of_purchase = body_data.get('year_of_purchase')
        gst = body_data.get('gst')
        description = body_data.get('description')
        instrument_range = body_data.get('instrument_range')
        least_count = body_data.get('least_count')
        type_of_tool_id = body_data.get('type_of_tool_id')
        calibration_frequency = body_data.get('calibration_frequency')

        # Create a dictionary with the extracted data
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

        # Create an InstrumentForm instance with the extracted data
        form = InstrumentForm(instrument_data)

        # Check if the form is valid
        if form.is_valid():
            # Save the form data
            form.save()
            return JsonResponse({'success': True})  # Return a JSON response indicating success
        else:
            # If form is not valid, return a JSON response with errors
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
        # Parse JSON data from the request body
        body_data = json.loads(request.body)

        # Extract instrument group master details from the parsed data
        # Adjust the keys according to your JSON structure
        # For example, if your JSON has 'group_name' instead of 'name', use body_data.get('group_name')
        name = body_data.get('name')
        description = body_data.get('description')

        # Create a dictionary with the extracted data
        instrument_group_master_data = {
            'name': name,
            'description': description
        }

        # Create an InstrumentGroupMasterForm instance with the extracted data
        form = InstrumentGroupMasterForm(instrument_group_master_data)

        # Check if the form is valid
        if form.is_valid():
            # Save the form data
            form.save()
            return JsonResponse({'success': True})  # Return a JSON response indicating success
        else:
            # If form is not valid, return a JSON response with errors
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
        # Parse JSON data from the request body
        body_data = json.loads(request.body)

        # Extract instrument family details from the parsed data
        # Adjust the keys according to your JSON structure
        # For example, if your JSON has 'family_name' instead of 'name', use body_data.get('family_name')
        name = body_data.get('name')

        # Create a dictionary with the extracted data
        instrument_family_data = {
            'instrument_family_name': name,
            'instrument_group_master': body_data.get('instrument_group_master') 
        }

        # Create an InstrumentFamilyGroupForm instance with the extracted data
        form = InstrumentFamilyGroupForm(instrument_family_data)

        # Check if the form is valid
        if form.is_valid():
            # Save the form data
            form.save()
            return JsonResponse({'success': True})  # Return a JSON response indicating success
        else:
            # If form is not valid, return a JSON response with errors
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})
        
@method_decorator(csrf_exempt, name='dispatch')
class AddVendorView(View):
    def get(self, request):
        form = VendorForm()
        return render(request, 'app1/vendor_form.html', {'form': form})

    def post(self, request):
        # Parse JSON data from the request body
        body_data = json.loads(request.body)

        # Extract vendor details from the parsed data
        name = body_data.get('name')
        location = body_data.get('location')
        address = body_data.get('address')
        phone_number = body_data.get('phone_number')

        # Create a dictionary with the extracted data
        vendor_data = {
            'name': name,
            'location': location,
            'address': address,
            'phone_number': phone_number
        }

        # Create a VendorForm instance with the extracted data
        form = VendorForm(vendor_data)

        # Check if the form is valid
        if form.is_valid():
            # Save the form data
            form.save()
            return JsonResponse({'success': True})  # Return a JSON response indicating success
        else:
            # If form is not valid, return a JSON response with errors
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})

@method_decorator(csrf_exempt, name='dispatch')
class AddVendorHandlesView(View):
    def get(self, request):

        form = VendorHandlesForm()
        return render(request, 'app1/vendor_handles_form.html', {'form': form})

    def post(self, request):
        # Parse JSON data from the request body
        body_data = json.loads(request.body)

        # Extract vendor handle details from the parsed data
        vendor_id = body_data.get('vendor_id')
        tool_id = body_data.get('tool_id')
        turnaround_time = body_data.get('turnaround_time')
        cost = body_data.get('cost')

        # Create a dictionary with the extracted data
        vendor_handles_data = {
            'vendor': vendor_id,
            'tool': tool_id,
            'turnaround_time': turnaround_time,
            'cost': cost
        }

        # Create a VendorHandlesForm instance with the extracted data
        form = VendorHandlesForm(vendor_handles_data)

        # Check if the form is valid
        if form.is_valid():
            # Save the form data
            form.save()
            return JsonResponse({'success': True})  # Return a JSON response indicating success
        else:
            # If form is not valid, return a JSON response with errors
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})

@method_decorator(csrf_exempt, name='dispatch')
class AddShedDetailsView(View):
    def get(self, request):
        # If you need to retrieve existing data, implement the GET method accordingly
        # For example:
        # shed_details = ShedDetails.objects.all()  # Retrieve all existing shed details
        # data = [{'id': sd.id, 'name': sd.name, 'location': sd.location, 'phone_number': sd.phone_number} for sd in shed_details]
        # return JsonResponse({'shed_details': data})

        form = ShedDetailsForm()
        return render(request, 'app1/shed_details_form.html', {'form': form})

    def post(self, request):
        # Parse JSON data from the request body
        body_data = json.loads(request.body)

        # Extract shed details from the parsed data
        name = body_data.get('name')
        location = body_data.get('location')
        address = body_data.get('address')
        phone_number = body_data.get('phone_number')

        # Create a dictionary with the extracted data
        shed_details_data = {
            'name': name,
            'location': location,
            'address': address,
            'phone_number': phone_number
        }

        # Create a ShedDetailsForm instance with the extracted data
        form = ShedDetailsForm(shed_details_data)

        # Check if the form is valid
        if form.is_valid():
            # Save the form data
            form.save()
            return JsonResponse({'success': True})  # Return a JSON response indicating success
        else:
            # If form is not valid, return a JSON response with errors
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})

@method_decorator(csrf_exempt, name='dispatch')
class AddShedToolsView(View):
    def get(self, request):
        form = ShedToolsForm()
        return render(request, 'app1/shed_tools_form.html', {'form': form})

    def post(self, request):
        # Parse JSON data from the request body
        body_data = json.loads(request.body)

        # Extract shed tool details from the parsed data
        shed_id = body_data.get('shed_id')
        tool_id = body_data.get('tool_id')

        # Create a dictionary with the extracted data
        shed_tools_data = {
            'shed': shed_id,
            'tool': tool_id
        }

        # Create a ShedToolsForm instance with the extracted data
        form = ShedToolsForm(shed_tools_data)

        # Check if the form is valid
        if form.is_valid():
            # Save the form data
            form.save()
            return JsonResponse({'success': True})  # Return a JSON response indicating success
        else:
            # If form is not valid, return a JSON response with errors
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})

class VendorDeleteView(View):
    def get(self, request, vendor_id):
        vendor = Vendor.objects.get(pk=vendor_id)
        return render(request, 'app1/delete_vendor.html', {'vendor': vendor})

    def post(self, request, vendor_id):
        vendor = get_object_or_404(Vendor, pk=vendor_id)
        vendor.delete()
        return redirect('home')

class ShedDeleteView(View):
    def get(self, request, shed_id):
        shed = get_object_or_404(ShedDetails, pk=shed_id)
        return render(request, 'app1/delete_shed.html', {'shed': shed})

    def post(self, request, shed_id):
        shed = get_object_or_404(ShedDetails, pk=shed_id)
        shed.delete()
        return redirect('home')
            
class TransportOrderDeleteView(View):
    def get(self, request, movement_id):
        transport_order = get_object_or_404(TransportOrder, pk=movement_id)
        return render(request, 'app1/delete_transport_order.html', {'transport_order': transport_order})

    def post(self, request, movement_id):
        transport_order = get_object_or_404(TransportOrder, pk=movement_id)
        transport_order.delete()
        return('home')
class ServiceOrderDeleteView(View):
    def get(self, request, service_id):
        service_order = get_object_or_404(ServiceOrder, pk=service_id)
        return render(request, 'app1/delete_service_order.html', {'service_order': service_order})

    def post(self, request, service_id):
        service_order = get_object_or_404(ServiceOrder, pk=service_id)
        service_order.delete()
        return redirect('home')

class DeleteDeliveryChallanView(View):
    def get(self, request, delivery_challan_id):
        delivery_challan = get_object_or_404(DeliveryChallan, pk=delivery_challan_id)
        return render(request, 'app1/delete_delivery_challan.html', {'delivery_challan': delivery_challan})

    def post(self, request, delivery_challan_id):
        delivery_challan = get_object_or_404(DeliveryChallan, pk=delivery_challan_id)
        delivery_challan.delete()
        return redirect('home')

class DeleteCalibrationReportView(View):
    def get(self, request, calibration_report_id):
        calibration_report = get_object_or_404(CalibrationReport, pk=calibration_report_id)
        return render(request, 'app1/delete_calibration_report.html', {'calibration_report': calibration_report})

    def post(self, request, calibration_report_id):
        calibration_report = get_object_or_404(CalibrationReport, pk=calibration_report_id)
        calibration_report.delete()
        return redirect('home')

class DeleteShedToolsView(View):
    def get(self, request, shedtool_id):
        shed_tool = get_object_or_404(ShedTools, pk=shedtool_id)
        return render(request, 'app1/delete_shed_tool.html', {'shed_tool': shed_tool})

    def post(self, request, shedtool_id):
        shed_tool = get_object_or_404(ShedTools, pk=shedtool_id)
        shed_tool.delete()
        return redirect('home')

class DeleteTransportToolsView(View):
    def get(self, request, transporttool_id):
        transport_tool = get_object_or_404(TransportTools, pk=transporttool_id)
        return render(request, 'app1/delete_transport_tool.html', {'transport_tool': transport_tool})

    def post(self, request, transporttool_id):
        transport_tool = get_object_or_404(TransportTools, pk=transporttool_id)
        transport_tool.delete()
        return redirect('home')

class DeleteServiceToolsView(View):
    def get(self, request, servicetool_id):
        service_tool = get_object_or_404(ServiceTools, pk=servicetool_id)
        return render(request, 'app1/delete_service_tool.html', {'service_tool': service_tool})

    def post(self, request, servicetool_id):
        service_tool = get_object_or_404(ServiceTools, pk=servicetool_id)
        service_tool.delete()
        return redirect('home') 


class DeleteDeliveryChallanToolsView(View):
    def get(self, request, deliverychallantool_id):
        delivery_challan_tool = get_object_or_404(DeliveryChallanTools, pk=deliverychallantool_id)
        return render(request, 'app1/delete_delivery_challan_tool.html', {'delivery_challan_tool': delivery_challan_tool})

    def post(self, request, deliverychallantool_id):
        delivery_challan_tool = get_object_or_404(DeliveryChallanTools, pk=deliverychallantool_id)
        delivery_challan_tool.delete()
        return redirect('home') 

class DeleteVendorHandlesView(View):
    def get(self, request, vendorhandle_id):
        vendor_handle = get_object_or_404(VendorHandles, pk=vendorhandle_id)
        return render(request, 'app1/delete_vendor_handles.html', {'vendor_handle': vendor_handle})

    def post(self, request, vendorhandle_id):
        vendor_handle = get_object_or_404(VendorHandles, pk=vendorhandle_id)
        vendor_handle.delete()
        return redirect('home')

class DeleteInstrumentGroupMasterView(View):
    def get(self, request, tool_id):
        instrument_group = get_object_or_404(InstrumentGroupMaster, pk=tool_id)
        return render(request, 'app1/delete_instrument_group.html', {'instrument_group': instrument_group})

    def post(self, request, tool_id):
        instrument_group = get_object_or_404(InstrumentGroupMaster, pk=tool_id)
        instrument_group.delete()
        return redirect('home')

class DeleteInstrumentFamilyGroupView(View):
    def get(self, request, instrumentfamilyid):
        instrument_family = get_object_or_404(InstrumentFamilyGroup, pk=instrumentfamilyid)
        return render(request, 'app1/delete_instrument_family_group.html', {'instrument_family': instrument_family})

    def post(self, request, instrumentfamilyid):
        instrument_family = get_object_or_404(InstrumentFamilyGroup, pk=instrumentfamilyid)
        instrument_family.delete()
        return redirect('home')

