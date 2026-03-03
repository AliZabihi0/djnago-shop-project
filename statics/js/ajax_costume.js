$(document).ready(function() {
    $('.remove-product-ajax').on('click', function(event) {
        event.preventDefault(); // جلوگیری از رفتار پیش‌فرض لینک

        var remove_url = $(this).attr('href'); // URL حذف از data-attribute
        var product_id = $(this).data('product-id'); // ID محصول برای شناسایی ردیف

        // ارسال درخواست AJAX POST
        $.ajax({
            url: remove_url,
            type: 'POST', // یا GET اگر در view از GET استفاده کردید
            data: {
                'id': product_id, // ارسال ID محصول (اگر view شما آن را نیاز دارد)
                'csrfmiddlewaretoken': '{{ csrf_token }}', // برای امنیت در Django
                'X-Requested-With': 'XMLHttpRequest' // برای شناسایی درخواست AJAX در view
            },
            success: function(response) {
                if (response.status === 'success') {
                    // حذف ردیف محصول از صفحه
                    $('#cart-item-' + product_id).remove();

                    // به‌روزرسانی جمع کل سبد خرید
                    $('#cart-total-items').text(response.cart_data.total_items);
                    $('#cart-total-price').text('USD ' + parseFloat(response.cart_data.total_price).toFixed(2));

                    // اگر سبد خرید خالی شد، پیام مناسب نمایش دهید
                    if (response.cart_data.total_items === 0) {
                        $('tbody').html('<tr><td colspan="5">سبد خرید شما خالی است.</td></tr>');
                    }

                    console.log('محصول حذف شد:', response.message);
                    // می‌تونید یک پیام کوتاه هم به کاربر نمایش بدید (مثل Toast)
                } else {
                    console.error('خطا در حذف محصول:', response.message);
                    // نمایش پیام خطا به کاربر
                }
            },
            error: function(xhr, status, error) {
                console.error('خطای AJAX:', error);
                // نمایش پیام خطا به کاربر
            }
        });
    });
});


