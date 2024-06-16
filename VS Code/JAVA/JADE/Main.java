import jade.core.Runtime;
import jade.core.Profile;
import jade.core.ProfileImpl;
import jade.wrapper.AgentContainer;
import jade.wrapper.AgentController;

public class Main {
    public static void main(String[] args) {
        // Get the JADE runtime instance
        Runtime rt = Runtime.instance();

        // Create a profile
        Profile p = new ProfileImpl();

        // Create a main container
        AgentContainer mainContainer = rt.createMainContainer(p);

        try {
            // Start the main container
            mainContainer.start();

            // Create and start your Jade agents here
            AgentController greetingAgent = mainContainer.createNewAgent("GreetingAgent", "GreetingAgent", null);
            greetingAgent.start();

            AgentController receiverAgent = mainContainer.createNewAgent("ReceiverAgent", "ReceiverAgent", null);
            receiverAgent.start();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
