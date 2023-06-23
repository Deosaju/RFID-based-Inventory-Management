from django.http import HttpResponse
from django.template.loader import render_to_string
import serial
import time 
from django.shortcuts import render, redirect
from .forms import MyForm
from .models import MyData

"""
 ser = serial.Serial('COM3', 9600)  # Replace 'COM1' with the appropriate serial port
        ser.flushInput()
        while True:
            if ser.in_waiting > 0:
                uid = ser.readline().decode().rstrip()
                print(f"RFID Tag UID: {uid}")
                attendance_list_html = render_to_string('attendance/attendance_list.html', {'students': uid})
                # Return the attendance list HTML as the response
                return HttpResponse(attendance_list_html)
"""

def my_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            ser = serial.Serial('COM3', 9600)
            ser.flushInput()        
            while True:
                if ser.in_waiting > 0:
                    uid = ser.readline().decode().rstrip()
                    print(f"RFID Tag UID: {uid}")
                    instance.serial = uid
                    instance.save()
                    break

            return redirect('success')  # Redirect to a success page
    else:
        form = MyForm()
    
    return render(request, 'attendance/my_form_template.html', {'form': form})

def success(request):
    return HttpResponse('<body style="background-color: rgb(99, 247, 95); font-size: larger; display: flex; justify-content: center; align-items: center;"><center>Success! Please return to home page.</center></body>')

        
def data_list_view(request):
    data = MyData.objects.all()
    return render(request, 'attendance/data_list_template.html', {'data': data})

def deregister_item_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')  # Assuming the name is submitted through a form field
        item = MyData.objects.filter(pid=name).first()
        if item:
            item.delete()
            return redirect('success')  # Redirect to a success page
        else:
            return redirect('not_found')  # Redirect to a not found page
    else:
        return render(request, 'attendance/deregister_item_template.html')
    
def scan_view(request):
    if request.method == 'POST':
        # Connect to Arduino using the appropriate serial port and baud rate
        arduino = serial.Serial('COM3', 9600)

        # Get all the RFID tags from MyData model
        saved_tags = MyData.objects.values_list('serial', flat=True)
         # Start scanning for 20 seconds
        start_time = time.time()
        scan_results = []
        while time.time() - start_time < 10:
            # Read RFID data from Arduino
            rfid_data = arduino.readline().decode().strip()
            # Check if the RFID data is already in scan_results and exists in MyData
            if rfid_data not in scan_results:
                # Append the scanned data to the results list
                scan_results.append(rfid_data)

        # Close the serial connection
        arduino.close()

        # If any scanned RFID was not found in MyData, display a warning page
        unregistered = []
        for rfid in scan_results:
            if not MyData.objects.filter(serial=rfid).exists():
                unregistered.append(rfid)

        missing_tags = set(saved_tags) - set(scan_results)
        # If any saved RFID tag was not scanned, display a warning page
        if missing_tags:
            warning_message = f"The following tags were not scanned: {', '.join(missing_tags)}"
            return render(request, 'attendance/warning.html', {'warning_message': warning_message , 'unregistered': unregistered })
        
        if unregistered:
            warning_message = f"The following tags were not scanned: {', '.join(unregistered)}"
            return render(request, 'attendance/warning.html', {'warning_message': "All registered item is Secure" , 'unregistered': unregistered })
          
            
        # Pass the scan_results to the template
        return render(request, 'attendance/scan.html', {'scan_results': scan_results})
    else:       
        return render(request, 'attendance/scan.html')
    