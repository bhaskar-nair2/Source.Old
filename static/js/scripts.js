var sock = io.connect();

function NameCheck(data) {
    if (data !== '') {
        sock.emit('name_check', data);
        sock.on('responded', function (msg) {
            if (msg) {
                document.getElementById('acceptIC').style['display'] = 'flex';
                document.getElementById('rejectIC').style['display'] = 'none';

            }
            else {
                document.getElementById('rejectIC').style['display'] = 'flex';
                document.getElementById('acceptIC').style['display'] = 'none';
            }
        })
    }
}

function signUP() {
    let data = [$('#signup-user').val(), $('#signup-mail').val(), $('#signup-pass').val()];
    if (data[0] !== '' && data[1] !== '' && data[2] !== '') {
        sock.emit('signup', data);
        sock.on('signedup', function (val) {
            if (val['bool']) {
                alert(val['msg']);
                $('#signInModal').modal('hide')
            }
            else {
                alert(val['msg']);
            }

        })
    }
}

function login() {
    let data = [$('#login-user').val(), $('#login-pass').val()];
    if (data[0] !== '' && data[1] !== '') {
        sock.emit('login', data);
        sock.on('loggedin', function (val) {
            if (val[0]) {
                alert(val[1]);
                $('#signInModal').modal('hide')
            }
            else {
                alert(val[1]);
            }
        })
    }
}


$("#searchBar").each(function () {
    let _this = $(this);
    _data = _this.data();

    _this.autocomplete({
        minLength: 2,
        delay: 500,
        source: function (request, response) {
            $('#searchIcon').addClass('fa-spinner').removeClass('fa-search');
            sock.emit('search', request.term);
            sock.on('objects', function (data) {
                $('#searchIcon').addClass('fa-search').removeClass('fa-spinner');
                response(data);
            });

        },
    });
});


