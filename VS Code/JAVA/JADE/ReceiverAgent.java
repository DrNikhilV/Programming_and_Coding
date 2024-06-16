import jade.core.Agent;
import jade.core.behaviours.CyclicBehaviour;
import jade.core.behaviours.OneShotBehaviour;
import jade.lang.acl.ACLMessage;
public class ReceiverAgent extends Agent {
    protected void setup() {
        addBehaviour(new ReceiveGreetingBehavior());
    }

    private class ReceiveGreetingBehavior extends CyclicBehaviour {
        public void action() {
            // Receive and process incoming messages
            ACLMessage msg = receive();

            if (msg != null) {
                String content = msg.getContent();
                System.out.println("Received a greeting: " + content);
            } else {
                block(); // Wait for messages
            }
        }
    }
}