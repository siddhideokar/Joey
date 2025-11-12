$(document).ready(function () {

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",

        },
        out: {
            effect: "bounceOut",

        },
    });

    //Siri configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true
    })
    //Siri message animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true
        },
        out: {
            effect: "fadeOutUp",
            sync: true
        },
    });


    //mic button click event

    //$("#MicBtn").click(function () {
    // $("#Oval").attr("hidden", true);       // Hide element
    // $("#SiriWave").removeAttr("hidden");   // Show element
    //});


    $("#MicBtn").click(function () {

        eel.playAssistantSound()
        $("#Oval").hide();       // jQuery’s built-in hide()
        $("#SiriWave").show();   // jQuery’s built-in show()
        eel.allCommands()()
    });


});