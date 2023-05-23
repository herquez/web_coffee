$(document).ready(function(e){
    const url_array = $(this)[0].URL.split("/");
    if(url_array.length > 4){
        switch (url_array[3]) {
            case 'about':
                $('#nav-about').addClass('active');
                break;
            case 'services':
                $('#nav-services').addClass('active');
                break;
            case 'store':
                $('#nav-store').addClass('active');
                break;
            case 'contact':
                $('#nav-contact').addClass('active');
                break;
            case 'blog':
                $('#nav-blog').addClass('active');
                break;
            default:
                break;
        }
    } else {
        $('#nav-home').addClass('active');
    }
});
