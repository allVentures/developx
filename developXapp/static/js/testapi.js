$(function () {

    const $form = $('#cashwithdrawalform');
    const $amount = $('#amount');
    const $apioutput = $('#apioutput');

    $form.on("submit", function (e) {
        e.preventDefault();
        $apioutput.empty();
        checkAmount = $amount.val();
        $.ajax({
            url: "http://127.0.0.1:8000/api",
            data: {
                amount: checkAmount,
            },
            type: "GET",
            dataType: "json"
        }).done(function (result) {
            var p = document.createElement('p');
            p.innerText = "Function result: " + result.notes;
            $apioutput.append(p);

        }).fail(function (xhr, status, err) {
        }).always(function (xhr, status) {
        });

    });
});