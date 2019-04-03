(function ($) {
    $(function () {
        $('.field-cheque_date').hide();
        $('.field-cheque_number').hide();
        $('.field-cheque_bank_name').hide();
        $('.field-dep_bank_id').hide();
        var selectBox = $('#id_payment_mode');
        selectBox.on('change', function () {
           
            var value = selectBox.val();
            if (value == 'Cash') {
                $('.field-cheque_date').hide();
                $('.field-cheque_number').hide();
                $('.field-cheque_bank_name').hide();
                $('.field-dep_bank_id').hide();
            } else {
                console.log('hello');
                $('.field-cheque_date').show();
                $('.field-cheque_number').show();
                $('.field-cheque_bank_name').show();
                $('.field-dep_bank_id').show();
            }
        })
    });
})(django.jQuery);