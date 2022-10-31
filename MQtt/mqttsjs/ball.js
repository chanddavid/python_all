const client = new Paho.MQTT.Client("110.44.123.47",9002, "myClientId" + new Date().getTime());

const myTopic = "apple/freeze-3/dev-3/temperature";

client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

client.connect({ onSuccess: onConnect });

let count = 0;
function onConnect() {
  console.log("onConnect");
  client.subscribe(myTopic);
}

function onConnectionLost(responseObject) {
  if (responseObject.errorCode !== 0) {
    console.log("onConnectionLost:" + responseObject.errorMessage);
  }
  client.connect({ onSuccess: onConnect });
}

function onMessageArrived(message) {
  let el = document.createElement('div')
  el.innerHTML = message.payloadString
  document.body.appendChild(el)
}



