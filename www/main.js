// main.js
$(document).ready(function () {

  // ===== Textillate animation =====
  $('.text').textillate({ loop: true, sync: true, in: { effect: "bounceIn" }, out: { effect: "bounceOut" } });

  // ===== SiriWave configuration =====
  var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800, height: 200, style: "ios9", amplitude: 1, speed: 0.3, autostart: true
  });

  // Siri message animation
  $('.siri-message').textillate({ loop: true, sync: true, in: { effect: "fadeInUp", sync: true }, out: { effect: "fadeOutUp", sync: true } });

  // Mic button click
  $("#MicBtn").click(function () {
    try { eel.playAssistantSound(); } catch (e) {}
    $("#Oval").hide();
    $("#SiriWave").show();
    try { eel.allCommands(); } catch (e) {}
  });

  // Keyboard shortcut (Ctrl/Cmd + J)
  function doc_keyUp(e) {
    if (e.key === 'j' && (e.ctrlKey || e.metaKey)) {
      try { eel.playAssistantSound(); } catch (e) {}
      $("#Oval").hide();
      $("#SiriWave").show();
      try { eel.allCommands(); } catch (e) {}
    }
  }
  document.addEventListener('keyup', doc_keyUp, false);

  // Chat Offcanvas button
  $("#ChatBtn").click(function () {
    var chatOffcanvasEl = document.getElementById('chatOffcanvas');
    var bsOffcanvas = new bootstrap.Offcanvas(chatOffcanvasEl);
    bsOffcanvas.show();
  });

  // PlayAssistant: called when user types message and sends
  function PlayAssistant(message) {
    if (!message || message.trim() === "") return;

    $("#Oval").hide();
    $("#SiriWave").show();

    try { eel.allCommands(message); } catch (e) {}

    $("#chatbox").val("");
    $("#MicBtn").show();
    $("#SendBtn").hide();

    // UI fallback; Python will call ShowHood when finished
    setTimeout(() => { $("#SiriWave").hide(); $("#Oval").show(); }, 2000);
  }

  // Toggle Mic/Send buttons
  function ShowHideButton(message) {
    if (!message || message.trim() === "") {
      $("#MicBtn").show();
      $("#SendBtn").hide();
    } else {
      $("#MicBtn").hide();
      $("#SendBtn").show();
    }
  }

  // Chatbox events
  $("#chatbox").on('input', function () { ShowHideButton($("#chatbox").val()); });

  $("#SendBtn").click(function () { PlayAssistant($("#chatbox").val()); });

  $("#chatbox").keypress(function (e) {
    if (e.which === 13) { PlayAssistant($("#chatbox").val()); }
  });

});
