$(document).ready(function () {
    /*$("a").click(function(){
        alert("you clicked " + $(this).text())
    });*/
    
    $("#buy").click(function(){
        alert("you clikckdaen buy button")
        let AJdata = { 'button': $(this).text() }
        $.ajax({
            data: AJdata,
            url: "{% url 'button_trade' 1 %}",
            //on success
            success: function(response) {
                $("#content").html("Hoii!")
            },

            error: function(response) {
                console.log(response.errors)
            }
        });
    });
    
});
