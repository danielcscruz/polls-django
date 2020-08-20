

$("#myClickButton").click(function() {
    $.get("output", function(data) {
        $("#myOutput").html(data);
    }, "html");
});