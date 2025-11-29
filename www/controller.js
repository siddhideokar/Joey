// controller.js
$(document).ready(function () {

  // Display text in Siri area (animated)
  eel.expose(DisplayMessage);
  function DisplayMessage(message) {
    if (!message) return;
    $(".siri-message .texts li").text(message);
    $('.siri-message').textillate('start');
  }

  // Show Hood (hide SiriWave and show circle)
  eel.expose(ShowHood);
  function ShowHood() {
    $("#Oval").show();
    $("#SiriWave").hide();
  }

  // Helper to insert chat bubble
  function addToUI(text, who) {
    if (!text || !text.trim()) return;
    var chatBox = document.getElementById("chat-canvas-body");
    if (!chatBox) return;

    var html = "";
    if (who === "user") {
      html = `
        <div class="row justify-content-end mb-4">
          <div class="width-size"><div class="sender_message">${text}</div></div>
        </div>`;
    } else {
      html = `
        <div class="row justify-content-start mb-4">
          <div class="width-size"><div class="receiver_message">${text}</div></div>
        </div>`;
    }

    chatBox.insertAdjacentHTML('beforeend', html);
    chatBox.scrollTop = chatBox.scrollHeight;
  }

  // user text (called from Python)
  eel.expose(senderText);
  function senderText(message) { addToUI(message, "user"); }

  // assistant reply (called from Python)
  eel.expose(receiverText);
  function receiverText(message) { addToUI(message, "assistant"); }

});
