
$(document).ready(function() {
    let target = null;
    $.get("/target", function(data) {
        target = data.target;
    });

    $("#submit").click(function() {
        const guess = $("#guess").val();
        $.post("/guess", {guess: guess, target: target}, function(data) {
            $("#message").text(data.message);
        });
    });
});
