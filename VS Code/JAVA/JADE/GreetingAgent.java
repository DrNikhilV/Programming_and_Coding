import jade.core.Agent;
import jade.core.behaviours.CyclicBehaviour;
import jade.core.behaviours.OneShotBehaviour;
import jade.lang.acl.ACLMessage;

public class GreetingAgent extends Agent {
    protected void setup() {
        addBehaviour(new SendGreetingBehavior());
    }

    private class SendGreetingBehavior extends OneShotBehaviour {
        public void action() {
            // Create a greeting message
            ACLMessage message = new ACLMessage(ACLMessage.INFORM);
            message.setContent("Hello, Receiver!");

            // Set the receiver's AID (Agent ID)
            message.addReceiver(new jade.core.AID("ReceiverAgent", jade.core.AID.ISLOCALNAME));

            // Send the message
            send(message);

            System.out.println("Sent a greeting to ReceiverAgent: " + message.getContent());
        }
    }
}