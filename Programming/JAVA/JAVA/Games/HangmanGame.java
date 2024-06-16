package Games;
import java.util.Scanner;

public class HangmanGame {
    private String[] words = { "hangman", "computer", "java", "programming", "openai" };
    private String word;
    private char[] wordProgress;
    private int attemptsLeft;
    private boolean gameWon;

    public void play() {
        selectWord();
        initializeWordProgress();

        Scanner scanner = new Scanner(System.in);

        while (!gameWon && attemptsLeft > 0) {
            System.out.println("Attempts left: " + attemptsLeft);
            System.out.println("Word: " + String.valueOf(wordProgress));
            System.out.print("Enter a letter: ");
            char letter = scanner.nextLine().charAt(0);

            if (!updateWordProgress(letter)) {
                attemptsLeft--;
            }

            if (isWordGuessed()) {
                gameWon = true;
            }
        }

        if (gameWon) {
            System.out.println("Congratulations! You guessed the word: " + word);
        } else {
            System.out.println("Game over! The word was: " + word);
        }

        scanner.close();
    }

    private void selectWord() {
        int index = (int) (Math.random() * words.length);
        word = words[index];
    }

    private void initializeWordProgress() {
        wordProgress = new char[word.length()];
        for (int i = 0; i < word.length(); i++) {
            wordProgress[i] = '_';
        }
        attemptsLeft = 6;
        gameWon = false;
    }

    private boolean updateWordProgress(char letter) {
        boolean found = false;
        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) == letter) {
                wordProgress[i] = letter;
                found = true;
            }
        }
        return found;
    }

    private boolean isWordGuessed() {
        for (char c : wordProgress) {
            if (c == '_') {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        HangmanGame game = new HangmanGame();
        game.play();
    }
}
