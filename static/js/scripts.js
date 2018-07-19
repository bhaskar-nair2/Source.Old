function CheckName() {
    console.log('Detected!');
    var Socket = new WebSocket('http://127.0.0.1:5000/nameCheck');
    
    return true;
}