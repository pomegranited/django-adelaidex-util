function add_dynamic() {
    var body = document.getElementsByTagName('body')[0];
    var div = document.createElement('div');
    div.innerHTML = 'javascript rocks';
    body.appendChild(div);
}
