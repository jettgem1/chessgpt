
# CHESS GPT: Elevating Chess Engines with Puzzles

## Introduction
CHESS GPT represents a groundbreaking venture into enhancing chess engines by incorporating the challenge of solving complex chess puzzles. Unlike traditional chess AI, which excels in standard game scenarios, our project focuses on navigating the intricacies of puzzles that require non-standard, creative solutions. This initiative stems from the recognition that while chess engines like Stockfish and AlphaZero have dominated standard play, their performance on chess puzzles—especially those designed to challenge their algorithmic foundations—has revealed significant gaps in their problem-solving capabilities.

## Motivation
The inspiration for CHESS GPT was sparked by the intriguing challenge that chess puzzles present. Traditional engines, while robust in their strategic play, often falter against the unique configurations and objectives posed by puzzles. This discrepancy highlighted an opportunity to explore AI's potential in a new light, aiming to equip chess engines with the creative and adaptive problem-solving skills akin to those of experienced human players.

## Background and Significance
Artificial Intelligence has had a profound impact on chess in several ways, revolutionizing the game and its community. In recent years, powerful chess engines like Stockfish have emerged, utilizing sophisticated algorithms to analyze positions and calculate variations at an incredible depth. AlphaZero, developed by DeepMind, took a different approach by using machine learning and neural networks. AlphaZero demonstrated extraordinary playing strength, mastering chess through self-play and learning from scratch, surpassing traditional engines. However, AlphaZero’s chess playing abilities were challenged by a chess puzzle crafted by Mathematician Sir Roger Penrose (Zahavy, Tom). His puzzle placed stronger black pieces (such as the queen and the rooks) on the board in awkward positions. An experienced human player, playing white, could readily steer the game into a draw, but powerful chess programs would say black had a clear advantage. These puzzles, termed ‘Penrose puzzles’ are still widely considered some of the hardest chess puzzles created to this day. Penrose used his puzzles to argue that human thinking is not entirely algorithmic and cannot be replaced sufficiently by complex computers (Penrose, 1994; Penrose and Mermin, 1990; Wikipedia, 2023).  After stumping the top chess programs with these puzzles, others adapted Penrose’s strategy to devise sprawling collections of chess puzzles that computers struggle to solve. 

This phenomenon piqued the interest of computer scientist Tom Zahavy. He sought to understand why these positions were so hard for computers to analyze when they were easily solvable by humans. This discovery has had broader implications in evaluating artificial intelligence’s current limitations in the field of game theory and decision-making. Zahavy suspected that a program made up of many diverse systems, working together as a group, could outperform the traditional AI chess program that was stumped by the Penrose-style puzzles. He weaved together multiple decision-making AI systems, each optimized and trained for different strategies. The new system showed more skill and creativity in dealing with Penrose-style puzzles when compared to AlphaZero, which had the best record competing against other top chess programs. The intuition was that the program would collaborate with itself: if one approach hit a wall, then the program simply turned to another offered by one of the other AI systems. This study has implications beyond the world of chess, suggesting that teams of diverse AI systems could potentially solve problems that single systems struggled with.

Zahavy concluded that AlphaZero and other traditional chess programs couldn’t solve most puzzles because it was so focused on winning entire games, start to finish. This approach leads to blind spots exposed by the unlikely arrangement of pieces shown in Penrose-style puzzles. When AlphaZero was tested solely on puzzles, it was able to solve less than four percent of Penrose-style puzzles and under twelve percent of the rest. Then, the researchers tried training AlphaZero to play against itself using the Penrose puzzle arrangement as the starting position instead of the full board of typical games. They saw massive improvements in the performance of the program - it solved ninety-six percent of the Penrose-style puzzles and seventy-six of the rest. In general, they concluded that if a chess program was trained on a specific puzzle, it could solve that puzzle, just as it could when it was trained on a full game. The researchers concluded that if a chess program could have access to all these different versions of AlphaZero that were trained on these different puzzles, it could spark the ability for these programs to approach new problems productively. This could potentially lead the program to have more creative approaches to any chess puzzle, not just Penrose puzzles. 

This revelation and research, which we delve into further detail under relevant literature, served as the motivation behind our project, in which we aim to enhance chess AI by focusing on puzzle-solving. Leveraging a standard chess AI trained in regular games, we explore its struggles with intricate puzzles requiring unconventional moves. Our primary objective is to showcase the inflexibility of conventional chess AI in scenarios where strategic sacrifices are essential, despite its proficiency in standard gameplay.

Examples such as Penrose's puzzles, demonstrate the persistent challenges that prompt our investigation into creative problem-solving approaches for chess AI. Through this exploration, we seek not only to unveil the limitations of current AI systems but also to pave the way for a more adaptive and versatile generation of chess-playing algorithms.

Our project focusing on AI puzzle-solving in chess holds significance for the broader field of artificial intelligence. By analyzing the intricacies of puzzle scenarios, we aim to address a crucial aspect of AI adaptability. As chess AI traditionally excels in standard gameplay but faces challenges with unconventional puzzles, our efforts seek to bridge this gap. The lessons learned from enhancing puzzle-solving abilities can extend beyond the chessboard, influencing the way AI approaches unexpected problems in various domains. This development may pave the way for more versatile and creative AI systems, contributing to advancements in real-world problem-solving scenarios beyond the realm of chess. 

