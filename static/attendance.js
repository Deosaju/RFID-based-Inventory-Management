document.addEventListener('DOMContentLoaded', function() {
    var scanBtn = document.getElementById('scan-btn');
    scanBtn.addEventListener('click', function() {
        // Make an AJAX request to the server to initiate the RFID scanning
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/scan/');
        xhr.send();
    });
});
