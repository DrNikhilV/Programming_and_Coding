$(document).ready(function () {
    $("form").submit(function (event) {
        event.preventDefault();

        $(".form-group").removeClass("has-error");
        $(".help-block").remove();

        var formData = {
            name: $("#name").val(),
            email: $("#email").val(),
            superheroAlias: $("#superheroAlias").val(),
        };

        $.ajax({
            type: "POST",
            url: "process.php",
            data: formData,
            dataType: "json",
            encode: true,
        })
        .done(function(data) {
            if (!data.success) {
                if (data.errors.name) $("#name-group").addClass("has-error").append('<div class="help-block">' + data.errors.name + '</div>');
                if (data.errors.email) $("#email-group").addClass("has-error").append('<div class="help-block">' + data.errors.email + '</div>');
                if (data.errors.superheroAlias) $("#superhero-group").addClass("has-error").append('<div class="help-block">' + data.errors.superheroAlias + '</div>');
            } else {
                $("form").html('<div class="alert alert-success">' + data.message + '</div>');
            }
        })
        .fail(function() {
            $("form").html('<div class="alert alert-danger">Could not reach server, please try again later.</div>');
        });
    });
});