## Project Overview
CHESS GPT aims to create a more adaptable and creative chess engine capable of solving puzzles that conventional algorithms struggle with. By integrating advanced AI techniques and leveraging a comprehensive database of puzzles, we develop and evaluate novel approaches to AI-driven puzzle solving. Our work encompasses several key areas:

- **Algorithm Development**: Designing and implementing algorithms that enhance the AI's ability to understand and solve complex chess puzzles.
- **Puzzle Database Expansion**: Curating a diverse set of puzzles that challenge the AI in various aspects of chess strategy and tactics.
- **Performance Evaluation**: Establishing rigorous metrics to assess the AI's puzzle-solving efficiency, creativity, and adaptability.


## Startup
After installing proper dependencies and files, navigate to the same directory as `main.py`. To run, type:
```shell
python3 main.py
```
After some time (to process the dataset) you will be prompted by:
1. Play Puzzle
2. Watch AI Play
3. Evaluate AI Performance

Enter your choice:
Simply type 1, 2, or 3 and press enter. Note that 3 is mostly used for evaluation metrics and are graphed below but will take a while to run. It’s likely you’ll prefer 2 or 1. After selecting, you’ll be again prompted to select what puzzle you want to play in an interactive chess window.

You’ll be asked:
1. Random Puzzle
2. Text-Based Puzzle

Enter your choice:

Selecting 1 immediately starts the User Interface sequence by randomly selecting a puzzle from the database. 

Selecting 2 prompts you again to select which puzzle the AI should play.

Whenever you see “User : ”, input a chess-puzzle related prompt or you won’t get your puzzle. For example,
```
User : I want a mate in 4 with a queen sacrifice
```
Then we use api calls and our lichess database to find a chess puzzle that fits the description. 

## Key Findings
Our exploration into the realm of AI-driven chess puzzle solving has yielded promising results, underscoring the potential of advanced AI techniques to enhance chess engines' problem-solving capabilities. Among our key findings:

- **Enhanced Creativity and Adaptability**: The AI demonstrated an improved ability to navigate puzzles with unconventional setups, showcasing creativity in its approach to problem-solving.
- **Superior Performance on Complex Puzzles**: Compared to traditional engines, CHESS GPT showed a higher success rate in solving complex puzzles, indicating a deeper understanding of the strategic and tactical nuances involved.
- **Insights into AI's Problem-Solving Limits**: Our work also shed light on the inherent limitations of current AI models when faced with tasks requiring high levels of creativity and adaptability, suggesting directions for future research.

## Developing a Chess UI with PyQt5 and Python-chess
In the development of a user interface (UI) for chess in Python, PyQt5 and the python-chess library were instrumental in creating a sophisticated and user-friendly environment for interacting with the game. By leveraging PyQt5, a comprehensive set of Python bindings for Qt, a cross-platform application development framework, I was able to design and implement a graphical interface that provides players with intuitive controls and clear visual representation of the chessboard. This made it possible to create a more engaging and accessible experience for users of varying skill levels.

The python-chess library, known for its extensive functionality in handling chess data and logic, including board setup, move generation, and game state management, served as the backbone of the chess engine. It allowed for the implementation of complex chess rules and the management of game states, ensuring that the UI could accurately reflect the progress of a game and enforce the rules of chess.

To advance the module and add unique features, I focused on integrating functionalities that enhance the user's experience and interaction with the game. This included the development of features such as move history, which allows players to review past moves, and undo functionality, enabling players to correct mistakes without restarting the game. These additions not only improved usability but also facilitated a deeper understanding of the game's dynamics and strategies for players.

Through the thoughtful integration of PyQt5 and python-chess, along with the targeted enhancements made to the module, I was able to create a comprehensive and user-friendly chess UI in Python. This project not only demonstrates the power of combining graphical interface development with robust game logic handling but also showcases the potential for further innovation in the realm of digital board games.

### Enhancements and Innovations
To further enrich the chess-playing experience and advance the module, I incorporated several key features:

- **Move History and Undo Functionality**: Players can review past moves and easily undo actions, facilitating a deeper understanding of game strategies and allowing for corrections without restarting the game.
- **Adjustable Difficulty Levels**: The AI's challenge can be customized, making the game engaging for beginners learning the game and seasoned players seeking to improve their skills.
- **Creative Problem-Solving in UI Design**: The integration of puzzle-solving elements into the UI showcases the engine's improved adaptability and strategic depth, offering a more engaging and challenging experience.

These advancements not only demonstrate the potential for digital innovation in board games but also underscore the project's commitment to enhancing the cognitive and strategic dimensions of chess through technology.

## Future Directions
Building on our findings, future work will aim to further enhance the AI's problem-solving capabilities, exploring new algorithmic approaches and expanding the puzzle database. We also plan to engage the broader AI and chess communities, fostering collaboration and innovation in this exciting field.

## Contributing
Contributions to CHESS GPT are welcome, including improvements to the AI algorithms, additions to the puzzle database, and enhancements to the evaluation framework. We encourage interested individuals to join us in advancing this project.

## Acknowledgements
We extend our gratitude to the Cornell University faculty and our peers for their guidance and support throughout this project. Our thanks also go to the broader chess and AI research communities for their inspiration and encouragement.

## License
CHESS GPT is released under the MIT license, facilitating open access and collaboration in the pursuit of advancing chess AI technology.