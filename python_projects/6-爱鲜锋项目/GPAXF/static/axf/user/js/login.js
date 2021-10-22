function parse_data() {
    var $password_input = $("#password_input");
    var password = $password_input.val().trim();
    $password_input.val(md5(password));

    return true;
}