// // card to handle stripe payment
// var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
// var clientSecret = $('#id_client_secret').text().slice(1, -1);
// var stripe = Stripe(stripePublicKey);
// var elements = stripe.elements();
// var card = elements.create('card');
// card.mount('#card-element');

// // handle real time errors on if card details are wrong 
// card.addEventListener('change', function (event) {
//     var errorDiv = document.getElementById('card-errors');
//     if (event.error) {
//         var html = `<span>${event.error.message}</span>`;
//         $(errorDiv).html(html);
//     } else {
//         errorDiv.textContent = '';
//     }
// });

// // handle form  submit
// var form = document.getElementById('payment-form');

// form.addEventListener('submit', function(ev) {
//     ev.preventDefault();
//     card.update({ 'disabled': true});
//     $('#submit-button').attr('disabled', true);

//     var saveInfo = Boolean($('#id-save-info').attr('checked'));
//     // From using {% csrf_token %} in the form
//     var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
//     var postData = {
//         'csrfmiddlewaretoken': csrfToken,
//         'client_secret': clientSecret,
//         'save_info': saveInfo,
//     };
//     var url = '/checkout/cache_checkout_data/';

//     $.post(url, postData).done(function() {
//         stripe.confirmCardPayment(clientSecret, {
//             payment_method: {
//                     card: card,
//                     billing_details: {
//                         name: $.trim(form.full_name.value),
//                         phone: $.trim(form.phone_number.value),
//                         email: $.trim(form.email.value),
//                         address:{
//                             line1: $.trim(form.street_address1.value),
//                             line2: $.trim(form.street_address2.value),
//                             city: $.trim(form.town_or_city.value),
//                             country: $.trim(form.country.value),
//                             state: $.trim(form.county.value),
//                         }
//                     }
//                 },
//                 shipping: {
//                     name: $.trim(form.full_name.value),
//                     phone: $.trim(form.phone_number.value),
//                     address: {
//                         line1: $.trim(form.street_address1.value),
//                         line2: $.trim(form.street_address2.value),
//                         city: $.trim(form.town_or_city.value),
//                         country: $.trim(form.country.value),
//                         postal_code: $.trim(form.postcode.value),
//                         state: $.trim(form.county.value),
//                     }
//                 },
//         }).then(function(result) {
//             if (result.error) {
//                 var errorDiv = document.getElementById('card-errors');
//                 var html = `<span role="alert">${result.error.message}</span>`;
//                 $(errorDiv).html(html);
//                 card.update({
//                     'disabled': false
//                 }); // enable to allow them to fix it
//                 $('#submit-button').attr('disabled', false);
//             } else {
//                 if (result.paymentIntent.status === 'succeeded') {
//                     form.submit();
//                 }
//             }
//         });
//     }).fail(function() {
//         location.reload();
//     })
// });
