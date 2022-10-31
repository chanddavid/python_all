const client = new Paho.MQTT.Client("localhost",9001, "myClientId" + new Date().getTime());
// const client = new Paho.MQTT.Client(location.hostname, Number(location.port), "clientId");

const myTopic = "TEMPERATURE1";

client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

client.connect({ onSuccess: onConnect });

let count = 0;
function onConnect() {
  console.log("onConnect");
  client.subscribe(myTopic);
  setInterval(() => { publish(myTopic, `${count++}`) }, 1000)

}

function onConnectionLost(responseObject) {
  if (responseObject.errorCode !== 0) {
    console.log("onConnectionLost:" + responseObject.errorMessage);
  }
  client.connect({ onSuccess: onConnect });
}

const publish = (dest, msg) => {
  console.log('published to:', dest, ' and message is', msg)
  let message = new Paho.MQTT.Message(msg);
  message.destinationName = dest;
  client.send(message);
}

function onMessageArrived(message) {
  let el = document.createElement('div')
  el.innerHTML = message.payloadString
  document.body.appendChild(el)
}


